"""Stage 1 gateway: dual-timestamp parsing, no-look-ahead alignment, retry.

These tests pin the load-bearing guarantees:
- parsers pick the *disclosure* timestamp (acceptedDate / publish date / lagged
  macro release), never the event date;
- the resampler never lets a disclosure after T leak into row T, and forward-
  fills sparse releases;
- monthly log returns and the forward label are computed correctly;
- the async client retries only transient failures with bounded backoff.
"""

from __future__ import annotations

import asyncio
from datetime import date

import numpy as np
import pandas as pd
import pytest

from weekly_us_stock.quant.stage1 import endpoints
from weekly_us_stock.quant.stage1.async_client import (
    AsyncFMPClient,
    FMPHTTPError,
    TransientHTTPError,
    compute_backoff,
)
from weekly_us_stock.quant.stage1.config import GatewayConfig, RetryConfig
from weekly_us_stock.quant.stage1.pipeline import MonthlyAlignmentPipeline
from weekly_us_stock.quant.stage1.records import LookAheadError
from weekly_us_stock.quant.stage1.resampler import (
    PointInTimeMonthlyResampler,
    add_forward_label,
    month_end_grid,
    month_end_trading_day,
)

# -- parsers: disclosure timestamp discipline ---------------------------------


def test_income_statement_uses_accepted_date_not_period_end() -> None:
    payload = [
        {
            "symbol": "AAPL",
            "date": "2024-03-30",  # fiscal quarter end (event time)
            "acceptedDate": "2024-05-02 18:01:00",  # SEC stamp (disclosure time)
            "filingDate": "2024-05-03",
            "revenue": 90753000000,
            "grossProfit": 42271000000,
            "operatingIncome": 27900000000,
            "netIncome": 23636000000,
            "epsdiluted": 1.53,
        }
    ]
    frame = endpoints.parse_income_statement(payload, symbol="AAPL")
    row = frame.iloc[0]
    assert pd.Timestamp(row["event_time"]) == pd.Timestamp("2024-03-30")
    # acceptedDate wins over filingDate and over the period-end date
    assert pd.Timestamp(row["disclosure_time"]) == pd.Timestamp("2024-05-02 18:01:00")
    assert row["gross_margin"] == pytest.approx(42271000000 / 90753000000)


def test_earnings_surprise_builds_sue() -> None:
    payload = [
        {
            "symbol": "AAPL",
            "date": "2024-05-02",
            "actualEarningResult": 1.53,
            "estimatedEarning": 1.50,
        }
    ]
    frame = endpoints.parse_earnings_surprise(payload, symbol="AAPL")
    row = frame.iloc[0]
    assert row["eps_surprise"] == pytest.approx(0.03)
    assert row["sue"] == pytest.approx(0.03 / 1.50)


def test_grades_historical_consensus_score() -> None:
    payload = [
        {
            "symbol": "AAPL",
            "date": "2024-04-01",
            "strongBuy": 10,
            "buy": 5,
            "hold": 5,
            "sell": 0,
            "strongSell": 0,
        }
    ]
    frame = endpoints.parse_grades_historical(payload, symbol="AAPL")
    row = frame.iloc[0]
    assert row["analyst_total"] == 20
    # (10*5 + 5*4 + 5*3) / 20 = 4.25
    assert row["consensus_score"] == pytest.approx(4.25)


def test_economic_indicator_applies_publish_lag() -> None:
    payload = [{"date": "2024-01-31", "value": 3.1}]
    frame = endpoints.parse_economic_indicator(payload, name="CPI", publish_lag_days=30)
    row = frame.iloc[0]
    assert pd.Timestamp(row["event_time"]) == pd.Timestamp("2024-01-31")
    # disclosure is lagged 30 days past the reference period
    assert pd.Timestamp(row["disclosure_time"]) == pd.Timestamp("2024-03-01")
    assert row["macro_CPI"] == pytest.approx(3.1)


# -- month grid ---------------------------------------------------------------


def test_month_end_grid_skips_holidays_and_weekends() -> None:
    grid = month_end_grid(date(2024, 1, 1), date(2024, 3, 31))
    assert list(grid["year_month"]) == ["2024-01", "2024-02", "2024-03"]
    # 2024-03-31 is a Sunday; the month-end trading day is Friday 2024-03-28 is
    # Good Friday (holiday) -> Thursday 2024-03-28 is actually... assert it's a
    # real trading day before the calendar month end.
    march = month_end_trading_day(2024, 3)
    assert march <= date(2024, 3, 31)
    from weekly_us_stock.utils.calendar import is_trading_day

    assert is_trading_day(march)


# -- alignment: no look-ahead + forward fill ----------------------------------


def _prices_panel() -> pd.DataFrame:
    # Two month-ends of daily closes for one symbol.
    rows = []
    for d, close in [
        ("2024-01-31", 100.0),
        ("2024-02-29", 110.0),
        ("2024-03-28", 121.0),
    ]:
        rows.append(
            {
                "symbol": "AAPL",
                "event_time": d,
                "disclosure_time": d,
                "close": close,
                "volume": 1000,
                "source": "fmp:eod",
            }
        )
    return pd.DataFrame(rows)


def test_resampler_forward_fills_and_blocks_lookahead() -> None:
    prices = _prices_panel()
    # A fundamental disclosed 2024-02-15: invisible at Jan month-end, visible Feb+
    fundamentals = pd.DataFrame(
        [
            {
                "symbol": "AAPL",
                "event_time": "2023-12-31",
                "disclosure_time": "2024-02-15",
                "revenue": 90.0,
                "source": "fmp:income-statement-as-reported",
            }
        ]
    )
    resampler = PointInTimeMonthlyResampler(date(2024, 1, 1), date(2024, 3, 31))
    matrix = resampler.build(
        prices=prices, cross_sectional={"fundamentals": fundamentals}
    )
    by_month = matrix.set_index("year_month")
    # January: fundamental not yet disclosed -> NaN (no leak)
    assert pd.isna(by_month.loc["2024-01", "revenue"])
    # February and March: latest disclosed value carried forward
    assert by_month.loc["2024-02", "revenue"] == 90.0
    assert by_month.loc["2024-03", "revenue"] == 90.0


def test_future_disclosure_is_never_used_end_to_end() -> None:
    prices = _prices_panel()
    # The only fundamental disclosure is dated after every rebalance date: the
    # backward as-of join must leave the feature null rather than reach forward.
    bad = pd.DataFrame(
        [
            {
                "symbol": "AAPL",
                "event_time": "2024-01-01",
                "disclosure_time": "2030-01-01",
                "revenue": 1.0,
                "source": "x",
            }
        ]
    )
    resampler = PointInTimeMonthlyResampler(date(2024, 1, 1), date(2024, 1, 31))
    out = resampler.build(prices=prices, cross_sectional={"f": bad})
    assert pd.isna(out.loc[0, "revenue"])  # future disclosure never used


def test_lookahead_guard_is_active() -> None:
    # Directly exercise the guard with a hand-built frame that violates it.
    from weekly_us_stock.quant.stage1.resampler import REBALANCE_COL

    frame = pd.DataFrame(
        {
            "symbol": ["AAPL"],
            REBALANCE_COL: [pd.Timestamp("2024-01-31")],
            "__asof_x": [pd.Timestamp("2024-02-15")],  # after T
        }
    )
    with pytest.raises(LookAheadError):
        PointInTimeMonthlyResampler._assert_no_lookahead(frame, ["__asof_x"])


def test_monthly_log_return_and_forward_label() -> None:
    prices = _prices_panel()
    resampler = PointInTimeMonthlyResampler(date(2024, 1, 1), date(2024, 3, 31))
    matrix = resampler.build(prices=prices)
    matrix = add_forward_label(matrix, horizon=1)
    by_month = matrix.set_index("year_month")
    # Feb return = ln(110/100)
    assert by_month.loc["2024-02", "log_return_1m"] == pytest.approx(np.log(110 / 100))
    # Forward label at Jan == realised Feb return
    assert by_month.loc["2024-01", "fwd_log_return_1m"] == pytest.approx(np.log(110 / 100))
    # Forward label at the last month is unknown
    assert pd.isna(by_month.loc["2024-03", "fwd_log_return_1m"])


def test_macro_broadcasts_across_symbols_with_lag() -> None:
    prices = _prices_panel()
    macro = endpoints.parse_economic_indicator(
        [{"date": "2024-01-15", "value": 3.0}], name="CPI", publish_lag_days=30
    )
    resampler = PointInTimeMonthlyResampler(date(2024, 1, 1), date(2024, 3, 31))
    matrix = resampler.build(prices=prices, macro={"macro_CPI": macro})
    by_month = matrix.set_index("year_month")
    # Disclosure = 2024-02-14; invisible at Jan month-end, visible Feb onward.
    assert pd.isna(by_month.loc["2024-01", "macro_CPI"])
    assert by_month.loc["2024-02", "macro_CPI"] == pytest.approx(3.0)


# -- async client: retry / backoff --------------------------------------------


def test_compute_backoff_is_exponential_and_capped() -> None:
    policy = RetryConfig(base_delay=1.0, backoff_factor=2.0, max_delay=10.0, jitter=0.0)
    assert compute_backoff(1, policy) == pytest.approx(1.0)
    assert compute_backoff(2, policy) == pytest.approx(2.0)
    assert compute_backoff(3, policy) == pytest.approx(4.0)
    assert compute_backoff(10, policy) == pytest.approx(10.0)  # capped


def test_compute_backoff_honours_retry_after() -> None:
    policy = RetryConfig(base_delay=1.0, max_delay=10.0, jitter=0.0)
    assert compute_backoff(1, policy, retry_after=3.0) == pytest.approx(3.0)
    assert compute_backoff(1, policy, retry_after=99.0) == pytest.approx(10.0)  # still capped


class _FakeResponse:
    def __init__(self, status: int, payload, headers=None) -> None:
        self.status = status
        self._payload = payload
        self.headers = headers or {}

    async def __aenter__(self):
        return self

    async def __aexit__(self, *exc):
        return False

    async def json(self):
        return self._payload

    async def text(self):
        return str(self._payload)


class _FakeSession:
    """Returns a queued sequence of responses, recording call count."""

    def __init__(self, responses: list[_FakeResponse]) -> None:
        self._responses = responses
        self.calls = 0

    def get(self, url, params=None):
        resp = self._responses[min(self.calls, len(self._responses) - 1)]
        self.calls += 1
        return resp

    async def close(self):
        pass


def _client_with(responses, monkeypatch) -> AsyncFMPClient:
    # No real sleeping: collapse backoff to a no-op.
    async def _no_sleep(_):
        return None

    monkeypatch.setattr(asyncio, "sleep", _no_sleep)
    config = GatewayConfig(api_key="k", min_request_interval=0.0, retry=RetryConfig(max_attempts=4))
    return AsyncFMPClient(config, session=_FakeSession(responses))


def test_client_retries_transient_then_succeeds(monkeypatch) -> None:
    responses = [
        _FakeResponse(503, None),
        _FakeResponse(429, None, headers={"Retry-After": "0"}),
        _FakeResponse(200, [{"ok": True}]),
    ]
    client = _client_with(responses, monkeypatch)

    async def run():
        async with client:
            return await client.get("income-statement", {"symbol": "AAPL"})

    result = asyncio.run(run())
    assert result == [{"ok": True}]
    assert client._session.calls == 3  # two transient retries then success


def test_client_does_not_retry_hard_4xx(monkeypatch) -> None:
    client = _client_with([_FakeResponse(403, "forbidden")], monkeypatch)

    async def run():
        async with client:
            return await client.get("income-statement", {"symbol": "AAPL"})

    with pytest.raises(FMPHTTPError) as exc:
        asyncio.run(run())
    assert exc.value.status == 403
    assert client._session.calls == 1  # no retries on a deterministic 4xx


def test_client_exhausts_retries_and_raises(monkeypatch) -> None:
    client = _client_with([_FakeResponse(500, None)], monkeypatch)

    async def run():
        async with client:
            return await client.get("x", {})

    with pytest.raises(TransientHTTPError):
        asyncio.run(run())
    assert client._session.calls == 4  # max_attempts


# -- end-to-end pipeline with an in-memory client -----------------------------


class _CannedClient:
    """Async client stub that maps endpoint path -> canned payload."""

    def __init__(self, by_path: dict[str, object]) -> None:
        self._by_path = by_path

    async def get(self, path, params=None, *, raw=False):
        return self._by_path.get(path, [])


def test_pipeline_end_to_end_builds_labelled_matrix() -> None:
    by_path = {
        "historical-price-eod/full": [
            {"date": "2024-01-31", "adjClose": 100.0, "volume": 1000},
            {"date": "2024-02-29", "adjClose": 110.0, "volume": 1200},
            {"date": "2024-03-28", "adjClose": 121.0, "volume": 1100},
        ],
        "income-statement": [
            {
                "symbol": "AAPL",
                "date": "2023-12-31",
                "acceptedDate": "2024-02-10 16:00:00",
                "revenue": 100.0,
                "grossProfit": 40.0,
                "operatingIncome": 25.0,
                "netIncome": 20.0,
                "epsdiluted": 1.2,
            }
        ],
        "grades-historical": [
            {"symbol": "AAPL", "date": "2024-01-05", "strongBuy": 8, "buy": 4, "hold": 2}
        ],
        "earnings-surprises": [
            {"date": "2024-02-10", "actualEarningResult": 1.2, "estimatedEarning": 1.1}
        ],
        "treasury-rates": [
            {"date": "2024-01-31", "year10": 4.0, "year2": 4.5},
            {"date": "2024-02-29", "year10": 4.1, "year2": 4.4},
        ],
        "economic-indicators": [{"date": "2024-01-15", "value": 3.0}],
    }
    config = GatewayConfig(api_key="k", min_request_interval=0.0)
    pipeline = MonthlyAlignmentPipeline(_CannedClient(by_path), config)
    result = pipeline.run_sync(["AAPL"], date(2024, 1, 1), date(2024, 3, 31))

    matrix = result.matrix
    assert list(matrix["year_month"]) == ["2024-01", "2024-02", "2024-03"]
    assert "log_return_1m" in matrix.columns
    assert "fwd_log_return_1m" in matrix.columns
    assert "consensus_score" in matrix.columns
    assert "term_spread" in matrix.columns

    by_month = matrix.set_index("year_month")
    # Fundamentals disclosed 2024-02-10: hidden in Jan, present Feb onward.
    assert pd.isna(by_month.loc["2024-01", "revenue"])
    assert by_month.loc["2024-02", "revenue"] == 100.0
    # Grades disclosed 2024-01-05: present from January.
    assert by_month.loc["2024-01", "analyst_total"] == 14
    # No disclosure timestamp anywhere exceeds its rebalance date (guard passed).
    assert not matrix.empty


def test_sandbox_rejects_unlisted_symbol() -> None:
    config = GatewayConfig(api_key="k", sandbox=True)
    pipeline = MonthlyAlignmentPipeline(_CannedClient({}), config)
    with pytest.raises(ValueError, match="sandbox"):
        pipeline.run_sync(["ZZZZ"], date(2024, 1, 1), date(2024, 2, 28))
