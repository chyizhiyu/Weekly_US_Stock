"""P1-2: boundary-assumption flags + extreme-valuation alerts."""

from __future__ import annotations

from weekly_us_stock.config import AlertSettings, RiskPreferenceSettings, ScenarioSettings
from weekly_us_stock.models.valuation import CompanyInputs
from weekly_us_stock.valuation.scenarios import (
    detect_assumption_flags,
    value_company,
)


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


def test_detect_assumption_flags_at_each_bound() -> None:
    cfg = ScenarioSettings()
    assert "base_growth_cap_hit" in detect_assumption_flags(_inputs(hist_revenue_cagr=0.50), cfg)
    assert "base_growth_floor_hit" in detect_assumption_flags(_inputs(hist_revenue_cagr=-0.50), cfg)
    assert "forward_roic_cap_hit" in detect_assumption_flags(_inputs(roic=0.90), cfg)
    assert "share_change_cap_hit" in detect_assumption_flags(
        _inputs(net_share_change_rate=0.20), cfg
    )
    flags = detect_assumption_flags(_inputs(wacc=0.14), cfg, wacc_bounds=(0.065, 0.14))
    assert "wacc_cap_hit" in flags


def test_base_growth_cap_lowers_model_confidence() -> None:
    # OMC analogue: base growth pinned at the configured cap.
    valuation = value_company(
        _inputs(hist_revenue_cagr=0.50), ScenarioSettings(), RiskPreferenceSettings()
    )
    assert "base_growth_cap_hit" in valuation.assumption_flags
    # a boundary hit must not read as a precise estimate: confidence is cut
    assert valuation.model_confidence < 1.0


def test_extreme_valuation_triggers_manual_review() -> None:
    # CF analogue: a deeply mispriced entry price makes base intrinsic dwarf
    # price and the bull case run away -> manual review, not a clean estimate.
    valuation = value_company(_inputs(price=4.0), ScenarioSettings(), RiskPreferenceSettings())
    assert valuation.requires_manual_review is True
    assert valuation.valuation_alerts  # non-empty
    assert "intrinsic_3x_price" in valuation.valuation_alerts


def test_alert_thresholds_are_configurable() -> None:
    inputs = _inputs(price=4.0)
    strict = value_company(inputs, ScenarioSettings(), RiskPreferenceSettings(),
                           alerts=AlertSettings(intrinsic_to_price_review=3.0))
    lax = value_company(inputs, ScenarioSettings(), RiskPreferenceSettings(),
                        alerts=AlertSettings(intrinsic_to_price_review=1e9,
                                             median_irr_review=1e9,
                                             bull_return_review=1e9,
                                             scenario_span_review=1e9))
    assert "intrinsic_3x_price" in strict.valuation_alerts
    assert lax.valuation_alerts == []  # nothing crosses the (huge) thresholds
