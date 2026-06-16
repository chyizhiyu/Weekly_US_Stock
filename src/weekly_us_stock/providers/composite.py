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

from weekly_us_stock.config import EnvSettings, SecReconciliationSettings, WaccSettings
from weekly_us_stock.providers.base import CodeList, DataProviderNotConfigured, IndexConstituents
from weekly_us_stock.providers.fmp import FMPProvider
from weekly_us_stock.providers.fred import FredProvider
from weekly_us_stock.providers.polygon import PolygonProvider
from weekly_us_stock.providers.sec import SecProvider, sec_divergence

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
        sec: SecProvider | None = None,
        sec_reconciliation: SecReconciliationSettings | None = None,
    ) -> None:
        self._degraded: list[str] = []
        self.wacc_settings = wacc_settings
        self.sec_reconciliation = sec_reconciliation or SecReconciliationSettings()

        self.fmp = fmp or FMPProvider(env.fmp_api_key)  # raises when unconfigured

        # SEC is an optional filing-grade cross-check; without credentials the
        # fundamentals are simply left unannotated (status "unchecked").
        self.sec = sec
        if self.sec is None and self.sec_reconciliation.enabled and env.sec_user_agent:
            try:
                self.sec = SecProvider(env.sec_user_agent)
            except DataProviderNotConfigured:
                self.sec = None

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
        return self._reconcile_with_sec(self.fmp.load_fundamentals(tickers, as_of))

    def _reconcile_with_sec(self, fundamentals: pd.DataFrame) -> pd.DataFrame:
        cfg = self.sec_reconciliation
        if fundamentals.empty or self.sec is None or not cfg.enabled:
            return fundamentals
        exempt = {t.upper() for t in cfg.exempt_tickers}
        frame = fundamentals.copy()
        status: dict[str, str] = {}
        divergence: dict[str, float | None] = {}
        penalty: dict[str, float] = {}
        for ticker, group in frame.groupby("ticker"):
            key = str(ticker)
            try:
                facts = self.sec.fetch_annual_facts(key)
            except Exception:
                logger.exception("SEC reconciliation failed for %s; unchecked", key)
                self._degraded.append("sec:fetch-error")
                facts = {}
            status[key], divergence[key], penalty[key] = _reconcile_one(
                group, facts, cfg, key.upper() in exempt
            )
        keys = frame["ticker"].astype(str)
        frame["sec_status"] = keys.map(status)
        frame["sec_max_divergence"] = keys.map(divergence)
        frame["sec_confidence_penalty"] = keys.map(penalty)
        return frame

    def recent_filings(self, tickers: CodeList) -> dict[str, list[dict]]:
        """Recent EDGAR filings per ticker for the event gate (8-K detection).
        Empty when SEC is unconfigured; per-ticker errors degrade softly."""

        if self.sec is None:
            return {}
        out: dict[str, list[dict]] = {}
        for ticker in tickers:
            key = str(ticker)
            try:
                out[key] = self.sec.fetch_recent_filings(key)
            except Exception:
                logger.exception("SEC filings fetch failed for %s", key)
                self._degraded.append("sec:filings-error")
        return out

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


def _opt_float(value: object) -> float | None:
    try:
        result = float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None
    return None if pd.isna(result) else result


def _reconcile_one(
    group: pd.DataFrame,
    facts: dict[str, dict[int, float]],
    cfg: SecReconciliationSettings,
    is_exempt: bool,
) -> tuple[str, float | None, float]:
    """Reconcile one ticker's FMP fundamentals against SEC 10-K facts on the
    latest fiscal year they share."""

    if not facts:
        return "unchecked", None, 0.0
    years = pd.to_numeric(group["fiscal_year"], errors="coerce")
    fmp_years = {int(y) for y in years.dropna()}
    sec_years = {int(fy) for series in facts.values() for fy in series}
    common = sorted(fmp_years & sec_years, reverse=True)
    if not common:
        return "unchecked", None, 0.0
    fiscal_year = common[0]
    fmp_row = group.loc[years == fiscal_year].iloc[-1]
    fmp_metrics = {
        "revenue": _opt_float(fmp_row.get("revenue")),
        "operating_income": _opt_float(fmp_row.get("operating_income")),
        "net_income": _opt_float(fmp_row.get("net_income")),
        "shares_diluted": _opt_float(fmp_row.get("shares_diluted")),
    }
    status, max_divergence, _worst = sec_divergence(
        fmp_metrics,
        facts,
        fiscal_year,
        soft=cfg.soft_divergence,
        hard=cfg.hard_divergence,
        min_metrics=cfg.min_metrics,
    )
    if status == "hard_divergence" and is_exempt:
        status = "exempt"
    penalty = cfg.confidence_penalty if status == "soft_divergence" else 0.0
    return status, max_divergence, penalty


def build_composite(
    env: EnvSettings,
    wacc_settings: WaccSettings,
    sec_reconciliation: SecReconciliationSettings | None = None,
) -> CompositeProvider:
    if not env.fmp_api_key:
        raise DataProviderNotConfigured(
            "Composite provider requires FMP_API_KEY; set it or run --provider sample"
        )
    return CompositeProvider(env, wacc_settings, sec_reconciliation=sec_reconciliation)
