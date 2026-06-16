"""Cross-asset spine skeleton (#7): registry, shared scorer, equity conformance."""
from __future__ import annotations

import weekly_us_stock.cross_asset  # noqa: F401  (import registers the equity plugin)
from weekly_us_stock.cross_asset.base import (
    AnchorModel,
    EligibilityGate,
    ReturnDistribution,
    RiskAggregator,
    RiskPreferences,
    ScenarioModel,
    ScenarioOutcome,
)
from weekly_us_stock.cross_asset.registry import get_asset_model, registered_asset_classes
from weekly_us_stock.models.valuation import CompanyInputs


def test_equity_plugin_registers_and_conforms_to_the_protocols() -> None:
    model = get_asset_model("equity")
    assert model.asset_class == "equity"
    assert "equity" in registered_asset_classes()
    # method-only protocols are runtime-checkable
    assert isinstance(model.eligibility_gate(), EligibilityGate)
    assert isinstance(model.anchor_model(), AnchorModel)
    assert isinstance(model.scenario_model(), ScenarioModel)


def test_shared_risk_aggregator_matches_the_equity_worst_case_formula() -> None:
    dist = ReturnDistribution(
        outcomes=(
            ScenarioOutcome("bear", 0.05, 0.25),
            ScenarioOutcome("base", 0.15, 0.50),
            ScenarioOutcome("bull", 0.25, 0.25),
        ),
    )
    score = RiskAggregator().score(dist, RiskPreferences(hurdle_rate=0.12, downside_aversion=1.0))
    assert score.worst_case == 0.05
    assert abs(score.median - 0.15) < 1e-9
    assert abs(score.worst_case_hurdle_gap - 0.07) < 1e-9  # 0.12 - 0.05
    # robust = conf*max(median-hurdle,0) - aversion*gap = 0.03 - 0.07 = -0.04
    assert abs(score.robust_return - (-0.04)) < 1e-9


def test_equity_scenario_model_emits_a_return_distribution() -> None:
    inputs = CompanyInputs(
        ticker="X", price=10.0, shares_outstanding=200.0, net_debt=0.0, latest_revenue=2500.0,
        normalized_operating_margin=0.15, current_operating_margin=0.15, tax_rate=0.21,
        hist_revenue_cagr=0.10, roic=0.18, wacc=0.10, cost_of_debt_after_tax=0.03,
    )
    dist = get_asset_model("equity").scenario_model().distribution(inputs)
    assert {o.label for o in dist.outcomes} == {"bear", "base", "bull"}
    assert all(0.0 <= o.probability <= 1.0 for o in dist.outcomes)
    # the shared scorer consumes the equity distribution unchanged
    score = RiskAggregator().score(dist, RiskPreferences())
    assert score.median == dist.median()
