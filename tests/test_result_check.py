"""OpenClaw freshness gate: stale or mismatched reports must never be sent."""

from __future__ import annotations

import json
from datetime import UTC, datetime

from weekly_us_stock.tools.verify_result_metadata import main, verify_metadata
from weekly_us_stock.utils.calendar import most_recent_schedule_start

# Saturday 2026-01-10 08:05 Beijing == 00:05 UTC, right after the weekly cron.
NOW = datetime(2026, 1, 10, 0, 5, tzinfo=UTC)
EXPECTED_AS_OF = "2026-01-09"
SCHEDULE_START = most_recent_schedule_start(NOW)


def _metadata(**overrides) -> dict:
    payload = {
        "as_of": EXPECTED_AS_OF,
        "generated_at": "2026-01-10T01:30:00+00:00",
    }
    payload.update(overrides)
    return payload


def test_current_result_passes() -> None:
    ok, message = verify_metadata(
        _metadata(), expected_as_of=EXPECTED_AS_OF, schedule_start=SCHEDULE_START
    )
    assert ok, message


def test_last_weeks_report_is_rejected() -> None:
    stale = _metadata(as_of="2026-01-02", generated_at="2026-01-03T01:30:00+00:00")
    ok, message = verify_metadata(
        stale, expected_as_of=EXPECTED_AS_OF, schedule_start=SCHEDULE_START
    )
    assert not ok
    assert "mismatch" in message


def test_right_as_of_but_generated_before_this_window_is_rejected() -> None:
    # Same as_of string but generated before this Saturday's trigger window
    # (e.g. a leftover manual run): refuse to relay it.
    replay = _metadata(generated_at="2026-01-08T10:00:00+00:00")
    ok, message = verify_metadata(
        replay, expected_as_of=EXPECTED_AS_OF, schedule_start=SCHEDULE_START
    )
    assert not ok
    assert "stale" in message


def test_missing_or_garbled_timestamps_are_rejected() -> None:
    for bad in [_metadata(generated_at=None), _metadata(generated_at="not-a-date")]:
        ok, _ = verify_metadata(
            bad, expected_as_of=EXPECTED_AS_OF, schedule_start=SCHEDULE_START
        )
        assert not ok


def test_cli_entrypoint_round_trip(tmp_path) -> None:
    fresh = tmp_path / "fresh.json"
    fresh.write_text(json.dumps(_metadata()), encoding="utf-8")
    assert main(["--file", str(fresh), "--now", NOW.isoformat()]) == 0

    stale = tmp_path / "stale.json"
    stale.write_text(
        json.dumps(_metadata(as_of="2026-01-02")), encoding="utf-8"
    )
    assert main(["--file", str(stale), "--now", NOW.isoformat()]) == 1
