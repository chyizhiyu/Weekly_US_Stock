"""Step 4: normalized operating model + industry model routing.

Produces one row per company with the Layer-2 metrics, WACC, analyst anchors
and a data-confidence score. Companies whose economics need a specialist model
(banks, insurers, REITs, pre-profit biotech) are routed to the WATCHLIST —
they are never force-ranked through the general DCF. Companies whose
normalized earning power cannot be estimated are rejected (fail closed).
"""

from __future__ import annotations

from dataclasses import dataclass, field

import pandas as pd

from weekly_us_stock.config import NormalizationSettings, WaccSettings
from weekly_us_stock.valuation.industry import route_model_family
from weekly_us_stock.valuation.normalize import normalize_company
from weekly_us_stock.valuation.wacc import compute_wacc


@dataclass(slots=True)
class NormalizedResult:
    modeled: pd.DataFrame
    watchlist: pd.DataFrame = field(default_factory=pd.DataFrame)
    rejected: pd.DataFrame = field(default_factory=pd.DataFrame)
    rejection_counts: dict[str, int] = field(default_factory=dict)


def run_normalized_model(
    candidates: pd.DataFrame,
    fundamentals: pd.DataFrame,
    estimates: pd.DataFrame,
    risk_free: float,
    normalization: NormalizationSettings,
    wacc_settings: WaccSettings,
) -> NormalizedResult:
    grouped = (
        {ticker: group for ticker, group in fundamentals.groupby("ticker")}
        if not fundamentals.empty
        else {}
    )
    estimate_map = _estimate_growth_map(estimates)

    modeled_rows: list[dict] = []
    watchlist_rows: list[dict] = []
    rejected_rows: list[dict] = []

    for _, candidate in candidates.iterrows():
        ticker = candidate["ticker"]
        base = candidate.to_dict()
        history = grouped.get(ticker)
        metrics = (
            normalize_company(history, normalization) if history is not None else None
        )
        if metrics is None:
            rejected_rows.append({**base, "rejection_reason": "normalization_failed"})
            continue

        row = {**base, **metrics}
        route = route_model_family(
            candidate.get("sector"),
            candidate.get("industry"),
            metrics["normalized_operating_margin"],
        )
        row["model_family"] = route.family

        if not route.supported:
            watchlist_rows.append({**row, "watchlist_reason": route.watchlist_reason})
            continue

        if metrics["normalized_operating_margin"] <= 0:
            # General-model company whose full-cycle earning power is negative:
            # normalized earnings cannot be estimated -> not rankable.
            rejected_rows.append({**base, "rejection_reason": "no_normalized_earnings"})
            continue

        estimate = estimate_map.get(ticker, {})
        row["analyst_growth"] = estimate.get("growth")
        row["analyst_dispersion"] = estimate.get("dispersion")
        row["has_estimates"] = bool(estimate)

        wacc, cost_of_debt = compute_wacc(
            risk_free=risk_free,
            beta=candidate.get("beta"),
            market_cap=float(row.get("market_cap") or 0.0),
            total_debt=max(float(row["net_debt"]), 0.0),
            interest_coverage=row["interest_coverage"],
            tax_rate=row["tax_rate"],
            settings=wacc_settings,
        )
        row["risk_free"] = risk_free
        row["wacc"] = wacc
        row["cost_of_debt_after_tax"] = cost_of_debt
        row["roic_minus_wacc"] = (row["roic"] - wacc) if row["roic"] is not None else None
        row["data_confidence"] = _data_confidence(row)

        modeled_rows.append(row)

    rejected = pd.DataFrame(rejected_rows)
    counts = (
        rejected["rejection_reason"].value_counts().to_dict() if not rejected.empty else {}
    )
    return NormalizedResult(
        modeled=pd.DataFrame(modeled_rows),
        watchlist=pd.DataFrame(watchlist_rows),
        rejected=rejected,
        rejection_counts={str(k): int(v) for k, v in counts.items()},
    )


def _estimate_growth_map(estimates: pd.DataFrame) -> dict[str, dict[str, float]]:
    """ticker -> forward revenue growth and dispersion from the nearest
    estimated fiscal year with analyst coverage."""

    if estimates.empty:
        return {}
    # Live feeds include already-reported fiscal years; keep forward years only
    # (the year before the snapshot year may still be unreported, so keep it).
    min_year = int(pd.to_datetime(estimates["as_of"]).dt.year.max()) - 1
    result: dict[str, dict[str, float]] = {}
    for ticker, group in estimates.groupby("ticker"):
        group = group.dropna(subset=["revenue_mean"]).sort_values("fiscal_year")
        group = group.loc[group["fiscal_year"] >= min_year]
        if len(group) < 2:
            continue
        first, second = group.iloc[0], group.iloc[1]
        if first["revenue_mean"] and first["revenue_mean"] > 0:
            growth = float(second["revenue_mean"]) / float(first["revenue_mean"]) - 1.0
            dispersion = None
            if second.get("revenue_high") and second.get("revenue_low"):
                dispersion = (
                    float(second["revenue_high"]) - float(second["revenue_low"])
                ) / float(second["revenue_mean"])
            entry: dict[str, float] = {"growth": growth}
            if dispersion is not None:
                entry["dispersion"] = dispersion
            result[str(ticker)] = entry
    return result


def _data_confidence(row: dict) -> float:
    """0.2..1.0 — how complete and fresh the inputs behind this company are."""

    confidence = 1.0
    years = int(row.get("years_of_data") or 0)
    if years < 8:
        confidence -= 0.05 * (8 - years)
    if not row.get("has_estimates"):
        confidence -= 0.15
    beta = row.get("beta")
    if beta is None or pd.isna(beta):
        confidence -= 0.05
    if not bool(row.get("is_price_fresh", True)):
        confidence -= 0.20
    if row.get("interest_coverage") is None and float(row.get("net_debt") or 0.0) > 0:
        confidence -= 0.05
    return max(confidence, 0.2)
