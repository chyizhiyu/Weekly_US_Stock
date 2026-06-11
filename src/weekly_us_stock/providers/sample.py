from __future__ import annotations

from collections.abc import Sequence
from datetime import date
from pathlib import Path

import pandas as pd

from weekly_us_stock.providers.base import (
    ESTIMATE_COLUMNS,
    FUNDAMENTAL_COLUMNS,
    MACRO_COLUMNS,
    PRICE_COLUMNS,
    UNIVERSE_COLUMNS,
    CodeList,
    require_columns,
)


class SampleDataProvider:
    """CSV-backed provider for offline runs, tests and CI smoke checks.

    The CSVs intentionally contain rows dated AFTER typical test as_of dates;
    the point-in-time filters below must hide them, which is what the
    look-ahead-bias tests assert.
    """

    name = "sample"

    def __init__(self, data_dir: str | Path) -> None:
        self.data_dir = Path(data_dir)

    def fetch_universe(self, as_of: date) -> pd.DataFrame:
        frame = self._read_csv("universe.csv", date_columns=["listing_date"])
        frame = frame.loc[pd.to_datetime(frame["listing_date"]).dt.date <= as_of]
        return require_columns(frame.reset_index(drop=True), UNIVERSE_COLUMNS, "universe")

    def load_prices(self, tickers: CodeList, as_of: date, lookback_days: int) -> pd.DataFrame:
        frame = self._read_csv("prices.csv", date_columns=["trade_date"])
        frame = self._filter_tickers(frame, tickers)
        frame = frame.loc[frame["trade_date"] <= pd.Timestamp(as_of)]
        frame = (
            frame.sort_values(["ticker", "trade_date"])
            .groupby("ticker", group_keys=False)
            .tail(lookback_days)
            .reset_index(drop=True)
        )
        return require_columns(frame, PRICE_COLUMNS, "prices")

    def load_fundamentals(self, tickers: CodeList, as_of: date) -> pd.DataFrame:
        frame = self._read_csv("fundamentals.csv", date_columns=["fiscal_end", "filing_date"])
        frame = self._filter_tickers(frame, tickers)
        # Point-in-time: a fiscal year exists only once its report was filed.
        frame = frame.loc[frame["filing_date"] <= pd.Timestamp(as_of)].reset_index(drop=True)
        return require_columns(frame, FUNDAMENTAL_COLUMNS, "fundamentals")

    def load_estimates(self, tickers: CodeList, as_of: date) -> pd.DataFrame:
        frame = self._read_csv("estimates.csv", date_columns=["as_of"])
        frame = self._filter_tickers(frame, tickers)
        frame = frame.loc[frame["as_of"] <= pd.Timestamp(as_of)]
        # Keep the latest snapshot per ticker and fiscal year.
        frame = (
            frame.sort_values(["ticker", "fiscal_year", "as_of"])
            .groupby(["ticker", "fiscal_year"], as_index=False)
            .tail(1)
            .reset_index(drop=True)
        )
        return require_columns(frame, ESTIMATE_COLUMNS, "estimates")

    def load_macro(self, as_of: date) -> pd.DataFrame:
        frame = self._read_csv("macro.csv", date_columns=["as_of"])
        frame = frame.loc[frame["as_of"] <= pd.Timestamp(as_of)]
        frame = (
            frame.sort_values(["series", "as_of"])
            .groupby("series", as_index=False)
            .tail(1)
            .reset_index(drop=True)
        )
        return require_columns(frame, MACRO_COLUMNS, "macro")

    def degraded_sources(self) -> list[str]:
        return []

    def _read_csv(self, filename: str, date_columns: Sequence[str] = ()) -> pd.DataFrame:
        frame = pd.read_csv(self.data_dir / filename)
        for column in date_columns:
            if column in frame:
                frame[column] = pd.to_datetime(frame[column])
        return frame

    @staticmethod
    def _filter_tickers(frame: pd.DataFrame, tickers: CodeList) -> pd.DataFrame:
        if tickers is None:
            return frame
        return frame.loc[frame["ticker"].isin(list(tickers))].reset_index(drop=True)
