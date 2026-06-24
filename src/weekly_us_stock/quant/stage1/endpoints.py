"""Pure FMP payload -> point-in-time panel transforms.

Each function takes a raw decoded FMP payload (a list of dicts, exactly what the
async client returns) and emits a tidy point-in-time panel: feature columns plus
``[symbol, event_time, disclosure_time, source]``. No network, no globals - so
every transform is unit-tested on a literal payload.

The single most important line in this module is, for each endpoint, *which raw
field becomes ``disclosure_time``*. That choice is what makes the downstream
alignment free of look-ahead:

============================  =======================  ============================
endpoint                      disclosure_time field    event_time field
============================  =======================  ============================
As-reported income statement  ``acceptedDate``         ``date`` (fiscal period end)
grades-historical             ``date``                 ``date``
earnings-surprise             ``date``                 ``date`` (report date)
economic indicator (GDP/CPI)  ``date`` + publish lag   ``date`` (reference period)
treasury rates                ``date``                 ``date``
EOD prices                    ``date``                 ``date``
============================  =======================  ============================

For statements FMP exposes both ``acceptedDate`` (when the SEC stamped the
filing) and ``filingDate``; we prefer ``acceptedDate`` because it is the precise
moment the document became public and fall back to ``filingDate`` only when the
accepted stamp is absent.
"""

from __future__ import annotations

from collections.abc import Iterable
from datetime import timedelta
from typing import Any

import pandas as pd

from weekly_us_stock.quant.stage1.records import (
    DISCLOSURE_TIME,
    EVENT_TIME,
    SOURCE,
    SYMBOL,
)

_GRADE_BUCKETS = {
    "strongBuy": "n_strong_buy",
    "buy": "n_buy",
    "hold": "n_hold",
    "sell": "n_sell",
    "strongSell": "n_strong_sell",
}

# Sell-side consensus mapped to an ordinal score (higher = more bullish) so a
# distribution collapses to one momentum-friendly number.
_GRADE_SCORE = {
    "n_strong_buy": 5.0,
    "n_buy": 4.0,
    "n_hold": 3.0,
    "n_sell": 2.0,
    "n_strong_sell": 1.0,
}


def _f(value: Any, default: float | None = None) -> float | None:
    if value is None or value == "":
        return default
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _empty(columns: Iterable[str]) -> pd.DataFrame:
    return pd.DataFrame(columns=list(columns))


def parse_income_statement(payload: list[dict[str, Any]], *, symbol: str) -> pd.DataFrame:
    """As-reported income statement -> fundamentals panel.

    ``acceptedDate`` (SEC accept stamp) is the disclosure time; the fiscal
    period end ``date`` is the event time. We keep raw levels plus a couple of
    margin features the later stages can difference into edges/factors.
    """

    cols = [
        SYMBOL,
        EVENT_TIME,
        DISCLOSURE_TIME,
        "revenue",
        "net_income",
        "eps_diluted",
        "gross_margin",
        "operating_margin",
        SOURCE,
    ]
    if not payload:
        return _empty(cols)
    rows = []
    for item in payload:
        revenue = _f(item.get("revenue"))
        gross = _f(item.get("grossProfit"))
        operating = _f(item.get("operatingIncome"))
        disclosure = item.get("acceptedDate") or item.get("filingDate") or item.get("date")
        rows.append(
            {
                SYMBOL: symbol,
                EVENT_TIME: item.get("date"),
                DISCLOSURE_TIME: disclosure,
                "revenue": revenue,
                "net_income": _f(item.get("netIncome")),
                "eps_diluted": _f(item.get("epsdiluted") or item.get("epsDiluted")),
                "gross_margin": (gross / revenue) if revenue else None,
                "operating_margin": (operating / revenue) if revenue else None,
                SOURCE: "fmp:income-statement-as-reported",
            }
        )
    return pd.DataFrame(rows, columns=cols)


def parse_grades_historical(payload: list[dict[str, Any]], *, symbol: str) -> pd.DataFrame:
    """``grades-historical`` -> daily analyst consensus distribution panel.

    Emits the five rating-bucket counts, the total coverage, and a coverage-
    weighted consensus score (higher = more bullish). The publish ``date`` is
    both event and disclosure time (a grade is usable the day it prints).
    """

    cols = [
        SYMBOL,
        EVENT_TIME,
        DISCLOSURE_TIME,
        *_GRADE_BUCKETS.values(),
        "analyst_total",
        "consensus_score",
        SOURCE,
    ]
    if not payload:
        return _empty(cols)
    rows = []
    for item in payload:
        counts = {col: _f(item.get(raw), 0.0) or 0.0 for raw, col in _GRADE_BUCKETS.items()}
        total = sum(counts.values())
        score = (
            sum(counts[col] * weight for col, weight in _GRADE_SCORE.items()) / total
            if total
            else None
        )
        rows.append(
            {
                SYMBOL: symbol,
                EVENT_TIME: item.get("date"),
                DISCLOSURE_TIME: item.get("date"),
                **counts,
                "analyst_total": total,
                "consensus_score": score,
                SOURCE: "fmp:grades-historical",
            }
        )
    return pd.DataFrame(rows, columns=cols)


def parse_earnings_surprise(payload: list[dict[str, Any]], *, symbol: str) -> pd.DataFrame:
    """``earnings-surprise`` -> SUE panel.

    Standardized Unexpected Earnings here is the simple analyst-relative
    surprise ``(actual - estimate) / |estimate|`` (a clean, scale-free proxy;
    the cross-sectional standardisation by historical surprise dispersion is a
    Stage 3 concern). The announcement ``date`` is the disclosure time.
    """

    cols = [
        SYMBOL,
        EVENT_TIME,
        DISCLOSURE_TIME,
        "eps_actual",
        "eps_estimated",
        "eps_surprise",
        "sue",
        SOURCE,
    ]
    if not payload:
        return _empty(cols)
    rows = []
    for item in payload:
        actual = _f(item.get("actualEarningResult") or item.get("actualEarningsResult"))
        estimated = _f(item.get("estimatedEarning") or item.get("estimatedEarnings"))
        surprise = (
            (actual - estimated) if actual is not None and estimated is not None else None
        )
        sue = (surprise / abs(estimated)) if surprise is not None and estimated else None
        rows.append(
            {
                SYMBOL: symbol,
                EVENT_TIME: item.get("date"),
                DISCLOSURE_TIME: item.get("date"),
                "eps_actual": actual,
                "eps_estimated": estimated,
                "eps_surprise": surprise,
                "sue": sue,
                SOURCE: "fmp:earnings-surprise",
            }
        )
    return pd.DataFrame(rows, columns=cols)


def parse_economic_indicator(
    payload: list[dict[str, Any]], *, name: str, publish_lag_days: int
) -> pd.DataFrame:
    """Economic indicator (GDP/CPI/unemployment) -> symbol-less macro panel.

    Macro prints reference a past period and are *announced later*. When the
    payload exposes no release timestamp we approximate disclosure as the
    reference ``date`` plus ``publish_lag_days`` so a month-end can never read a
    figure before it was plausibly released.
    """

    value_col = f"macro_{name}"
    cols = [EVENT_TIME, DISCLOSURE_TIME, value_col, SOURCE]
    if not payload:
        return _empty(cols)
    rows = []
    for item in payload:
        event = pd.to_datetime(item.get("date"), errors="coerce")
        if pd.isna(event):
            continue
        disclosure = event + timedelta(days=publish_lag_days)
        rows.append(
            {
                EVENT_TIME: event,
                DISCLOSURE_TIME: disclosure,
                value_col: _f(item.get("value")),
                SOURCE: f"fmp:economic-{name}",
            }
        )
    return pd.DataFrame(rows, columns=cols)


def parse_treasury_rates(payload: list[dict[str, Any]]) -> pd.DataFrame:
    """``treasury-rates`` -> macro panel with the 10y/2y yields and the slope.

    Yields arrive in percent and are stored as decimals. The term spread
    (10y - 2y) is the classic regime feature later stages route on.
    """

    cols = [EVENT_TIME, DISCLOSURE_TIME, "treasury_10y", "treasury_2y", "term_spread", SOURCE]
    if not payload:
        return _empty(cols)
    rows = []
    for item in payload:
        event = pd.to_datetime(item.get("date"), errors="coerce")
        if pd.isna(event):
            continue
        y10 = _f(item.get("year10"))
        y2 = _f(item.get("year2"))
        rows.append(
            {
                EVENT_TIME: event,
                DISCLOSURE_TIME: event,  # released same day
                "treasury_10y": y10 / 100.0 if y10 is not None else None,
                "treasury_2y": y2 / 100.0 if y2 is not None else None,
                "term_spread": (y10 - y2) / 100.0 if y10 is not None and y2 is not None else None,
                SOURCE: "fmp:treasury-rates",
            }
        )
    return pd.DataFrame(rows, columns=cols)


def parse_eod_prices(payload: list[dict[str, Any]], *, symbol: str) -> pd.DataFrame:
    """EOD price history -> daily price panel for one symbol.

    The trade ``date`` is both event and disclosure time (a close is known at
    that day's close). Adjusted close is preferred when present so total-return
    splits/dividends do not masquerade as price moves.
    """

    cols = [SYMBOL, EVENT_TIME, DISCLOSURE_TIME, "close", "volume", SOURCE]
    if not payload:
        return _empty(cols)
    rows = []
    for item in payload:
        close = _f(item.get("adjClose"))
        if close is None:
            close = _f(item.get("close"))
        rows.append(
            {
                SYMBOL: symbol,
                EVENT_TIME: item.get("date"),
                DISCLOSURE_TIME: item.get("date"),
                "close": close,
                "volume": _f(item.get("volume"), 0.0),
                SOURCE: "fmp:eod",
            }
        )
    return pd.DataFrame(rows, columns=cols)
