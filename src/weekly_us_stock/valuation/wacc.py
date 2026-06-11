"""CAPM-based WACC with explicit, auditable inputs."""

from __future__ import annotations

import math

from weekly_us_stock.config import WaccSettings


def cost_of_equity(risk_free: float, beta: float | None, settings: WaccSettings) -> float:
    effective_beta = settings.default_beta if beta is None or math.isnan(beta) else float(beta)
    effective_beta = min(max(effective_beta, 0.5), 2.5)
    return risk_free + effective_beta * settings.equity_risk_premium


def cost_of_debt_after_tax(
    risk_free: float,
    interest_coverage: float | None,
    tax_rate: float,
    settings: WaccSettings,
) -> float:
    spread = settings.base_credit_spread
    if interest_coverage is not None and interest_coverage < 4:
        spread = settings.stressed_credit_spread
    return (risk_free + spread) * (1.0 - tax_rate)


def compute_wacc(
    *,
    risk_free: float,
    beta: float | None,
    market_cap: float,
    total_debt: float,
    interest_coverage: float | None,
    tax_rate: float,
    settings: WaccSettings,
) -> tuple[float, float]:
    """Return (wacc, after-tax cost of debt), both clamped to configured bounds."""

    ke = cost_of_equity(risk_free, beta, settings)
    kd = cost_of_debt_after_tax(risk_free, interest_coverage, tax_rate, settings)
    capital = max(market_cap, 0.0) + max(total_debt, 0.0)
    if capital <= 0:
        wacc = ke
    else:
        weight_equity = max(market_cap, 0.0) / capital
        wacc = weight_equity * ke + (1.0 - weight_equity) * kd
    wacc = min(max(wacc, settings.min_wacc), settings.max_wacc)
    return wacc, kd
