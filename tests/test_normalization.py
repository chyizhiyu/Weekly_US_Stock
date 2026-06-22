"""Layer-2 normalization: one-offs, cyclical peaks, SBC as a real expense."""

from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from weekly_us_stock.config import NormalizationSettings, WaccSettings
from weekly_us_stock.steps.step4_normalized import run_normalized_model
from weekly_us_stock.valuation.industry import route_model_family
from weekly_us_stock.valuation.normalize import normalize_company


@pytest.fixture
def normalization() -> NormalizationSettings:
    return NormalizationSettings()


def _history(
    margins: list[float],
    *,
    one_offs: dict[int, float] | None = None,
    sbc_pct: float = 0.01,
    revenue: float = 1_000e6,
) -> pd.DataFrame:
    rows = []
    one_offs = one_offs or {}
    for index, margin in enumerate(margins):
        year = 2024 - len(margins) + 1 + index
        one_off = one_offs.get(year, 0.0)
        operating_income = revenue * margin + one_off
        net_income = (operating_income - 5e6) * 0.79
        rows.append(
            {
                "ticker": "TEST",
                "fiscal_year": year,
                "filing_date": pd.Timestamp(f"{year + 1}-02-20"),
                "revenue": revenue,
                "gross_profit": revenue * 0.4,
                "operating_income": operating_income,
                "one_off_items": one_off,
                "net_income": net_income,
                "ocf": net_income + revenue * 0.04 + revenue * sbc_pct,
                "capex": revenue * 0.04,
                "depreciation": revenue * 0.04,
                "sbc": revenue * sbc_pct,
                "dividends_paid": 0.0,
                "buybacks": 0.0,
                "share_issuance": 0.0,
                "shares_diluted": 100e6,
                "total_debt": 200e6,
                "cash": 100e6,
                "interest_expense": 5e6,
                "total_equity": 900e6,
                "effective_tax_rate": 0.21,
            }
        )
    return pd.DataFrame(rows)


def test_one_off_gains_excluded_from_normalized_earnings(
    normalization: NormalizationSettings,
) -> None:
    margins = [0.15] * 6
    clean = normalize_company(_history(margins), normalization)
    inflated = normalize_company(
        _history(margins, one_offs={2024: 200e6}), normalization
    )
    assert clean is not None and inflated is not None
    # The one-off inflates reported operating income but not normalized earnings.
    assert inflated["reported_operating_income"] == pytest.approx(350e6)
    assert inflated["normalized_operating_income"] == pytest.approx(
        clean["normalized_operating_income"]
    )
    assert inflated["normalized_operating_income"] < inflated["reported_operating_income"]


def test_peak_cycle_margins_do_not_create_fake_cheapness(
    normalization: NormalizationSettings,
) -> None:
    # Cyclical at its margin peak: the model must anchor at the full-cycle
    # median, not at today's peak profitability.
    margins = [0.08, 0.06, 0.04, 0.07, 0.09, 0.05, 0.14, 0.16]
    metrics = normalize_company(_history(margins), normalization)
    assert metrics is not None
    assert metrics["normalized_operating_margin"] == pytest.approx(0.075)
    assert metrics["current_operating_margin"] == pytest.approx(0.16)
    assert metrics["normalized_operating_income"] < metrics["reported_operating_income"] * 0.5


def test_sbc_is_a_real_expense_not_an_ocf_addback(
    normalization: NormalizationSettings,
) -> None:
    # GAAP adds SBC back inside OCF. A naive OCF - capex "free cash flow"
    # therefore overstates owner earnings by the SBC amount; the normalized
    # model must strip that add-back so heavy issuers cannot look cheap.
    history = _history([0.20] * 6, sbc_pct=0.08)
    metrics = normalize_company(history, normalization)
    assert metrics is not None
    latest = history.iloc[-1]
    naive_fcf = float(latest["ocf"] - latest["capex"])
    sbc = float(latest["sbc"])
    assert metrics["normalized_fcf"] == pytest.approx(naive_fcf - sbc, rel=1e-6)
    assert metrics["sbc_intensity"] == pytest.approx(0.08)


def test_split_adjusted_market_shares_replace_stale_statement_shares(
    normalization: NormalizationSettings,
) -> None:
    # Recent stock splits can make the quote and universe share count adjust
    # before the latest filed diluted-share figure does. Valuation must use the
    # split-adjusted market share count; otherwise every per-share value is
    # inflated by the split factor.
    history = _history([0.20] * 6)
    candidate = pd.DataFrame(
        [
            {
                "ticker": "TEST",
                "sector": "Technology",
                "industry": "Semiconductors",
                "shares_outstanding": 1_000e6,  # 10x the filed diluted shares
                "beta": 1.0,
                "price": 25.0,
                "market_cap": 25_000e6,
                "is_price_fresh": True,
            }
        ]
    )

    result = run_normalized_model(
        candidate,
        history,
        pd.DataFrame(),
        0.04,
        normalization,
        WaccSettings(),
        as_of=date(2026, 6, 18),
    )

    row = result.modeled.iloc[0]
    assert row["shares_diluted"] == pytest.approx(1_000e6)
    assert row["statement_shares_diluted_raw"] == pytest.approx(100e6)
    assert row["share_count_alignment"] == "market_split_adjusted:10x"
    assert row["normalized_fcf_per_share"] == pytest.approx(
        row["normalized_fcf"] / 1_000e6
    )


def test_short_history_returns_none_fail_closed(
    normalization: NormalizationSettings,
) -> None:
    assert normalize_company(_history([0.15] * 3), normalization) is None


def test_industry_router() -> None:
    assert not route_model_family("Financial Services", "Banks - Regional", 0.3).supported
    assert not route_model_family("Financial Services", "Insurance - Life", 0.2).supported
    assert not route_model_family("Real Estate", "REIT - Diversified", 0.4).supported
    assert not route_model_family("Healthcare", "Biotechnology", -0.5).supported
    # Profitable biotech is rankable through the general model.
    assert route_model_family("Healthcare", "Biotechnology", 0.25).supported
    assert route_model_family("Technology", "Software - Application", 0.2).supported


def test_entire_financial_sector_is_watchlisted() -> None:
    # Cash/leverage/working capital mean different things for financials:
    # NONE of the sector may flow through the general owner-earnings DCF.
    cases = {
        ("Financial Services", "Asset Management"): "asset_management",
        ("Financial Services", "Capital Markets"): "asset_management",
        ("Financial Services", "Credit Services"): "consumer_finance",
        ("Financial Services", "Mortgage Finance"): "consumer_finance",
        ("Financial Services", "Financial Data & Stock Exchanges"): "financial_other",
    }
    for (sector, industry), family in cases.items():
        route = route_model_family(sector, industry, 0.3)
        assert not route.supported, industry
        assert route.family == family


def test_incremental_roic_unestimable_when_capital_shrinks(
    normalization: NormalizationSettings,
) -> None:
    # NOPAT up while invested capital falls: incremental ROIC is undefined and
    # must NOT become an optimistic fixed constant (the old 60% bug).
    history = _history([0.10, 0.11, 0.12, 0.14, 0.16, 0.18])
    history["total_equity"] = [900e6, 850e6, 800e6, 750e6, 700e6, 650e6]
    metrics = normalize_company(history, normalization)
    assert metrics is not None
    assert metrics["incremental_roic"] is None


def test_ttm_row_anchors_current_level(normalization: NormalizationSettings) -> None:
    history = _history([0.15] * 6)
    ttm = {
        "revenue": 1_200e6,  # 20% above the last annual report
        "gross_profit": 480e6,
        "operating_income": 1_200e6 * 0.18,
        "one_off_items": 0.0,
        "shares_diluted": 95e6,  # buybacks since fiscal year end
        "total_debt": 250e6,
        "cash": 150e6,
        "total_equity": 950e6,
        "depreciation": 48e6,
        "interest_expense": 6e6,
        "dividends_paid": 0.0,
        "buybacks": 50e6,
        "filing_date": pd.Timestamp("2025-11-14"),
        "is_ttm": True,
    }
    annual_only = normalize_company(history, normalization)
    anchored = normalize_company(history, normalization, ttm_row=ttm)
    assert annual_only is not None and anchored is not None
    assert anchored["anchor_source"] == "ttm"
    assert anchored["revenue"] == pytest.approx(1_200e6)
    assert anchored["shares_diluted"] == pytest.approx(95e6)
    assert anchored["current_operating_margin"] == pytest.approx(0.18)
    # Normalized earning power = full-cycle ANNUAL median margin x TTM revenue.
    assert anchored["normalized_operating_margin"] == pytest.approx(
        annual_only["normalized_operating_margin"]
    )
    assert anchored["normalized_operating_income"] == pytest.approx(0.15 * 1_200e6)
    assert anchored["net_debt"] == pytest.approx(100e6)
