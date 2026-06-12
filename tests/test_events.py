"""Material-event gate: price shocks pull names out of the ranking."""

from __future__ import annotations

import pandas as pd

from weekly_us_stock.config import EventGateSettings
from weekly_us_stock.steps.step2_events import detect_material_events

SETTINGS = EventGateSettings()


def _prices(ticker: str, closes: list[float]) -> pd.DataFrame:
    dates = pd.bdate_range(end="2026-01-09", periods=len(closes))
    return pd.DataFrame(
        {"ticker": ticker, "trade_date": dates, "close": closes}
    )


def _candidates(*tickers: str) -> pd.DataFrame:
    return pd.DataFrame([{"ticker": ticker, "name": ticker} for ticker in tickers])


def test_weekly_crash_is_flagged() -> None:
    closes = [100.0] * 20 + [95.0, 88.0, 80.0, 74.0, 70.0]  # -30% in a week
    result = detect_material_events(_candidates("CRSH"), _prices("CRSH", closes), SETTINGS)
    assert result.candidates.empty
    row = result.rejected.iloc[0]
    assert row["watchlist_reason"] == "material_event_requires_reunderwriting"
    assert "weekly_drop" in row["event_flags"]


def test_slow_grind_drawdown_is_flagged() -> None:
    # No single bad week, but the price has bled 45% from its recent high.
    closes = [100.0 - i * 1.0 for i in range(46)]
    result = detect_material_events(_candidates("BLED"), _prices("BLED", closes), SETTINGS)
    assert "drawdown_from_high" in result.rejected.iloc[0]["event_flags"]


def test_normal_volatility_passes() -> None:
    closes = [100.0 + (i % 5) for i in range(30)]
    result = detect_material_events(_candidates("CALM"), _prices("CALM", closes), SETTINGS)
    assert result.rejected.empty
    assert list(result.candidates["ticker"]) == ["CALM"]


def test_gate_can_be_disabled() -> None:
    closes = [100.0] * 20 + [60.0] * 5
    disabled = EventGateSettings(enabled=False)
    result = detect_material_events(_candidates("CRSH"), _prices("CRSH", closes), disabled)
    assert result.rejected.empty
