"""P0-1: non-finite and implausibly high valuations must fail closed.

Covers the IRR solver status enum, the validity classifier, end-to-end routing
through value_company, and the step6 valid/invalid partition. Catastrophic
below-bound losses remain in the risk distribution.
"""

from __future__ import annotations

import math

import pandas as pd

from weekly_us_stock.config import RiskPreferenceSettings, ScenarioSettings
from weekly_us_stock.models.valuation import CompanyInputs, ScenarioAssumptions, ScenarioValuation
from weekly_us_stock.steps.step6_valuation import run_scenario_valuations
from weekly_us_stock.valuation.irr import (
    LOWER_BOUND,
    UPPER_BOUND,
    solve_irr,
    solve_irr_detailed,
)
from weekly_us_stock.valuation.scenarios import _classify_validity, value_company

# -- IRR solver status -----------------------------------------------------------


def test_solve_irr_detailed_distinguishes_states() -> None:
    assert solve_irr_detailed([-100.0, 110.0]).status == "valid"
    assert solve_irr_detailed([float("nan"), 1.0]).status == "non_finite_input"
    assert solve_irr_detailed([float("inf"), 1.0]).status == "non_finite_input"
    assert solve_irr_detailed([100.0]).status == "degenerate_input"  # too short
    assert solve_irr_detailed([100.0, 110.0]).status == "degenerate_input"  # no outlay
    # IRR far above 200%: still positive NPV at the upper bound.
    assert solve_irr_detailed([-1.0, 1000.0]).status == "above_upper_bound"
    # IRR below -95%: NPV already negative at the lower bound.
    assert solve_irr_detailed([-100.0, 1.0]).status == "below_lower_bound"


def test_solve_irr_wrapper_returns_none_unless_valid() -> None:
    assert solve_irr([-1.0, 1000.0]) is None  # above upper bound
    assert solve_irr([-100.0, 1.0]) is None  # below lower bound
    assert solve_irr([float("nan"), 1.0]) is None
    rate = solve_irr([-100.0, 130.0])
    assert rate is not None and math.isfinite(rate)
    assert LOWER_BOUND < rate < UPPER_BOUND  # never returns a bound as a rate


# -- validity classifier ---------------------------------------------------------


def _scenario(name: str, *, status: str = "valid", finite: bool = True) -> ScenarioValuation:
    return ScenarioValuation(
        assumptions=ScenarioAssumptions(
            name=name,  # type: ignore[arg-type]
            probability=0.33,
            revenue_growth_y1=0.05,
            terminal_growth=0.02,
            operating_margin=0.15,
            forward_roic=0.15,
            terminal_roic=0.10,
            share_change_rate=0.0,
        ),
        intrinsic_value_per_share=100.0,
        irr_3y=0.1,
        irr_5y=0.1,
        exit_value_per_share=120.0,
        total_return_5y=0.5,
        reinvestment_rate_y1=0.3,
        irr_5y_status=status,
        is_finite=finite,
    )


_OK_METRICS = {
    "expected_irr": 0.1,
    "median_irr": 0.12,
    "p10_irr": -0.2,
    "p90_irr": 0.4,
    "hurdle_cvar": 0.03,
    "expected_shortfall": 0.1,
    "intrinsic_value_base": 100.0,
}


def test_classify_validity_passes_clean_valuation() -> None:
    scenarios = [_scenario(n) for n in ("bear", "base", "bull")]
    status, reason, fields = _classify_validity(scenarios, _OK_METRICS)
    assert status == "valid" and reason is None and fields == []


def test_classify_validity_flags_irr_above_bound() -> None:
    scenarios = [
        _scenario("bear"),
        _scenario("base"),
        _scenario("bull", status="above_upper_bound"),
    ]
    status, reason, fields = _classify_validity(scenarios, _OK_METRICS)
    assert status == "invalid"
    assert reason == "irr_above_solver_bound"
    assert "irr_5y[bull]" in fields


def test_classify_validity_keeps_below_bound_loss_but_rejects_non_finite() -> None:
    below = [_scenario("bear", status="below_lower_bound"), _scenario("base"), _scenario("bull")]
    assert _classify_validity(below, _OK_METRICS) == ("valid", None, [])

    no_root = [_scenario("bear", status="no_root"), _scenario("base"), _scenario("bull")]
    assert _classify_validity(no_root, _OK_METRICS)[0] == "invalid"

    bad_metrics = {**_OK_METRICS, "median_irr": float("nan")}
    status, reason, fields = _classify_validity(
        [_scenario(n) for n in ("bear", "base", "bull")], bad_metrics
    )
    assert status == "invalid" and reason == "invalid_valuation_output"
    assert "median_irr" in fields

    non_finite_scn = [_scenario("bear", finite=False), _scenario("base"), _scenario("bull")]
    assert _classify_validity(non_finite_scn, _OK_METRICS)[0] == "invalid"


# -- end-to-end through value_company --------------------------------------------


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
        hist_revenue_cagr=0.05,
        roic=0.15,
        wacc=0.09,
        cost_of_debt_after_tax=0.03,
    )
    base.update(overrides)
    return CompanyInputs(**base)  # type: ignore[arg-type]


def test_value_company_normal_inputs_are_valid() -> None:
    valuation = value_company(_inputs(), ScenarioSettings(), RiskPreferenceSettings())
    assert valuation.valuation_status == "valid"
    assert all(
        math.isfinite(v)
        for v in (valuation.expected_irr, valuation.median_irr, valuation.hurdle_cvar)
    )


def test_value_company_tiny_price_is_flagged_above_bound() -> None:
    # A near-zero entry price makes every annual payoff dwarf the outlay, so the
    # IRR blows past the 200% solver cap -> data artifact, not an opportunity.
    valuation = value_company(_inputs(price=0.01), ScenarioSettings(), RiskPreferenceSettings())
    assert valuation.valuation_status == "invalid"
    assert valuation.invalid_reason == "irr_above_solver_bound"


# -- step6 partition -------------------------------------------------------------


def _quality_row(ticker: str, price: float) -> dict:
    return {
        "ticker": ticker,
        "price": price,
        "shares_diluted": 100.0,
        "net_debt": 0.0,
        "revenue": 1000.0,
        "normalized_operating_margin": 0.15,
        "current_operating_margin": 0.15,
        "tax_rate": 0.21,
        "revenue_cagr": 0.05,
        "roic": 0.15,
        "wacc": 0.09,
        "cost_of_debt_after_tax": 0.03,
        "financial_persistence_score": 0.6,
        "data_confidence": 1.0,
        "model_confidence": 1.0,
    }


def test_step6_partitions_invalid_out_of_metrics() -> None:
    frame = pd.DataFrame([_quality_row("GOOD", 100.0), _quality_row("ARTIFACT", 0.01)])
    result = run_scenario_valuations(frame, ScenarioSettings(), RiskPreferenceSettings())

    assert set(result.metrics["ticker"]) == {"GOOD"}
    assert set(result.invalid["ticker"]) == {"ARTIFACT"}
    assert result.invalid.iloc[0]["invalid_reason"] == "irr_above_solver_bound"
    # nothing silently lost: every company is either ranked or flagged
    assert len(result.metrics) + len(result.invalid) == 2
    # every value used for ranking is finite
    for col in ("expected_irr", "median_irr", "p10_irr", "p90_irr", "hurdle_cvar"):
        assert result.metrics[col].map(math.isfinite).all()
    assert "catastrophic_tail_floor_applied" in result.metrics.columns


def test_step6_keeps_catastrophic_loss_in_rankable_risk_distribution() -> None:
    row = _quality_row("TAIL", 100.0)
    row["net_debt"] = 5_000.0
    result = run_scenario_valuations(
        pd.DataFrame([row]), ScenarioSettings(), RiskPreferenceSettings()
    )

    assert set(result.metrics["ticker"]) == {"TAIL"}
    assert result.invalid.empty
    metric = result.metrics.iloc[0]
    assert bool(metric["catastrophic_tail_floor_applied"])
    assert metric["catastrophic_tail_scenarios"] == "bear;base;bull"
    assert metric["p10_irr"] == LOWER_BOUND
