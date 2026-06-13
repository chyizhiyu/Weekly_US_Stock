"""Material-event gate: price-shock detection from the daily bars.

The VRRM failure mode: the market has already repriced a contract loss /
guidance cut / regulatory hit, but the model still values the company on
pre-event earning power — a manufactured "bargain". News and 8-K ingestion is
roadmapped; until then large price shocks are the observable shadow of every
event class on that list, and any name showing one is pulled from the ranking
into the event watchlist for manual re-underwriting:

- 1-week return below -weekly_drop_threshold, or
- drawdown from the lookback-window high below -drawdown_threshold.

Names return to the ranking only once revenue/margin/growth assumptions have
been re-underwritten (i.e., post-event filings or estimates flow in).
"""

from __future__ import annotations

import pandas as pd

from weekly_us_stock.config import EventGateSettings
from weekly_us_stock.models.screening import FilterFrameResult

MATERIAL_EVENT_REASON = WATCHLIST_REASON = "material_event_requires_reunderwriting"


def detect_material_events(
    candidates: pd.DataFrame,
    prices: pd.DataFrame,
    settings: EventGateSettings,
) -> FilterFrameResult:
    """Split candidates into (clean, event-flagged). The flagged frame carries
    ``watchlist_reason`` and an auditable ``event_flags`` column."""

    if candidates.empty or prices.empty or not settings.enabled:
        return FilterFrameResult(candidates=candidates)

    flags = _price_shock_flags(prices, settings)
    frame = candidates.copy()
    frame["event_flags"] = frame["ticker"].map(flags).fillna("")
    flagged = frame.loc[frame["event_flags"] != ""].copy()
    clean = frame.loc[frame["event_flags"] == ""].drop(columns=["event_flags"])
    if flagged.empty:
        return FilterFrameResult(candidates=clean.reset_index(drop=True))
    flagged["watchlist_reason"] = WATCHLIST_REASON
    return FilterFrameResult(
        candidates=clean.reset_index(drop=True),
        rejected=flagged.reset_index(drop=True),
        rejection_counts={WATCHLIST_REASON: int(len(flagged))},
    )


def _price_shock_flags(prices: pd.DataFrame, settings: EventGateSettings) -> dict[str, str]:
    flags: dict[str, str] = {}
    bars = prices.sort_values(["ticker", "trade_date"])
    for ticker, group in bars.groupby("ticker"):
        closes = group["close"].astype(float).tail(settings.lookback_high_days)
        if len(closes) < 6:
            continue
        reasons = []
        last = float(closes.iloc[-1])
        week_ago = float(closes.iloc[-6])  # five sessions back
        if week_ago > 0 and last / week_ago - 1.0 <= -settings.weekly_drop_threshold:
            reasons.append(f"weekly_drop:{last / week_ago - 1.0:.0%}")
        high = float(closes.max())
        if high > 0 and last / high - 1.0 <= -settings.drawdown_threshold:
            reasons.append(f"drawdown_from_high:{last / high - 1.0:.0%}")
        if reasons:
            flags[str(ticker)] = ";".join(reasons)
    return flags
