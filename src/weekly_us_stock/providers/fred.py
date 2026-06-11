"""FRED provider for the risk-free rate (10y Treasury, series DGS10)."""

from __future__ import annotations

import logging
from datetime import UTC, date, datetime, timedelta
from typing import Any

import pandas as pd
import requests
from tenacity import retry, stop_after_attempt, wait_exponential

from weekly_us_stock.providers.base import DataProviderNotConfigured

logger = logging.getLogger(__name__)

BASE_URL = "https://api.stlouisfed.org/fred"


def transform_observations(
    payload: dict[str, Any], series: str, fetched_at: str
) -> pd.DataFrame:
    rows = []
    for item in payload.get("observations") or []:
        raw = item.get("value")
        if raw in (None, "", "."):
            continue
        rows.append(
            {
                "series": series,
                "value": float(raw) / 100.0,  # FRED yields are in percent
                "as_of": item.get("date"),
                "source": "fred",
                "fetched_at": fetched_at,
            }
        )
    return pd.DataFrame(rows)


class FredProvider:
    name = "fred"

    def __init__(
        self,
        api_key: str | None,
        session: requests.Session | None = None,
        base_url: str = BASE_URL,
        request_timeout: float = 30.0,
    ) -> None:
        if not api_key:
            raise DataProviderNotConfigured("FRED_API_KEY is not set")
        self.api_key = api_key
        self.session = session or requests.Session()
        self.base_url = base_url.rstrip("/")
        self.request_timeout = request_timeout

    def load_macro(self, as_of: date) -> pd.DataFrame:
        fetched_at = datetime.now(UTC).isoformat()
        payload = self._get(
            "/series/observations",
            {
                "series_id": "DGS10",
                "observation_start": (as_of - timedelta(days=30)).isoformat(),
                "observation_end": as_of.isoformat(),
            },
        )
        frame = transform_observations(payload or {}, "risk_free_10y", fetched_at)
        if frame.empty:
            return frame
        frame["as_of"] = pd.to_datetime(frame["as_of"])
        return frame.sort_values("as_of").tail(1).reset_index(drop=True)

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, max=30), reraise=True)
    def _get(self, path: str, params: dict[str, Any]) -> Any:
        response = self.session.get(
            f"{self.base_url}{path}",
            params={**params, "api_key": self.api_key, "file_type": "json"},
            timeout=self.request_timeout,
        )
        response.raise_for_status()
        return response.json()
