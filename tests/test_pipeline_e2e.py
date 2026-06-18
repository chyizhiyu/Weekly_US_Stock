"""Offline end-to-end run on the sample provider, including week-over-week."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from tests.conftest import AS_OF as AS_OF_DATE

EXPECTED_ARTIFACTS = [
    "universe.csv",
    "hard_filter_candidates.csv",
    "hard_filter_rejected.csv",
    "material_events.csv",
    "normalized_financials.csv",
    "scenario_valuations.csv",
    "robust_ranking.csv",
    "upside_ranking.csv",
    "watchlist.csv",
    "funnel_ledger.csv",
    "result.json",
    "dashboard.md",
    "feishu_summary.md",
    "run_metadata.json",
]


def _ranks(frame: pd.DataFrame) -> dict[str, int]:
    return dict(zip(frame["ticker"], frame["rank"].astype(int), strict=True))


def test_all_required_artifacts_exist(pipeline_runs: dict[str, Path]) -> None:
    for artifact in EXPECTED_ARTIFACTS:
        assert (pipeline_runs["first"] / artifact).exists(), artifact


def test_hard_filter_audit_trail(pipeline_runs: dict[str, Path]) -> None:
    rejected = pd.read_csv(pipeline_runs["first"] / "hard_filter_rejected.csv")
    reasons = dict(zip(rejected["ticker"], rejected["rejection_reason"], strict=True))
    assert reasons["SPCX"] == "security_type"
    assert reasons["ETFX"] == "security_type"
    assert reasons["WRNT"] == "security_type"
    assert reasons["PREF"] == "security_type"
    assert reasons["OTCP"] == "exchange_not_allowed"
    assert reasons["ADRX"] == "adr_excluded"
    assert reasons["NEWIPO"] == "listing_age"
    assert reasons["TINY"] == "market_cap"
    assert reasons["ILLQ"] == "liquidity"
    assert reasons["LOSS"] == "consecutive_losses"
    assert reasons["DEBT"] == "interest_coverage"
    assert reasons["MISS"] == "insufficient_financial_history"
    assert reasons["SDIL"] == "severe_dilution"
    assert reasons["ACCT"] == "earnings_cash_mismatch"
    assert reasons["STBL.B"] == "duplicate_share_class"
    assert "all_rejection_reasons" in rejected.columns


def test_funnel_ledger_accounts_for_every_universe_ticker(
    pipeline_runs: dict[str, Path],
) -> None:
    universe = pd.read_csv(pipeline_runs["first"] / "universe.csv")
    ledger = pd.read_csv(pipeline_runs["first"] / "funnel_ledger.csv").set_index("ticker")
    assert len(ledger) == len(universe)
    assert not (ledger["final_bucket"] == "unaccounted").any()
    assert ledger.loc["ADRX", "decision_reason"] == "adr_excluded"
    assert ledger.loc["BNKA", "decision_reason"] == "specialist_missing_fundamentals"
    assert ledger.loc["STBL", "final_bucket"] == "eligible"


def test_material_event_goes_to_watchlist_not_ranking(pipeline_runs: dict[str, Path]) -> None:
    # EVNT lost its anchor contract in the week before as_of: the price has
    # repriced but the filings have not. It must be pulled for re-underwriting.
    watchlist = pd.read_csv(pipeline_runs["first"] / "watchlist.csv")
    reasons = dict(zip(watchlist["ticker"], watchlist["watchlist_reason"], strict=True))
    assert reasons["EVNT"] == "material_event_requires_reunderwriting"
    robust = pd.read_csv(pipeline_runs["first"] / "robust_ranking.csv")
    assert "EVNT" not in set(robust["ticker"])
    flags = watchlist.set_index("ticker").loc["EVNT", "event_flags"]
    assert "weekly_drop" in str(flags)
    events = pd.read_csv(pipeline_runs["first"] / "material_events.csv")
    evnt_events = events.loc[events["ticker"] == "EVNT"]
    assert not evnt_events.empty
    assert set(
        ["ticker", "event_date", "source", "event_type", "detail", "revaluation_status"]
    ).issubset(events.columns)
    assert "weekly_drop" in set(evnt_events["event_type"])


def test_watchlist_routing(pipeline_runs: dict[str, Path]) -> None:
    watchlist = pd.read_csv(pipeline_runs["first"] / "watchlist.csv")
    reasons = dict(zip(watchlist["ticker"], watchlist["watchlist_reason"], strict=True))
    assert reasons["BNKA"] == "specialist_missing_fundamentals"
    assert reasons["INSU"] == "specialist_missing_fundamentals"
    assert reasons["RLTY"] == "specialist_missing_fundamentals"
    assert reasons["BIOX"] == "preprofit_biotech_not_supported"
    # Watchlisted names never appear in the rankings.
    robust = pd.read_csv(pipeline_runs["first"] / "robust_ranking.csv")
    assert not set(watchlist["ticker"]) & set(robust["ticker"])


def test_unestimable_normalized_earnings_rejected(pipeline_runs: dict[str, Path]) -> None:
    rejected = pd.read_csv(pipeline_runs["first"] / "normalization_rejected.csv")
    reasons = dict(zip(rejected["ticker"], rejected["rejection_reason"], strict=True))
    assert reasons["NEGM"] == "no_normalized_earnings"


def test_peak_cycle_normalization_in_outputs(pipeline_runs: dict[str, Path]) -> None:
    normalized = pd.read_csv(pipeline_runs["first"] / "normalized_financials.csv")
    cycp = normalized.set_index("ticker").loc["CYCP"]
    assert cycp["normalized_operating_income"] < cycp["reported_operating_income"] * 0.5
    # The base scenario margin must equal the normalized, not the peak, margin.
    scenarios = pd.read_csv(pipeline_runs["first"] / "scenario_valuations.csv")
    base = scenarios.query("ticker == 'CYCP' and scenario == 'base'").iloc[0]
    assert abs(base["operating_margin"] - cycp["normalized_operating_margin"]) < 1e-9


def test_designed_ranking_relationships(pipeline_runs: dict[str, Path]) -> None:
    robust = pd.read_csv(pipeline_runs["first"] / "robust_ranking.csv")
    upside = pd.read_csv(pipeline_runs["first"] / "upside_ranking.csv")
    robust_ranks, upside_ranks = _ranks(robust), _ranks(upside)

    # Growth with incremental ROIC < WACC must not rank high.
    assert robust_ranks["STBL"] < robust_ranks["GROW"]
    assert upside_ranks["STBL"] < upside_ranks["GROW"]

    # Buybacks beat equivalent-economics dilution on per-share value.
    assert robust_ranks["BYBK"] < robust_ranks["DILU"]
    assert upside_ranks["BYBK"] < upside_ranks["DILU"]

    # The lottery stock tops Upside but is downweighted in Robust.
    assert upside_ranks["LOTO"] == 1
    assert robust_ranks["LOTO"] > robust_ranks["STBL"]

    # The stable compounder leads the risk-adjusted list.
    assert robust_ranks["STBL"] == 1


def test_rankings_keep_raw_metrics_no_opaque_score(pipeline_runs: dict[str, Path]) -> None:
    robust = pd.read_csv(pipeline_runs["first"] / "robust_ranking.csv")
    for column in [
        "expected_irr",
        "median_irr",
        "p10_irr",
        "p90_irr",
        "above_hurdle_weight",
        "permanent_loss_weight",
        "worst_case_shortfall",
        "worst_case_hurdle_gap",
        "expected_shortfall",
        "hurdle_cvar",
        "model_uncertainty",
        "business_quality",
        "valuation_excess",
        "evidence_confidence",
        "hurdle_penalty",
        "downside_penalty",
        "ambiguity_penalty",
        "permanent_loss_penalty",
        "robust_return",
        "model_confidence",
        "data_confidence",
        "intrinsic_value_low",
        "intrinsic_value_base",
        "intrinsic_value_high",
        "risk_flags",
    ]:
        assert column in robust.columns, column


def test_risk_flags_are_explicit(pipeline_runs: dict[str, Path]) -> None:
    robust = pd.read_csv(pipeline_runs["first"] / "robust_ranking.csv").set_index("ticker")
    assert "heavy_sbc" in str(robust.loc["DILU", "risk_flags"])
    assert "incremental_roic_below_wacc" in str(robust.loc["GROW", "risk_flags"])
    assert "peak_cycle_margins" in str(robust.loc["CYCP", "risk_flags"])


def test_run_metadata_provenance(pipeline_runs: dict[str, Path]) -> None:
    metadata = json.loads((pipeline_runs["first"] / "run_metadata.json").read_text("utf-8"))
    assert metadata["as_of"] == "2026-01-09"
    assert metadata["week_key"] == "2026-W02"
    assert metadata["provider"] == "sample"
    assert metadata["hurdle_rate"] == 0.12
    assert "generated_at" in metadata
    assert metadata["fresh_price_coverage"] == 1.0
    assert metadata["funnel"]["step1_universe"] == 29


def test_feishu_summary_content(pipeline_runs: dict[str, Path]) -> None:
    summary = (pipeline_runs["first"] / "feishu_summary.md").read_text("utf-8")
    assert "2026-01-09" in summary
    assert "扫描 29 只" in summary
    # P0-4: eligible candidates lead; Upside is an explicitly labelled, non-
    # actionable research queue (never an "Upside Top" buy list).
    assert "达标候选" in summary
    assert "Upside 研究队列" in summary and "非可执行" in summary
    assert "预期IRR" in summary and "P10" in summary
    assert "最差缺口" in summary and "质量" in summary and "置信" in summary
    assert "观察名单" in summary
    assert "不构成交易指令" in summary
    # Scenario weights must never masquerade as calibrated probabilities.
    assert "情景权重为人工设定" in summary


def test_week_over_week_comparison(pipeline_runs: dict[str, Path]) -> None:
    dashboard = (pipeline_runs["second"] / "dashboard.md").read_text("utf-8")
    assert "Previous run: 2026-01-09" in dashboard
    first_dashboard = (pipeline_runs["first"] / "dashboard.md").read_text("utf-8")
    assert "First tracked run" in first_dashboard


def test_post_valuation_confidence_haircut_is_rechecked(
    tmp_path: Path, sample_provider
) -> None:
    from weekly_us_stock.config import load_settings
    from weekly_us_stock.models.screening import PipelineRequest
    from weekly_us_stock.pipeline import WeeklyUSStockPipeline

    settings = load_settings()
    settings.app.output_dir = str(tmp_path)
    settings.confidence.watchlist_model_confidence = 0.40
    WeeklyUSStockPipeline(settings=settings, provider=sample_provider).run(
        PipelineRequest(as_of=AS_OF_DATE, provider="sample")
    )

    run_dir = tmp_path / AS_OF_DATE.strftime("%Y%m%d")
    robust = pd.read_csv(run_dir / "robust_ranking.csv")
    watchlist = pd.read_csv(run_dir / "watchlist.csv").set_index("ticker")
    assert "LOTO" not in set(robust["ticker"])
    assert (
        watchlist.loc["LOTO", "watchlist_reason"]
        == "insufficient_post_valuation_model_confidence"
    )


def test_production_modes_fail_closed_without_credentials() -> None:
    # auto/fmp without an FMP key must abort, never silently publish sample
    # data to the results branch.
    import pytest

    from weekly_us_stock.config import EnvSettings, load_settings
    from weekly_us_stock.models.screening import PipelineRequest
    from weekly_us_stock.pipeline import WeeklyUSStockPipeline
    from weekly_us_stock.providers.base import DataProviderNotConfigured

    pipeline = WeeklyUSStockPipeline(
        settings=load_settings(),
        env=EnvSettings(fmp_api_key=None, polygon_api_key=None, fred_api_key=None),
    )
    for source in ["auto", "fmp"]:
        request = PipelineRequest(as_of=AS_OF_DATE, provider=source)
        with pytest.raises(DataProviderNotConfigured):
            pipeline._resolve_provider(request)


def test_ttm_anchor_flows_into_outputs(pipeline_runs: dict[str, Path]) -> None:
    normalized = pd.read_csv(pipeline_runs["first"] / "normalized_financials.csv")
    stbl = normalized.set_index("ticker").loc["STBL"]
    assert stbl["anchor_source"] == "ttm"
    # The TTM window (filed 2025-11-14) anchors revenue above FY2024.
    assert pd.to_datetime(stbl["latest_filing_date"]) == pd.Timestamp("2025-11-14")
    assert int(stbl["latest_fiscal_year"]) == 2024  # annual history unchanged


def test_no_future_data_in_outputs(pipeline_runs: dict[str, Path]) -> None:
    # All financial inputs visible in the audit trail must have been filed
    # on or before the run date.
    normalized = pd.read_csv(pipeline_runs["first"] / "normalized_financials.csv")
    assert (pd.to_datetime(normalized["latest_filing_date"]) <= pd.Timestamp("2026-01-09")).all()
    assert int(normalized["latest_fiscal_year"].max()) == 2024


def test_incomplete_valuation_inputs_routed_to_watchlist(
    tmp_path: Path, sample_provider, monkeypatch
) -> None:
    # Guards the pipeline wiring (not just the funnel unit test): a name that
    # reaches the engine with incomplete valuation inputs must be routed to the
    # watchlist and accounted for in the ledger, never left unaccounted.
    from weekly_us_stock.config import load_settings
    from weekly_us_stock.models.screening import PipelineRequest
    from weekly_us_stock.pipeline import WeeklyUSStockPipeline
    from weekly_us_stock.steps import step6_valuation

    original = step6_valuation._to_inputs

    def drop_stbl(row: pd.Series) -> object:
        return None if row.get("ticker") == "STBL" else original(row)

    monkeypatch.setattr(step6_valuation, "_to_inputs", drop_stbl)

    settings = load_settings()
    settings.app.output_dir = str(tmp_path)
    WeeklyUSStockPipeline(settings=settings, provider=sample_provider).run(
        PipelineRequest(as_of=AS_OF_DATE, provider="sample")
    )

    run_dir = tmp_path / AS_OF_DATE.strftime("%Y%m%d")
    watchlist = pd.read_csv(run_dir / "watchlist.csv").set_index("ticker")
    assert watchlist.loc["STBL", "watchlist_reason"] == "incomplete_valuation_inputs"
    ledger = pd.read_csv(run_dir / "funnel_ledger.csv").set_index("ticker")
    assert ledger.loc["STBL", "final_bucket"] == "watchlist"
    assert not (ledger["final_bucket"] == "unaccounted").any()


def test_failed_rerun_preserves_previous_report(
    tmp_path: Path, sample_provider, monkeypatch
) -> None:
    # The run writes to a staging dir and only swaps it into runs/YYYYMMDD on
    # success, so a same-date rerun that fails mid-way must leave the previous
    # successful report fully intact (never a half-written or empty dir).
    import pytest

    from weekly_us_stock import pipeline as pipeline_mod
    from weekly_us_stock.config import load_settings
    from weekly_us_stock.models.screening import PipelineRequest
    from weekly_us_stock.pipeline import WeeklyUSStockPipeline

    settings = load_settings()
    settings.app.output_dir = str(tmp_path)
    request = PipelineRequest(as_of=AS_OF_DATE, provider="sample")

    WeeklyUSStockPipeline(settings=settings, provider=sample_provider).run(request)
    run_dir = tmp_path / AS_OF_DATE.strftime("%Y%m%d")
    good_result = (run_dir / "result.json").read_text("utf-8")
    good_files = sorted(p.name for p in run_dir.iterdir())

    def boom(*args: object, **kwargs: object) -> object:
        raise RuntimeError("provider exploded mid-run")

    monkeypatch.setattr(pipeline_mod, "build_funnel_ledger", boom)
    with pytest.raises(RuntimeError):
        WeeklyUSStockPipeline(settings=settings, provider=sample_provider).run(request)

    # The official report is untouched; no staging dir is promoted on failure.
    assert (run_dir / "result.json").read_text("utf-8") == good_result
    assert sorted(p.name for p in run_dir.iterdir()) == good_files
    # The failed run cleaned up its own staging dir (no partial-report leak).
    assert [p.name for p in tmp_path.iterdir() if p.name.endswith(".tmp")] == []


def test_promotion_failure_rolls_back_to_previous_report(
    tmp_path: Path, monkeypatch
) -> None:
    # If promotion itself fails (rename/disk error), the previous report must be
    # rolled back into place, never left deleted.
    import pytest

    from weekly_us_stock.pipeline import WeeklyUSStockPipeline

    final = tmp_path / "20260109"
    final.mkdir()
    (final / "result.json").write_text("GOOD", encoding="utf-8")
    staging = tmp_path / ".20260109.unique.tmp"
    staging.mkdir()
    (staging / "result.json").write_text("NEW", encoding="utf-8")

    real_rename = Path.rename

    def flaky_rename(self: Path, target: object) -> Path:
        if self == staging:
            raise OSError("rename exploded mid-promotion")
        return real_rename(self, target)

    monkeypatch.setattr(Path, "rename", flaky_rename)

    with pytest.raises(OSError):
        WeeklyUSStockPipeline._promote_run_dir(staging, final)

    assert final.exists()
    assert (final / "result.json").read_text(encoding="utf-8") == "GOOD"


def test_recover_promotion_restores_orphaned_backup(tmp_path: Path) -> None:
    # Simulate a crash after the old report was stepped aside but before the new
    # one landed: the next run must restore the backup, not start from nothing.
    from weekly_us_stock.pipeline import WeeklyUSStockPipeline

    final = tmp_path / "20260109"
    backup = tmp_path / ".20260109.bak"
    backup.mkdir()
    (backup / "result.json").write_text("GOOD", encoding="utf-8")

    WeeklyUSStockPipeline._recover_promotion(final)

    assert final.exists()
    assert (final / "result.json").read_text(encoding="utf-8") == "GOOD"
    assert not backup.exists()


def test_concurrent_promotions_do_not_lose_reports(tmp_path: Path) -> None:
    # Several same-date promotions running at once must serialize on the per-date
    # lock so they never interleave their backup/promote steps and delete every
    # report. Every worker must succeed (the lock serializes them), exactly one
    # report survives intact, and no .bak/.tmp dirs are left behind.
    import tempfile
    from concurrent.futures import ThreadPoolExecutor

    from weekly_us_stock.pipeline import WeeklyUSStockPipeline

    output = tmp_path
    final = output / "20260109"
    final.mkdir()
    (final / "result.json").write_text("ORIGINAL", encoding="utf-8")

    def promote(tag: str) -> None:
        staging = Path(tempfile.mkdtemp(prefix=".20260109.", suffix=".tmp", dir=output))
        (staging / "result.json").write_text(tag, encoding="utf-8")
        with WeeklyUSStockPipeline._date_lock(output, "20260109"):
            WeeklyUSStockPipeline._recover_promotion(final)
            WeeklyUSStockPipeline._promote_run_dir(staging, final)

    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(promote, f"RUN{i}") for i in range(4)]
    # .result() re-raises any exception a worker hit; no promotion may fail.
    for future in futures:
        future.result()

    assert final.exists()
    assert (final / "result.json").read_text(encoding="utf-8").startswith("RUN")
    assert [p.name for p in output.iterdir() if p.name.endswith((".tmp", ".bak"))] == []


def test_promotion_recovers_orphaned_backup_before_promoting(
    tmp_path: Path, monkeypatch
) -> None:
    # Double fault: another run's promotion crashed leaving only a .bak (final
    # missing), then THIS run's promotion also fails. Recovery inside the
    # promotion lock must restore the orphaned backup before promoting, so the
    # last good report survives both failures instead of being deleted.
    import tempfile

    import pytest

    from weekly_us_stock.pipeline import WeeklyUSStockPipeline

    output = tmp_path
    final = output / "20260109"
    backup = output / ".20260109.bak"
    backup.mkdir()
    (backup / "result.json").write_text("LAST_GOOD", encoding="utf-8")

    staging = Path(tempfile.mkdtemp(prefix=".20260109.", suffix=".tmp", dir=output))
    (staging / "result.json").write_text("NEW", encoding="utf-8")

    real_rename = Path.rename

    def flaky_rename(self: Path, target: object) -> Path:
        if self == staging:
            raise OSError("this run's promotion also fails")
        return real_rename(self, target)

    monkeypatch.setattr(Path, "rename", flaky_rename)

    # Exactly what _execute does inside the promotion lock.
    WeeklyUSStockPipeline._recover_promotion(final)
    with pytest.raises(OSError):
        WeeklyUSStockPipeline._promote_run_dir(staging, final)

    assert final.exists()
    assert (final / "result.json").read_text(encoding="utf-8") == "LAST_GOOD"
    assert not backup.exists()


def test_startup_recovery_runs_before_provider_resolution(tmp_path: Path) -> None:
    # If a prior promotion crashed (only a .bak survives) and the next run then
    # fails at provider/credential resolution, the orphaned report must still be
    # recovered — recovery runs before the provider is resolved.
    import pytest

    from weekly_us_stock.config import EnvSettings, load_settings
    from weekly_us_stock.models.screening import PipelineRequest
    from weekly_us_stock.pipeline import WeeklyUSStockPipeline
    from weekly_us_stock.providers.base import DataProviderNotConfigured

    settings = load_settings()
    settings.app.output_dir = str(tmp_path)
    backup = tmp_path / ".20260109.bak"
    backup.mkdir()
    (backup / "result.json").write_text("LAST_GOOD", encoding="utf-8")

    pipeline = WeeklyUSStockPipeline(
        settings=settings,
        env=EnvSettings(fmp_api_key=None, polygon_api_key=None, fred_api_key=None),
    )
    with pytest.raises(DataProviderNotConfigured):
        pipeline.run(PipelineRequest(as_of=AS_OF_DATE, provider="fmp"))

    final = tmp_path / "20260109"
    assert final.exists()
    assert (final / "result.json").read_text(encoding="utf-8") == "LAST_GOOD"
    assert not backup.exists()
