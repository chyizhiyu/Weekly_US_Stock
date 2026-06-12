"""Financial Modeling Prep provider built on the current "stable" API.

Accounts created after 2025-08-31 cannot use the legacy /api/v3 endpoints, so
everything here targets https://financialmodelingprep.com/stable/. With this
single key the provider covers what Polygon and FRED would otherwise supply:

- daily bars  -> /stable/batch-eod (whole market per trading day)
- risk-free   -> /stable/treasury-rates (10y yield)
- metadata    -> /stable/company-screener + /stable/profile-bulk (CSV parts
                 with ipoDate, isAdr, averageVolume, sector/industry)

HTTP access is isolated in ``_get``; every payload-to-frame transformation is
a pure function so tests run on canned payloads without network access.

Known limitations (documented, not hidden):
- FMP does not expose a clean one-off/non-recurring item line, so
  ``one_off_items`` is 0 here; normalization still works through full-cycle
  margin medians, and the SEC provider exists for spot validation.
- If batch-eod is unavailable on a plan, prices degrade to a quote snapshot
  (single pseudo-bar, day volume as the liquidity proxy) and the run is
  flagged via degraded_sources().
"""

from __future__ import annotations

import csv
import io
import logging
import threading
import time
from datetime import UTC, date, datetime, timedelta
from typing import Any

import pandas as pd
import requests
from tenacity import retry, stop_after_attempt, wait_exponential

from weekly_us_stock.providers.base import (
    CodeList,
    DataProviderNotConfigured,
)
from weekly_us_stock.utils.calendar import is_trading_day, previous_trading_day

logger = logging.getLogger(__name__)

BASE_URL = "https://financialmodelingprep.com/stable"

_EXCHANGE_ALIASES = {
    "NYSE": "NYSE",
    "NEW YORK STOCK EXCHANGE": "NYSE",
    "NASDAQ": "NASDAQ",
    "NASDAQ GLOBAL SELECT": "NASDAQ",
    "NASDAQ GLOBAL MARKET": "NASDAQ",
    "NASDAQ CAPITAL MARKET": "NASDAQ",
    "AMEX": "AMEX",
    "NYSE AMERICAN": "AMEX",
    "OTC": "OTC",
    "OTCBB": "OTC",
    "PNK": "OTC",
}


def normalize_exchange(raw: str | None) -> str:
    if not raw:
        return "UNKNOWN"
    return _EXCHANGE_ALIASES.get(str(raw).strip().upper(), str(raw).strip().upper())


def classify_security(symbol: str, name: str, *, is_etf: bool, is_fund: bool) -> str:
    """Best-effort security-type classification from FMP flags plus naming
    conventions. Anything ambiguous should fail closed downstream."""

    if is_etf:
        return "etf"
    if is_fund:
        return "mutual_fund"
    upper_name = (name or "").upper()
    upper_symbol = (symbol or "").upper()
    if upper_symbol.endswith(("-WT", ".WS", "+")) or "WARRANT" in upper_name:
        return "warrant"
    if "-P" in upper_symbol or " PREF" in upper_name or "PREFERRED" in upper_name:
        return "preferred"
    if (
        upper_symbol.endswith((".U", "-UN"))
        or upper_name.endswith(" UNITS")
        or " UNIT" in upper_name
    ):
        return "unit"
    if (
        "ACQUISITION CORP" in upper_name
        or "ACQUISITION COMPANY" in upper_name
        or "SPAC" in upper_name
    ):
        return "spac"
    if "ETN" in upper_name.split():
        return "etn"
    if "CLOSED END FUND" in upper_name or upper_name.endswith(" FUND"):
        return "closed_end_fund"
    return "common_stock"


def transform_screener(payload: list[dict[str, Any]], fetched_at: str, as_of: date) -> pd.DataFrame:
    rows = []
    for item in payload:
        symbol = item.get("symbol", "")
        name = item.get("companyName") or ""
        price = _f(item.get("price"))
        market_cap = _f(item.get("marketCap"))
        shares = market_cap / price if market_cap and price else None
        rows.append(
            {
                "ticker": symbol,
                "name": name,
                "exchange": normalize_exchange(item.get("exchangeShortName")),
                "security_type": classify_security(
                    symbol,
                    name,
                    is_etf=bool(item.get("isEtf")),
                    is_fund=bool(item.get("isFund")),
                ),
                "is_adr": str(item.get("country") or "US").upper() != "US",
                "listing_date": None,  # enriched from profile-bulk
                "sector": item.get("sector") or "",
                "industry": item.get("industry") or "",
                "country": item.get("country") or "US",
                "shares_outstanding": shares,
                "beta": item.get("beta"),
                "market_cap_hint": market_cap,
                "as_of": as_of.isoformat(),
                "source": "fmp:company-screener",
                "fetched_at": fetched_at,
            }
        )
    return pd.DataFrame(rows)


def transform_profile_bulk(csv_text: str) -> pd.DataFrame:
    """One /stable/profile-bulk CSV part -> enrichment columns."""

    rows = []
    for item in csv.DictReader(io.StringIO(csv_text)):
        price = _f(item.get("price"))
        market_cap = _f(item.get("marketCap"))
        shares = market_cap / price if market_cap and price else None
        rows.append(
            {
                "ticker": item.get("symbol"),
                "listing_date_profile": item.get("ipoDate") or None,
                "is_adr_profile": str(item.get("isAdr", "")).strip().lower() == "true",
                "is_etf_profile": str(item.get("isEtf", "")).strip().lower() == "true",
                "is_fund_profile": str(item.get("isFund", "")).strip().lower() == "true",
                "shares_outstanding_profile": shares,
                "beta_profile": _f(item.get("beta")),
                "avg_volume_profile": _f(item.get("averageVolume")),
            }
        )
    return pd.DataFrame(rows)


def transform_statements(
    income: list[dict[str, Any]],
    balance: list[dict[str, Any]],
    cashflow: list[dict[str, Any]],
    fetched_at: str,
    as_of: date,
) -> pd.DataFrame:
    balance_by_year = {str(item.get("fiscalYear")): item for item in balance}
    cash_by_year = {str(item.get("fiscalYear")): item for item in cashflow}
    rows = []
    for item in income:
        year = str(item.get("fiscalYear") or "")
        bal = balance_by_year.get(year, {})
        cf = cash_by_year.get(year, {})
        pretax = _f(item.get("incomeBeforeTax"))
        tax = _f(item.get("incomeTaxExpense"))
        effective_tax = tax / pretax if pretax and tax is not None and pretax > 0 else None
        buybacks = -_f(cf.get("commonStockRepurchased"), 0.0)  # negative cash out in FMP
        dividends = _f(cf.get("commonDividendsPaid"), None)
        if dividends is None:
            dividends = _f(cf.get("netDividendsPaid"), 0.0)
        rows.append(
            {
                "ticker": item.get("symbol"),
                "fiscal_year": int(year) if year.isdigit() else None,
                "fiscal_end": item.get("date"),
                "filing_date": item.get("filingDate") or item.get("date"),
                "revenue": _f(item.get("revenue")),
                "gross_profit": _f(item.get("grossProfit")),
                "operating_income": _f(item.get("operatingIncome")),
                "one_off_items": 0.0,  # not separable from FMP statements
                "net_income": _f(item.get("netIncome")),
                "ocf": _f(cf.get("operatingCashFlow")),
                "capex": abs(_f(cf.get("capitalExpenditure"), 0.0)),
                "depreciation": _f(cf.get("depreciationAndAmortization")),
                "sbc": _f(cf.get("stockBasedCompensation"), 0.0),
                "dividends_paid": abs(dividends or 0.0),
                "buybacks": max(buybacks, 0.0),
                "share_issuance": _f(cf.get("commonStockIssuance"), 0.0),
                "shares_diluted": _f(item.get("weightedAverageShsOutDil")),
                "total_debt": _f(bal.get("totalDebt")),
                "cash": _f(bal.get("cashAndShortTermInvestments")),
                "interest_expense": _f(item.get("interestExpense"), 0.0),
                "total_equity": _f(bal.get("totalStockholdersEquity")),
                "effective_tax_rate": effective_tax,
                "is_estimate": False,
                "as_of": as_of.isoformat(),
                "source": "fmp:statements",
                "fetched_at": fetched_at,
            }
        )
    return pd.DataFrame(rows)


def transform_estimates(
    payload: list[dict[str, Any]], fetched_at: str, as_of: date
) -> pd.DataFrame:
    rows = []
    for item in payload:
        raw_date = str(item.get("date") or "")
        rows.append(
            {
                "ticker": item.get("symbol"),
                "fiscal_year": int(raw_date[:4]) if raw_date[:4].isdigit() else None,
                "revenue_mean": _f(item.get("revenueAvg")),
                "revenue_low": _f(item.get("revenueLow")),
                "revenue_high": _f(item.get("revenueHigh")),
                "eps_mean": _f(item.get("epsAvg")),
                "eps_low": _f(item.get("epsLow")),
                "eps_high": _f(item.get("epsHigh")),
                "num_analysts": item.get("numAnalystsRevenue") or item.get("numAnalystsEps"),
                "is_estimate": True,
                "as_of": as_of.isoformat(),
                "source": "fmp:analyst-estimates",
                "fetched_at": fetched_at,
            }
        )
    return pd.DataFrame(rows)


def transform_batch_eod(
    payload: list[dict[str, Any]], trade_date: date, fetched_at: str, as_of: date
) -> pd.DataFrame:
    rows = []
    for item in payload:
        close = _f(item.get("close"))
        volume = _f(item.get("volume"), 0.0)
        rows.append(
            {
                "ticker": item.get("symbol"),
                "trade_date": trade_date.isoformat(),
                "close": close,
                "volume": volume,
                "dollar_volume": (close or 0.0) * (volume or 0.0),
                "as_of": as_of.isoformat(),
                "source": "fmp:batch-eod",
                "fetched_at": fetched_at,
            }
        )
    return pd.DataFrame(rows)


def transform_quotes(payload: list[dict[str, Any]], fetched_at: str, as_of: date) -> pd.DataFrame:
    """Quote snapshot -> single pseudo-bar per ticker (fallback price source)."""

    rows = []
    for item in payload:
        price = _f(item.get("price"))
        volume = _f(item.get("volume"), 0.0)
        trade_ts = item.get("timestamp")
        trade_date = (
            datetime.fromtimestamp(int(trade_ts), tz=UTC).date().isoformat()
            if trade_ts
            else as_of.isoformat()
        )
        rows.append(
            {
                "ticker": item.get("symbol"),
                "trade_date": trade_date,
                "close": price,
                "volume": volume,
                "dollar_volume": (price or 0.0) * (volume or 0.0),
                "as_of": as_of.isoformat(),
                "source": "fmp:quote-proxy",
                "fetched_at": fetched_at,
            }
        )
    return pd.DataFrame(rows)


def transform_treasury(payload: list[dict[str, Any]], fetched_at: str) -> pd.DataFrame:
    """/stable/treasury-rates rows -> macro frame with the 10y yield."""

    rows = []
    for item in payload:
        value = _f(item.get("year10"))
        if value is None:
            continue
        rows.append(
            {
                "series": "risk_free_10y",
                "value": value / 100.0,  # FMP yields are in percent
                "as_of": item.get("date"),
                "source": "fmp:treasury",
                "fetched_at": fetched_at,
            }
        )
    return pd.DataFrame(rows)


def _f(value: Any, default: float | None = None) -> float | None:
    if value is None or value == "":
        return default
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


class FMPProvider:
    name = "fmp"

    def __init__(
        self,
        api_key: str | None,
        session: requests.Session | None = None,
        base_url: str = BASE_URL,
        request_timeout: float = 60.0,
        min_request_interval: float = 0.21,  # ~285 req/min, under the 300/min plan cap
        max_bulk_parts: int = 20,
    ) -> None:
        if not api_key:
            raise DataProviderNotConfigured("FMP_API_KEY is not set")
        self.api_key = api_key
        self.session = session or requests.Session()
        self.base_url = base_url.rstrip("/")
        self.request_timeout = request_timeout
        self.min_request_interval = min_request_interval
        self.max_bulk_parts = max_bulk_parts
        self._degraded: list[str] = []
        self._throttle_lock = threading.Lock()
        self._last_request = 0.0

    # -- DataProvider interface -------------------------------------------------

    def fetch_universe(self, as_of: date) -> pd.DataFrame:
        fetched_at = _now_iso()
        # One request per exchange: the combined market exceeds the screener's
        # 10000-row page and would silently truncate. ETFs/funds are excluded
        # at the source; the type filter still catches stragglers via the
        # profile flags and name heuristics.
        frames = []
        for exchange in ("NYSE", "NASDAQ", "AMEX"):
            payload = self._get(
                "company-screener",
                {
                    "exchange": exchange,
                    "limit": 10000,
                    "isActivelyTrading": "true",
                    "isEtf": "false",
                    "isFund": "false",
                },
            )
            frames.append(transform_screener(payload or [], fetched_at, as_of))
        frame = pd.concat(frames, ignore_index=True).drop_duplicates(subset=["ticker"])
        if frame.empty:
            return frame
        # market_cap_hint stays in the frame: it lets bounded smoke runs pick
        # the largest names and adds provenance to the universe export.
        return self._enrich_with_bulk_profiles(frame)

    def load_prices(self, tickers: CodeList, as_of: date, lookback_days: int) -> pd.DataFrame:
        fetched_at = _now_iso()
        wanted = set(tickers or [])
        day = as_of if is_trading_day(as_of) else previous_trading_day(as_of)
        frames = []
        for _ in range(lookback_days):
            try:
                payload = self._get("batch-eod", {"date": day.isoformat()})
            except requests.RequestException:
                logger.exception("batch-eod failed for %s", day)
                payload = None
            if payload:
                frame = transform_batch_eod(payload, day, fetched_at, as_of)
                if wanted:
                    frame = frame.loc[frame["ticker"].isin(wanted)]
                frames.append(frame)
            day = previous_trading_day(day)
        result = (
            pd.concat(frames, ignore_index=True)
            if frames
            else pd.DataFrame()
        )
        if result.empty:
            self._degraded.append("fmp:batch-eod-empty->quote-proxy")
            return self._quote_proxy(sorted(wanted), as_of)
        result["trade_date"] = pd.to_datetime(result["trade_date"])
        return result.sort_values(["ticker", "trade_date"]).reset_index(drop=True)

    def load_fundamentals(self, tickers: CodeList, as_of: date) -> pd.DataFrame:
        fetched_at = _now_iso()
        frames = []
        for symbol in tickers or []:
            params = {"symbol": symbol, "period": "annual", "limit": 12}
            income = self._get("income-statement", params)
            balance = self._get("balance-sheet-statement", params)
            cashflow = self._get("cash-flow-statement", params)
            frames.append(
                transform_statements(income or [], balance or [], cashflow or [], fetched_at, as_of)
            )
        result = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
        if not result.empty:
            result["fiscal_end"] = pd.to_datetime(result["fiscal_end"])
            result["filing_date"] = pd.to_datetime(result["filing_date"])
            result = result.loc[result["filing_date"] <= pd.Timestamp(as_of)]
        return result.reset_index(drop=True)

    def load_estimates(self, tickers: CodeList, as_of: date) -> pd.DataFrame:
        fetched_at = _now_iso()
        frames = []
        for symbol in tickers or []:
            payload = self._get(
                "analyst-estimates", {"symbol": symbol, "period": "annual", "limit": 10}
            )
            frames.append(transform_estimates(payload or [], fetched_at, as_of))
        return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()

    def load_macro(self, as_of: date) -> pd.DataFrame:
        fetched_at = _now_iso()
        payload = self._get(
            "treasury-rates",
            {
                "from": (as_of - timedelta(days=30)).isoformat(),
                "to": as_of.isoformat(),
            },
        )
        frame = transform_treasury(payload or [], fetched_at)
        if frame.empty:
            return frame
        frame["as_of"] = pd.to_datetime(frame["as_of"])
        frame = frame.loc[frame["as_of"] <= pd.Timestamp(as_of)]
        return frame.sort_values("as_of").tail(1).reset_index(drop=True)

    def degraded_sources(self) -> list[str]:
        return list(dict.fromkeys(self._degraded))

    # -- internals --------------------------------------------------------------

    def _enrich_with_bulk_profiles(self, frame: pd.DataFrame) -> pd.DataFrame:
        parts = []
        for part in range(self.max_bulk_parts):
            try:
                text = self._get("profile-bulk", {"part": part}, raw=True)
            except requests.RequestException:
                break  # parts end with a 400 once exhausted
            if not text or not text.strip():
                break
            chunk = transform_profile_bulk(text)
            if chunk.empty:
                break
            parts.append(chunk)
        if not parts:
            self._degraded.append("fmp:profile-bulk-unavailable(listing-age-unknown)")
            return frame
        profiles = pd.concat(parts, ignore_index=True).drop_duplicates(subset=["ticker"])
        merged = frame.merge(profiles, on="ticker", how="left")
        merged["listing_date"] = merged["listing_date_profile"]
        merged["is_adr"] = merged["is_adr"] | merged["is_adr_profile"].fillna(False)
        merged["shares_outstanding"] = merged["shares_outstanding_profile"].combine_first(
            merged["shares_outstanding"]
        )
        merged["beta"] = merged["beta"].combine_first(merged["beta_profile"])
        # The profile flags are more reliable than name heuristics for funds.
        etf_mask = merged["is_etf_profile"].fillna(False)
        fund_mask = merged["is_fund_profile"].fillna(False)
        merged.loc[etf_mask, "security_type"] = "etf"
        merged.loc[fund_mask & ~etf_mask, "security_type"] = "mutual_fund"
        return merged.drop(
            columns=[
                "listing_date_profile",
                "is_adr_profile",
                "is_etf_profile",
                "is_fund_profile",
                "shares_outstanding_profile",
                "beta_profile",
                "avg_volume_profile",
            ],
            errors="ignore",
        )

    def _quote_proxy(self, tickers: list[str], as_of: date) -> pd.DataFrame:
        fetched_at = _now_iso()
        frames = []
        for chunk in _chunks(tickers, 100):
            payload = self._get("batch-quote", {"symbols": ",".join(chunk)})
            frames.append(transform_quotes(payload or [], fetched_at, as_of))
        if "fmp:quote-proxy" not in self._degraded:
            self._degraded.append("fmp:quote-proxy")
        result = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
        if not result.empty:
            result["trade_date"] = pd.to_datetime(result["trade_date"])
            result = result.loc[result["trade_date"] <= pd.Timestamp(as_of)]
        return result.reset_index(drop=True)

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, max=30), reraise=True)
    def _get(self, path: str, params: dict[str, Any], raw: bool = False) -> Any:
        self._throttle()
        response = self.session.get(
            f"{self.base_url}/{path}",
            params={**params, "apikey": self.api_key},
            timeout=self.request_timeout,
        )
        response.raise_for_status()
        return response.text if raw else response.json()

    def _throttle(self) -> None:
        if self.min_request_interval <= 0:
            return
        with self._throttle_lock:
            wait = self._last_request + self.min_request_interval - time.monotonic()
            if wait > 0:
                time.sleep(wait)
            self._last_request = time.monotonic()


def _now_iso() -> str:
    return datetime.now(UTC).isoformat()


def _chunks(items: list[str], size: int) -> list[list[str]]:
    return [items[i : i + size] for i in range(0, len(items), size)]
