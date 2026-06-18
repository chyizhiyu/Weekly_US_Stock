from __future__ import annotations

import pandas as pd
import pytest

from weekly_us_stock.config import (
    RiskPreferenceSettings,
    SpecialistModelSettings,
    WaccSettings,
)
from weekly_us_stock.steps.step6_specialists import run_specialist_valuations
from weekly_us_stock.valuation.industry import BANK, REIT
from weekly_us_stock.valuation.ranking import add_robust_components


def _candidate(ticker: str, family: str, price: float) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "ticker": ticker,
                "name": ticker,
                "sector": "Financial Services" if family == BANK else "Real Estate",
                "industry": "Banks - Regional" if family == BANK else "REIT - Diversified",
                "model_family": family,
                "watchlist_reason": f"{family}_model_not_supported",
                "price": price,
                "price_as_of": "2026-06-12",
                "is_price_fresh": True,
                "market_cap": price * 100.0,
                "shares_outstanding": 100.0,
                "beta": 1.0,
            }
        ]
    )


def _bank_history(ticker: str = "BNK") -> pd.DataFrame:
    rows = []
    for idx, year in enumerate(range(2021, 2026), start=1):
        equity = 900.0 + idx * 40.0
        rows.append(
            {
                "ticker": ticker,
                "fiscal_year": year,
                "net_income": equity * 0.12,
                "total_equity": equity,
                "depreciation": 0.0,
                "shares_diluted": 100.0,
            }
        )
    return pd.DataFrame(rows)


def _reit_history(ticker: str = "RLT") -> pd.DataFrame:
    rows = []
    for idx, year in enumerate(range(2021, 2026), start=1):
        rows.append(
            {
                "ticker": ticker,
                "fiscal_year": year,
                "net_income": 70.0 + idx * 4.0,
                "depreciation": 65.0 + idx * 2.0,
                "total_equity": 1_000.0,
                "shares_diluted": 100.0,
            }
        )
    return pd.DataFrame(rows)


def test_bank_specialist_outputs_rank_compatible_metrics() -> None:
    prefs = RiskPreferenceSettings()
    result = run_specialist_valuations(
        _candidate("BNK", BANK, 10.0),
        _bank_history("BNK"),
        risk_free=0.04,
        settings=SpecialistModelSettings(),
        wacc_settings=WaccSettings(),
        risk_preferences=prefs,
    )

    assert result.watchlist.empty
    row = result.metrics.iloc[0]
    assert row["model_family"] == BANK
    assert row["intrinsic_value_base"] > row["price"]
    assert row["median_irr"] > 0
    assert row["model_confidence"] == pytest.approx(0.60)
    scored = add_robust_components(result.metrics, prefs)
    assert "robust_return" in scored


def test_reit_specialist_uses_affo_proxy() -> None:
    result = run_specialist_valuations(
        _candidate("RLT", REIT, 15.0),
        _reit_history("RLT"),
        risk_free=0.04,
        settings=SpecialistModelSettings(),
        wacc_settings=WaccSettings(),
        risk_preferences=RiskPreferenceSettings(),
    )

    assert result.watchlist.empty
    row = result.metrics.iloc[0]
    assert row["model_family"] == REIT
    assert row["intrinsic_value_base"] > 0
    assert "P/AFFO" in row["specialist_model_note"]
    assert set(result.scenario_rows["scenario"]) == {"bear", "base", "bull"}


def test_specialist_fails_closed_on_missing_history() -> None:
    result = run_specialist_valuations(
        _candidate("BNK", BANK, 10.0),
        pd.DataFrame(columns=["ticker", "fiscal_year"]),
        risk_free=0.04,
        settings=SpecialistModelSettings(),
        wacc_settings=WaccSettings(),
        risk_preferences=RiskPreferenceSettings(),
    )

    assert result.metrics.empty
    assert result.watchlist.iloc[0]["watchlist_reason"] == "specialist_missing_fundamentals"
