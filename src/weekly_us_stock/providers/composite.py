"""Composite provider: FMP as the workhorse, Polygon/FRED as optional
overrides, with explicit degradation notes when fallbacks engage.

Degradation policy (mirrors the project contract):
- FMP missing -> the composite cannot run; callers fall back to the sample
  provider and the run is marked degraded.
- Polygon missing -> FMP batch-eod serves equivalent daily bars (no flag);
  only the quote-proxy last resort flags the run.
- FRED missing -> FMP treasury-rates serves the 10y yield (no flag); the
  configured constant is the flagged last resort.
Core per-stock data gaps are never papered over here; downstream filters fail
closed instead.
"""

from __future__ import annotations

import logging
from datetime import UTC, date, datetime

import pandas as pd

from weekly_us_stock.config import EnvSettings, WaccSettings
from weekly_us_stock.providers.base import CodeList, DataProviderNotConfigured, IndexConstituents
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
        # No Polygon key is fine: FMP's batch-eod endpoint provides equivalent
        # full-market daily bars; only the quote-proxy fallback marks a run
        # as degraded (see FMPProvider.load_prices).

        self.fred = fred
        if self.fred is None and env.fred_api_key:
            self.fred = FredProvider(env.fred_api_key)
        # No FRED key is fine: FMP's treasury endpoint serves the 10y yield.

    def fetch_universe(self, as_of: date) -> pd.DataFrame:
        return self.fmp.fetch_universe(as_of)

    def index_constituents(self, indices: list[str], as_of: date) -> IndexConstituents:
        return self.fmp.index_constituents(indices, as_of)

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

    def load_ttm(self, tickers: CodeList, as_of: date) -> pd.DataFrame:
        try:
            return self.fmp.load_ttm(tickers, as_of)
        except Exception:
            logger.exception("TTM load failed; anchoring on latest annual reports")
            self._degraded.append("fmp:ttm-unavailable->annual-anchor")
            return pd.DataFrame()

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
                self._degraded.append("fred:empty->fmp-treasury")
            except Exception:
                logger.exception("FRED macro load failed; trying FMP treasury")
                self._degraded.append("fred:error->fmp-treasury")
        try:
            frame = self.fmp.load_macro(as_of)
            if not frame.empty:
                return frame
            self._degraded.append("fmp-treasury:empty->fallback-risk-free")
        except Exception:
            logger.exception("FMP treasury load failed; using fallback risk-free rate")
            self._degraded.append("fmp-treasury:error->fallback-risk-free")
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
