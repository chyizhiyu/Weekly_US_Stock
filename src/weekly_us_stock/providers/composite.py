"""Composite provider: FMP for reference data, Polygon for prices, FRED for
macro, with explicit degradation when an optional source is unavailable.

Degradation policy (mirrors the project contract):
- FMP missing  -> the composite cannot run; callers fall back to the sample
  provider and the run is marked degraded.
- Polygon missing -> FMP quote proxy is used for liquidity; flagged.
- FRED missing -> the configured fallback risk-free rate is used; flagged.
Core per-stock data gaps are never papered over here; downstream filters fail
closed instead.
"""

from __future__ import annotations

import logging
from datetime import UTC, date, datetime

import pandas as pd

from weekly_us_stock.config import EnvSettings, WaccSettings
from weekly_us_stock.providers.base import CodeList, DataProviderNotConfigured
from weekly_us_stock.providers.fmp import FMPProvider
from weekly_us_stock.providers.fred import FredProvider
from weekly_us_stock.providers.polygon import PolygonProvider

logger = logging.getLogger(__name__)


class CompositeProvider:
    name = "composite"

    def __init__(
        self,
        env: EnvSettings,
        wacc_settings: WaccSettings,
        fmp: FMPProvider | None = None,
        polygon: PolygonProvider | None = None,
        fred: FredProvider | None = None,
    ) -> None:
        self._degraded: list[str] = []
        self.wacc_settings = wacc_settings

        self.fmp = fmp or FMPProvider(env.fmp_api_key)  # raises when unconfigured

        self.polygon = polygon
        if self.polygon is None and env.polygon_api_key:
            self.polygon = PolygonProvider(env.polygon_api_key)
        if self.polygon is None:
            self._degraded.append("polygon:missing-key->fmp-quote-proxy")

        self.fred = fred
        if self.fred is None and env.fred_api_key:
            self.fred = FredProvider(env.fred_api_key)
        if self.fred is None:
            self._degraded.append("fred:missing-key->fallback-risk-free")

    def fetch_universe(self, as_of: date) -> pd.DataFrame:
        return self.fmp.fetch_universe(as_of)

    def load_prices(self, tickers: CodeList, as_of: date, lookback_days: int) -> pd.DataFrame:
        if self.polygon is not None:
            try:
                return self.polygon.load_prices(tickers, as_of, lookback_days)
            except Exception:
                logger.exception("Polygon price load failed; degrading to FMP quote proxy")
                self._degraded.append("polygon:error->fmp-quote-proxy")
        return self.fmp.load_prices(tickers, as_of, lookback_days)

    def load_fundamentals(self, tickers: CodeList, as_of: date) -> pd.DataFrame:
        return self.fmp.load_fundamentals(tickers, as_of)

    def load_estimates(self, tickers: CodeList, as_of: date) -> pd.DataFrame:
        try:
            return self.fmp.load_estimates(tickers, as_of)
        except Exception:
            logger.exception("Estimate load failed; continuing without estimates")
            self._degraded.append("fmp:estimates-unavailable")
            return pd.DataFrame()

    def load_macro(self, as_of: date) -> pd.DataFrame:
        if self.fred is not None:
            try:
                frame = self.fred.load_macro(as_of)
                if not frame.empty:
                    return frame
                self._degraded.append("fred:empty->fallback-risk-free")
            except Exception:
                logger.exception("FRED macro load failed; using fallback risk-free rate")
                self._degraded.append("fred:error->fallback-risk-free")
        return pd.DataFrame(
            [
                {
                    "series": "risk_free_10y",
                    "value": self.wacc_settings.fallback_risk_free,
                    "as_of": as_of.isoformat(),
                    "source": "config:fallback",
                    "fetched_at": datetime.now(UTC).isoformat(),
                }
            ]
        )

    def degraded_sources(self) -> list[str]:
        return list(dict.fromkeys(self._degraded + self.fmp.degraded_sources()))


def build_composite(env: EnvSettings, wacc_settings: WaccSettings) -> CompositeProvider:
    if not env.fmp_api_key:
        raise DataProviderNotConfigured(
            "Composite provider requires FMP_API_KEY; set it or run --provider sample"
        )
    return CompositeProvider(env, wacc_settings)
