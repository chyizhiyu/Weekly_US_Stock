"""Financial Modeling Prep provider: universe, fundamentals, estimates, quotes.

HTTP access is isolated in ``_get``; every payload-to-frame transformation is a
pure function so tests can run on canned JSON without network access.

Known limitations (documented, not hidden):
- FMP does not expose a clean one-off/non-recurring item line, so
  ``one_off_items`` is 0 here; normalization still works through full-cycle
  margin medians, and the SEC provider exists for spot validation.
- When Polygon is unavailable, daily dollar volume is approximated from the
  quote endpoint's average volume; rows are tagged source="fmp:quote-proxy".
"""

from __future__ import annotations

import logging
from datetime import UTC, date, datetime
from typing import Any

import pandas as pd
import requests
from tenacity import retry, stop_after_attempt, wait_exponential

from weekly_us_stock.providers.base import (
    CodeList,
    DataProviderNotConfigured,
)

logger = logging.getLogger(__name__)

BASE_URL = "https://financialmodelingprep.com/api/v3"

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
                "listing_date": None,  # enriched from profiles
                "sector": item.get("sector") or "",
                "industry": item.get("industry") or "",
                "country": item.get("country") or "US",
                "shares_outstanding": None,
                "beta": item.get("beta"),
                "market_cap_hint": item.get("marketCap"),
                "as_of": as_of.isoformat(),
                "source": "fmp:stock-screener",
                "fetched_at": fetched_at,
            }
        )
    return pd.DataFrame(rows)


def transform_profiles(payloads: list[dict[str, Any]]) -> pd.DataFrame:
    rows = []
    for item in payloads:
        shares = None
        if item.get("mktCap") and item.get("price"):
            try:
                shares = float(item["mktCap"]) / float(item["price"])
            except (TypeError, ValueError, ZeroDivisionError):
                shares = None
        rows.append(
            {
                "ticker": item.get("symbol"),
                "listing_date": item.get("ipoDate") or None,
                "is_adr_profile": bool(item.get("isAdr", False)),
                "shares_outstanding": shares,
                "beta_profile": item.get("beta"),
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
    balance_by_year = {item.get("calendarYear"): item for item in balance}
    cash_by_year = {item.get("calendarYear"): item for item in cashflow}
    rows = []
    for item in income:
        year = item.get("calendarYear")
        bal = balance_by_year.get(year, {})
        cf = cash_by_year.get(year, {})
        pretax = _f(item.get("incomeBeforeTax"))
        tax = _f(item.get("incomeTaxExpense"))
        effective_tax = tax / pretax if pretax and pretax > 0 else None
        buybacks = -_f(cf.get("commonStockRepurchased"), 0.0)  # FMP reports negative cash out
        rows.append(
            {
                "ticker": item.get("symbol"),
                "fiscal_year": int(year) if year else None,
                "fiscal_end": item.get("date"),
                "filing_date": item.get("fillingDate")
                or item.get("filingDate")
                or item.get("date"),
                "revenue": _f(item.get("revenue")),
                "gross_profit": _f(item.get("grossProfit")),
                "operating_income": _f(item.get("operatingIncome")),
                "one_off_items": 0.0,  # not separable from FMP statements
                "net_income": _f(item.get("netIncome")),
                "ocf": _f(cf.get("operatingCashFlow")),
                "capex": abs(_f(cf.get("capitalExpenditure"), 0.0)),
                "depreciation": _f(cf.get("depreciationAndAmortization")),
                "sbc": _f(cf.get("stockBasedCompensation"), 0.0),
                "dividends_paid": abs(_f(cf.get("dividendsPaid"), 0.0)),
                "buybacks": max(buybacks, 0.0),
                "share_issuance": _f(cf.get("commonStockIssued"), 0.0),
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
        raw_date = item.get("date") or ""
        rows.append(
            {
                "ticker": item.get("symbol"),
                "fiscal_year": int(str(raw_date)[:4]) if raw_date else None,
                "revenue_mean": _f(item.get("estimatedRevenueAvg")),
                "revenue_low": _f(item.get("estimatedRevenueLow")),
                "revenue_high": _f(item.get("estimatedRevenueHigh")),
                "eps_mean": _f(item.get("estimatedEpsAvg")),
                "eps_low": _f(item.get("estimatedEpsLow")),
                "eps_high": _f(item.get("estimatedEpsHigh")),
                "num_analysts": item.get("numberAnalystEstimatedRevenue")
                or item.get("numberAnalystsEstimatedRevenue"),
                "is_estimate": True,
                "as_of": as_of.isoformat(),
                "source": "fmp:analyst-estimates",
                "fetched_at": fetched_at,
            }
        )
    return pd.DataFrame(rows)


def transform_quotes(payload: list[dict[str, Any]], fetched_at: str, as_of: date) -> pd.DataFrame:
    """Quote snapshot -> single pseudo-bar per ticker (price freshness proxy)."""

    rows = []
    for item in payload:
        price = _f(item.get("price"))
        avg_volume = _f(item.get("avgVolume"), 0.0)
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
                "volume": avg_volume,
                "dollar_volume": (price or 0.0) * avg_volume,
                "as_of": as_of.isoformat(),
                "source": "fmp:quote-proxy",
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
        profile_batch_size: int = 100,
        request_timeout: float = 30.0,
    ) -> None:
        if not api_key:
            raise DataProviderNotConfigured("FMP_API_KEY is not set")
        self.api_key = api_key
        self.session = session or requests.Session()
        self.base_url = base_url.rstrip("/")
        self.profile_batch_size = profile_batch_size
        self.request_timeout = request_timeout
        self._degraded: list[str] = []

    # -- DataProvider interface -------------------------------------------------

    def fetch_universe(self, as_of: date) -> pd.DataFrame:
        fetched_at = _now_iso()
        payload = self._get(
            "stock-screener",
            {
                "exchange": "nyse,nasdaq,amex",
                "limit": 10000,
                "isActivelyTrading": "true",
                "country": "US,CN,GB,DE,JP,KR,TW,IN,IL,NL,FR,CA,BR,AR",
            },
        )
        frame = transform_screener(payload or [], fetched_at, as_of)
        if frame.empty:
            return frame
        frame = self._enrich_profiles(frame, fetched_at)
        return frame.drop(columns=["market_cap_hint"], errors="ignore")

    def load_prices(self, tickers: CodeList, as_of: date, lookback_days: int) -> pd.DataFrame:
        fetched_at = _now_iso()
        symbols = list(tickers or [])
        frames = []
        for chunk in _chunks(symbols, 100):
            payload = self._get(f"quote/{','.join(chunk)}", {})
            frames.append(transform_quotes(payload or [], fetched_at, as_of))
        if "fmp:quote-proxy" not in self._degraded:
            self._degraded.append("fmp:quote-proxy")
        result = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
        if not result.empty:
            result["trade_date"] = pd.to_datetime(result["trade_date"])
            result = result.loc[result["trade_date"] <= pd.Timestamp(as_of)]
        return result.reset_index(drop=True)

    def load_fundamentals(self, tickers: CodeList, as_of: date) -> pd.DataFrame:
        fetched_at = _now_iso()
        frames = []
        for symbol in tickers or []:
            income = self._get(f"income-statement/{symbol}", {"period": "annual", "limit": 12})
            balance = self._get(
                f"balance-sheet-statement/{symbol}", {"period": "annual", "limit": 12}
            )
            cashflow = self._get(f"cash-flow-statement/{symbol}", {"period": "annual", "limit": 12})
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
            payload = self._get(f"analyst-estimates/{symbol}", {"period": "annual", "limit": 4})
            frames.append(transform_estimates(payload or [], fetched_at, as_of))
        return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()

    def load_macro(self, as_of: date) -> pd.DataFrame:
        return pd.DataFrame()  # macro comes from FRED in the composite provider

    def degraded_sources(self) -> list[str]:
        return list(self._degraded)

    # -- internals --------------------------------------------------------------

    def _enrich_profiles(self, frame: pd.DataFrame, fetched_at: str) -> pd.DataFrame:
        candidates = frame.loc[frame["security_type"] == "common_stock", "ticker"].tolist()
        payloads: list[dict[str, Any]] = []
        for chunk in _chunks(candidates, self.profile_batch_size):
            payload = self._get(f"profile/{','.join(chunk)}", {})
            payloads.extend(payload or [])
        if not payloads:
            self._degraded.append("fmp:profiles")
            return frame
        profiles = transform_profiles(payloads)
        merged = frame.merge(profiles, on="ticker", how="left")
        merged["listing_date"] = merged["listing_date_y"].combine_first(merged["listing_date_x"])
        merged["is_adr"] = merged["is_adr"] | merged["is_adr_profile"].fillna(False)
        merged["shares_outstanding"] = merged["shares_outstanding_y"].combine_first(
            merged["shares_outstanding_x"]
        )
        merged["beta"] = merged["beta"].combine_first(merged["beta_profile"])
        return merged.drop(
            columns=[
                "listing_date_x",
                "listing_date_y",
                "is_adr_profile",
                "shares_outstanding_x",
                "shares_outstanding_y",
                "beta_profile",
            ],
            errors="ignore",
        )

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, max=30), reraise=True)
    def _get(self, path: str, params: dict[str, Any]) -> Any:
        response = self.session.get(
            f"{self.base_url}/{path}",
            params={**params, "apikey": self.api_key},
            timeout=self.request_timeout,
        )
        response.raise_for_status()
        return response.json()


def _now_iso() -> str:
    return datetime.now(UTC).isoformat()


def _chunks(items: list[str], size: int) -> list[list[str]]:
    return [items[i : i + size] for i in range(0, len(items), size)]
