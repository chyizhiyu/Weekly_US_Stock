from __future__ import annotations

from collections.abc import Sequence
from datetime import date
from typing import Protocol

import pandas as pd

CodeList = Sequence[str] | None

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

    def load_prices(self, tickers: CodeList, as_of: date, lookback_days: int) -> pd.DataFrame:
        """Daily bars up to and including as_of for liquidity and entry price."""
        ...

    def load_fundamentals(self, tickers: CodeList, as_of: date) -> pd.DataFrame:
        """Annual statements filed on or before as_of."""
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


def require_columns(frame: pd.DataFrame, columns: Sequence[str], dataset: str) -> pd.DataFrame:
    missing = [column for column in columns if column not in frame.columns]
    if missing:
        raise ValueError(f"{dataset} frame is missing required columns: {missing}")
    return frame
