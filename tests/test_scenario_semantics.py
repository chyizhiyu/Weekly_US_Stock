"""P1-1: named bear/base/bull vs statistical low/base/high; order inversions."""

from __future__ import annotations

import pytest

from weekly_us_stock.config import RiskPreferenceSettings, ScenarioSettings
from weekly_us_stock.models.valuation import CompanyInputs, ScenarioAssumptions
from weekly_us_stock.valuation.scenarios import _scenario_order_note, value_company


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
        hist_revenue_cagr=0.08,
        roic=0.18,
        wacc=0.09,
        cost_of_debt_after_tax=0.03,
    )
    base.update(overrides)
    return CompanyInputs(**base)  # type: ignore[arg-type]


def test_interval_brackets_named_values_by_construction() -> None:
    valuation = value_company(_inputs(), ScenarioSettings(), RiskPreferenceSettings())
    named = (
        valuation.intrinsic_value_bear,
        valuation.intrinsic_value_base,
        valuation.intrinsic_value_bull,
    )
    # statistical interval is always ordered; named values are kept separately
    assert valuation.intrinsic_value_low == min(named)
    assert valuation.intrinsic_value_high == max(named)
    assert (
        valuation.intrinsic_value_low
        <= valuation.intrinsic_value_base
        <= valuation.intrinsic_value_high
    )


@pytest.mark.parametrize(
    "overrides",
    [
        {"roic": 0.30, "wacc": 0.08},  # healthy, monotone
        {"roic": 0.03, "wacc": 0.14, "hist_revenue_cagr": 0.20},  # ROIC << WACC
        {"roic": 0.06, "wacc": 0.10, "net_debt": 5000.0},  # leveraged
        {"roic": 0.18, "wacc": 0.09, "net_share_change_rate": -0.05},  # buybacks
    ],
)
def test_inversion_flag_matches_actual_ordering(overrides: dict) -> None:
    valuation = value_company(_inputs(**overrides), ScenarioSettings(), RiskPreferenceSettings())
    bear, base, bull = (
        valuation.intrinsic_value_bear,
        valuation.intrinsic_value_base,
        valuation.intrinsic_value_bull,
    )
    monotone = bear <= base <= bull
    # the flag is exactly "not monotone", never assumed away
    assert valuation.scenario_order_inversion == (not monotone)
    assert (valuation.scenario_order_note is not None) == valuation.scenario_order_inversion
    # the statistical interval brackets every named value by construction
    assert valuation.intrinsic_value_low == min(bear, base, bull)
    assert valuation.intrinsic_value_high == max(bear, base, bull)


def test_scenario_order_note_explains_growth_value_destruction() -> None:
    sub_cost = ScenarioAssumptions(
        name="base", probability=0.5, revenue_growth_y1=0.10, terminal_growth=0.02,
        operating_margin=0.15, forward_roic=0.05, terminal_roic=0.09, share_change_rate=0.0,
    )
    assert "destroys value" in _scenario_order_note(_inputs(wacc=0.12), sub_cost)
    above_cost = sub_cost.model_copy(update={"forward_roic": 0.25})
    assert "not monotone" in _scenario_order_note(_inputs(wacc=0.09), above_cost)
