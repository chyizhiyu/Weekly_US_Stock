from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

ScenarioName = Literal["bear", "base", "bull"]


class CompanyInputs(BaseModel):
    """Everything the scenario engine needs for one company.

    All monetary fields share one currency unit (the pipeline uses USD
    millions); price and per-share values are in USD per share.
    """

    ticker: str
    price: float
    shares_outstanding: float
    net_debt: float
    latest_revenue: float
    normalized_operating_margin: float
    current_operating_margin: float
    tax_rate: float
    hist_revenue_cagr: float
    analyst_growth: float | None = None
    analyst_dispersion: float | None = None
    roic: float
    incremental_roic: float | None = None
    wacc: float
    cost_of_debt_after_tax: float
    financial_persistence: float = 0.5  # 0..1, HISTORICAL persistence evidence only
    cyclicality: float = 0.0  # stdev of yoy revenue growth
    margin_volatility: float = 0.0  # stdev of operating margin
    net_share_change_rate: float = 0.0  # historical net share count CAGR (+ dilutes)
    data_confidence: float = 1.0
    model_confidence: float = 1.0


class ScenarioAssumptions(BaseModel):
    name: ScenarioName
    probability: float
    revenue_growth_y1: float
    terminal_growth: float
    operating_margin: float
    forward_roic: float
    terminal_roic: float
    share_change_rate: float


class ScenarioValuation(BaseModel):
    assumptions: ScenarioAssumptions
    intrinsic_value_per_share: float
    irr_3y: float | None
    irr_5y: float | None
    exit_value_per_share: float
    total_return_5y: float
    reinvestment_rate_y1: float
    projected_fcf: list[float] = Field(default_factory=list)
    # P1-3: realized share count at the horizon after FCF-constrained, decaying
    # buybacks (or persistent dilution) - never the mechanical (1+rate)^h path.
    ending_shares: float = 0.0
    # P0-1: WHY the 5y IRR could (not) be solved, and whether every projected
    # output for this scenario is a finite number. Drives fail-closed routing.
    irr_5y_status: str = "valid"
    is_finite: bool = True


class CompanyValuation(BaseModel):
    """Scenario-weighted valuation metrics.

    All *_weight fields are weighted by the ANALYST-SET bear/base/bull
    scenario weights - they are stress labels, not calibrated probabilities.
    """

    ticker: str
    price: float
    scenarios: list[ScenarioValuation]
    expected_irr: float
    median_irr: float
    p10_irr: float
    p90_irr: float
    above_hurdle_weight: float
    permanent_loss_weight: float
    expected_shortfall: float
    hurdle_cvar: float  # tail mean of max(0, hurdle - irr): shortfall vs the hurdle
    # P1-1: keep the NAMED scenario values and the STATISTICAL interval separate.
    # low/high are min/max of the three scenarios (so low <= base <= high holds
    # by construction); intrinsic_value_bear/bull keep the economic identity of
    # the bear/bull case, which need not be the lowest/highest (low growth can
    # destroy less value when ROIC < WACC).
    intrinsic_value_low: float
    intrinsic_value_base: float
    intrinsic_value_high: float
    intrinsic_value_bear: float
    intrinsic_value_bull: float
    scenario_order_inversion: bool = False
    scenario_order_note: str | None = None
    model_confidence: float
    data_confidence: float
    model_uncertainty: float
    # P0-1: "valid" means every ranked output is finite and not an implausibly
    # high solver-bound result. Catastrophic below-bound loss cases remain in the
    # distribution at a conservative floor; other invalid results route to the
    # watchlist with an auditable list of offending fields.
    valuation_status: str = "valid"
    invalid_reason: str | None = None
    invalid_fields: list[str] = Field(default_factory=list)
    # P1-2: assumptions that hit a configured bound (growth/ROIC/share/WACC...),
    # extreme-valuation alerts, and whether the name needs manual re-underwriting
    # before being treated as a precise estimate.
    assumption_flags: list[str] = Field(default_factory=list)
    valuation_alerts: list[str] = Field(default_factory=list)
    requires_manual_review: bool = False
