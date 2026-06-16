"""Material-event gate: price shocks + SEC 8-K filings pull names out of the ranking.

The VRRM failure mode: the market has already repriced a contract loss / guidance
cut / regulatory hit, but the model still values the company on pre-event earning
power - a manufactured "bargain". Two detectors guard against it:

- price shocks (the observable shadow on the daily bars): a 1-week return below
  -weekly_drop_threshold, or a drawdown from the lookback high below
  -drawdown_threshold;
- SEC 8-K filings (the event itself, before the price fully reflects it): a
  material 8-K item within sec_8k_lookback_days - contract termination (1.02),
  impairment (2.06), auditor change (4.01), non-reliance/restatement (4.02),
  officer change (5.02).

Flagged names carry an auditable ``event_flags`` string and are pulled into the
event watchlist for re-underwriting; structured events (ticker, event_date,
source, event_type, detail, revaluation_status) are emitted for the archive. The
8-K detector is a no-op without filings, so price-only runs are unchanged.
"""
from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from datetime import date, timedelta

import pandas as pd

from weekly_us_stock.config import EventGateSettings
from weekly_us_stock.models.screening import FilterFrameResult

MATERIAL_EVENT_REASON = WATCHLIST_REASON = "material_event_requires_reunderwriting"
_REVALUATION_STATUS = "requires_reunderwriting"

# Adverse / structural 8-K item codes -> event type. Routine items (2.02
# earnings, 7.01 Reg FD, 9.01 exhibits) are intentionally NOT gated.
_8K_ITEM_EVENTS = {
    "1.02": "material_agreement_terminated",
    "2.06": "material_impairment",
    "4.01": "auditor_change",
    "4.02": "non_reliance_restatement",
    "5.02": "officer_director_change",
}

_EVENT_COLUMNS = ["ticker", "event_date", "source", "event_type", "detail", "revaluation_status"]


@dataclass(slots=True)
class MaterialEvent:
    ticker: str
    event_date: str
    source: str
    event_type: str
    detail: str
    revaluation_status: str = _REVALUATION_STATUS


def detect_material_events(
    candidates: pd.DataFrame,
    prices: pd.DataFrame,
    settings: EventGateSettings,
    *,
    filings_by_ticker: dict[str, list[dict]] | None = None,
    as_of: date | None = None,
) -> FilterFrameResult:
    """Split candidates into (clean, event-flagged). The flagged frame carries
    ``watchlist_reason`` and an auditable ``event_flags`` column. Price shocks need
    ``prices``; 8-K events need ``filings_by_ticker`` + ``as_of`` (else a no-op)."""

    if candidates.empty or not settings.enabled:
        return FilterFrameResult(candidates=candidates)
    flags: dict[str, list[str]] = {}
    for event in _collect_events(prices, settings, filings_by_ticker, as_of):
        flags.setdefault(event.ticker, []).append(f"{event.event_type}:{event.detail}")
    frame = candidates.copy()
    frame["event_flags"] = frame["ticker"].astype(str).map(lambda t: ";".join(flags.get(t, [])))
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


def build_material_events_frame(
    candidates: pd.DataFrame,
    prices: pd.DataFrame,
    settings: EventGateSettings,
    *,
    filings_by_ticker: dict[str, list[dict]] | None = None,
    as_of: date | None = None,
) -> pd.DataFrame:
    """One row per detected event (the five audit fields), restricted to the
    candidate set - for the run's events.csv archive."""

    if candidates.empty or not settings.enabled:
        return pd.DataFrame(columns=_EVENT_COLUMNS)
    wanted = set(candidates["ticker"].astype(str))
    events = [
        asdict(event)
        for event in _collect_events(prices, settings, filings_by_ticker, as_of)
        if event.ticker in wanted
    ]
    return pd.DataFrame(events, columns=_EVENT_COLUMNS)


def _collect_events(
    prices: pd.DataFrame,
    settings: EventGateSettings,
    filings_by_ticker: dict[str, list[dict]] | None,
    as_of: date | None,
) -> list[MaterialEvent]:
    events: list[MaterialEvent] = []
    if prices is not None and not prices.empty:
        events.extend(_price_shock_events(prices, settings))
    if settings.sec_8k_enabled and filings_by_ticker and as_of is not None:
        events.extend(detect_8k_events(filings_by_ticker, as_of, settings))
    return events


def _price_shock_events(prices: pd.DataFrame, settings: EventGateSettings) -> list[MaterialEvent]:
    events: list[MaterialEvent] = []
    bars = prices.sort_values(["ticker", "trade_date"])
    for ticker, group in bars.groupby("ticker"):
        closes = group["close"].astype(float).tail(settings.lookback_high_days)
        if len(closes) < 6:
            continue
        last = float(closes.iloc[-1])
        week_ago = float(closes.iloc[-6])  # five sessions back
        high = float(closes.max())
        when = str(group["trade_date"].iloc[-1])[:10]
        if week_ago > 0 and last / week_ago - 1.0 <= -settings.weekly_drop_threshold:
            events.append(
                MaterialEvent(str(ticker), when, "price_shock", "weekly_drop",
                              f"{last / week_ago - 1.0:.0%}")
            )
        if high > 0 and last / high - 1.0 <= -settings.drawdown_threshold:
            events.append(
                MaterialEvent(str(ticker), when, "price_shock", "drawdown_from_high",
                              f"{last / high - 1.0:.0%}")
            )
    return events


def detect_8k_events(
    filings_by_ticker: dict[str, list[dict]],
    as_of: date,
    settings: EventGateSettings,
) -> list[MaterialEvent]:
    """Material 8-K filings within the lookback window -> structured events. Item
    codes are matched by regex so separators/prefixes do not matter; routine items
    not in material_8k_items are ignored."""

    cutoff = as_of - timedelta(days=settings.sec_8k_lookback_days)
    material = set(settings.material_8k_items)
    events: list[MaterialEvent] = []
    for ticker, filings in (filings_by_ticker or {}).items():
        for filing in filings or []:
            form = str(filing.get("form", "")).upper()
            if form not in {"8-K", "8-K/A"}:
                continue
            try:
                filed = date.fromisoformat(str(filing.get("filing_date", ""))[:10])
            except ValueError:
                continue
            if filed < cutoff or filed > as_of:  # within lookback, never future
                continue
            hits = sorted(set(re.findall(r"\d\.\d\d", str(filing.get("items", "")))) & material)
            for code in hits:
                events.append(
                    MaterialEvent(
                        ticker=str(ticker),
                        event_date=filed.isoformat(),
                        source="sec_8k",
                        event_type=_8K_ITEM_EVENTS.get(code, "material_8k"),
                        detail=f"item {code}",
                    )
                )
    return events
