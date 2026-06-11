"""Industry model routing.

Companies whose economics break the general owner-earnings DCF (banks,
insurers, REITs, pre-profit biotech) are routed to the watchlist instead of
being force-ranked through the wrong model. Deep cyclicals stay in the general
model but get wider scenario spreads via their measured volatility.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

GENERAL = "general_dcf"
BANK = "bank"
INSURANCE = "insurance"
REIT = "reit"
BIOTECH_PREPROFIT = "biotech_preprofit"

SUPPORTED_FAMILIES = {GENERAL}

_WATCHLIST_REASONS = {
    BANK: "bank_model_not_supported",
    INSURANCE: "insurance_model_not_supported",
    REIT: "reit_model_not_supported",
    BIOTECH_PREPROFIT: "preprofit_biotech_not_supported",
}


@dataclass(slots=True)
class ModelRoute:
    family: str
    supported: bool
    watchlist_reason: str | None = None


def route_model_family(
    sector: str | None,
    industry: str | None,
    normalized_operating_margin: float | None,
) -> ModelRoute:
    sector_text = (sector or "").lower()
    industry_text = (industry or "").lower()

    if "bank" in industry_text:
        return _unsupported(BANK)
    if "insurance" in industry_text or "reinsurance" in industry_text:
        return _unsupported(INSURANCE)
    if "reit" in industry_text or (
        "real estate" in sector_text and "trust" in industry_text
    ):
        return _unsupported(REIT)
    if "biotech" in industry_text and (
        normalized_operating_margin is None or normalized_operating_margin <= 0
    ):
        return _unsupported(BIOTECH_PREPROFIT)
    return ModelRoute(family=GENERAL, supported=True)


def _unsupported(family: str) -> ModelRoute:
    return ModelRoute(family=family, supported=False, watchlist_reason=_WATCHLIST_REASONS[family])


def route_unsupported_industries(
    candidates: pd.DataFrame,
    fundamentals: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split candidates into (general-model, watchlist) BEFORE the financial
    hard filters run.

    Banks, insurers and REITs must not be graded by non-financial solvency
    metrics (interest coverage, net debt/EBITDA) — they leave the funnel here
    with an explicit watchlist reason instead of a misleading rejection.
    Pre-profit biotech is watchlisted rather than rejected for losses.
    """

    if candidates.empty:
        return candidates, pd.DataFrame()

    profitability = _median_net_income_map(fundamentals)
    watch_rows: list[dict] = []
    keep_rows: list[dict] = []
    for _, row in candidates.iterrows():
        margin_proxy = profitability.get(str(row["ticker"]))
        route = route_model_family(row.get("sector"), row.get("industry"), margin_proxy)
        if route.supported:
            keep_rows.append(row.to_dict())
        else:
            watch_rows.append(
                {
                    **row.to_dict(),
                    "model_family": route.family,
                    "watchlist_reason": route.watchlist_reason,
                }
            )
    return pd.DataFrame(keep_rows), pd.DataFrame(watch_rows)


def _median_net_income_map(fundamentals: pd.DataFrame) -> dict[str, float | None]:
    """ticker -> median net income of the last three filed years (a cheap
    profitability proxy for the biotech pre-profit decision)."""

    if fundamentals.empty:
        return {}
    result: dict[str, float | None] = {}
    for ticker, group in fundamentals.groupby("ticker"):
        recent = group.sort_values("fiscal_year").tail(3)["net_income"].dropna()
        result[str(ticker)] = float(recent.median()) if not recent.empty else None
    return result
