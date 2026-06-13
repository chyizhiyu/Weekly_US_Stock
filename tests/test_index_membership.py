"""Index-membership universe restriction (sp500 / nasdaq100 / dowjones)."""

from __future__ import annotations

from datetime import UTC, date, datetime

import pytest

from weekly_us_stock.config import UniverseSettings
from weekly_us_stock.providers.base import PointInTimeUnavailable
from weekly_us_stock.providers.fmp import FMPProvider, extract_constituent_symbols


def _today() -> date:
    return datetime.now(UTC).date()


def test_extract_constituent_symbols_upcases_and_skips_blanks() -> None:
    payload = [
        {"symbol": "aapl", "name": "Apple"},
        {"symbol": " MSFT ", "name": "Microsoft"},
        {"symbol": "", "name": "blank"},
        {"name": "no symbol key"},
        {"symbol": None},
    ]
    assert extract_constituent_symbols(payload) == {"AAPL", "MSFT"}
    assert extract_constituent_symbols([]) == set()


def test_index_constituents_refuses_historical_as_of() -> None:
    # Constituent lists are CURRENT membership: a stale as_of would leak
    # survivorship bias, so the provider must refuse before any HTTP.
    provider = FMPProvider("test-key", min_request_interval=0.0)
    with pytest.raises(PointInTimeUnavailable):
        provider.index_constituents(["sp500"], date(2020, 1, 3))


def test_index_constituents_unions_endpoints(monkeypatch) -> None:
    calls: list[str] = []
    canned = {
        "sp500-constituent": [{"symbol": "AAPL"}, {"symbol": "MSFT"}],
        "nasdaq-constituent": [{"symbol": "MSFT"}, {"symbol": "NVDA"}],
    }

    def fake_get(self, path, params, raw=False):  # noqa: ANN001
        calls.append(path)
        return canned[path]

    monkeypatch.setattr(FMPProvider, "_get", fake_get)
    provider = FMPProvider("test-key", min_request_interval=0.0)
    result = provider.index_constituents(["sp500", "nasdaq100"], _today())
    assert result.symbols == {"AAPL", "MSFT", "NVDA"}
    assert result.union_count == 3
    assert result.per_index_counts == {"sp500": 2, "nasdaq100": 2}
    assert result.restrict is True
    assert result.errors == []
    assert calls == ["sp500-constituent", "nasdaq-constituent"]


def test_index_constituents_rejects_unknown_index() -> None:
    provider = FMPProvider("test-key", min_request_interval=0.0)
    with pytest.raises(ValueError):
        provider.index_constituents(["russell2000"], _today())


def test_universe_settings_normalizes_and_validates_membership() -> None:
    settings = UniverseSettings(index_membership=["SP500", "Nasdaq100", "sp500"])
    assert settings.index_membership == ["sp500", "nasdaq100"]  # lowercased, deduped
    assert UniverseSettings().index_membership == []  # default = full market
    with pytest.raises(ValueError):
        UniverseSettings(index_membership=["dax"])
