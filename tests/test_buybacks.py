"""P1-3: buybacks are FCF-constrained and decay; dilution is never weakened."""

from __future__ import annotations

from weekly_us_stock.config import RiskPreferenceSettings, ScenarioSettings
from weekly_us_stock.models.valuation import CompanyInputs, CompanyValuation, ScenarioValuation
from weekly_us_stock.valuation.scenarios import _buyback_blocked, value_company


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


def _base(valuation: CompanyValuation) -> ScenarioValuation:
    return next(s for s in valuation.scenarios if s.assumptions.name == "base")


def test_buyback_blocked_on_high_leverage_or_losses() -> None:
    cfg = ScenarioSettings()
    assert _buyback_blocked(_inputs(net_debt=0.0), cfg) is False
    assert _buyback_blocked(_inputs(net_debt=100_000.0), cfg) is True  # >> 4x NOPAT
    assert _buyback_blocked(_inputs(net_debt=50.0, normalized_operating_margin=-0.10), cfg) is True


def test_unaffordable_buyback_does_not_shrink_shares() -> None:
    # Loss-making: no positive distributable FCF, so the buyback cannot execute.
    loss = value_company(
        _inputs(
            normalized_operating_margin=-0.05,
            current_operating_margin=-0.05,
            net_share_change_rate=-0.05,
        ),
        ScenarioSettings(),
        RiskPreferenceSettings(),
    )
    assert _base(loss).ending_shares >= 0.999 * 100.0  # essentially flat - no buyback
    # A healthy company with the same buyback intent DOES retire shares.
    healthy = value_company(
        _inputs(net_share_change_rate=-0.05), ScenarioSettings(), RiskPreferenceSettings()
    )
    assert _base(healthy).ending_shares < 100.0


def test_buyback_decays_below_the_mechanical_path() -> None:
    cfg = ScenarioSettings()
    healthy = value_company(
        _inputs(net_share_change_rate=-0.05), cfg, RiskPreferenceSettings()
    )
    realized = _base(healthy).ending_shares
    mechanical = 100.0 * (1.0 - 0.05) ** cfg.horizon_years  # old unconditional shrink
    assert realized > mechanical  # decay + FCF cap -> shrank less than mechanical


def test_dilution_persists_at_full_rate() -> None:
    cfg = ScenarioSettings()
    diluter = value_company(_inputs(net_share_change_rate=0.05), cfg, RiskPreferenceSettings())
    expected = 100.0 * (1.05) ** cfg.horizon_years
    assert abs(_base(diluter).ending_shares - expected) < 1e-6  # dilution not decayed


def test_bear_scenario_drops_buybacks() -> None:
    valuation = value_company(
        _inputs(net_share_change_rate=-0.05), ScenarioSettings(), RiskPreferenceSettings()
    )
    bear = next(s for s in valuation.scenarios if s.assumptions.name == "bear")
    assert bear.assumptions.share_change_rate == 0.0  # bear does not assume buybacks
