"""Validate that a published run_metadata.json belongs to the current weekly task.

Reads metadata JSON from stdin (or --file) and exits 0 only when:
- as_of equals the expected trading day for this scheduling window, and
- generated_at falls at or after the most recent Saturday 00:00 UTC trigger.

This is what stops OpenClaw from replaying last week's report. Standard
library only so OpenClaw hosts can run it straight from the repo checkout.

Usage:
    git show origin/weekly-us-stock-results:latest/run_metadata.json \
      | PYTHONPATH=src python3 -m weekly_us_stock.tools.verify_result_metadata
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import UTC, datetime
from pathlib import Path

from weekly_us_stock.utils.calendar import (
    expected_weekly_as_of,
    most_recent_schedule_start,
)


def verify_metadata(
    metadata: dict,
    *,
    expected_as_of: str,
    schedule_start: datetime,
) -> tuple[bool, str]:
    as_of = metadata.get("as_of")
    if as_of != expected_as_of:
        return False, f"as_of mismatch: result={as_of!r}, expected={expected_as_of!r}"

    raw_generated = metadata.get("generated_at")
    if not raw_generated:
        return False, "metadata is missing generated_at"
    try:
        generated_at = datetime.fromisoformat(str(raw_generated))
    except ValueError:
        return False, f"generated_at is not ISO-8601: {raw_generated!r}"
    if generated_at.tzinfo is None:
        generated_at = generated_at.replace(tzinfo=UTC)
    generated_at = generated_at.astimezone(UTC)

    if generated_at < schedule_start:
        return False, (
            f"stale result: generated_at={generated_at.isoformat()} predates the "
            f"current schedule window starting {schedule_start.isoformat()}"
        )
    return True, f"result for {as_of} generated at {generated_at.isoformat()} is current"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", type=Path, help="Metadata JSON path; default stdin.")
    parser.add_argument(
        "--expected-as-of",
        help="Override the expected as_of (YYYY-MM-DD); default derives from the NYSE calendar.",
    )
    parser.add_argument(
        "--now",
        help="Override the current time (ISO-8601, for tests).",
    )
    args = parser.parse_args(argv)

    now = None
    if args.now:
        now = datetime.fromisoformat(args.now)
        if now.tzinfo is None:
            now = now.replace(tzinfo=UTC)

    raw = args.file.read_text(encoding="utf-8") if args.file else sys.stdin.read()
    try:
        metadata = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"verify_result_metadata: invalid JSON: {exc}", file=sys.stderr)
        return 1

    expected = args.expected_as_of or expected_weekly_as_of(now).isoformat()
    ok, message = verify_metadata(
        metadata,
        expected_as_of=expected,
        schedule_start=most_recent_schedule_start(now),
    )
    print(f"verify_result_metadata: {message}", file=sys.stderr)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
