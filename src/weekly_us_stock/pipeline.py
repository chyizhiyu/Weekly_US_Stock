"""Eight-step weekly screening pipeline.

Funnel: universe -> hard filters -> standardized data -> normalized model ->
quality/risk -> scenario valuation -> risk-adjusted ranking -> reports.
Every step logs input/output counts, elapsed time and rejection reasons, and
exports its frames so each run leaves a complete audit trail under
runs/YYYYMMDD/.
"""

from __future__ import annotations

import logging
import time
from collections.abc import Callable
from datetime import UTC, datetime
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
from weekly_us_stock.providers.base import DataProvider
from weekly_us_stock.providers.sample import SampleDataProvider
from weekly_us_stock.reports.compare import (
    compare_with_previous,
    find_previous_run_dir,
)
from weekly_us_stock.reports.dashboard import build_dashboard
from weekly_us_stock.reports.exporters import export_dataframe, export_json, export_text
from weekly_us_stock.reports.feishu import build_feishu_summary
from weekly_us_stock.steps.step1_universe import build_market_snapshot, fetch_universe
from weekly_us_stock.steps.step2_hard_filters import (
    combine_results,
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

        # Step 1: universe + market snapshot -----------------------------------
        universe, summary = self._timed(
            "step1_universe",
            input_count=0,
            work=lambda: fetch_universe(provider, as_of),
            output_count=len,
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
        # Banks/insurers/REITs/pre-profit biotech leave for the watchlist here:
        # the non-financial solvency gates below must not judge them.
        routed_candidates, early_watchlist = route_unsupported_industries(
            market_result.candidates, fundamentals
        )
        financial_result = run_financial_hard_filters(
            routed_candidates, fundamentals, self.settings.hard_filters
        )
        rejected = pd.concat(
            [type_result.rejected, market_result.rejected, financial_result.rejected],
            ignore_index=True,
        )
        summary = StepSummary(
            name="step2_hard_filters",
            input_count=len(universe),
            output_count=len(financial_result.candidates),
            elapsed_seconds=time.perf_counter() - started,
            rejection_counts=combine_results(type_result, market_result, financial_result),
        )
        if not early_watchlist.empty:
            summary.notes.append(
                f"routed {len(early_watchlist)} unsupported-industry names to the watchlist"
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
            ),
            output_count=lambda result: len(result.modeled),
        )
        summary.rejection_counts = normalized.rejection_counts
        watchlist_frames = []
        if not early_watchlist.empty:
            watchlist_frames.append(early_watchlist)
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
            robust, upside, previous_dir, self.settings.ranking.top_n
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


def _records(frame: pd.DataFrame) -> list[dict[str, Any]]:
    if frame.empty:
        return []
    import json

    return json.loads(frame.to_json(orient="records", date_format="iso"))
