"""Task #3-A: MAD-based one-off detection and its confidence haircut."""
from __future__ import annotations

import pandas as pd

from weekly_us_stock.config import NormalizationSettings
from weekly_us_stock.steps.step4_normalized import _data_confidence
from weekly_us_stock.valuation.normalize import (
    _mad_anomaly,
    _one_off_suspected,
    normalize_company,
)

_S = NormalizationSettings()


def test_mad_anomaly_excludes_latest_and_floors_zero_mad() -> None:
    # Flat history then a spike: MAD is 0, so the absolute floor (not div-by-zero)
    # governs and the spike still reads as large. The latest point is excluded
    # from the baseline it is judged against.
    z = _mad_anomaly(pd.Series([0.10, 0.10, 0.10, 0.10, 0.30]), _S.one_off_mad_abs_floor)
    assert z > 10
    # A tiny wobble on a flat history is NOT amplified into a false anomaly.
    small = _mad_anomaly(pd.Series([0.10, 0.10, 0.10, 0.10, 0.105]), _S.one_off_mad_abs_floor)
    assert abs(small) < 1.0
    # Too little history -> no signal.
    assert _mad_anomaly(pd.Series([0.10, 0.20]), _S.one_off_mad_abs_floor) == 0.0


def test_one_off_suspected_requires_an_uncorroborated_margin_spike() -> None:
    assert _one_off_suspected(18.0, 0.2, _S) is True    # margin spike, OCF flat -> one-off
    assert _one_off_suspected(18.0, 16.0, _S) is False   # both move -> real improvement
    assert _one_off_suspected(18.0, 2.0, _S) is True     # same direction, not comparable
    assert _one_off_suspected(-18.0, -16.0, _S) is False  # both fall together -> real
    assert _one_off_suspected(18.0, -16.0, _S) is True   # opposite directions -> not corroborated
    assert _one_off_suspected(2.0, 0.0, _S) is False     # within the band


def test_one_off_flag_docks_data_confidence_by_the_penalty() -> None:
    base = {
        "years_of_data": 8, "has_estimates": True, "beta": 1.0,
        "is_price_fresh": True, "anchor_source": "ttm",
    }
    clean = _data_confidence({**base, "one_off_suspected": False}, _S)
    flagged = _data_confidence({**base, "one_off_suspected": True}, _S)
    assert abs((clean - flagged) - _S.one_off_confidence_penalty) < 1e-9


def test_ttm_current_anchor_is_checked_for_one_offs() -> None:
    annual = pd.DataFrame(
        [
            {
                "fiscal_year": year,
                "filing_date": f"{year + 1}-02-01",
                "revenue": 100.0,
                "gross_profit": 50.0,
                "operating_income": 10.0,
                "one_off_items": 0.0,
                "net_income": 8.0,
                "ocf": 10.0,
                "capex": 2.0,
                "depreciation": 2.0,
                "sbc": 1.0,
                "dividends_paid": 0.0,
                "buybacks": 0.0,
                "shares_diluted": 10.0,
                "total_debt": 5.0,
                "cash": 1.0,
                "interest_expense": 1.0,
                "total_equity": 20.0,
                "effective_tax_rate": 0.21,
            }
            for year in range(2020, 2025)
        ]
    )
    ttm = {
        **annual.iloc[-1].to_dict(),
        "is_ttm": True,
        "revenue": 100.0,
        "operating_income": 30.0,
        "ocf": 10.0,
    }

    metrics = normalize_company(annual, _S, ttm)
    assert metrics is not None
    assert metrics["anchor_source"] == "ttm"
    assert metrics["cashflow_period_semantics"] == "unknown"
    assert metrics["ttm_cashflow_status"] == "unverified"
    assert metrics["one_off_suspected"] is True
