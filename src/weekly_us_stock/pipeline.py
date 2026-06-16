"""Eight-step weekly screening pipeline.

Funnel: universe -> hard filters -> standardized data -> normalized model ->
quality/risk -> scenario valuation -> risk-adjusted ranking -> reports.
Every step logs input/output counts, elapsed time and rejection reasons, and
exports its frames so each run leaves a complete audit trail under
runs/YYYYMMDD/.
"""

from __future__ import annotations

import errno
import logging
import os
import shutil
import tempfile
import time
from collections.abc import Callable, Iterator
from contextlib import contextmanager
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
from weekly_us_stock.reports.archive import build_paper_portfolio, build_run_manifest
from weekly_us_stock.reports.compare import (
    compare_with_previous,
    find_previous_run_dir,
)
from weekly_us_stock.reports.dashboard import build_dashboard
from weekly_us_stock.reports.exporters import export_dataframe, export_json, export_text
from weekly_us_stock.reports.feishu import build_feishu_summary
from weekly_us_stock.reports.funnel import build_funnel_ledger
from weekly_us_stock.reports.turnaround import build_turnaround_watchlist
from weekly_us_stock.steps.step1_universe import build_market_snapshot, fetch_universe
from weekly_us_stock.steps.step2_events import (
    MATERIAL_EVENT_REASON,
    build_material_events_frame,
    detect_material_events,
)
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
from weekly_us_stock.valuation.eligibility import classify_eligibility
from weekly_us_stock.valuation.industry import route_unsupported_industries
from weekly_us_stock.valuation.ranking import build_rankings

# Cross-process run-date lock. Retry ONLY on genuine lock contention, re-raise
# every other OSError (bad descriptor, a filesystem that does not support
# locks), and time out instead of spinning forever (e.g. a network share that
# never grants the lock) so the run fails closed rather than hanging.
_LOCK_TIMEOUT_SECONDS = 120.0
_LOCK_POLL_SECONDS = 0.1

if os.name == "nt":  # pragma: no cover - exercised only on Windows
    import msvcrt

    _LOCK_RETRY_ERRNOS = frozenset({errno.EACCES, errno.EDEADLOCK})

    def _try_acquire(handle: Any) -> bool:
        try:
            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            return True
        except OSError as exc:
            if exc.errno not in _LOCK_RETRY_ERRNOS:
                raise
            return False

    def _unlock(handle: Any) -> None:
        handle.seek(0)
        try:
            msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
        except OSError:
            pass  # closing the handle releases the lock regardless

else:  # POSIX
    import fcntl

    _LOCK_RETRY_ERRNOS = frozenset({errno.EAGAIN, errno.EWOULDBLOCK, errno.EACCES})

    def _try_acquire(handle: Any) -> bool:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
            return True
        except OSError as exc:
            if exc.errno not in _LOCK_RETRY_ERRNOS:
                raise
            return False

    def _unlock(handle: Any) -> None:
        fcntl.flock(handle, fcntl.LOCK_UN)


def _lock_exclusive(handle: Any) -> None:
    handle.seek(0)
    deadline = time.monotonic() + _LOCK_TIMEOUT_SECONDS
    while not _try_acquire(handle):
        if time.monotonic() >= deadline:
            raise TimeoutError(
                "could not acquire run-date lock within "
                f"{_LOCK_TIMEOUT_SECONDS:g}s"
            )
        time.sleep(_LOCK_POLL_SECONDS)


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
        # Recover any report orphaned by a crashed promotion BEFORE anything that
        # can fail (provider/credential resolution), so a failed startup never
        # leaves the last good report stranded in a backup dir.
        self._recover_run_dir(request)
        provider = self._resolve_provider(request)
        run_dir = self._create_staging_dir(request)
        try:
            return self._execute(request, provider, run_dir)
        finally:
            # If the run did not reach promotion (it raised), drop its own
            # staging dir so failed/retried runs do not accumulate partial
            # reports. After a successful promotion the staging dir has been
            # renamed away, so this is a no-op.
            if run_dir.exists():
                shutil.rmtree(run_dir, ignore_errors=True)

    def _execute(
        self, request: PipelineRequest, provider: DataProvider, run_dir: Path
    ) -> PipelineResult:
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
        # news - or a material 8-K already filed - must not be ranked against
        # pre-event earning power.
        gate_candidates = financial_result.candidates
        filings_by_ticker = self._recent_filings(provider, gate_candidates)
        event_result = detect_material_events(
            gate_candidates,
            prices,
            self.settings.events,
            filings_by_ticker=filings_by_ticker,
            as_of=as_of,
        )
        events_frame = build_material_events_frame(
            gate_candidates,
            prices,
            self.settings.events,
            filings_by_ticker=filings_by_ticker,
            as_of=as_of,
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
        self._export(run_dir, "material_events", events_frame, summary, artifacts)
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
                quality,
                self.settings.scenarios,
                self.settings.risk_preferences,
                wacc_settings=self.settings.wacc,
                alert_settings=self.settings.alerts,
            ),
            output_count=lambda result: len(result.metrics),
        )
        if not valuation_result.skipped.empty:
            summary.rejection_counts = (
                valuation_result.skipped["skip_reason"].value_counts().to_dict()
            )
            # Names that never entered the engine (incomplete valuation inputs)
            # are un-rankable; route them to the watchlist so they are accounted
            # for in the funnel ledger instead of silently going unaccounted.
            skipped_watchlist = valuation_result.skipped.copy()
            skipped_watchlist["watchlist_reason"] = skipped_watchlist["skip_reason"]
            watchlist_frames.append(skipped_watchlist)
        self._export(
            run_dir, "scenario_valuations", valuation_result.scenario_rows, summary, artifacts
        )
        # P0-1: non-finite, implausibly high, or base/bull below-bound valuations
        # are not precise enough to rank. Only a bear below-bound (catastrophic
        # downside) stays in the distribution, visible in Robust and the queue.
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
                f"removed {len(flagged)} non-finite/out-of-bound valuations from ranking"
            )
        # P1-4: names whose ROIC is not economically meaningful are not valued
        # as low-but-positive; they wait on the watchlist for a dedicated model.
        if not valuation_result.roic_routed.empty:
            routed = valuation_result.roic_routed.copy()
            watchlist_frames.append(routed)
            self._export(run_dir, "roic_routed", routed, summary, artifacts)
            summary.rejection_counts = {
                **(summary.rejection_counts or {}),
                **routed["watchlist_reason"].value_counts().to_dict(),
            }
            summary.notes.append(
                f"routed {len(routed)} names with non-meaningful ROIC to the watchlist"
            )
        # Step 6 can lower model confidence further when assumptions hit
        # configured bounds. Re-check the same hard confidence floor after those
        # haircuts so every route into the ranking obeys one consistent gate.
        if not valuation_result.metrics.empty:
            low_post_valuation_confidence = valuation_result.metrics["model_confidence"] < (
                self.settings.confidence.watchlist_model_confidence
            )
            if low_post_valuation_confidence.any():
                flagged = valuation_result.metrics.loc[low_post_valuation_confidence].copy()
                flagged["watchlist_reason"] = "insufficient_post_valuation_model_confidence"
                watchlist_frames.append(flagged)
                valuation_result.metrics = valuation_result.metrics.loc[
                    ~low_post_valuation_confidence
                ].reset_index(drop=True)
                summary.output_count = len(valuation_result.metrics)
                summary.rejection_counts = {
                    **(summary.rejection_counts or {}),
                    "insufficient_post_valuation_model_confidence": int(len(flagged)),
                }
                summary.notes.append(
                    f"moved {len(flagged)} post-valuation low-confidence names to the watchlist"
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
        # P0-4: ranking != investability. Flag each ranked name eligible/not and
        # split out a research queue so reports never pad with sub-bar names.
        eligibility = classify_eligibility(robust, self.settings.eligibility)
        robust = eligibility.ranked  # carries `eligible` + `ineligible_reasons`
        eligible = eligibility.eligible
        research_queue = eligibility.research_queue
        self._export(run_dir, "robust_ranking", robust, summary, artifacts)
        self._export(run_dir, "upside_ranking", upside, summary, artifacts)
        self._export(run_dir, "eligible_candidates", eligible, summary, artifacts)
        self._export(run_dir, "research_queue", research_queue, summary, artifacts)
        # P2-2: freeze the actionable picks as a forward paper-portfolio entry.
        self._export(
            run_dir, "paper_portfolio", build_paper_portfolio(eligible, as_of), summary, artifacts
        )
        summary.notes.append(
            f"eligible candidates: {len(eligible)}/{len(robust)} "
            f"(research queue {len(research_queue)})"
        )
        steps.append(summary)
        _log_step(summary)

        # Step 8: compare with previous run and build reports --------------------
        watchlist = (
            pd.concat(watchlist_frames, ignore_index=True)
            if watchlist_frames
            else pd.DataFrame(columns=["ticker", "name", "watchlist_reason"])
        )
        # P2-1: structure the material-event names into a turnaround watchlist
        # with a state machine and the evidence each needs to re-enter ranking.
        event_rows = (
            watchlist.loc[watchlist["watchlist_reason"] == MATERIAL_EVENT_REASON]
            if "watchlist_reason" in watchlist.columns
            else watchlist.iloc[0:0]
        )
        turnaround = build_turnaround_watchlist(event_rows, as_of)
        funnel_ledger = build_funnel_ledger(
            universe,
            rejected,
            normalized.rejected,
            watchlist,
            robust,
        )
        previous_dir = self._resolve_previous_dir(request)
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
            eligible=eligible,
            scenarios=valuation_result.scenario_rows,
            watchlist=watchlist,
            turnaround=turnaround,
            comparison=comparison,
            freshness=freshness,
            top_n=self.settings.ranking.top_n,
        )
        feishu = build_feishu_summary(
            request=request,
            steps=steps,
            robust=robust,
            upside=upside,
            eligible=eligible,
            watchlist=watchlist,
            turnaround=turnaround,
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
        # P0-4: the watchlist is the "invalid or not-yet-rankable" bucket; export
        # it under the spec's name too so the three audiences are explicit files.
        self._export(run_dir, "invalid_or_watchlist", watchlist, summary, artifacts)
        self._export(run_dir, "turnaround_watchlist", turnaround, summary, artifacts)  # P2-1
        self._export(run_dir, "funnel_ledger", funnel_ledger, summary, artifacts)
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
        # result.json and run_manifest.json are themselves self-describing
        # entries: give BOTH the result and the manifest the same complete
        # artifact index (every file in the run dir, these two included).
        result_path = run_dir / "result.json"
        artifacts.append(str(result_path))
        artifacts.append(str(run_dir / "run_manifest.json"))
        # We write to a staging dir and promote it on success below. Record the
        # FINAL (post-swap) paths in result.json — both the top-level artifact
        # index and every step's artifact list — so they are valid once the run
        # dir is in place.
        final_dir = self._resolve_path(self.settings.app.output_dir) / request.as_of.strftime(
            "%Y%m%d"
        )

        def _to_final(path: object) -> str:
            return str(path).replace(str(run_dir), str(final_dir))

        result.artifacts = list(dict.fromkeys(_to_final(a) for a in artifacts))
        for step in result.steps:
            step.artifacts = [_to_final(a) for a in step.artifacts]
        export_json(result.model_dump(mode="json"), result_path)

        # P2-2: a self-describing manifest tying this run's archive to its
        # universe/config fingerprints for later out-of-sample validation.
        manifest = build_run_manifest(
            as_of=request.as_of,
            fingerprints={
                "universe_fingerprint": self._universe_fingerprint,
                "config_fingerprint": self._config_fingerprint,
                "universe_ticker_hash": self._universe_ticker_hash,
                "index_membership": self.settings.universe.index_membership,
                "source_sha": os.environ.get("GITHUB_SHA", ""),
            },
            counts={
                "universe": steps[0].output_count if steps else 0,
                "ranked": int(len(robust)),
                "eligible": int(len(eligible)),
                "research_queue": int(len(research_queue)),
                "watchlist": int(len(watchlist)),
                "turnaround": int(len(turnaround)),
                "invalid_valuations": int(len(valuation_result.invalid)),
                "roic_routed": int(len(valuation_result.roic_routed)),
            },
            artifacts=[Path(a).name for a in artifacts],
            paper_portfolio_size=int(len(eligible)),
        )
        export_json(manifest, run_dir / "run_manifest.json")
        # Promote under a per-date lock so concurrent same-date runs cannot
        # interleave. Recovery runs inside the SAME lock immediately before
        # promotion, so an orphaned backup left by another run's crashed
        # promotion is restored before we touch anything — a double fault no
        # longer destroys the last good report.
        with self._date_lock(final_dir.parent, final_dir.name):
            self._recover_promotion(final_dir)
            self._promote_run_dir(run_dir, final_dir)
        return result

    # -- provider wiring ------------------------------------------------------

    def _recent_filings(
        self, provider: DataProvider, candidates: pd.DataFrame
    ) -> dict[str, list[dict]]:
        """Recent EDGAR filings for the candidate set, for the 8-K event gate.
        Empty unless 8-K detection is enabled and the provider can supply them
        (the sample provider cannot), so price-only runs are unaffected."""

        if (
            not self.settings.events.sec_8k_enabled
            or candidates.empty
            or not hasattr(provider, "recent_filings")
        ):
            return {}
        return provider.recent_filings(candidates["ticker"].astype(str).tolist())

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

            return build_composite(
                self.env, self.settings.wacc, self.settings.sec_reconciliation
            )
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

    def _resolve_previous_dir(self, request: PipelineRequest) -> Path | None:
        if request.previous_dir:
            path = Path(request.previous_dir)
            return path if path.exists() else None
        output_dir = self._resolve_path(self.settings.app.output_dir)
        # Key on the run date, not the staging dir name (a non-digit ".tmp"
        # dir that find_previous_run_dir intentionally ignores).
        return find_previous_run_dir(output_dir, request.as_of.strftime("%Y%m%d"))

    def _recover_run_dir(self, request: PipelineRequest) -> None:
        # Restore (or discard) a report left in a backup dir by a crashed
        # promotion, under the per-date lock. Called before provider resolution
        # so a startup failure can never skip recovery.
        output_dir = self._resolve_path(self.settings.app.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        date_key = request.as_of.strftime("%Y%m%d")
        with self._date_lock(output_dir, date_key):
            self._recover_promotion(output_dir / date_key)

    def _create_staging_dir(self, request: PipelineRequest) -> Path:
        # A UNIQUE staging dir; run() promotes it to runs/YYYYMMDD only after the
        # run fully succeeds. A failed rerun never destroys the previous report,
        # and two same-date runs never share a staging dir.
        output_dir = self._resolve_path(self.settings.app.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        date_key = request.as_of.strftime("%Y%m%d")
        return Path(tempfile.mkdtemp(prefix=f".{date_key}.", suffix=".tmp", dir=output_dir))

    @staticmethod
    @contextmanager
    def _date_lock(output_dir: Path, date_key: str) -> Iterator[None]:
        # A cross-process exclusive lock per run date. Recovery and promotion run
        # inside it so two same-date processes serialize their backup/promote
        # steps instead of interleaving and destroying each other's report.
        with open(output_dir / f".{date_key}.lock", "w", encoding="utf-8") as handle:
            _lock_exclusive(handle)
            try:
                yield
            finally:
                _unlock(handle)

    @staticmethod
    def _recover_promotion(final_dir: Path) -> None:
        # A previous promotion that crashed between stepping the old report aside
        # and moving the new one in leaves the old report in a .bak dir. Restore
        # it if the new report never landed; drop it if it did.
        backup = final_dir.with_name(f".{final_dir.name}.bak")
        if not backup.exists():
            return
        if final_dir.exists():
            shutil.rmtree(backup)
        else:
            backup.rename(final_dir)

    @staticmethod
    def _promote_run_dir(staging: Path, final_dir: Path) -> None:
        # Replace final_dir with staging through a recoverable backup. The old
        # report is only deleted AFTER the new one is in place; if the swap
        # fails, it is rolled back. Callers MUST run _recover_promotion under the
        # same lock first, so no orphaned backup survives to here.
        backup = final_dir.with_name(f".{final_dir.name}.bak")
        if backup.exists():
            # A surviving backup is the only copy of a prior report from a
            # crashed promotion. Recovery (run under the same lock just before
            # this) should have cleared it; fail closed rather than destroy the
            # last recoverable copy.
            raise RuntimeError(f"refusing to promote over an unrecovered backup: {backup}")
        stepped_aside = False
        if final_dir.exists():
            final_dir.rename(backup)
            stepped_aside = True
        try:
            staging.rename(final_dir)
        except OSError:
            if stepped_aside:
                if final_dir.exists():
                    shutil.rmtree(final_dir)
                backup.rename(final_dir)
            raise
        if stepped_aside:
            shutil.rmtree(backup)

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
