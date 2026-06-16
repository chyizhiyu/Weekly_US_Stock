"""Layer-3 scenario engine: value-creation mechanics the thesis depends on."""

from __future__ import annotations

import pytest

from weekly_us_stock.config import RiskPreferenceSettings, ScenarioSettings
from weekly_us_stock.models.valuation import CompanyInputs, ScenarioAssumptions
from weekly_us_stock.valuation.scenarios import (
    _terminal_value,
    build_scenarios,
    value_company,
    value_scenario,
)

CFG = ScenarioSettings()
PREFS = RiskPreferenceSettings()


def _inputs(**overrides) -> CompanyInputs:
    base = {
        "ticker": "TEST",
        "price": 50.0,
        "shares_outstanding": 100e6,
        "net_debt": 0.0,
        "latest_revenue": 2_000e6,
        "normalized_operating_margin": 0.25,
        "current_operating_margin": 0.25,
        "tax_rate": 0.21,
        "hist_revenue_cagr": 0.08,
        "roic": 0.18,
        "incremental_roic": 0.18,
        "wacc": 0.09,
        "cost_of_debt_after_tax": 0.04,
        "financial_persistence": 0.7,
        "cyclicality": 0.03,
        "margin_volatility": 0.01,
        "net_share_change_rate": 0.0,
        "data_confidence": 1.0,
        "model_confidence": 1.0,
    }
    base.update(overrides)
    return CompanyInputs(**base)


def _base_assumption(**overrides) -> ScenarioAssumptions:
    fields = {
        "name": "base",
        "probability": 1.0,
        "revenue_growth_y1": 0.08,
        "terminal_growth": 0.025,
        "operating_margin": 0.25,
        "forward_roic": 0.18,
        "terminal_roic": 0.15,
        "share_change_rate": 0.0,
    }
    fields.update(overrides)
    return ScenarioAssumptions(**fields)


class TestValueCreationMechanics:
    def test_terminal_value_collapses_when_roic_equals_wacc(self) -> None:
        # ROIC == WACC means growth adds nothing: TV must equal NOPAT/WACC
        # regardless of the assumed terminal growth rate.
        nopat = 100e6
        wacc = 0.09
        slow_growth = _base_assumption(terminal_growth=0.01, terminal_roic=wacc)
        fast_growth = _base_assumption(terminal_growth=0.03, terminal_roic=wacc)
        slow = _terminal_value(nopat, slow_growth, wacc)
        fast = _terminal_value(nopat, fast_growth, wacc)
        assert slow == pytest.approx(nopat / wacc, rel=1e-6)
        assert fast == pytest.approx(nopat / wacc, rel=1e-6)

    def test_growth_without_roic_does_not_earn_a_high_value(self) -> None:
        # Same 20% growth; one company reinvests at 6% ROIC (below 9% WACC),
        # the other at 20%. The low-ROIC grower must be worth much less.
        low_roic = value_scenario(
            _inputs(),
            _base_assumption(revenue_growth_y1=0.20, forward_roic=0.06, terminal_roic=0.09),
            CFG,
        )
        high_roic = value_scenario(
            _inputs(),
            _base_assumption(revenue_growth_y1=0.20, forward_roic=0.20, terminal_roic=0.15),
            CFG,
        )
        assert low_roic.intrinsic_value_per_share < high_roic.intrinsic_value_per_share * 0.75
        assert (low_roic.irr_5y or -1) < (high_roic.irr_5y or -1)

    def test_dilution_reduces_per_share_value(self) -> None:
        flat = value_scenario(_inputs(), _base_assumption(share_change_rate=0.0), CFG)
        diluted = value_scenario(_inputs(), _base_assumption(share_change_rate=0.06), CFG)
        assert (diluted.irr_5y or -1) < (flat.irr_5y or -1)
        assert diluted.total_return_5y < flat.total_return_5y

    def test_buybacks_below_intrinsic_value_raise_per_share_returns(self) -> None:
        # Price (50) is well below intrinsic value here, so retiring shares
        # creates per-share value even after charging the buyback cash cost.
        flat = value_scenario(_inputs(), _base_assumption(share_change_rate=0.0), CFG)
        buyback = value_scenario(_inputs(), _base_assumption(share_change_rate=-0.03), CFG)
        assert flat.intrinsic_value_per_share > 50.0
        assert (buyback.irr_5y or -1) > (flat.irr_5y or -1)

    def test_scenarios_anchor_at_normalized_margin(self) -> None:
        # Peak-cycle company: current margin 16%, normalized 7.5%. The base
        # case must be built on the normalized margin, not today's peak.
        inputs = _inputs(
            normalized_operating_margin=0.075,
            current_operating_margin=0.16,
            margin_volatility=0.04,
        )
        scenarios = {a.name: a for a in build_scenarios(inputs, CFG)}
        assert scenarios["base"].operating_margin == pytest.approx(0.075)
        assert scenarios["bear"].operating_margin < 0.075
        assert scenarios["bull"].operating_margin < 0.16

    def test_weak_moat_widens_scenario_spread(self) -> None:
        narrow = build_scenarios(_inputs(financial_persistence=0.9), CFG)
        wide = build_scenarios(_inputs(financial_persistence=0.1), CFG)

        def spread(scenarios) -> float:
            by_name = {a.name: a for a in scenarios}
            return by_name["bull"].revenue_growth_y1 - by_name["bear"].revenue_growth_y1

        assert spread(wide) > spread(narrow)

    def test_bear_case_has_no_terminal_value_creation(self) -> None:
        scenarios = {a.name: a for a in build_scenarios(_inputs(), CFG)}
        assert scenarios["bear"].terminal_roic == pytest.approx(_inputs().wacc)
        assert scenarios["base"].terminal_roic > scenarios["bear"].terminal_roic


class TestAggregation:
    def test_distribution_metrics(self) -> None:
        valuation = value_company(_inputs(), CFG, PREFS)
        assert valuation.p10_irr <= valuation.median_irr <= valuation.p90_irr
        assert 0.0 <= valuation.above_hurdle_weight <= 1.0
        assert 0.0 <= valuation.permanent_loss_weight <= 1.0
        assert valuation.worst_case_shortfall >= 0.0
        assert valuation.worst_case_hurdle_gap >= 0.0
        assert valuation.expected_shortfall == pytest.approx(valuation.worst_case_shortfall)
        assert valuation.hurdle_cvar == pytest.approx(valuation.worst_case_hurdle_gap)
        assert valuation.expected_shortfall >= 0.0
        assert valuation.hurdle_cvar >= 0.0
        assert valuation.intrinsic_value_low <= valuation.intrinsic_value_high
        probabilities = [s.assumptions.probability for s in valuation.scenarios]
        assert sum(probabilities) == pytest.approx(1.0)

    def test_lower_confidence_raises_model_uncertainty(self) -> None:
        confident = value_company(_inputs(), CFG, PREFS)
        uncertain = value_company(
            _inputs(model_confidence=0.4, data_confidence=0.5), CFG, PREFS
        )
        assert uncertain.model_uncertainty > confident.model_uncertainty
