"""P1-4: negative / undefined ROIC is routed, not silently valued at 2%."""

from __future__ import annotations

import pandas as pd

from weekly_us_stock.config import RiskPreferenceSettings, ScenarioSettings
from weekly_us_stock.models.valuation import CompanyInputs
from weekly_us_stock.steps.step6_valuation import run_scenario_valuations
from weekly_us_stock.valuation.scenarios import classify_roic


def _inputs(**overrides: object) -> CompanyInputs:
    base = dict(
        ticker="TST",
        price=100.0,
        shares_outstanding=100.0,
        net_debt=0.0,
        latest_revenue=1000.0,
        normalized_operating_margin=0.15,
        current_operating_margin=0.15,
        tax_rate=0.21,
        hist_revenue_cagr=0.06,
        roic=0.18,
        wacc=0.09,
        cost_of_debt_after_tax=0.03,
    )
    base.update(overrides)
    return CompanyInputs(**base)  # type: ignore[arg-type]


def test_classify_roic_distinguishes_cases() -> None:
    assert classify_roic(_inputs(roic=0.18)) == "ok"
    # profitable but ROIC < 0 -> negative invested capital, ratio meaningless
    profitable_negative = _inputs(roic=-0.20, normalized_operating_margin=0.15)
    assert classify_roic(profitable_negative) == "meaningless_capital"
    # loss-making -> genuine negative operating return
    loss_making = _inputs(roic=-0.20, normalized_operating_margin=-0.05)
    assert classify_roic(loss_making) == "negative_returns"
    assert classify_roic(_inputs(roic=float("nan"))) == "data_anomaly"


def _quality_row(ticker: str, roic: float, margin: float) -> dict:
    return {
        "ticker": ticker,
        "price": 100.0,
        "shares_diluted": 100.0,
        "net_debt": 0.0,
        "revenue": 1000.0,
        "normalized_operating_margin": margin,
        "current_operating_margin": margin,
        "tax_rate": 0.21,
        "revenue_cagr": 0.06,
        "roic": roic,
        "wacc": 0.09,
        "cost_of_debt_after_tax": 0.03,
        "financial_persistence_score": 0.6,
        "data_confidence": 1.0,
        "model_confidence": 1.0,
        "name": f"{ticker} Corp",
        "sector": "Technology",
        "industry": "Software",
        "market_cap": 10_000.0,
    }


def test_step6_routes_non_meaningful_roic_to_watchlist() -> None:
    frame = pd.DataFrame(
        [
            _quality_row("OK", roic=0.15, margin=0.15),
            _quality_row("NEGCAP", roic=-0.10, margin=0.15),  # meaningless_capital
        ]
    )
    result = run_scenario_valuations(frame, ScenarioSettings(), RiskPreferenceSettings())

    assert set(result.metrics["ticker"]) == {"OK"}  # only the meaningful one is valued
    assert set(result.roic_routed["ticker"]) == {"NEGCAP"}
    routed = result.roic_routed.iloc[0]
    assert routed["roic_status"] == "meaningless_capital"
    assert routed["watchlist_reason"] == "roic_not_meaningful:meaningless_capital"
    assert routed["name"] == "NEGCAP Corp"
    assert routed["sector"] == "Technology"
    assert routed["financial_persistence_score"] == 0.6
    # the negative-ROIC name never received a forward 2% valuation
    assert "NEGCAP" not in set(result.scenario_rows.get("ticker", pd.Series(dtype=str)))
