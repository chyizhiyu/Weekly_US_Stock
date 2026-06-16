"""SEC 8-K event detection in the material-event gate (v1)."""
from __future__ import annotations

from datetime import date

import pandas as pd

from weekly_us_stock.config import EventGateSettings
from weekly_us_stock.steps.step2_events import (
    build_material_events_frame,
    detect_8k_events,
    detect_material_events,
)

_S = EventGateSettings()
_AS_OF = date(2026, 1, 9)
_NO_PRICES = pd.DataFrame(columns=["ticker", "trade_date", "close"])


def _filing(form: str, filing_date: str, items: str = "") -> dict:
    return {"form": form, "filing_date": filing_date, "items": items}


def test_material_8k_within_lookback_is_detected() -> None:
    filings = {
        "REST": [_filing("8-K/A", "2026-01-05", "4.02,9.01")]
    }  # restatement + routine amendment
    events = detect_8k_events(filings, _AS_OF, _S)
    assert len(events) == 1
    event = events[0]
    assert event.ticker == "REST" and event.source == "sec_8k"
    assert event.event_type == "non_reliance_restatement"
    assert event.event_date == "2026-01-05"
    assert event.revaluation_status == "requires_reunderwriting"


def test_routine_stale_future_and_nonform_filings_are_ignored() -> None:
    filings = {
        "RTN": [_filing("8-K", "2026-01-05", "2.02,7.01,9.01")],  # routine items only
        "OLD": [_filing("8-K", "2025-06-01", "4.02")],            # outside the 90d lookback
        "TEN": [_filing("10-K", "2026-01-05", "")],               # not an 8-K
        "FUT": [_filing("8-K", "2026-02-01", "1.02")],            # future-dated
    }
    assert detect_8k_events(filings, _AS_OF, _S) == []


def test_gate_flags_8k_names_and_is_a_noop_without_filings() -> None:
    candidates = pd.DataFrame(
        [{"ticker": "REST", "name": "Restate Co"}, {"ticker": "OK", "name": "Clean Co"}]
    )
    filings = {"REST": [_filing("8-K", "2026-01-03", "1.02")]}  # contract termination
    flagged = detect_material_events(
        candidates, _NO_PRICES, _S, filings_by_ticker=filings, as_of=_AS_OF
    )
    assert set(flagged.rejected["ticker"]) == {"REST"}
    assert "material_agreement_terminated" in flagged.rejected.iloc[0]["event_flags"]
    assert list(flagged.candidates["ticker"]) == ["OK"]
    # No filings -> price-only path -> unchanged (nothing flagged here).
    assert detect_material_events(candidates, _NO_PRICES, _S).rejected.empty


def test_events_frame_carries_the_audit_fields() -> None:
    candidates = pd.DataFrame([{"ticker": "REST", "name": "R"}])
    filings = {"REST": [_filing("8-K", "2026-01-05", "4.02")]}
    frame = build_material_events_frame(
        candidates, _NO_PRICES, _S, filings_by_ticker=filings, as_of=_AS_OF
    )
    assert list(frame.columns) == [
        "ticker", "event_date", "source", "event_type", "detail", "revaluation_status",
    ]
    assert frame.iloc[0]["event_type"] == "non_reliance_restatement"
