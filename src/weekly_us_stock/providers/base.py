from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field
from datetime import date
from typing import Protocol

import pandas as pd

CodeList = Sequence[str] | None


def normalize_ticker(symbol: object) -> str:
    """Canonical ticker key for matching across data sources.

    Vendors disagree on share-class punctuation (``BRK.B`` vs ``BRK-B`` vs
    ``BRK/B``). Fold them to one key so an index constituent is never silently
    dropped just because the screener spells it differently.
    """

    text = str(symbol or "").strip().upper()
    for separator in (".", "/", " "):
        text = text.replace(separator, "-")
    return text


@dataclass(frozen=True)
class IndexConstituents:
    """Structured result of an index-membership fetch (P0-2).

    ``restrict`` is False only for sources that explicitly do not enforce index
    membership (e.g. the sample provider) - never inferred from an empty set.
    """

    requested: list[str]
    per_index_counts: dict[str, int]
    symbols: set[str]
    source: str
    snapshot_date: str | None = None
    errors: list[str] = field(default_factory=list)
    restrict: bool = True

    @property
    def union_count(self) -> int:
        return len(self.symbols)

# Every frame a provider returns must carry provenance columns so reports can
# disclose where each number came from and how fresh it is.
PROVENANCE_COLUMNS = ["as_of", "source", "fetched_at"]

UNIVERSE_COLUMNS = [
    "ticker",
    "name",
    "exchange",
    "security_type",
    "is_adr",
    "listing_date",
    "sector",
    "industry",
    "country",
    "shares_outstanding",
    "beta",
    *PROVENANCE_COLUMNS,
]

PRICE_COLUMNS = ["ticker", "trade_date", "close", "volume", "dollar_volume", *PROVENANCE_COLUMNS]

FUNDAMENTAL_COLUMNS = [
    "ticker",
    "fiscal_year",
    "fiscal_end",
    "filing_date",
    "revenue",
    "gross_profit",
    "operating_income",
    "one_off_items",
    "net_income",
    "ocf",
    "capex",
    "depreciation",
    "sbc",
    "dividends_paid",
    "buybacks",
    "share_issuance",
    "shares_diluted",
    "total_debt",
    "cash",
    "interest_expense",
    "total_equity",
    "effective_tax_rate",
    "is_estimate",
    *PROVENANCE_COLUMNS,
]

ESTIMATE_COLUMNS = [
    "ticker",
    "fiscal_year",
    "revenue_mean",
    "revenue_low",
    "revenue_high",
    "eps_mean",
    "eps_low",
    "eps_high",
    "num_analysts",
    "is_estimate",
    *PROVENANCE_COLUMNS,
]

MACRO_COLUMNS = ["series", "value", *PROVENANCE_COLUMNS]


class DataProvider(Protocol):
    """Point-in-time data access. Implementations MUST NOT return information
    that was not public at ``as_of`` (prices after as_of, filings whose
    filing_date is after as_of, estimate snapshots taken after as_of)."""

    name: str

    def fetch_universe(self, as_of: date) -> pd.DataFrame:
        """US-listed instruments with type/exchange/listing metadata."""
        ...

    def index_constituents(self, indices: list[str], as_of: date) -> IndexConstituents:
        """CURRENT membership of the named indices (``sp500``, ``nasdaq100``,
        ``dowjones``) as a structured result with per-index counts, union
        symbols, source, snapshot date and per-index fetch errors. The caller
        fails closed on empty/incomplete/abnormal results; ``restrict=False``
        means the source does not enforce membership (e.g. the sample
        provider), never an empty set."""
        ...

    def load_prices(self, tickers: CodeList, as_of: date, lookback_days: int) -> pd.DataFrame:
        """Daily bars up to and including as_of for liquidity and entry price."""
        ...

    def load_fundamentals(self, tickers: CodeList, as_of: date) -> pd.DataFrame:
        """Annual statements filed on or before as_of."""
        ...

    def load_ttm(self, tickers: CodeList, as_of: date) -> pd.DataFrame:
        """Trailing-twelve-month anchor rows (one per ticker) built from the
        four most recent quarters filed on or before as_of. Flows are summed;
        balance items and diluted shares come from the latest quarter. May be
        empty, in which case callers anchor on the latest annual report."""
        ...

    def load_estimates(self, tickers: CodeList, as_of: date) -> pd.DataFrame:
        """Analyst estimates as last published on or before as_of."""
        ...

    def load_macro(self, as_of: date) -> pd.DataFrame:
        """Macro series (risk-free rate) as of the run date."""
        ...

    def degraded_sources(self) -> list[str]:
        """Names of sources that were unavailable and replaced by fallbacks."""
        ...


class DataProviderNotConfigured(RuntimeError):
    """Raised when a provider is selected but its credentials are missing."""


class IndexUniverseUnavailable(RuntimeError):
    """Raised when a configured index universe cannot be built safely (empty,
    a constituent endpoint failed, or a count is implausibly low). The run
    fails closed rather than silently screening the full market (P0-2)."""


class PointInTimeUnavailable(RuntimeError):
    """Raised when a historical as_of is requested from a source that only has
    CURRENT snapshots (analyst estimates, active-listing universe). Replaying
    history through such a source would leak future data and survivorship
    bias into the result, so it is refused instead."""


def require_columns(frame: pd.DataFrame, columns: Sequence[str], dataset: str) -> pd.DataFrame:
    missing = [column for column in columns if column not in frame.columns]
    if missing:
        raise ValueError(f"{dataset} frame is missing required columns: {missing}")
    return frame
