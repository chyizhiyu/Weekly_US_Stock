"""Specialist valuation models for financials and REITs.

The general owner-earnings DCF treats debt, cash, working capital and capex in
ways that are wrong for banks, insurers and REITs. This step values those names
with simple, auditable specialist models and emits the same company-level
metrics as the general scenario engine so ranking can stay shared.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import pandas as pd

from weekly_us_stock.config import (
    RiskPreferenceSettings,
    SpecialistModelSettings,
    WaccSettings,
)
from weekly_us_stock.valuation.industry import BANK, INSURANCE, REIT
from weekly_us_stock.valuation.wacc import cost_of_equity

_SPECIALIST_FAMILIES = {BANK, INSURANCE, REIT}
_SCENARIOS = {"bear": 0.25, "base": 0.50, "bull": 0.25}
_MIN_DENOMINATOR = 0.01
_IRR_FLOOR = -0.95


@dataclass(slots=True)
class SpecialistValuationResult:
    metrics: pd.DataFrame
    scenario_rows: pd.DataFrame
    watchlist: pd.DataFrame


def run_specialist_valuations(
    routed_watchlist: pd.DataFrame,
    fundamentals: pd.DataFrame,
    *,
    risk_free: float,
    settings: SpecialistModelSettings,
    wacc_settings: WaccSettings,
    risk_preferences: RiskPreferenceSettings,
) -> SpecialistValuationResult:
    """Value bank/insurance/REIT rows that were routed out of the general DCF.

    Rows for unsupported families or incomplete specialist inputs stay in the
    watchlist with an explicit reason. The returned metrics are rank-compatible
    with ``run_scenario_valuations``.
    """

    if routed_watchlist.empty:
        return SpecialistValuationResult(pd.DataFrame(), pd.DataFrame(), pd.DataFrame())
    if not settings.enabled:
        return SpecialistValuationResult(pd.DataFrame(), pd.DataFrame(), routed_watchlist.copy())

    history_by_ticker = (
        {str(ticker): group for ticker, group in fundamentals.groupby("ticker")}
        if not fundamentals.empty
        else {}
    )
    metrics: list[dict] = []
    scenario_rows: list[dict] = []
    watchlist: list[dict] = []

    for _, candidate in routed_watchlist.iterrows():
        family = str(candidate.get("model_family") or "")
        if family not in _SPECIALIST_FAMILIES:
            watchlist.append(candidate.to_dict())
            continue
        history = history_by_ticker.get(str(candidate.get("ticker")))
        if history is None:
            watchlist.append(_watch(candidate, "specialist_missing_fundamentals"))
            continue
        result = _value_one(
            candidate,
            history,
            family=family,
            risk_free=risk_free,
            settings=settings,
            wacc_settings=wacc_settings,
            risk_preferences=risk_preferences,
        )
        if result is None:
            watchlist.append(_watch(candidate, "specialist_valuation_failed"))
            continue
        metric, rows = result
        if metric["valuation_status"] != "valid":
            watchlist.append(_watch(candidate, str(metric["invalid_reason"])))
            continue
        metrics.append(metric)
        scenario_rows.extend(rows)

    return SpecialistValuationResult(
        metrics=pd.DataFrame(metrics),
        scenario_rows=pd.DataFrame(scenario_rows),
        watchlist=pd.DataFrame(watchlist),
    )


def _value_one(
    candidate: pd.Series,
    history: pd.DataFrame,
    *,
    family: str,
    risk_free: float,
    settings: SpecialistModelSettings,
    wacc_settings: WaccSettings,
    risk_preferences: RiskPreferenceSettings,
) -> tuple[dict, list[dict]] | None:
    frame = history.dropna(subset=["fiscal_year"]).sort_values("fiscal_year")
    frame = frame.tail(settings.lookback_years).reset_index(drop=True)
    if len(frame) < settings.min_years:
        return _invalid(candidate, family, "specialist_insufficient_history"), []

    price = _float(candidate.get("price"))
    shares = _latest_positive(frame, "shares_diluted") or _float(
        candidate.get("shares_outstanding")
    )
    equity = _latest_positive(frame, "total_equity")
    if not price or price <= 0 or not shares or shares <= 0 or not equity or equity <= 0:
        return _invalid(candidate, family, "specialist_missing_book_or_price"), []

    beta = _float(candidate.get("beta"))
    ke = max(
        cost_of_equity(risk_free, beta, wacc_settings),
        settings.terminal_growth + _MIN_DENOMINATOR,
    )
    book_ps = equity / shares

    if family in {BANK, INSURANCE}:
        scenarios = _bank_insurance_scenarios(frame, book_ps, price, ke, settings)
    elif family == REIT:
        scenarios = _reit_scenarios(frame, shares, price, ke, settings)
    else:
        return None
    if not scenarios:
        return _invalid(candidate, family, "specialist_no_positive_earning_power"), []
    for row in scenarios:
        row["ticker"] = candidate.get("ticker")
        row["model_family"] = family
        row["price"] = price

    distribution = [(row["irr_5y"], row["probability"]) for row in scenarios]
    expected_irr = sum(value * prob for value, prob in distribution)
    median_irr = _quantile(distribution, 0.50)
    p10_irr = _quantile(distribution, 0.10)
    p90_irr = _quantile(distribution, 0.90)
    worst_irr = min(value for value, _prob in distribution)
    worst_case_shortfall = max(0.0, -worst_irr)
    worst_case_hurdle_gap = max(0.0, risk_preferences.hurdle_rate - worst_irr)
    permanent_loss_weight = sum(
        row["probability"]
        for row in scenarios
        if row["intrinsic_value_per_share"] / price - 1.0
        < risk_preferences.permanent_loss_threshold
    )
    model_uncertainty = (max(p90_irr - p10_irr, 0.0) / 2.0) + (
        risk_preferences.uncertainty_per_missing_confidence
        * (1.0 - settings.model_confidence + 1.0 - settings.data_confidence)
    )
    by_name = {row["scenario"]: row for row in scenarios}
    base_iv = by_name["base"]["intrinsic_value_per_share"]
    metric = {
        **_carry(candidate),
        "price": price,
        "model_family": family,
        "expected_irr": expected_irr,
        "median_irr": median_irr,
        "p10_irr": p10_irr,
        "p90_irr": p90_irr,
        "above_hurdle_weight": sum(
            prob for value, prob in distribution if value > risk_preferences.hurdle_rate
        ),
        "hurdle_rate": risk_preferences.hurdle_rate,
        "permanent_loss_weight": permanent_loss_weight,
        "worst_case_shortfall": worst_case_shortfall,
        "worst_case_hurdle_gap": worst_case_hurdle_gap,
        "expected_shortfall": worst_case_shortfall,
        "hurdle_cvar": worst_case_hurdle_gap,
        "intrinsic_value_low": min(row["intrinsic_value_per_share"] for row in scenarios),
        "intrinsic_value_base": base_iv,
        "intrinsic_value_high": max(row["intrinsic_value_per_share"] for row in scenarios),
        "intrinsic_value_bear": by_name["bear"]["intrinsic_value_per_share"],
        "intrinsic_value_bull": by_name["bull"]["intrinsic_value_per_share"],
        "scenario_order_inversion": False,
        "scenario_order_note": None,
        "upside_to_base": base_iv / price - 1.0,
        "model_confidence": settings.model_confidence,
        "data_confidence": settings.data_confidence,
        "model_uncertainty": model_uncertainty,
        "business_quality": _quality_score(scenarios),
        "valuation_excess": median_irr - risk_preferences.hurdle_rate,
        "evidence_confidence": settings.model_confidence * settings.data_confidence,
        "valuation_status": "valid",
        "invalid_reason": None,
        "invalid_fields": "",
        "assumption_flags": "specialist_model_v1",
        "valuation_alerts": "",
        "requires_manual_review": False,
        "roic_status": "specialist",
        "catastrophic_tail_floor_applied": False,
        "catastrophic_tail_scenarios": "",
        "specialist_model_note": _model_note(family),
    }
    return metric, scenarios


def _bank_insurance_scenarios(
    frame: pd.DataFrame,
    book_ps: float,
    price: float,
    cost_equity: float,
    settings: SpecialistModelSettings,
) -> list[dict]:
    roe = _ratio_series(frame["net_income"], frame["total_equity"])
    if roe.empty:
        return []
    normalized_roe = float(roe.median())
    if normalized_roe <= 0:
        return []
    volatility = float(roe.std(ddof=0)) if len(roe) > 1 else 0.0
    values = {
        "bear": max(0.0, normalized_roe * (1.0 - settings.roe_bear_haircut) - 0.5 * volatility),
        "base": normalized_roe,
        "bull": min(
            settings.max_roe,
            normalized_roe * (1.0 + settings.roe_bull_uplift) + 0.5 * volatility,
        ),
    }
    return [
        _scenario_row(
            scenario=name,
            probability=_SCENARIOS[name],
            intrinsic=_justified_book_value(book_ps, scenario_roe, cost_equity, settings),
            price_context=price,
            model_input=scenario_roe,
            input_name="normalized_roe",
            settings=settings,
        )
        for name, scenario_roe in values.items()
    ]


def _reit_scenarios(
    frame: pd.DataFrame,
    shares: float,
    price: float,
    cost_equity: float,
    settings: SpecialistModelSettings,
) -> list[dict]:
    ffo = frame["net_income"].astype(float) + frame["depreciation"].fillna(0.0).astype(float)
    affo = ffo * (1.0 - settings.reit_maintenance_capex_haircut)
    positive = affo.loc[affo > 0]
    if positive.empty:
        return []
    affo_ps = float(positive.median()) / shares
    growth = _growth_from_series(positive, settings)
    values = {
        "bear": growth - settings.reit_growth_spread,
        "base": growth,
        "bull": growth + settings.reit_growth_spread,
    }
    rows = []
    for name, scenario_growth in values.items():
        g = min(max(scenario_growth, settings.growth_floor), settings.growth_cap)
        g = min(g, cost_equity - _MIN_DENOMINATOR)
        intrinsic = max(0.0, affo_ps * (1.0 + g) / max(cost_equity - g, _MIN_DENOMINATOR))
        rows.append(
            _scenario_row(
                scenario=name,
                probability=_SCENARIOS[name],
                intrinsic=intrinsic,
                price_context=price,
                model_input=g,
                input_name="affo_growth",
                settings=settings,
            )
        )
    return rows


def _scenario_row(
    *,
    scenario: str,
    probability: float,
    intrinsic: float,
    price_context: float | None,
    model_input: float,
    input_name: str,
    settings: SpecialistModelSettings,
) -> dict:
    price = price_context
    irr = 0.0
    if price is not None and price > 0:
        irr = _annualized_gap(intrinsic, price)
    return {
        "scenario": scenario,
        "probability": probability,
        "intrinsic_value_per_share": intrinsic,
        "irr_5y": irr,
        "irr_3y": None,
        "exit_value_per_share": intrinsic,
        "total_return_5y": intrinsic / price - 1.0 if price else 0.0,
        input_name: model_input,
        "terminal_growth": settings.terminal_growth,
        "irr_5y_status": "valid",
        "scenario_is_finite": math.isfinite(intrinsic),
    }


def _carry(candidate: pd.Series) -> dict:
    keep = [
        "ticker",
        "name",
        "sector",
        "industry",
        "market_cap",
        "price_as_of",
        "is_price_fresh",
        "shares_outstanding",
        "beta",
    ]
    return {column: candidate.get(column) for column in keep if column in candidate.index}


def _watch(candidate: pd.Series, reason: str) -> dict:
    row = candidate.to_dict()
    row["watchlist_reason"] = reason
    return row


def _invalid(candidate: pd.Series, family: str, reason: str) -> dict:
    return {
        **_carry(candidate),
        "model_family": family,
        "valuation_status": "invalid",
        "invalid_reason": reason,
    }


def _model_note(family: str) -> str:
    if family == REIT:
        return "P/AFFO Gordon proxy; no property-level NOI or maintenance-capex detail"
    return "Justified P/B residual-income proxy; no regulatory-capital or reserve-detail model"


def _quality_score(scenarios: list[dict]) -> float:
    base = next(row for row in scenarios if row["scenario"] == "base")
    bear = next(row for row in scenarios if row["scenario"] == "bear")
    if base["intrinsic_value_per_share"] <= 0:
        return 0.0
    return min(max(bear["intrinsic_value_per_share"] / base["intrinsic_value_per_share"], 0.0), 1.0)


def _justified_book_value(
    book_ps: float,
    roe: float,
    cost_equity_: float,
    settings: SpecialistModelSettings,
) -> float:
    g = min(settings.terminal_growth, cost_equity_ - _MIN_DENOMINATOR)
    justified_pb = max(0.0, (roe - g) / max(cost_equity_ - g, _MIN_DENOMINATOR))
    return book_ps * justified_pb


def _annualized_gap(intrinsic: float, price: float, horizon: int = 5) -> float:
    if intrinsic <= 0 or price <= 0:
        return _IRR_FLOOR
    return (intrinsic / price) ** (1.0 / horizon) - 1.0


def _quantile(distribution: list[tuple[float, float]], q: float) -> float:
    ordered = sorted(distribution, key=lambda item: item[0])
    cumulative = 0.0
    for value, probability in ordered:
        cumulative += probability
        if cumulative >= q - 1e-12:
            return value
    return ordered[-1][0]


def _ratio_series(numerator: pd.Series, denominator: pd.Series) -> pd.Series:
    values = numerator.astype(float) / denominator.astype(float)
    values = values.replace([math.inf, -math.inf], math.nan).dropna()
    return values


def _latest_positive(frame: pd.DataFrame, column: str) -> float | None:
    if column not in frame:
        return None
    values = frame[column].dropna().astype(float)
    values = values.loc[values > 0]
    return float(values.iloc[-1]) if not values.empty else None


def _growth_from_series(series: pd.Series, settings: SpecialistModelSettings) -> float:
    growth = series.astype(float).pct_change().replace([math.inf, -math.inf], math.nan).dropna()
    if growth.empty:
        return settings.terminal_growth
    return min(max(float(growth.median()), settings.growth_floor), settings.growth_cap)


def _float(value: object) -> float | None:
    if value is None:
        return None
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return None if math.isnan(result) else result
