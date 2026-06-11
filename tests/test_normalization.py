"""Layer-2 normalization: one-offs, cyclical peaks, SBC as a real expense."""

from __future__ import annotations

import pandas as pd
import pytest

from weekly_us_stock.config import NormalizationSettings
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
