"""Step 1: assemble the US-listed universe and a market snapshot.

The snapshot (price, market cap, trailing dollar volume, price freshness) is
derived from point-in-time daily bars so later steps never touch raw vendor
payloads directly.
"""

from __future__ import annotations

from datetime import date

import pandas as pd

from weekly_us_stock.config import FreshnessSettings, HardFilterSettings
from weekly_us_stock.providers.base import DataProvider


def fetch_universe(provider: DataProvider, as_of: date) -> pd.DataFrame:
    universe = provider.fetch_universe(as_of)
    if universe.empty:
        return universe
    universe = universe.drop_duplicates(subset=["ticker"]).reset_index(drop=True)
    universe["listing_date"] = pd.to_datetime(universe["listing_date"], errors="coerce")
    return universe


def build_market_snapshot(
    universe: pd.DataFrame,
    prices: pd.DataFrame,
    as_of: date,
    hard_filters: HardFilterSettings,
    freshness: FreshnessSettings,
) -> pd.DataFrame:
    """One row per ticker: latest close, trailing average dollar volume,
    market cap and a freshness flag."""

    if prices.empty:
        snapshot = universe[["ticker", "shares_outstanding", "beta"]].copy()
        snapshot["price"] = pd.NA
        snapshot["price_as_of"] = pd.NaT
        snapshot["avg_dollar_volume"] = pd.NA
        snapshot["market_cap"] = pd.NA
        snapshot["is_price_fresh"] = False
        return snapshot

    bars = prices.sort_values(["ticker", "trade_date"])
    window = bars.groupby("ticker", group_keys=False).tail(hard_filters.liquidity_window_days)
    liquidity = (
        window.groupby("ticker")["dollar_volume"].mean().rename("avg_dollar_volume")
    )
    latest = window.groupby("ticker").tail(1).set_index("ticker")

    snapshot = universe[["ticker", "shares_outstanding", "beta"]].merge(
        latest[["close", "trade_date"]].rename(
            columns={"close": "price", "trade_date": "price_as_of"}
        ),
        on="ticker",
        how="left",
    )
    snapshot = snapshot.merge(liquidity, on="ticker", how="left")
    snapshot["market_cap"] = snapshot["price"] * snapshot["shares_outstanding"]
    staleness = pd.Timestamp(as_of) - snapshot["price_as_of"]
    snapshot["is_price_fresh"] = (
        snapshot["price_as_of"].notna()
        & (staleness <= pd.Timedelta(days=freshness.max_price_staleness_days))
    )
    return snapshot
