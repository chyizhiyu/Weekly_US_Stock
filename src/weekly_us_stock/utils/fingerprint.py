"""Stable fingerprints for universe and config comparability (P0-3).

Week-over-week comparison is only meaningful when both runs screened the same
pool with the same result-affecting configuration. These hashes make that
checkable and auditable: a mismatch resets the comparison baseline instead of
emitting bogus "entered / exited / rank change" rows.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Iterable

from weekly_us_stock.providers.base import normalize_ticker

# Config blocks that change neither which names are comparable nor how they
# score: output paths/timezone (app), display-only knobs (report). The universe
# block is fingerprinted separately so a pool change is attributable.
_NON_RESULT_BLOCKS = {"app", "report", "universe"}


def stable_hash(payload: object) -> str:
    text = json.dumps(payload, sort_keys=True, default=str, separators=(",", ":"))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def ticker_set_hash(tickers: Iterable[str]) -> str:
    """Hash of the normalized, sorted ticker set actually screened this run."""

    return stable_hash(sorted({normalize_ticker(ticker) for ticker in tickers}))


def universe_fingerprint(settings: object) -> str:
    """Pool definition: index membership + eligibility filters (not the volatile
    constituent snapshot, so ordinary constituent drift stays comparable)."""

    return stable_hash(settings.universe.model_dump())  # type: ignore[attr-defined]


def config_fingerprint(settings: object) -> str:
    """Hash of every result-affecting model/scoring block."""

    dump = settings.model_dump()  # type: ignore[attr-defined]
    return stable_hash({k: v for k, v in dump.items() if k not in _NON_RESULT_BLOCKS})
