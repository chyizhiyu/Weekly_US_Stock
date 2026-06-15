"""Invariants for the expense-method-with-fade SBC model (Task #2).

SBC is kept as a fading operating expense and is never returned to the share
count, so it is counted exactly once. A zero-SBC name must be unaffected.
"""
from __future__ import annotations

from weekly_us_stock.config import RiskPreferenceSettings, ScenarioSettings
from weekly_us_stock.models.valuation import CompanyInputs
from weekly_us_stock.valuation.scenarios import build_scenarios, value_company

_CFG = ScenarioSettings()
_PREFS = RiskPreferenceSettings()

_BASE = dict(
    ticker="X", price=10.0, shares_outstanding=200.0, net_debt=0.0,
    latest_revenue=2500.0, normalized_operating_margin=0.15,
    current_operating_margin=0.15, tax_rate=0.21, hist_revenue_cagr=0.20,
    roic=0.18, wacc=0.10, cost_of_debt_after_tax=0.03, net_share_change_rate=0.03,
)


def _base_share_change(inp: CompanyInputs) -> float:
    return {s.name: s for s in build_scenarios(inp, _CFG)}["base"].share_change_rate


def test_zero_sbc_is_invariant_to_the_sbc_machinery() -> None:
    # No SBC => the fade target, fade speed and dilution stripping are all no-ops.
    a = value_company(
        CompanyInputs(**_BASE, sbc_intensity=0.0, mature_sbc_intensity=0.02), _CFG, _PREFS
    )
    b = value_company(
        CompanyInputs(**_BASE, sbc_intensity=0.0, mature_sbc_intensity=0.10), _CFG, _PREFS
    )
    assert a.median_irr == b.median_irr
    assert a.intrinsic_value_base == b.intrinsic_value_base
    # The full historical net share change is kept (nothing stripped).
    assert _base_share_change(CompanyInputs(**_BASE, sbc_intensity=0.0)) == 0.03


def test_sbc_is_stripped_from_dilution_and_floored_for_a_diluter() -> None:
    # proxy (0.06 * 2500 / 2000 = 0.075) exceeds the +3% net issuance, so the
    # residual dilution floors at 0 rather than manufacturing a phantom buyback.
    hi = CompanyInputs(**_BASE, sbc_intensity=0.06, mature_sbc_intensity=0.03)
    assert _base_share_change(hi) == 0.0
    # A moderate-SBC diluter keeps the non-SBC remainder of its dilution.
    mod = CompanyInputs(
        **{**_BASE, "net_share_change_rate": 0.05}, sbc_intensity=0.01, mature_sbc_intensity=0.01
    )
    proxy = 0.01 * 2500.0 / 2000.0
    assert abs(_base_share_change(mod) - (0.05 - proxy)) < 1e-9


def test_per_scenario_fade_speed_is_bear_slow_bull_fast() -> None:
    scs = {
        s.name: s
        for s in build_scenarios(
            CompanyInputs(**_BASE, sbc_intensity=0.06, mature_sbc_intensity=0.03), _CFG
        )
    }
    assert scs["bear"].sbc_fade_speed < scs["base"].sbc_fade_speed < scs["bull"].sbc_fade_speed


def test_fading_sbc_toward_a_lower_target_lifts_value() -> None:
    # Identical company; only difference is whether SBC normalizes. More fade
    # (a lower mature target) expands the effective margin and raises value.
    no_fade = value_company(
        CompanyInputs(**_BASE, sbc_intensity=0.06, mature_sbc_intensity=0.06), _CFG, _PREFS
    )
    fade = value_company(
        CompanyInputs(**_BASE, sbc_intensity=0.06, mature_sbc_intensity=0.03), _CFG, _PREFS
    )
    assert fade.intrinsic_value_base > no_fade.intrinsic_value_base
    assert fade.median_irr > no_fade.median_irr
