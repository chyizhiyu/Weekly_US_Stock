"""Step 5: financial persistence, earnings quality and risk flags.

``financial_persistence_score`` is deliberately NOT called a moat score: it
measures only HISTORICAL financial persistence (years of ROIC above WACC,
margin stability, excess-return size). It cannot see regulatory change,
substitution, customer concentration or any other structural threat —
structural-moat evidence with explicit failure conditions is roadmapped.
The score is not a bonus; it feeds exactly these channels:
- how long excess returns persist (terminal ROIC persistence in scenarios),
- margin stability (bear-case margin haircut scaling),
- scenario spread width,
- model confidence.
Risk flags are kept as explicit strings for the audit trail and reports.
"""

from __future__ import annotations

import pandas as pd


def run_quality_assessment(modeled: pd.DataFrame, fundamentals: pd.DataFrame) -> pd.DataFrame:
    if modeled.empty:
        return modeled
    frame = modeled.copy()
    grouped = (
        {
            ticker: group.sort_values("fiscal_year")
            for ticker, group in fundamentals.groupby("ticker")
        }
        if not fundamentals.empty
        else {}
    )

    financial_persistence_scores: list[float] = []
    persistence_years: list[int] = []
    model_confidences: list[float] = []
    cyclicality: list[float] = []
    flags: list[str] = []

    for _, row in frame.iterrows():
        history = grouped.get(row["ticker"])
        roic_years = _years_roic_above_wacc(history, row)
        margin_stability = _margin_stability(row)
        moat = _financial_persistence_score(roic_years, margin_stability, row)
        financial_persistence_scores.append(moat)
        persistence_years.append(roic_years)
        cyclicality.append(float(row.get("revenue_volatility") or 0.0))
        model_confidences.append(_model_confidence(row, moat))
        flags.append(";".join(_risk_flags(row)))

    frame["financial_persistence_score"] = financial_persistence_scores
    frame["roic_above_wacc_years"] = persistence_years
    frame["cyclicality"] = cyclicality
    frame["model_confidence"] = model_confidences
    frame["risk_flags"] = flags
    return frame


def _years_roic_above_wacc(history: pd.DataFrame | None, row: pd.Series) -> int:
    if history is None or row.get("wacc") is None:
        return 0
    tax_rate = float(row["tax_rate"])
    wacc = float(row["wacc"])
    count = 0
    for _, year in history.iterrows():
        revenue = float(year.get("revenue") or 0.0)
        if revenue <= 0:
            continue
        adj_op = float(year.get("operating_income") or 0.0) - float(
            year.get("one_off_items") or 0.0
        )
        invested = (
            float(year.get("total_equity") or 0.0)
            + float(year.get("total_debt") or 0.0)
            - float(year.get("cash") or 0.0)
        )
        if invested <= 0:
            continue
        if adj_op * (1.0 - tax_rate) / invested > wacc:
            count += 1
    return count


def _margin_stability(row: pd.Series) -> float:
    margin = float(row.get("normalized_operating_margin") or 0.0)
    volatility = float(row.get("margin_volatility") or 0.0)
    if margin <= 0:
        return 0.0
    return max(0.0, 1.0 - volatility / abs(margin))


def _financial_persistence_score(roic_years: int, margin_stability: float, row: pd.Series) -> float:
    """0..1 from observable persistence evidence only."""

    persistence = min(roic_years / 8.0, 1.0)
    excess = float(row.get("roic_minus_wacc") or 0.0)
    excess_component = min(max(excess / 0.15, 0.0), 1.0)
    score = 0.45 * persistence + 0.30 * margin_stability + 0.25 * excess_component
    return round(min(max(score, 0.0), 1.0), 4)


def _model_confidence(row: pd.Series, moat: float) -> float:
    confidence = 1.0
    confidence -= min(float(row.get("revenue_volatility") or 0.0) * 1.5, 0.35)
    margin = float(row.get("normalized_operating_margin") or 1.0)
    if margin > 0:
        confidence -= min(float(row.get("margin_volatility") or 0.0) / margin, 0.30) * 0.5
    dispersion = row.get("analyst_dispersion")
    if dispersion is not None and not pd.isna(dispersion):
        confidence -= min(float(dispersion), 0.5) * 0.3
    confidence -= 0.15 * (1.0 - moat)
    return round(max(confidence, 0.2), 4)


def _risk_flags(row: pd.Series) -> list[str]:
    flags: list[str] = []
    if float(row.get("net_debt_to_ebitda") or 0.0) > 3.0:
        flags.append("elevated_leverage")
    coverage = row.get("interest_coverage")
    if coverage is not None and not pd.isna(coverage) and float(coverage) < 5.0:
        flags.append("thin_interest_coverage")
    if float(row.get("sbc_intensity") or 0.0) > 0.05:
        flags.append("heavy_sbc")
    if float(row.get("net_share_change_cagr") or 0.0) > 0.03:
        flags.append("ongoing_dilution")
    if float(row.get("revenue_volatility") or 0.0) > 0.15:
        flags.append("cyclical_revenue")
    margin = float(row.get("normalized_operating_margin") or 0.0)
    current = float(row.get("current_operating_margin") or 0.0)
    if margin > 0 and current > margin * 1.5:
        flags.append("peak_cycle_margins")
    ocf_ratio = row.get("ocf_to_net_income")
    if ocf_ratio is not None and not pd.isna(ocf_ratio) and float(ocf_ratio) < 0.8:
        flags.append("weak_cash_conversion")
    incremental = row.get("incremental_roic")
    wacc = float(row.get("wacc") or 0.0)
    if incremental is not None and not pd.isna(incremental) and float(incremental) < wacc:
        flags.append("incremental_roic_below_wacc")
    return flags
