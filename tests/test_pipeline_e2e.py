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
    "normalized_financials.csv",
    "scenario_valuations.csv",
    "robust_ranking.csv",
    "upside_ranking.csv",
    "watchlist.csv",
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


def test_watchlist_routing(pipeline_runs: dict[str, Path]) -> None:
    watchlist = pd.read_csv(pipeline_runs["first"] / "watchlist.csv")
    reasons = dict(zip(watchlist["ticker"], watchlist["watchlist_reason"], strict=True))
    assert reasons["BNKA"] == "bank_model_not_supported"
    assert reasons["INSU"] == "insurance_model_not_supported"
    assert reasons["RLTY"] == "reit_model_not_supported"
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
    assert "Robust Top" in summary and "Upside Top" in summary
    assert "预期IRR" in summary and "P10" in summary
    assert "门槛CVaR" in summary and "质量" in summary and "置信" in summary
    assert "观察名单" in summary
    assert "不构成交易指令" in summary
    # Scenario weights must never masquerade as calibrated probabilities.
    assert "情景权重为人工设定" in summary


def test_week_over_week_comparison(pipeline_runs: dict[str, Path]) -> None:
    dashboard = (pipeline_runs["second"] / "dashboard.md").read_text("utf-8")
    assert "Previous run: 2026-01-09" in dashboard
    first_dashboard = (pipeline_runs["first"] / "dashboard.md").read_text("utf-8")
    assert "First tracked run" in first_dashboard


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
