"""Probabilistic scenario valuation (Layer 3).

For each company three auditable scenarios (bear/base/bull) project revenue,
margins, reinvestment and share count to derive per-share cash flows, a
terminal value and implied IRRs. Design properties the tests pin down:

- Profitability anchors at the NORMALIZED margin, so peak-cycle earnings do
  not produce fake cheapness.
- Reinvestment is growth/ROIC and terminal value uses
  NOPAT*(1-g/ROIC_terminal)/(WACC-g). When ROIC fades to WACC the terminal
  value collapses to NOPAT/WACC: growth only creates value while ROIC > WACC.
- Financial-persistence evidence widens or narrows the scenario spread, sets
  how long high returns persist (terminal ROIC persistence), and feeds model
  confidence - it is never a score bonus.
- Share dilution shrinks per-share cash flows; buybacks shrink the share
  count but their cash cost is charged against distributable FCF, so they
  only add value when executed below intrinsic value.

A Monte Carlo layer can later replace the discrete distribution; every
aggregate below operates on generic (value, probability) pairs already.
"""

from __future__ import annotations

import math

from weekly_us_stock.config import AlertSettings, RiskPreferenceSettings, ScenarioSettings
from weekly_us_stock.models.valuation import (
    CompanyInputs,
    CompanyValuation,
    ScenarioAssumptions,
    ScenarioValuation,
)
from weekly_us_stock.valuation.irr import (
    LOWER_BOUND,
    UPPER_BOUND,
    solve_irr,
    solve_irr_detailed,
)

_MIN_DENOMINATOR = 0.01

# Aggregate outputs that must be finite for a company to be RANKED. A NaN,
# Infinity or implausibly high bound-saturated value routes the name to the
# watchlist (P0-1) instead of into a pseudo-precise ranking row. A catastrophic
# below-bound loss stays in the risk distribution at the conservative floor.
_REQUIRED_FINITE_METRICS = (
    "expected_irr",
    "median_irr",
    "p10_irr",
    "p90_irr",
    "hurdle_cvar",
    "expected_shortfall",
    "intrinsic_value_base",
)


def build_scenarios(inputs: CompanyInputs, cfg: ScenarioSettings) -> list[ScenarioAssumptions]:
    base_growth = _blend_growth(inputs, cfg)
    spread = _growth_spread(inputs, cfg)

    forward_roic = _forward_roic(inputs)
    share_change = min(
        max(inputs.net_share_change_rate, cfg.min_share_change_rate),
        cfg.max_share_change_rate,
    )

    moat = min(max(inputs.financial_persistence, 0.0), 1.0)
    margin = inputs.normalized_operating_margin
    bear_margin = margin * (1.0 - cfg.bear_margin_haircut * (1.5 - moat)) - 0.5 * (
        inputs.margin_volatility
    )
    bull_margin = margin * (1.0 + cfg.bull_margin_uplift) + 0.5 * inputs.margin_volatility

    probabilities = cfg.probabilities

    # P1-3: scenarios differ on buybacks. The bear case does not assume
    # management keeps buying back into a downturn (a buyback rate is floored at
    # zero), while dilution is kept across every scenario.
    bear_share = max(share_change, 0.0)

    def _assumption(
        name: str,
        growth: float,
        scenario_margin: float,
        roic: float,
        terminal_roic: float,
        terminal_growth: float,
        *,
        share: float,
    ) -> ScenarioAssumptions:
        return ScenarioAssumptions(
            name=name,  # type: ignore[arg-type]
            probability=probabilities[name],
            revenue_growth_y1=growth,
            terminal_growth=terminal_growth,
            operating_margin=scenario_margin,
            forward_roic=roic,
            terminal_roic=max(terminal_roic, terminal_growth + _MIN_DENOMINATOR),
            share_change_rate=share,
        )

    wacc = inputs.wacc
    # Terminal ROIC: competition pushes returns toward WACC; moat evidence
    # governs how much of today's excess return survives.
    base_excess = max(0.0, forward_roic - wacc)
    return [
        _assumption(
            "bear",
            base_growth - spread * cfg.bear_spread_skew,
            max(bear_margin, -0.10),
            max(forward_roic * 0.75, 0.02),
            wacc,  # no enduring value creation in the bear case
            max(cfg.terminal_growth - 0.005, 0.0),
            share=bear_share,
        ),
        _assumption(
            "base",
            base_growth,
            margin,
            forward_roic,
            wacc + base_excess * moat,
            cfg.terminal_growth,
            share=share_change,
        ),
        _assumption(
            "bull",
            base_growth + spread,
            bull_margin,
            min(forward_roic * 1.10, 0.60),
            wacc + base_excess * min(1.0, moat + 0.2),
            cfg.terminal_growth + 0.005,
            share=share_change,
        ),
    ]


def value_scenario(
    inputs: CompanyInputs,
    assumption: ScenarioAssumptions,
    cfg: ScenarioSettings,
) -> ScenarioValuation:
    horizon = cfg.horizon_years
    tax = inputs.tax_rate
    wacc = inputs.wacc

    growth_path = _fade_path(assumption.revenue_growth_y1, assumption.terminal_growth, horizon)
    margin_path = _margin_path(
        inputs.current_operating_margin, assumption.operating_margin, horizon
    )

    revenue = inputs.latest_revenue
    nopat_path: list[float] = []
    fcf_path: list[float] = []
    reinvest_y1 = 0.0
    for year in range(1, horizon + 1):
        revenue *= 1.0 + growth_path[year - 1]
        nopat = revenue * margin_path[year - 1] * (1.0 - tax)
        next_growth = (
            growth_path[year] if year < horizon else assumption.terminal_growth
        )
        reinvestment = _reinvestment_rate(next_growth, assumption.forward_roic, cfg)
        if year == 1:
            reinvest_y1 = reinvestment
        nopat_path.append(nopat)
        fcf_path.append(nopat * (1.0 - reinvestment))

    interest_drag = inputs.net_debt * inputs.cost_of_debt_after_tax

    # P1-3: the share count is not mechanically extrapolated. Buybacks decay
    # toward zero each year, can only spend a fraction of POSITIVE distributable
    # FCF, and stop entirely when leverage is too high - so a company never gets
    # a per-share lift from share shrinkage its cash flow cannot fund. Dilution
    # (positive rate) persists at full strength so the issuance penalty stays.
    base_rate = assumption.share_change_rate
    buyback_blocked = _buyback_blocked(inputs, cfg)
    current_shares = inputs.shares_outstanding
    shares_path: list[float] = []
    per_share_flows: list[float] = []
    for year in range(1, horizon + 1):
        equity_fcf = fcf_path[year - 1] - interest_drag
        if base_rate < 0:
            decayed_rate = base_rate * (cfg.buyback_decay ** (year - 1))
            price_year = inputs.price * (1.0 + cfg.price_anchor_growth) ** year
            budget = 0.0 if buyback_blocked else cfg.buyback_max_fcf_fraction * max(
                0.0, equity_fcf
            )
            desired_spend = abs(decayed_rate) * current_shares * price_year
            actual_spend = min(desired_spend, budget)
            shares_retired = actual_spend / price_year if price_year > 0 else 0.0
            current_shares = max(current_shares - shares_retired, _MIN_DENOMINATOR)
            equity_fcf -= actual_spend
        else:
            current_shares = current_shares * (1.0 + base_rate)
        shares_path.append(current_shares)
        per_share_flows.append(equity_fcf / current_shares)

    exit_5 = _exit_value_per_share(
        nopat_path[-1], assumption, inputs, shares_path[-1]
    )
    flows_5y = [-inputs.price, *per_share_flows[:-1], per_share_flows[-1] + exit_5]
    irr_solution = solve_irr_detailed(flows_5y)
    irr_5y = irr_solution.rate
    irr_5y_status = irr_solution.status
    if irr_5y is None and irr_5y_status == "below_lower_bound":
        # Catastrophic downside (IRR < -95%): floor the magnitude so weighted
        # aggregates stay finite. This is an economically plausible loss case,
        # so keep it in the risk distribution and let the robust gate penalize it.
        irr_5y = LOWER_BOUND
    elif irr_5y is None and irr_5y_status == "above_upper_bound":
        # IRR > 200%: the cap comment calls this a data artifact. Keep a finite
        # placeholder for the distribution; the status removes it from lists.
        irr_5y = UPPER_BOUND

    exit_year = min(cfg.exit_year, horizon)
    exit_3 = _exit_value_per_share(
        nopat_path[exit_year - 1], assumption, inputs, shares_path[exit_year - 1]
    )
    flows_3y = [
        -inputs.price,
        *per_share_flows[: exit_year - 1],
        per_share_flows[exit_year - 1] + exit_3,
    ]
    irr_3y = solve_irr(flows_3y)

    # Intrinsic value: firm-level DCF at WACC minus net debt, on today's
    # share count (SBC is already expensed inside FCF).
    pv_fcf = sum(fcf_path[t] / (1.0 + wacc) ** (t + 1) for t in range(horizon))
    terminal_nopat = nopat_path[-1] * (1.0 + assumption.terminal_growth)
    tv_firm = _terminal_value(terminal_nopat, assumption, wacc)
    firm_value = pv_fcf + tv_firm / (1.0 + wacc) ** horizon
    equity_value = firm_value - inputs.net_debt
    intrinsic_per_share = equity_value / inputs.shares_outstanding

    total_return_5y = (sum(per_share_flows) + exit_5) / inputs.price - 1.0

    # Fail-closed backstop: every projected per-share output must be a finite
    # number. Clamps usually prevent NaN/Infinity, but data artifacts (zero
    # shares at exit, degenerate denominators) can still leak through.
    scenario_finite = all(
        math.isfinite(value)
        for value in (intrinsic_per_share, exit_5, total_return_5y, *per_share_flows)
    )

    return ScenarioValuation(
        assumptions=assumption,
        intrinsic_value_per_share=intrinsic_per_share,
        irr_3y=irr_3y,
        irr_5y=irr_5y,
        exit_value_per_share=exit_5,
        total_return_5y=total_return_5y,
        reinvestment_rate_y1=reinvest_y1,
        projected_fcf=[round(value, 4) for value in fcf_path],
        ending_shares=shares_path[-1],
        irr_5y_status=irr_5y_status,
        is_finite=scenario_finite,
    )


def aggregate_valuation(
    inputs: CompanyInputs,
    scenarios: list[ScenarioValuation],
    prefs: RiskPreferenceSettings,
) -> CompanyValuation:
    distribution = [
        (s.irr_5y if s.irr_5y is not None else LOWER_BOUND, s.assumptions.probability)
        for s in scenarios
    ]
    expected_irr = sum(irr * p for irr, p in distribution)
    median_irr = _quantile(distribution, 0.50)
    p10_irr = _quantile(distribution, 0.10)
    p90_irr = _quantile(distribution, 0.90)
    above_hurdle_weight = sum(p for irr, p in distribution if irr > prefs.hurdle_rate)
    permanent_loss_weight = sum(
        s.assumptions.probability
        for s in scenarios
        if s.total_return_5y < prefs.permanent_loss_threshold
    )
    expected_shortfall = _expected_shortfall(distribution, prefs.cvar_alpha)
    # Shortfall measured against the investor's hurdle, not just zero: a bear
    # case earning 7% against a 12% hurdle is still a 5-point miss.
    hurdle_cvar = _tail_mean(
        [(max(0.0, prefs.hurdle_rate - irr), p) for irr, p in distribution],
        prefs.cvar_alpha,
        worst="largest",
    )

    half_spread = max(p90_irr - p10_irr, 0.0) / 2.0
    model_uncertainty = half_spread + prefs.uncertainty_per_missing_confidence * (
        (1.0 - inputs.model_confidence) + (1.0 - inputs.data_confidence)
    )

    by_name = {s.assumptions.name: s for s in scenarios}
    bear_iv = by_name["bear"].intrinsic_value_per_share
    base_iv = by_name["base"].intrinsic_value_per_share
    bull_iv = by_name["bull"].intrinsic_value_per_share
    # P1-1: the named order need not be monotone (low growth destroys less value
    # when ROIC < WACC). Flag the inversion and explain the driver instead of
    # forcing the numbers to look ordered.
    inversion = not (bear_iv <= base_iv <= bull_iv)
    order_note = _scenario_order_note(inputs, by_name["base"].assumptions) if inversion else None

    required_metrics = {
        "expected_irr": expected_irr,
        "median_irr": median_irr,
        "p10_irr": p10_irr,
        "p90_irr": p90_irr,
        "hurdle_cvar": hurdle_cvar,
        "expected_shortfall": expected_shortfall,
        "intrinsic_value_base": base_iv,
    }
    status, reason, invalid_fields = _classify_validity(scenarios, required_metrics)
    return CompanyValuation(
        ticker=inputs.ticker,
        price=inputs.price,
        scenarios=scenarios,
        expected_irr=expected_irr,
        median_irr=median_irr,
        p10_irr=p10_irr,
        p90_irr=p90_irr,
        above_hurdle_weight=above_hurdle_weight,
        permanent_loss_weight=permanent_loss_weight,
        expected_shortfall=expected_shortfall,
        hurdle_cvar=hurdle_cvar,
        intrinsic_value_low=min(bear_iv, base_iv, bull_iv),
        intrinsic_value_base=base_iv,
        intrinsic_value_high=max(bear_iv, base_iv, bull_iv),
        intrinsic_value_bear=bear_iv,
        intrinsic_value_bull=bull_iv,
        scenario_order_inversion=inversion,
        scenario_order_note=order_note,
        model_confidence=inputs.model_confidence,
        data_confidence=inputs.data_confidence,
        model_uncertainty=model_uncertainty,
        valuation_status=status,
        invalid_reason=reason,
        invalid_fields=invalid_fields,
    )


def _scenario_order_note(inputs: CompanyInputs, base: ScenarioAssumptions) -> str:
    """Explain why bear/base/bull intrinsic values are not monotone."""

    if base.forward_roic <= inputs.wacc + _MIN_DENOMINATOR:
        return (
            f"growth destroys value: forward ROIC {base.forward_roic:.1%} at/below "
            f"WACC {inputs.wacc:.1%}, so higher-growth scenarios reinvest below the "
            "cost of capital and are worth less than the bear case"
        )
    return (
        "intrinsic value is not monotone in growth: margin and reinvestment "
        "assumptions reorder the bear/base/bull cases"
    )


def _classify_validity(
    scenarios: list[ScenarioValuation], required_metrics: dict[str, float]
) -> tuple[str, str | None, list[str]]:
    """Decide whether a valuation is precise enough to be ranked.

    Returns (status, headline_reason, offending_fields). A name is invalid when
    an IRR is above the solver bound, when any scenario produced a non-finite
    output, or when any required aggregate metric is not finite. A below-bound
    loss stays at the conservative lower-bound value so its tail risk remains
    visible in the research queue.
    """

    fields: list[str] = []
    reasons: set[str] = set()
    for scenario in scenarios:
        label = scenario.assumptions.name
        status = scenario.irr_5y_status
        if status == "above_upper_bound":
            fields.append(f"irr_5y[{label}]")
            reasons.add("irr_above_solver_bound")
        elif status not in {"valid", "below_lower_bound"}:
            fields.append(f"irr_5y[{label}]")
            reasons.add("invalid_valuation_output")
        if not scenario.is_finite:
            fields.append(f"scenario[{label}]")
            reasons.add("invalid_valuation_output")

    for key, value in required_metrics.items():
        if value is None or not math.isfinite(value):
            fields.append(key)
            reasons.add("invalid_valuation_output")

    if not fields:
        return "valid", None, []

    priority = (
        "irr_above_solver_bound",
        "invalid_valuation_output",
    )
    headline = next((r for r in priority if r in reasons), sorted(reasons)[0])
    return "invalid", headline, sorted(set(fields))


def value_company(
    inputs: CompanyInputs,
    cfg: ScenarioSettings,
    prefs: RiskPreferenceSettings,
    *,
    wacc_bounds: tuple[float, float] | None = None,
    alerts: AlertSettings | None = None,
) -> CompanyValuation:
    assumptions = build_scenarios(inputs, cfg)
    scenarios = [value_scenario(inputs, assumption, cfg) for assumption in assumptions]
    valuation = aggregate_valuation(inputs, scenarios, prefs)
    _apply_assumption_alerts(valuation, inputs, cfg, prefs, wacc_bounds, alerts or AlertSettings())
    return valuation


# Forward ROIC clamp bounds, mirrored from _forward_roic for boundary detection.
_FORWARD_ROIC_FLOOR = 0.02
_FORWARD_ROIC_CAP = 0.60


def detect_assumption_flags(
    inputs: CompanyInputs,
    cfg: ScenarioSettings,
    wacc_bounds: tuple[float, float] | None = None,
) -> list[str]:
    """Assumptions that hit a configured bound before clamping (P1-2)."""

    flags: list[str] = []
    anchors = [inputs.hist_revenue_cagr]
    if inputs.analyst_growth is not None:
        anchors.append(inputs.analyst_growth)
    blended_growth = sum(anchors) / len(anchors)
    if blended_growth >= cfg.base_growth_cap:
        flags.append("base_growth_cap_hit")
    elif blended_growth <= cfg.base_growth_floor:
        flags.append("base_growth_floor_hit")

    raw_roic = (
        0.7 * inputs.incremental_roic + 0.3 * inputs.roic
        if inputs.incremental_roic is not None
        else inputs.roic
    )
    if raw_roic >= _FORWARD_ROIC_CAP:
        flags.append("forward_roic_cap_hit")
    elif raw_roic <= _FORWARD_ROIC_FLOOR:
        flags.append("forward_roic_floor_hit")

    if inputs.net_share_change_rate >= cfg.max_share_change_rate:
        flags.append("share_change_cap_hit")
    elif inputs.net_share_change_rate <= cfg.min_share_change_rate:
        flags.append("share_change_floor_hit")

    if wacc_bounds is not None:
        low, high = wacc_bounds
        if inputs.wacc >= high:
            flags.append("wacc_cap_hit")
        elif inputs.wacc <= low:
            flags.append("wacc_floor_hit")
    return flags


def detect_valuation_alerts(
    valuation: CompanyValuation, inputs: CompanyInputs, alerts: AlertSettings
) -> tuple[list[str], list[str]]:
    """Return (review_alerts, soft_flags) for extreme valuation outputs."""

    review: list[str] = []
    soft: list[str] = []
    ratio = valuation.intrinsic_value_base / inputs.price if inputs.price else 0.0
    if ratio >= alerts.intrinsic_to_price_review:
        review.append("intrinsic_3x_price")
    elif ratio >= alerts.intrinsic_to_price_flag:
        soft.append("intrinsic_2x_price")
    if valuation.median_irr >= alerts.median_irr_review:
        review.append("median_irr_extreme")
    bull = next((s for s in valuation.scenarios if s.assumptions.name == "bull"), None)
    if bull is not None and bull.total_return_5y >= alerts.bull_return_review:
        review.append("bull_return_extreme")
    if (valuation.p90_irr - valuation.p10_irr) >= alerts.scenario_span_review:
        review.append("scenario_span_extreme")
    return review, soft


def _apply_assumption_alerts(
    valuation: CompanyValuation,
    inputs: CompanyInputs,
    cfg: ScenarioSettings,
    prefs: RiskPreferenceSettings,
    wacc_bounds: tuple[float, float] | None,
    alerts: AlertSettings,
) -> None:
    flags = detect_assumption_flags(inputs, cfg, wacc_bounds)
    # reinvestment cap is a per-scenario clamp; detect it on the computed paths.
    if any(s.reinvestment_rate_y1 >= cfg.max_reinvestment_rate for s in valuation.scenarios):
        flags.append("reinvestment_cap_hit")

    review, soft = detect_valuation_alerts(valuation, inputs, alerts)
    valuation.assumption_flags = flags + soft
    valuation.valuation_alerts = review
    valuation.requires_manual_review = bool(review)

    # A boundary hit lowers model confidence (and raises uncertainty) so a
    # boundary-driven number is never read as an ordinary precise estimate.
    if flags:
        valuation.model_confidence *= alerts.model_confidence_haircut_per_flag ** len(flags)
        half_spread = max(valuation.p90_irr - valuation.p10_irr, 0.0) / 2.0
        valuation.model_uncertainty = half_spread + prefs.uncertainty_per_missing_confidence * (
            (1.0 - valuation.model_confidence) + (1.0 - valuation.data_confidence)
        )


# -- helpers ---------------------------------------------------------------------


def _blend_growth(inputs: CompanyInputs, cfg: ScenarioSettings) -> float:
    anchors = [inputs.hist_revenue_cagr]
    if inputs.analyst_growth is not None:
        anchors.append(inputs.analyst_growth)
    blended = sum(anchors) / len(anchors)
    return min(max(blended, cfg.base_growth_floor), cfg.base_growth_cap)


def _growth_spread(inputs: CompanyInputs, cfg: ScenarioSettings) -> float:
    dispersion = inputs.analyst_dispersion if inputs.analyst_dispersion is not None else 0.10
    moat = min(max(inputs.financial_persistence, 0.0), 1.0)
    raw = cfg.base_growth_spread + 0.5 * inputs.cyclicality + 0.25 * dispersion
    return raw * (1.5 - moat)


def classify_roic(inputs: CompanyInputs) -> str:
    """P1-4: is ROIC a meaningful positive return, or undefined?

    A negative ROIC is NOT silently floored to a small positive number. We
    distinguish a genuine negative operating return from a ratio made
    meaningless by a negative/near-zero invested-capital base (accumulated
    buybacks, negative equity) and from a non-finite data artifact, so the
    capital-light / impaired names route to the watchlist instead of being
    valued as if they earned a low-but-positive 2% ROIC.
    """

    if not math.isfinite(inputs.roic) or (
        inputs.incremental_roic is not None and not math.isfinite(inputs.incremental_roic)
    ):
        return "data_anomaly"
    if inputs.roic < 0:
        # NOPAT is positive (margin > 0) yet ROIC < 0 -> invested capital is
        # negative: the ratio has no economic meaning here.
        if inputs.normalized_operating_margin > 0:
            return "meaningless_capital"
        return "negative_returns"
    return "ok"


def _forward_roic(inputs: CompanyInputs) -> float:
    # Only reached for "ok" (non-negative ROIC) companies; negative/meaningless
    # ROIC is routed out by classify_roic before valuation (P1-4).
    if inputs.incremental_roic is not None:
        blended = 0.7 * inputs.incremental_roic + 0.3 * inputs.roic
    else:
        blended = inputs.roic
    return min(max(blended, 0.02), 0.60)


def _fade_path(growth_y1: float, terminal_growth: float, horizon: int) -> list[float]:
    if horizon == 1:
        return [growth_y1]
    return [
        growth_y1 + (terminal_growth - growth_y1) * t / horizon for t in range(horizon)
    ]


def _margin_path(current: float, target: float, horizon: int) -> list[float]:
    # Two-year glide from today's margin to the scenario margin, then flat.
    path = []
    for year in range(1, horizon + 1):
        if year >= 3:
            path.append(target)
        else:
            weight = year / 3.0
            path.append(current + (target - current) * weight)
    return path


def _reinvestment_rate(growth: float, roic: float, cfg: ScenarioSettings) -> float:
    if growth <= 0:
        return 0.0
    return min(growth / max(roic, _MIN_DENOMINATOR), cfg.max_reinvestment_rate)


def _buyback_blocked(inputs: CompanyInputs, cfg: ScenarioSettings) -> bool:
    """Stop buybacks when leverage is too high to fund them prudently (P1-3)."""

    if inputs.net_debt <= 0:
        return False
    nopat = inputs.latest_revenue * inputs.normalized_operating_margin * (1.0 - inputs.tax_rate)
    if nopat <= 0:
        return True  # levered and not earning: no buybacks
    return inputs.net_debt > cfg.buyback_max_net_debt_to_nopat * nopat


def _terminal_value(terminal_nopat: float, assumption: ScenarioAssumptions, wacc: float) -> float:
    g = assumption.terminal_growth
    roic = max(assumption.terminal_roic, g + _MIN_DENOMINATOR)
    denominator = max(wacc - g, _MIN_DENOMINATOR)
    return terminal_nopat * (1.0 - g / roic) / denominator


def _exit_value_per_share(
    nopat_at_exit: float,
    assumption: ScenarioAssumptions,
    inputs: CompanyInputs,
    shares_at_exit: float,
) -> float:
    terminal_nopat = nopat_at_exit * (1.0 + assumption.terminal_growth)
    tv_firm = _terminal_value(terminal_nopat, assumption, inputs.wacc)
    equity = max(tv_firm - inputs.net_debt, 0.0)
    return equity / shares_at_exit


def _quantile(distribution: list[tuple[float, float]], q: float) -> float:
    ordered = sorted(distribution, key=lambda item: item[0])
    cumulative = 0.0
    for value, probability in ordered:
        cumulative += probability
        if cumulative >= q - 1e-12:
            return value
    return ordered[-1][0]


def _expected_shortfall(distribution: list[tuple[float, float]], alpha: float) -> float:
    """CVaR of the IRR distribution: mean of the worst alpha tail, reported as
    a non-negative loss magnitude."""

    return max(0.0, -_tail_mean(distribution, alpha, worst="smallest"))


def _tail_mean(
    distribution: list[tuple[float, float]],
    alpha: float,
    *,
    worst: str,
) -> float:
    """Mean of the worst alpha tail of a discrete (value, weight) distribution.

    worst="smallest" treats LOW values as bad (IRRs); worst="largest" treats
    HIGH values as bad (shortfalls)."""

    ordered = sorted(distribution, key=lambda item: item[0], reverse=worst == "largest")
    remaining = alpha
    weighted = 0.0
    for value, probability in ordered:
        take = min(probability, remaining)
        weighted += value * take
        remaining -= take
        if remaining <= 1e-12:
            break
    return weighted / alpha
