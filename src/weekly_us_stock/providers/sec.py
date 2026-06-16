"""SEC EDGAR Company Facts: filing-grade cross-checks and fallback evidence.

Used to spot-validate vendor fundamentals (revenue/net income per fiscal year)
rather than as a primary feed. SEC requires a descriptive User-Agent that
identifies the caller; set SEC_USER_AGENT in the environment.
"""

from __future__ import annotations

import logging
from typing import Any

import requests
from tenacity import retry, stop_after_attempt, wait_exponential

from weekly_us_stock.providers.base import DataProviderNotConfigured

logger = logging.getLogger(__name__)

TICKER_MAP_URL = "https://www.sec.gov/files/company_tickers.json"
COMPANY_FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"

_REVENUE_TAGS = ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues"]
_OPERATING_INCOME_TAGS = ["OperatingIncomeLoss"]
_NET_INCOME_TAGS = ["NetIncomeLoss"]
_SHARES_TAGS = [
    "WeightedAverageNumberOfDilutedSharesOutstanding",
    "WeightedAverageNumberOfSharesOutstandingBasic",
]
_SEC_METRICS = ("revenue", "operating_income", "net_income", "shares_diluted")


def extract_annual_concept(
    facts: dict[str, Any], tags: list[str], unit: str = "USD"
) -> dict[int, float]:
    """fiscal_year -> value for the first tag with annual 10-K data in `unit`
    ("USD" for dollar concepts, "shares" for share counts)."""

    us_gaap = (facts.get("facts") or {}).get("us-gaap") or {}
    for tag in tags:
        units = (us_gaap.get(tag) or {}).get("units") or {}
        series = units.get(unit) or []
        annual = {
            int(item["fy"]): float(item["val"])
            for item in series
            if item.get("form") == "10-K" and item.get("fp") == "FY" and item.get("fy")
        }
        if annual:
            return annual
    return {}


class SecProvider:
    name = "sec"

    def __init__(
        self,
        user_agent: str | None,
        session: requests.Session | None = None,
        request_timeout: float = 30.0,
    ) -> None:
        if not user_agent:
            raise DataProviderNotConfigured("SEC_USER_AGENT is not set")
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": user_agent})
        self.request_timeout = request_timeout
        self._ticker_to_cik: dict[str, int] | None = None

    def cik_for_ticker(self, ticker: str) -> int | None:
        if self._ticker_to_cik is None:
            payload = self._get(TICKER_MAP_URL)
            self._ticker_to_cik = {
                str(item["ticker"]).upper(): int(item["cik_str"])
                for item in (payload or {}).values()
            }
        return self._ticker_to_cik.get(ticker.upper())

    def fetch_annual_facts(self, ticker: str) -> dict[str, dict[int, float]]:
        """Return {"revenue": {fy: value}, "net_income": {fy: value}} from 10-K facts."""

        cik = self.cik_for_ticker(ticker)
        if cik is None:
            return {}
        payload = self._get(COMPANY_FACTS_URL.format(cik=cik))
        if not payload:
            return {}
        return {
            "revenue": extract_annual_concept(payload, _REVENUE_TAGS),
            "operating_income": extract_annual_concept(payload, _OPERATING_INCOME_TAGS),
            "net_income": extract_annual_concept(payload, _NET_INCOME_TAGS),
            "shares_diluted": extract_annual_concept(
                payload, _SHARES_TAGS, unit="shares"
            ),
        }

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, max=30), reraise=True)
    def _get(self, url: str) -> Any:
        response = self.session.get(url, timeout=self.request_timeout)
        response.raise_for_status()
        return response.json()


def sec_divergence(
    fmp_metrics: dict[str, float | None],
    sec_facts: dict[str, dict[int, float]],
    fiscal_year: int,
    *,
    soft: float,
    hard: float,
    min_metrics: int,
) -> tuple[str, float, str | None]:
    """Compare FMP vs SEC 10-K values for ONE fiscal year across the core
    metrics (same fiscal year, same unit). Returns (status, max_divergence,
    worst_metric); status is ok | soft_divergence | hard_divergence |
    unchecked (too few metrics in common)."""

    divergences: dict[str, float] = {}
    for metric in _SEC_METRICS:
        fmp_value = fmp_metrics.get(metric)
        sec_value = (sec_facts.get(metric) or {}).get(fiscal_year)
        if fmp_value is None or sec_value is None:
            continue
        denom = max(abs(float(sec_value)), 1e-9)
        divergences[metric] = abs(float(fmp_value) - float(sec_value)) / denom
    if len(divergences) < min_metrics:
        return "unchecked", 0.0, None
    worst_metric = max(divergences, key=divergences.__getitem__)
    max_divergence = divergences[worst_metric]
    if max_divergence >= hard:
        return "hard_divergence", max_divergence, worst_metric
    if max_divergence >= soft:
        return "soft_divergence", max_divergence, worst_metric
    return "ok", max_divergence, worst_metric
