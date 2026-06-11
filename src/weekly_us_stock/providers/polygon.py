"""Polygon.io provider: daily bars via grouped aggregates.

One request per trading day returns bars for the whole US market, which keeps
the weekly run within modest rate limits. Transformations are pure functions.
"""

from __future__ import annotations

import logging
from datetime import UTC, date, datetime
from typing import Any

import pandas as pd
import requests
from tenacity import retry, stop_after_attempt, wait_exponential

from weekly_us_stock.providers.base import CodeList, DataProviderNotConfigured
from weekly_us_stock.utils.calendar import is_trading_day, previous_trading_day

logger = logging.getLogger(__name__)

BASE_URL = "https://api.polygon.io"


def transform_grouped(
    payload: dict[str, Any], trade_date: date, fetched_at: str, as_of: date
) -> pd.DataFrame:
    rows = []
    for item in payload.get("results") or []:
        close = item.get("c")
        volume = item.get("v")
        rows.append(
            {
                "ticker": item.get("T"),
                "trade_date": trade_date.isoformat(),
                "close": close,
                "volume": volume,
                "dollar_volume": (close or 0.0) * (volume or 0.0),
                "as_of": as_of.isoformat(),
                "source": "polygon:grouped-daily",
                "fetched_at": fetched_at,
            }
        )
    return pd.DataFrame(rows)


class PolygonProvider:
    name = "polygon"

    def __init__(
        self,
        api_key: str | None,
        session: requests.Session | None = None,
        base_url: str = BASE_URL,
        request_timeout: float = 30.0,
    ) -> None:
        if not api_key:
            raise DataProviderNotConfigured("POLYGON_API_KEY is not set")
        self.api_key = api_key
        self.session = session or requests.Session()
        self.base_url = base_url.rstrip("/")
        self.request_timeout = request_timeout

    def load_prices(self, tickers: CodeList, as_of: date, lookback_days: int) -> pd.DataFrame:
        fetched_at = datetime.now(UTC).isoformat()
        day = as_of if is_trading_day(as_of) else previous_trading_day(as_of)
        frames = []
        for _ in range(lookback_days):
            payload = self._get(f"/v2/aggs/grouped/locale/us/market/stocks/{day.isoformat()}")
            frames.append(transform_grouped(payload or {}, day, fetched_at, as_of))
            day = previous_trading_day(day)
        result = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
        if result.empty:
            return result
        result["trade_date"] = pd.to_datetime(result["trade_date"])
        if tickers is not None:
            result = result.loc[result["ticker"].isin(list(tickers))]
        return result.sort_values(["ticker", "trade_date"]).reset_index(drop=True)

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, max=30), reraise=True)
    def _get(self, path: str) -> Any:
        response = self.session.get(
            f"{self.base_url}{path}",
            params={"adjusted": "true", "apiKey": self.api_key},
            timeout=self.request_timeout,
        )
        response.raise_for_status()
        return response.json()
