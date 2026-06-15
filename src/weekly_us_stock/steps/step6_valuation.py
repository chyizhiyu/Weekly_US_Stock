"""Step 6: run the scenario engine for every modeled company.

Emits two frames: one scenario-level (3 rows per company, fully auditable
assumptions) and one company-level metrics frame consumed by the ranking.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from weekly_us_stock.config import (
    AlertSettings,
    RiskPreferenceSettings,
    ScenarioSettings,
    WaccSettings,
)
from weekly_us_stock.models.valuation import CompanyInputs
from weekly_us_stock.valuation.scenarios import classify_roic, value_company

_CARRY_COLUMNS = [
    "name",
    "sector",
    "industry",
    "model_family",
    "market_cap",
    "financial_persistence_score",
    "roic",
    "incremental_roic",
    "wacc",
    "roic_minus_wacc",
    "normalized_operating_margin",
    "current_operating_margin",
    "revenue_cagr",
    "net_debt_to_ebitda",
    "sbc_intensity",
    "net_share_change_cagr",
    "risk_flags",
    "years_of_data",
    "latest_fiscal_year",
    "anchor_source",
    "latest_filing_date",
    "price_as_of",
    "is_price_fresh",
]


@dataclass(slots=True)
class ValuationStepResult:
    metrics: pd.DataFrame  # finite, in-bound, rankable companies only
    scenario_rows: pd.DataFrame
    skipped: pd.DataFrame  # incomplete inputs, never entered the engine
    invalid: pd.DataFrame  # ran but failed the finite/implausibly-high guard (P0-1)
    roic_routed: pd.DataFrame  # ROIC not meaningful; needs a dedicated model (P1-4)


def run_scenario_valuations(
    quality_frame: pd.DataFrame,
    scenario_settings: ScenarioSettings,
    risk_preferences: RiskPreferenceSettings,
    hurdle_rate: float | None = None,
    *,
    wacc_settings: WaccSettings | None = None,
    alert_settings: AlertSettings | None = None,
) -> ValuationStepResult:
    hurdle = hurdle_rate if hurdle_rate is not None else risk_preferences.hurdle_rate
    wacc_bounds = (
        (wacc_settings.min_wacc, wacc_settings.max_wacc) if wacc_settings is not None else None
    )
    metric_rows: list[dict] = []
    scenario_rows: list[dict] = []
    skipped_rows: list[dict] = []
    roic_routed_rows: list[dict] = []

    # Fade target per company: the industry (then sector) peer-median SBC
    # intensity, falling back to the configured default for thin groups.
    quality_frame = quality_frame.copy()
    quality_frame["mature_sbc_intensity"] = _peer_mature_sbc(
        quality_frame,
        scenario_settings.mature_sbc_intensity_default,
        scenario_settings.sbc_peer_min_count,
    )

    for _, row in quality_frame.iterrows():
        inputs = _to_inputs(row)
        if inputs is None:
            skipped_rows.append(
                {"ticker": row.get("ticker"), "skip_reason": "incomplete_valuation_inputs"}
            )
            continue
        # P1-4: a negative / undefined ROIC is not valued as a low positive one;
        # route it to a dedicated-model watchlist with its status.
        roic_status = classify_roic(inputs)
        if roic_status != "ok":
            routed = {
                "ticker": inputs.ticker,
                "price": inputs.price,
                "roic": inputs.roic,
                "incremental_roic": inputs.incremental_roic,
                "roic_status": roic_status,
                "watchlist_reason": f"roic_not_meaningful:{roic_status}",
                "data_confidence": inputs.data_confidence,
                "model_confidence": inputs.model_confidence,
            }
            for column in _CARRY_COLUMNS:
                if column in row.index:
                    routed[column] = row[column]
            roic_routed_rows.append(routed)
            continue
        valuation = value_company(
            inputs,
            scenario_settings,
            risk_preferences,
            wacc_bounds=wacc_bounds,
            alerts=alert_settings,
        )
        catastrophic_tail_scenarios = [
            scenario.assumptions.name
            for scenario in valuation.scenarios
            if scenario.irr_5y_status == "below_lower_bound"
        ]

        for scenario in valuation.scenarios:
            assumption = scenario.assumptions
            scenario_rows.append(
                {
                    "ticker": inputs.ticker,
                    "scenario": assumption.name,
                    "probability": assumption.probability,
                    "revenue_growth_y1": assumption.revenue_growth_y1,
                    "terminal_growth": assumption.terminal_growth,
                    "operating_margin": assumption.operating_margin,
                    "forward_roic": assumption.forward_roic,
                    "terminal_roic": assumption.terminal_roic,
                    "share_change_rate": assumption.share_change_rate,
                    "sbc_fade_speed": assumption.sbc_fade_speed,
                    "reinvestment_rate_y1": scenario.reinvestment_rate_y1,
                    "intrinsic_value_per_share": scenario.intrinsic_value_per_share,
                    "irr_3y": scenario.irr_3y,
                    "irr_5y": scenario.irr_5y,
                    "exit_value_per_share": scenario.exit_value_per_share,
                    "total_return_5y": scenario.total_return_5y,
                    "irr_5y_status": scenario.irr_5y_status,
                    "scenario_is_finite": scenario.is_finite,
                }
            )

        metric = {
            "ticker": inputs.ticker,
            "price": inputs.price,
            "expected_irr": valuation.expected_irr,
            "median_irr": valuation.median_irr,
            "p10_irr": valuation.p10_irr,
            "p90_irr": valuation.p90_irr,
            "above_hurdle_weight": valuation.above_hurdle_weight,
            "hurdle_rate": hurdle,
            "permanent_loss_weight": valuation.permanent_loss_weight,
            "expected_shortfall": valuation.expected_shortfall,
            "hurdle_cvar": valuation.hurdle_cvar,
            "intrinsic_value_low": valuation.intrinsic_value_low,
            "intrinsic_value_base": valuation.intrinsic_value_base,
            "intrinsic_value_high": valuation.intrinsic_value_high,
            "intrinsic_value_bear": valuation.intrinsic_value_bear,
            "intrinsic_value_bull": valuation.intrinsic_value_bull,
            "scenario_order_inversion": valuation.scenario_order_inversion,
            "scenario_order_note": valuation.scenario_order_note,
            "upside_to_base": valuation.intrinsic_value_base / inputs.price - 1.0
            if inputs.price
            else None,
            "model_confidence": valuation.model_confidence,
            "data_confidence": valuation.data_confidence,
            "model_uncertainty": valuation.model_uncertainty,
            # Three separate lenses, never compressed into one score:
            # quality of the business, attractiveness of the price, and how
            # much the evidence behind both can be trusted.
            "business_quality": inputs.financial_persistence,
            "valuation_excess": valuation.median_irr - hurdle,
            "evidence_confidence": valuation.data_confidence * valuation.model_confidence,
            # P0-1 fail-closed routing fields.
            "valuation_status": valuation.valuation_status,
            "invalid_reason": valuation.invalid_reason,
            "invalid_fields": ";".join(valuation.invalid_fields),
            # P1-2 boundary / extreme-valuation audit.
            "assumption_flags": ";".join(valuation.assumption_flags),
            "valuation_alerts": ";".join(valuation.valuation_alerts),
            "requires_manual_review": valuation.requires_manual_review,
            "roic_status": roic_status,  # "ok" here; non-ok was routed out (P1-4)
            "catastrophic_tail_floor_applied": bool(catastrophic_tail_scenarios),
            "catastrophic_tail_scenarios": ";".join(catastrophic_tail_scenarios),
        }
        for column in _CARRY_COLUMNS:
            if column in row.index:
                metric[column] = row[column]
        metric_rows.append(metric)

    all_metrics = pd.DataFrame(metric_rows)
    if all_metrics.empty:
        valid_metrics = all_metrics
        invalid_metrics = all_metrics
    else:
        # P0-1: only finite, in-bound valuations are rankable. Everything else
        # is routed to the watchlist by the pipeline with its auditable reason.
        is_valid = all_metrics["valuation_status"] == "valid"
        valid_metrics = all_metrics.loc[is_valid].reset_index(drop=True)
        invalid_metrics = all_metrics.loc[~is_valid].reset_index(drop=True)

    return ValuationStepResult(
        metrics=valid_metrics,
        scenario_rows=pd.DataFrame(scenario_rows),
        skipped=pd.DataFrame(skipped_rows),
        invalid=invalid_metrics,
        roic_routed=pd.DataFrame(roic_routed_rows),
    )


def _peer_mature_sbc(frame: pd.DataFrame, default: float, min_count: int) -> pd.Series:
    """Per-company SBC fade target: the median SBC intensity of its industry
    peers, falling back to its sector peers, then the configured default.
    Groups with fewer than ``min_count`` members are not trusted."""

    if frame.empty or "sbc_intensity" not in frame.columns:
        return pd.Series(default, index=frame.index, dtype=float)
    own = pd.to_numeric(frame["sbc_intensity"], errors="coerce").clip(lower=0.0).fillna(0.0)
    result = own.copy()  # no peer evidence => no fade (target = own intensity)
    resolved = pd.Series(False, index=frame.index)
    for column in ("industry", "sector"):  # finest grouping first
        if column not in frame.columns:
            continue
        grouped = own.groupby(frame[column])
        median = grouped.transform("median")
        count = grouped.transform("count")
        eligible = (
            (~resolved) & frame[column].notna() & (count >= min_count) & median.notna()
        )
        result = result.mask(eligible, median)
        resolved = resolved | eligible
    # Never assume SBC fades below the configured floor.
    return result.clip(lower=default)


def _to_inputs(row: pd.Series) -> CompanyInputs | None:
    required = [
        "ticker",
        "price",
        "shares_diluted",
        "net_debt",
        "revenue",
        "normalized_operating_margin",
        "current_operating_margin",
        "tax_rate",
        "revenue_cagr",
        "roic",
        "wacc",
        "cost_of_debt_after_tax",
    ]
    for column in required:
        value = row.get(column)
        if value is None or (isinstance(value, float) and pd.isna(value)):
            return None
    if float(row["price"]) <= 0 or float(row["shares_diluted"]) <= 0:
        return None

    return CompanyInputs(
        ticker=str(row["ticker"]),
        price=float(row["price"]),
        shares_outstanding=float(row["shares_diluted"]),
        net_debt=float(row["net_debt"]),
        latest_revenue=float(row["revenue"]),
        normalized_operating_margin=float(row["normalized_operating_margin"]),
        current_operating_margin=float(row["current_operating_margin"]),
        tax_rate=float(row["tax_rate"]),
        hist_revenue_cagr=float(row["revenue_cagr"]),
        analyst_growth=_optional_float(row.get("analyst_growth")),
        analyst_dispersion=_optional_float(row.get("analyst_dispersion")),
        roic=float(row["roic"]),
        incremental_roic=_optional_float(row.get("incremental_roic")),
        wacc=float(row["wacc"]),
        cost_of_debt_after_tax=float(row["cost_of_debt_after_tax"]),
        financial_persistence=float(row.get("financial_persistence_score") or 0.5),
        cyclicality=float(row.get("cyclicality") or 0.0),
        margin_volatility=float(row.get("margin_volatility") or 0.0),
        net_share_change_rate=float(row.get("net_share_change_cagr") or 0.0),
        sbc_intensity=float(row.get("sbc_intensity") or 0.0),
        mature_sbc_intensity=float(row.get("mature_sbc_intensity") or 0.02),
        data_confidence=float(row.get("data_confidence") or 1.0),
        model_confidence=float(row.get("model_confidence") or 1.0),
    )


def _optional_float(value: object) -> float | None:
    if value is None:
        return None
    try:
        result = float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None
    return None if pd.isna(result) else result
