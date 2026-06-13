"""P0-2: a configured index universe fails closed and matches tickers robustly."""

from __future__ import annotations

from datetime import UTC, date, datetime

import pandas as pd
import pytest

from weekly_us_stock.config import load_settings
from weekly_us_stock.models.screening import StepSummary
from weekly_us_stock.pipeline import WeeklyUSStockPipeline
from weekly_us_stock.providers.base import (
    IndexConstituents,
    IndexUniverseUnavailable,
    normalize_ticker,
)
from weekly_us_stock.providers.sample import SampleDataProvider


def _today() -> date:
    return datetime.now(UTC).date()


class _FakeProvider:
    """Only needs index_constituents; the restriction helper calls nothing else."""

    def __init__(self, constituents: IndexConstituents) -> None:
        self._constituents = constituents

    def index_constituents(self, indices: list[str], as_of: date) -> IndexConstituents:
        return self._constituents


def _pipeline(min_floors: dict[str, int] | None = None) -> WeeklyUSStockPipeline:
    settings = load_settings()
    if min_floors is not None:
        settings.universe.index_min_constituents = min_floors
    return WeeklyUSStockPipeline(settings=settings)


def _summary() -> StepSummary:
    return StepSummary(name="step1_universe", input_count=0, output_count=0, elapsed_seconds=0.0)


def _universe(tickers: list[str]) -> pd.DataFrame:
    return pd.DataFrame({"ticker": tickers})


def test_normalize_ticker_folds_share_class_punctuation() -> None:
    assert normalize_ticker("BRK.B") == "BRK-B"
    assert normalize_ticker("BRK/B") == "BRK-B"
    assert normalize_ticker("brk-b") == "BRK-B"
    assert normalize_ticker(" aapl ") == "AAPL"


def test_empty_union_fails_closed() -> None:
    constituents = IndexConstituents(
        requested=["sp500"], per_index_counts={"sp500": 0}, symbols=set(),
        source="fmp:constituent", restrict=True,
    )
    with pytest.raises(IndexUniverseUnavailable):
        _pipeline()._restrict_to_index_universe(
            _universe(["AAPL"]), _FakeProvider(constituents), ["sp500"], _today(), _summary()
        )


def test_partial_endpoint_failure_fails_closed() -> None:
    constituents = IndexConstituents(
        requested=["sp500", "nasdaq100"],
        per_index_counts={"sp500": 500, "nasdaq100": 0},
        symbols={f"T{i}" for i in range(500)},
        source="fmp:constituent",
        errors=["nasdaq100: fetch failed (ConnectionError)"],
        restrict=True,
    )
    with pytest.raises(IndexUniverseUnavailable):
        _pipeline()._restrict_to_index_universe(
            _universe(["T1"]), _FakeProvider(constituents),
            ["sp500", "nasdaq100"], _today(), _summary(),
        )


def test_implausibly_low_count_fails_closed() -> None:
    # sp500 floor defaults to 400; 50 constituents must abort.
    constituents = IndexConstituents(
        requested=["sp500"], per_index_counts={"sp500": 50},
        symbols={f"T{i}" for i in range(50)}, source="fmp:constituent", restrict=True,
    )
    with pytest.raises(IndexUniverseUnavailable):
        _pipeline()._restrict_to_index_universe(
            _universe(["T1"]), _FakeProvider(constituents), ["sp500"], _today(), _summary()
        )


def test_restriction_normalizes_and_reports_unmatched() -> None:
    constituents = IndexConstituents(
        requested=["sp500"], per_index_counts={"sp500": 3},
        symbols={"AAPL", "BRK.B", "GHOST"}, source="fmp:constituent", restrict=True,
    )
    pipe = _pipeline(min_floors={"sp500": 1})
    universe = _universe(["AAPL", "BRK-B", "MSFT"])  # MSFT not a member; BRK-B == BRK.B
    summary = _summary()
    restricted = pipe._restrict_to_index_universe(
        universe, _FakeProvider(constituents), ["sp500"], _today(), summary
    )
    # BRK-B kept via normalization (not silently dropped); MSFT (non-member) gone.
    assert set(restricted["ticker"]) == {"AAPL", "BRK-B"}
    # GHOST is a constituent with no screener security: surfaced, not hidden.
    assert pipe._index_universe["unmatched_count"] == 1
    assert "GHOST" in pipe._index_universe["unmatched_symbols"]
    assert pipe._index_universe["matched_count"] == 2


def test_sample_provider_does_not_restrict() -> None:
    sample = SampleDataProvider("data/samples")
    result = sample.index_constituents(["sp500"], _today())
    assert result.restrict is False and result.symbols == set()

    universe = _universe(["AAA", "BBB"])
    out = _pipeline()._restrict_to_index_universe(
        universe, sample, ["sp500"], _today(), _summary()
    )
    assert set(out["ticker"]) == {"AAA", "BBB"}  # full sample universe untouched
