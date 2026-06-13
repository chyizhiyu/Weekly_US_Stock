"""Eight-step weekly screening pipeline.

Funnel: universe -> hard filters -> standardized data -> normalized model ->
quality/risk -> scenario valuation -> risk-adjusted ranking -> reports.
Every step logs input/output counts, elapsed time and rejection reasons, and
exports its frames so each run leaves a complete audit trail under
runs/YYYYMMDD/.
"""

from __future__ import annotations

import logging
import os
import time
from collections.abc import Callable
from datetime import UTC, date, datetime
from pathlib import Path
from typing import Any, TypeVar

import pandas as pd

from weekly_us_stock import __version__
from weekly_us_stock.config import EnvSettings, Settings, load_settings, project_root
from weekly_us_stock.models.screening import (
    DataFreshness,
    DataNotReadyError,
    FilterFrameResult,
    PipelineRequest,
    PipelineResult,
    StepSummary,
)
from weekly_us_stock.providers.base import (
    DataProvider,
    IndexUniverseUnavailable,
    normalize_ticker,
)
from weekly_us_stock.providers.sample import SampleDataProvider
from weekly_us_stock.reports.compare import (
    compare_with_previous,
    find_previous_run_dir,
)
from weekly_us_stock.reports.dashboard import build_dashboard
from weekly_us_stock.reports.exporters import export_dataframe, export_json, export_text
from weekly_us_stock.reports.feishu import build_feishu_summary
from weekly_us_stock.steps.step1_universe import build_market_snapshot, fetch_universe
from weekly_us_stock.steps.step2_events import detect_material_events
from weekly_us_stock.steps.step2_hard_filters import (
    combine_results,
    drop_duplicate_share_classes,
    run_financial_hard_filters,
    run_market_filters,
    run_security_type_filters,
)
from weekly_us_stock.steps.step3_standardize import (
    extract_risk_free,
    standardize_estimates,
    standardize_fundamentals,
)
from weekly_us_stock.steps.step4_normalized import run_normalized_model
from weekly_us_stock.steps.step5_quality import run_quality_assessment
from weekly_us_stock.steps.step6_valuation import run_scenario_valuations
from weekly_us_stock.utils.calendar import week_key
from weekly_us_stock.utils.fingerprint import (
    config_fingerprint,
    ticker_set_hash,
    universe_fingerprint,
)
from weekly_us_stock.valuation.industry import route_unsupported_industries
from weekly_us_stock.valuation.ranking import build_rankings

logger = logging.getLogger(__name__)

T = TypeVar("T")


class WeeklyUSStockPipeline:
    def __init__(
        self,
        settings: Settings | None = None,
        provider: DataProvider | None = None,
        env: EnvSettings | None = None,
    ) -> None:
        self.settings = settings or load_settings()
        self.env = env or EnvSettings()
        self.provider = provider

    def run(self, request: PipelineRequest) -> PipelineResult:
        provider = self._resolve_provider(request)
        run_dir = self._run_dir(request)
        steps: list[StepSummary] = []
        artifacts: list[str] = []
        as_of = request.as_of
        self._index_universe: dict | None = None  # set when an index pool restricts
        self._universe_fingerprint: str | None = None
        self._config_fingerprint: str | None = None
        self._universe_ticker_hash: str | None = None

        # Step 1: universe + market snapshot -----------------------------------
        universe, summary = self._timed(
            "step1_universe",
            input_count=0,
            work=lambda: fetch_universe(provider, as_of),
            output_count=len,
        )
        membership = self.settings.universe.index_membership
        if membership and not universe.empty:
            universe = self._restrict_to_index_universe(
                universe, provider, membership, as_of, summary
            )
        if request.limit is not None and not universe.empty:
            # Smoke-test mode: keep the N largest names so a bounded real-data
            # run still exercises every later step.
            if "market_cap_hint" in universe:
                universe = universe.sort_values("market_cap_hint", ascending=False)
            universe = universe.head(request.limit).reset_index(drop=True)
            summary.output_count = len(universe)
            summary.notes.append(f"universe truncated to {request.limit} for smoke testing")
        self._export(run_dir, "universe", universe, summary, artifacts)
        # P0-3: fingerprints make week-over-week comparability checkable.
        self._universe_fingerprint = universe_fingerprint(self.settings)
        self._config_fingerprint = config_fingerprint(self.settings)
        self._universe_ticker_hash = (
            ticker_set_hash(universe["ticker"]) if not universe.empty else None
        )
        steps.append(summary)
        _log_step(summary)

        # Step 2: hard filters (non-compensatory) -------------------------------
        type_result = run_security_type_filters(
            universe, as_of, self.settings.universe, self.settings.hard_filters
        )
        survivors = type_result.candidates["ticker"].tolist()
        prices = self._timed_data(
            "prices",
            len(survivors),
            lambda: provider.load_prices(
                survivors, as_of, self.settings.hard_filters.liquidity_window_days
            ),
        )
        snapshot = build_market_snapshot(
            type_result.candidates,
            prices,
            as_of,
            self.settings.hard_filters,
            self.settings.freshness,
        )
        market_result = run_market_filters(
            type_result.candidates, snapshot, self.settings.hard_filters
        )
        financial_tickers = market_result.candidates["ticker"].tolist()
        raw_fundamentals = self._timed_data(
            "fundamentals",
            len(financial_tickers),
            lambda: provider.load_fundamentals(financial_tickers, as_of),
        )
        fundamentals = standardize_fundamentals(raw_fundamentals, as_of)
        started = time.perf_counter()
        # One economic entity, one slot (GOOG/GOOGL, BRK-A/BRK-B).
        dedupe_result = drop_duplicate_share_classes(market_result.candidates)
        # Banks/insurers/REITs/pre-profit biotech leave for the watchlist here:
        # the non-financial solvency gates below must not judge them.
        routed_candidates, early_watchlist = route_unsupported_industries(
            dedupe_result.candidates, fundamentals
        )
        financial_result = run_financial_hard_filters(
            routed_candidates, fundamentals, self.settings.hard_filters
        )
        # Material-event gate (the VRRM trap): a price already reflecting bad
        # news must not be ranked against pre-event earning power.
        event_result = detect_material_events(
            financial_result.candidates, prices, self.settings.events
        )
        financial_result = FilterFrameResult(
            candidates=event_result.candidates,
            rejected=financial_result.rejected,
            rejection_counts=financial_result.rejection_counts,
        )
        rejected = pd.concat(
            [
                type_result.rejected,
                market_result.rejected,
                dedupe_result.rejected,
                financial_result.rejected,
            ],
            ignore_index=True,
        )
        summary = StepSummary(
            name="step2_hard_filters",
            input_count=len(universe),
            output_count=len(financial_result.candidates),
            elapsed_seconds=time.perf_counter() - started,
            rejection_counts=combine_results(
                type_result, market_result, dedupe_result, financial_result, event_result
            ),
        )
        if not early_watchlist.empty:
            summary.notes.append(
                f"routed {len(early_watchlist)} unsupported-industry names to the watchlist"
            )
        if not event_result.rejected.empty:
            summary.notes.append(
                f"moved {len(event_result.rejected)} names to the event watchlist "
                "pending re-underwriting"
            )
        self._export(
            run_dir, "hard_filter_candidates", financial_result.candidates, summary, artifacts
        )
        self._export(run_dir, "hard_filter_rejected", rejected, summary, artifacts)
        steps.append(summary)
        _log_step(summary)

        freshness = self._build_freshness(request, snapshot, financial_result, provider)
        if request.strict_freshness and freshness.fresh_price_coverage < (
            self.settings.freshness.min_fresh_price_coverage
        ):
            raise DataNotReadyError(
                f"Fresh price coverage {freshness.fresh_price_coverage:.1%} is below "
                f"{self.settings.freshness.min_fresh_price_coverage:.1%}; data not ready yet"
            )

        # Step 3: standardize estimates and macro -------------------------------
        candidates = financial_result.candidates
        tickers = candidates["ticker"].tolist()
        estimates = standardize_estimates(
            self._timed_data(
                "estimates", len(tickers), lambda: provider.load_estimates(tickers, as_of)
            ),
            as_of,
        )
        macro = self._timed_data("macro", 1, lambda: provider.load_macro(as_of))
        risk_free, risk_free_source = extract_risk_free(
            macro, self.settings.wacc.fallback_risk_free
        )
        summary = StepSummary(
            name="step3_standardize",
            input_count=len(candidates),
            output_count=len(candidates),
            elapsed_seconds=0.0,
            notes=[f"risk_free={risk_free:.4f} ({risk_free_source})"],
        )
        steps.append(summary)
        _log_step(summary)

        # Trailing-twelve-month anchors so valuation does not lag the latest
        # quarters; missing TTM rows fall back to the latest annual report.
        ttm = self._timed_data(
            "ttm", len(tickers), lambda: provider.load_ttm(tickers, as_of)
        )

        # Step 4: normalized model + industry routing ---------------------------
        normalized, summary = self._timed(
            "step4_normalized_model",
            input_count=len(candidates),
            work=lambda: run_normalized_model(
                candidates,
                fundamentals,
                estimates,
                risk_free,
                self.settings.normalization,
                self.settings.wacc,
                ttm=ttm,
                as_of=as_of,
            ),
            output_count=lambda result: len(result.modeled),
        )
        summary.rejection_counts = normalized.rejection_counts
        watchlist_frames = []
        if not early_watchlist.empty:
            watchlist_frames.append(early_watchlist)
        if not event_result.rejected.empty:
            watchlist_frames.append(event_result.rejected)
        if not normalized.watchlist.empty:
            watchlist_frames.append(normalized.watchlist)
        modeled = normalized.modeled
        if not modeled.empty:
            low_confidence = modeled["data_confidence"] < (
                self.settings.confidence.watchlist_data_confidence
            )
            if low_confidence.any():
                flagged = modeled.loc[low_confidence].copy()
                flagged["watchlist_reason"] = "insufficient_confidence"
                watchlist_frames.append(flagged)
                modeled = modeled.loc[~low_confidence].reset_index(drop=True)
                summary.notes.append(
                    f"moved {len(flagged)} low-data-confidence names to the watchlist"
                )
        self._export(run_dir, "normalized_financials", modeled, summary, artifacts)
        if not normalized.rejected.empty:
            self._export(run_dir, "normalization_rejected", normalized.rejected, summary, artifacts)
        steps.append(summary)
        _log_step(summary)

        # Step 5: quality, moat evidence, risk flags ----------------------------
        quality, summary = self._timed(
            "step5_quality_risk",
            input_count=len(modeled),
            work=lambda: run_quality_assessment(modeled, fundamentals),
            output_count=len,
        )
        if not quality.empty:
            # Hard gate: a valuation the model itself does not trust cannot be
            # ranked — it goes to the watchlist with its confidence on record.
            low_model = quality["model_confidence"] < (
                self.settings.confidence.watchlist_model_confidence
            )
            if low_model.any():
                flagged = quality.loc[low_model].copy()
                flagged["watchlist_reason"] = "insufficient_model_confidence"
                watchlist_frames.append(flagged)
                quality = quality.loc[~low_model].reset_index(drop=True)
                summary.output_count = len(quality)
                summary.notes.append(
                    f"moved {len(flagged)} low-model-confidence names to the watchlist"
                )
        steps.append(summary)
        _log_step(summary)

        # Step 6: probabilistic scenario valuation ------------------------------
        valuation_result, summary = self._timed(
            "step6_scenario_valuation",
            input_count=len(quality),
            work=lambda: run_scenario_valuations(
                quality, self.settings.scenarios, self.settings.risk_preferences
            ),
            output_count=lambda result: len(result.metrics),
        )
        if not valuation_result.skipped.empty:
            summary.rejection_counts = (
                valuation_result.skipped["skip_reason"].value_counts().to_dict()
            )
        self._export(
            run_dir, "scenario_valuations", valuation_result.scenario_rows, summary, artifacts
        )
        # P0-1: valuations with a non-finite or solver-bound-saturated required
        # output are not precise enough to rank; route them to the watchlist
        # with an auditable reason instead of letting pseudo-precise numbers
        # into Robust/Upside.
        if not valuation_result.invalid.empty:
            flagged = valuation_result.invalid.copy()
            flagged["watchlist_reason"] = flagged["invalid_reason"].fillna(
                "invalid_valuation_output"
            )
            watchlist_frames.append(flagged)
            self._export(run_dir, "invalid_valuations", flagged, summary, artifacts)
            summary.rejection_counts = {
                **(summary.rejection_counts or {}),
                **flagged["watchlist_reason"].value_counts().to_dict(),
            }
            summary.notes.append(
                f"removed {len(flagged)} non-finite/bound-saturated valuations from ranking"
            )
        steps.append(summary)
        _log_step(summary)

        # Step 7: dual rankings --------------------------------------------------
        (robust, upside), summary = self._timed(
            "step7_risk_adjusted_ranking",
            input_count=len(valuation_result.metrics),
            work=lambda: build_rankings(
                valuation_result.metrics, self.settings.risk_preferences
            ),
            output_count=lambda result: len(result[0]),
        )
        self._export(run_dir, "robust_ranking", robust, summary, artifacts)
        self._export(run_dir, "upside_ranking", upside, summary, artifacts)
        steps.append(summary)
        _log_step(summary)

        # Step 8: compare with previous run and build reports --------------------
        watchlist = (
            pd.concat(watchlist_frames, ignore_index=True)
            if watchlist_frames
            else pd.DataFrame(columns=["ticker", "name", "watchlist_reason"])
        )
        previous_dir = self._resolve_previous_dir(request, run_dir)
        comparison = compare_with_previous(
            robust,
            upside,
            previous_dir,
            self.settings.ranking.top_n,
            current_universe_fingerprint=self._universe_fingerprint,
            current_config_fingerprint=self._config_fingerprint,
        )
        started = time.perf_counter()
        dashboard = build_dashboard(
            request=request,
            steps=steps,
            robust=robust,
            upside=upside,
            scenarios=valuation_result.scenario_rows,
            watchlist=watchlist,
            comparison=comparison,
            freshness=freshness,
            top_n=self.settings.ranking.top_n,
        )
        feishu = build_feishu_summary(
            request=request,
            steps=steps,
            robust=robust,
            upside=upside,
            watchlist=watchlist,
            comparison=comparison,
            freshness=freshness,
            top_n=self.settings.report.feishu_top_n,
        )
        summary = StepSummary(
            name="step8_reports",
            input_count=len(robust),
            output_count=len(robust),
            elapsed_seconds=time.perf_counter() - started,
            notes=[
                f"previous_run={comparison.previous_as_of or 'none'}",
            ],
        )
        self._export(run_dir, "watchlist", watchlist, summary, artifacts)
        artifacts.append(str(export_text(dashboard, run_dir / "dashboard.md")))
        artifacts.append(str(export_text(feishu, run_dir / "feishu_summary.md")))
        steps.append(summary)
        _log_step(summary)

        result = PipelineResult(
            request=request,
            robust_top=_records(robust.head(self.settings.ranking.top_n)),
            upside_top=_records(upside.head(self.settings.ranking.top_n)),
            watchlist=_records(watchlist),
            steps=steps,
            freshness=freshness,
            artifacts=artifacts,
        )
        metadata = self._run_metadata(request, provider, freshness, steps)
        metadata["time_consistency"] = _time_consistency(request, estimates, modeled)
        artifacts.append(str(export_json(metadata, run_dir / "run_metadata.json")))
        result_path = run_dir / "result.json"
        result.artifacts.append(str(result_path))
        export_json(result.model_dump(mode="json"), result_path)
        return result

    # -- provider wiring ------------------------------------------------------

    def _resolve_provider(self, request: PipelineRequest) -> DataProvider:
        if self.provider is not None:
            return self.provider
        source = (request.provider or self.settings.app.data_source).lower()
        if source == "sample":
            return SampleDataProvider(self._resolve_path(self.settings.app.sample_data_dir))
        if source in {"fmp", "composite", "auto"}:
            # Fail closed: a production run must never silently publish sample
            # data. Missing credentials abort the run with a clear error; the
            # sample provider is only ever an EXPLICIT choice.
            from weekly_us_stock.providers.composite import build_composite

            return build_composite(self.env, self.settings.wacc)
        raise ValueError(f"Unsupported data source: {source}")

    # -- universe restriction --------------------------------------------------

    def _restrict_to_index_universe(
        self,
        universe: pd.DataFrame,
        provider: DataProvider,
        membership: list[str],
        as_of: date,
        summary: StepSummary,
    ) -> pd.DataFrame:
        """Narrow the universe to configured index members, failing closed.

        A provider that does not enforce membership (sample) is a no-op. For an
        enforcing provider, an empty union, a failed constituent endpoint, or an
        implausibly low count aborts the run instead of silently screening the
        full market (P0-2).
        """

        constituents = provider.index_constituents(membership, as_of)
        if not constituents.restrict:
            summary.notes.append(
                f"provider '{constituents.source}' does not enforce index "
                f"membership {membership}; using full universe"
            )
            return universe

        floors = self.settings.universe.index_min_constituents
        problems: list[str] = list(constituents.errors)
        if constituents.union_count == 0:
            problems.append("constituent union is empty")
        for index in constituents.requested:
            count = constituents.per_index_counts.get(index, 0)
            floor = floors.get(index, 1)
            if count < floor:
                problems.append(f"{index}: {count} constituents below floor {floor}")
        if problems:
            raise IndexUniverseUnavailable(
                f"configured index universe {membership} could not be built "
                f"safely (source={constituents.source}): {'; '.join(problems)}"
            )

        allowed = {normalize_ticker(symbol) for symbol in constituents.symbols}
        universe_keys = universe["ticker"].map(normalize_ticker)
        mask = universe_keys.isin(allowed)
        unmatched = sorted(allowed - set(universe_keys[mask]))
        before = len(universe)
        restricted = universe.loc[mask].reset_index(drop=True)
        summary.output_count = len(restricted)
        summary.notes.append(
            f"restricted to {'+'.join(membership)}: {len(restricted)}/{before} "
            f"(union {constituents.union_count}, unmatched {len(unmatched)})"
        )
        if unmatched:
            # Never silently drop a constituent: list those with no matching
            # screener security so a ticker-format drift is visible (P0-2).
            logger.warning(
                "index constituents with no universe match (%d): %s",
                len(unmatched),
                ", ".join(unmatched[:50]),
            )
        self._index_universe = {
            "source": constituents.source,
            "snapshot_date": constituents.snapshot_date,
            "requested": constituents.requested,
            "per_index_counts": constituents.per_index_counts,
            "union_count": constituents.union_count,
            "matched_count": int(len(restricted)),
            "unmatched_count": len(unmatched),
            "unmatched_symbols": unmatched,
        }
        return restricted

    # -- helpers ---------------------------------------------------------------

    def _build_freshness(
        self,
        request: PipelineRequest,
        snapshot: pd.DataFrame,
        financial_result: FilterFrameResult,
        provider: DataProvider,
    ) -> DataFreshness:
        # Coverage is measured over the snapshot (pre-gate): the stale_price
        # hard filter removes stale names from the ranking, and this metric
        # reports how much of the market was actually current.
        priced = (
            snapshot.loc[snapshot["price"].notna()]
            if not snapshot.empty and "price" in snapshot
            else pd.DataFrame()
        )
        if priced.empty or "is_price_fresh" not in priced:
            coverage, stale = 0.0, 0
        else:
            fresh = priced["is_price_fresh"].fillna(False).astype(bool)
            coverage = float(fresh.mean())
            stale = int((~fresh).sum())
        degraded = list(provider.degraded_sources())
        notes = []
        if degraded:
            notes.append(
                "Run degraded: some sources were replaced by fallbacks; see degraded_sources."
            )
        return DataFreshness(
            expected_as_of=request.as_of.isoformat(),
            fresh_price_coverage=coverage,
            stale_tickers=stale,
            degraded_sources=degraded,
            notes=notes,
        )

    def _run_metadata(
        self,
        request: PipelineRequest,
        provider: DataProvider,
        freshness: DataFreshness,
        steps: list[StepSummary],
    ) -> dict[str, Any]:
        return {
            "as_of": request.as_of.isoformat(),
            "week_key": week_key(request.as_of),
            "universe_limit": request.limit,
            "generated_at": datetime.now(UTC).isoformat(),
            "pipeline_version": __version__,
            "provider": provider.name,
            "data_source_setting": request.provider or self.settings.app.data_source,
            "hurdle_rate": self.settings.risk_preferences.hurdle_rate,
            "degraded_sources": freshness.degraded_sources,
            "fresh_price_coverage": freshness.fresh_price_coverage,
            "stale_tickers": freshness.stale_tickers,
            "funnel": {step.name: step.output_count for step in steps},
            # P0-3: universe definition + fingerprints make each run's
            # comparability and exact pool auditable.
            "index_membership": self.settings.universe.index_membership,
            "universe_definition": self._index_universe
            or {
                "index_membership": self.settings.universe.index_membership,
                "restrict": False,
            },
            "universe_fingerprint": self._universe_fingerprint,
            "universe_ticker_hash": self._universe_ticker_hash,
            "config_fingerprint": self._config_fingerprint,
            "source_sha": os.environ.get("GITHUB_SHA", ""),
        }

    def _resolve_previous_dir(self, request: PipelineRequest, run_dir: Path) -> Path | None:
        if request.previous_dir:
            path = Path(request.previous_dir)
            return path if path.exists() else None
        output_dir = self._resolve_path(self.settings.app.output_dir)
        return find_previous_run_dir(output_dir, run_dir.name)

    def _run_dir(self, request: PipelineRequest) -> Path:
        run_dir = self._resolve_path(self.settings.app.output_dir) / request.as_of.strftime(
            "%Y%m%d"
        )
        run_dir.mkdir(parents=True, exist_ok=True)
        return run_dir

    @staticmethod
    def _resolve_path(path: str | Path) -> Path:
        candidate = Path(path)
        return candidate if candidate.is_absolute() else project_root() / candidate

    @staticmethod
    def _timed(
        name: str,
        input_count: int,
        work: Callable[[], T],
        output_count: Callable[[T], int],
    ) -> tuple[T, StepSummary]:
        started = time.perf_counter()
        result = work()
        summary = StepSummary(
            name=name,
            input_count=input_count,
            output_count=output_count(result),
            elapsed_seconds=time.perf_counter() - started,
        )
        return result, summary

    @staticmethod
    def _timed_data(label: str, input_count: int, work: Callable[[], pd.DataFrame]) -> pd.DataFrame:
        started = time.perf_counter()
        frame = work()
        logger.info(
            "[Data Load %s] input=%s rows=%s elapsed=%.3fs",
            label,
            input_count,
            len(frame),
            time.perf_counter() - started,
        )
        return frame

    @staticmethod
    def _export(
        run_dir: Path,
        name: str,
        frame: pd.DataFrame,
        summary: StepSummary,
        artifacts: list[str],
    ) -> None:
        path = export_dataframe(frame, run_dir / f"{name}.csv")
        summary.artifacts.append(str(path))
        artifacts.append(str(path))


def _log_step(summary: StepSummary) -> None:
    logger.info(
        "[%s] input=%s output=%s rejected=%s elapsed=%.3fs reasons=%s notes=%s",
        summary.name,
        summary.input_count,
        summary.output_count,
        max(summary.input_count - summary.output_count, 0),
        summary.elapsed_seconds,
        summary.rejection_counts or {},
        summary.notes or [],
    )


def _time_consistency(
    request: PipelineRequest, estimates: pd.DataFrame, modeled: pd.DataFrame
) -> dict[str, Any]:
    """Audit block proving price, filings, estimates and the event check all
    refer to the same point in time."""

    block: dict[str, Any] = {
        "price_as_of": request.as_of.isoformat(),
        "material_event_checked_at": request.as_of.isoformat(),
        "estimate_as_of": None,
        "filing_age_days_median": None,
        "filing_age_days_max": None,
        "ttm_anchor_coverage": None,
    }
    if not estimates.empty and "as_of" in estimates:
        block["estimate_as_of"] = str(pd.to_datetime(estimates["as_of"]).max().date())
    if not modeled.empty:
        if "filing_age_days" in modeled:
            ages = pd.to_numeric(modeled["filing_age_days"], errors="coerce").dropna()
            if not ages.empty:
                block["filing_age_days_median"] = int(ages.median())
                block["filing_age_days_max"] = int(ages.max())
        if "anchor_source" in modeled:
            block["ttm_anchor_coverage"] = float(
                (modeled["anchor_source"] == "ttm").mean()
            )
    return block


def _records(frame: pd.DataFrame) -> list[dict[str, Any]]:
    if frame.empty:
        return []
    import json

    return json.loads(frame.to_json(orient="records", date_format="iso"))
