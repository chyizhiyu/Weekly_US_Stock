"""P2-1: structured turnaround watchlist + re-underwriting state machine."""

from __future__ import annotations

from datetime import date

import pandas as pd

from weekly_us_stock.reports.turnaround import TURNAROUND_STATES, build_turnaround_watchlist

AS_OF = date(2026, 6, 12)


def _event_frame(**overrides: object) -> pd.DataFrame:
    base = {
        "ticker": "SMCI",
        "event_flags": "weekly_drop:-30%;drawdown_from_high:-45%",
        "latest_filing_date": "2026-01-15",  # stale, predates the shock
        "price_as_of": "2026-06-12",
    }
    base.update(overrides)
    return pd.DataFrame([base])


def test_event_parsed_and_awaiting_evidence_by_default() -> None:
    row = build_turnaround_watchlist(_event_frame(), AS_OF).iloc[0]
    assert row["ticker"] == "SMCI"
    assert row["event_triggers"] == "weekly_drop;drawdown_from_high"
    assert abs(row["weekly_drop"] - (-0.30)) < 1e-9
    assert abs(row["drawdown_from_high"] - (-0.45)) < 1e-9
    assert row["status"] == "awaiting_new_evidence"
    assert row["status"] in TURNAROUND_STATES
    assert "post-event" in row["evidence_needed"]
    assert row["reason_unrankable"]  # states WHY it cannot be ranked


def test_fresh_post_event_filing_becomes_reunderwriting_ready() -> None:
    row = build_turnaround_watchlist(_event_frame(latest_filing_date="2026-06-05"), AS_OF).iloc[0]
    assert row["status"] == "reunderwriting_ready"
    assert "re-underwriting" in row["evidence_needed"]


def test_never_auto_assigns_structural_impairment() -> None:
    # Without news/8-K the system must not decide temporary vs structural.
    row = build_turnaround_watchlist(_event_frame(latest_filing_date="2019-01-01"), AS_OF).iloc[0]
    assert row["status"] != "structural_impairment"


def test_empty_event_frame_is_safe() -> None:
    out = build_turnaround_watchlist(pd.DataFrame(), AS_OF)
    assert out.empty
    assert {"ticker", "status", "evidence_needed"} <= set(out.columns)
