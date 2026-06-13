"""Structured turnaround watchlist for material-event names (P2-1).

The event gate (step2_events) correctly pulls a price-shocked name out of the
ranking, but a risk control is only half of a turnaround strategy. This builds
the other half: a structured record of WHY each name is un-rankable and WHAT
evidence it needs before it can be re-underwritten, with an explicit status on a
state machine. Crucially it never auto-decides whether an impairment is
temporary or structural - that needs news / 8-K ingestion, which is roadmapped;
until then a name waits in `awaiting_new_evidence` / `reunderwriting_ready`.
"""

from __future__ import annotations

import re
from datetime import date, timedelta

import pandas as pd

# A filing this recent (relative to the weekly event detection) is plausibly a
# post-event report a human can re-underwrite against. Older filings predate the
# shock, so the name keeps waiting for new evidence. News/8-K ingestion would
# replace this heuristic with the exact event date.
_FRESH_FILING_WINDOW_DAYS = 14

# State machine. event_detected is the entry transient; the persisted states are
# awaiting_new_evidence (no post-event filing yet) and reunderwriting_ready (a
# post-event filing/guidance exists, a human can re-underwrite). reunderwritten
# and structural_impairment are reached only by human judgement / news, never
# auto-assigned here.
TURNAROUND_STATES = (
    "event_detected",
    "awaiting_new_evidence",
    "reunderwriting_ready",
    "reunderwritten",
    "structural_impairment",
)

_COLUMNS = [
    "ticker",
    "event_triggers",
    "weekly_drop",
    "drawdown_from_high",
    "event_detected_as_of",
    "latest_filing_date",
    "price_as_of",
    "status",
    "reason_unrankable",
    "evidence_needed",
]


def build_turnaround_watchlist(event_flagged: pd.DataFrame, as_of: date) -> pd.DataFrame:
    if event_flagged.empty:
        return pd.DataFrame(columns=_COLUMNS)

    rows: list[dict] = []
    for _, row in event_flagged.iterrows():
        flags = str(row.get("event_flags") or "")
        triggers = ";".join(part.split(":")[0] for part in flags.split(";") if part)
        filing = row.get("latest_filing_date")
        has_new_evidence = _has_fresh_post_event_filing(filing, as_of)
        status = "reunderwriting_ready" if has_new_evidence else "awaiting_new_evidence"
        price_as_of = row.get("price_as_of")
        rows.append(
            {
                "ticker": row.get("ticker"),
                "event_triggers": triggers,
                "weekly_drop": _parse_pct(flags, "weekly_drop"),
                "drawdown_from_high": _parse_pct(flags, "drawdown_from_high"),
                "event_detected_as_of": as_of.isoformat(),
                "latest_filing_date": "" if filing is None or pd.isna(filing) else str(filing),
                "price_as_of": "" if price_as_of is None else str(price_as_of),
                "status": status,
                "reason_unrankable": (
                    "price already reflects the event; pre-event earning power is stale"
                ),
                "evidence_needed": (
                    "human re-underwriting of revenue/margin/growth on the post-event filing"
                    if has_new_evidence
                    else "a post-event 10-Q/10-K or updated guidance reflecting the event"
                ),
            }
        )
    return pd.DataFrame(rows, columns=_COLUMNS)


def _parse_pct(flags: str, key: str) -> float | None:
    match = re.search(rf"{key}:(-?\d+)%", flags)
    return int(match.group(1)) / 100.0 if match else None


def _has_fresh_post_event_filing(filing: object, as_of: date) -> bool:
    if filing is None or (isinstance(filing, float) and pd.isna(filing)):
        return False
    try:
        filing_date = pd.to_datetime(filing).date()
    except (ValueError, TypeError):
        return False
    return as_of - timedelta(days=_FRESH_FILING_WINDOW_DAYS) <= filing_date <= as_of
