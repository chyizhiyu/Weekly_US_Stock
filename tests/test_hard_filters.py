"""Layer-1 hard filters: security types, size/liquidity, fail-closed data gates."""

from __future__ import annotations

import pandas as pd
import pytest

from tests.conftest import AS_OF
from weekly_us_stock.config import Settings
from weekly_us_stock.providers.sample import SampleDataProvider
from weekly_us_stock.steps.step1_universe import build_market_snapshot, fetch_universe
from weekly_us_stock.steps.step2_hard_filters import (
    run_financial_hard_filters,
    run_market_filters,
    run_security_type_filters,
)


@pytest.fixture(scope="module")
def universe(sample_provider: SampleDataProvider) -> pd.DataFrame:
    return fetch_universe(sample_provider, AS_OF)


def _reasons(rejected: pd.DataFrame) -> dict[str, str]:
    return dict(zip(rejected["ticker"], rejected["rejection_reason"], strict=True))


class TestSecurityTypeFilters:
    def test_non_common_stock_types_rejected(
        self, universe: pd.DataFrame, settings: Settings
    ) -> None:
        result = run_security_type_filters(
            universe, AS_OF, settings.universe, settings.hard_filters
        )
        reasons = _reasons(result.rejected)
        assert reasons["SPCX"] == "security_type"  # SPAC
        assert reasons["ETFX"] == "security_type"  # ETF
        assert reasons["WRNT"] == "security_type"  # warrant
        assert reasons["PREF"] == "security_type"  # preferred
        assert reasons["OTCP"] == "exchange_not_allowed"  # OTC venue
        assert reasons["NEWIPO"] == "listing_age"  # listed < 3 years
        assert reasons["ADRX"] == "adr_excluded"  # default excludes ADRs
        survivors = set(result.candidates["ticker"])
        assert {"STBL", "LOTO", "BNKA"} <= survivors

    def test_adr_inclusion_is_configurable(
        self, universe: pd.DataFrame, settings: Settings
    ) -> None:
        relaxed = settings.universe.model_copy(update={"include_adrs": True})
        result = run_security_type_filters(universe, AS_OF, relaxed, settings.hard_filters)
        assert "ADRX" in set(result.candidates["ticker"])


class TestMarketFilters:
    def test_market_cap_and_liquidity(
        self,
        universe: pd.DataFrame,
        sample_provider: SampleDataProvider,
        settings: Settings,
    ) -> None:
        type_result = run_security_type_filters(
            universe, AS_OF, settings.universe, settings.hard_filters
        )
        prices = sample_provider.load_prices(
            type_result.candidates["ticker"].tolist(),
            AS_OF,
            settings.hard_filters.liquidity_window_days,
        )
        snapshot = build_market_snapshot(
            type_result.candidates, prices, AS_OF, settings.hard_filters, settings.freshness
        )
        result = run_market_filters(type_result.candidates, snapshot, settings.hard_filters)
        reasons = _reasons(result.rejected)
        assert reasons["TINY"] == "market_cap"
        assert reasons["ILLQ"] == "liquidity"
        assert "STBL" in set(result.candidates["ticker"])

    def test_stale_price_fails_closed(self, settings: Settings) -> None:
        # An IRR computed off an old quote is a guess: stale names are
        # rejected with an explicit reason instead of being ranked.
        candidates = pd.DataFrame([{"ticker": "OLDQ", "name": "Stale Quote Corp"}])
        snapshot = pd.DataFrame(
            [
                {
                    "ticker": "OLDQ",
                    "price": 50.0,
                    "price_as_of": pd.Timestamp("2025-11-01"),
                    "market_cap": 2e9,
                    "avg_dollar_volume": 1e8,
                    "is_price_fresh": False,
                }
            ]
        )
        result = run_market_filters(candidates, snapshot, settings.hard_filters)
        assert _reasons(result.rejected)["OLDQ"] == "stale_price"

    def test_missing_market_data_fails_closed(self, settings: Settings) -> None:
        candidates = pd.DataFrame([{"ticker": "GHOST", "name": "No Price Corp"}])
        snapshot = pd.DataFrame(
            [
                {
                    "ticker": "GHOST",
                    "price": None,
                    "price_as_of": pd.NaT,
                    "market_cap": None,
                    "avg_dollar_volume": None,
                    "is_price_fresh": False,
                }
            ]
        )
        result = run_market_filters(candidates, snapshot, settings.hard_filters)
        assert _reasons(result.rejected)["GHOST"] == "missing_market_data"


def _history(ticker: str, years: int, **overrides) -> pd.DataFrame:
    rows = []
    for index in range(years):
        year = 2024 - years + 1 + index
        row = {
            "ticker": ticker,
            "fiscal_year": year,
            "revenue": 1_000e6,
            "operating_income": 150e6,
            "net_income": 100e6,
            "ocf": 140e6,
            "capex": 40e6,
            "depreciation": 40e6,
            "sbc": 10e6,
            "shares_diluted": 100e6,
            "total_debt": 200e6,
            "cash": 300e6,
            "interest_expense": 10e6,
            "total_equity": 800e6,
        }
        for key, values in overrides.items():
            row[key] = values[index] if isinstance(values, list) else values
        rows.append(row)
    return pd.DataFrame(rows)


class TestFinancialHardFilters:
    def test_sample_dataset_reasons(
        self,
        universe: pd.DataFrame,
        sample_provider: SampleDataProvider,
        settings: Settings,
    ) -> None:
        tickers = ["LOSS", "DEBT", "MISS", "SDIL", "ACCT", "STBL"]
        candidates = universe.loc[universe["ticker"].isin(tickers)]
        fundamentals = sample_provider.load_fundamentals(tickers, AS_OF)
        result = run_financial_hard_filters(candidates, fundamentals, settings.hard_filters)
        reasons = _reasons(result.rejected)
        assert reasons["LOSS"] == "consecutive_losses"
        assert reasons["DEBT"] == "interest_coverage"
        assert reasons["MISS"] == "insufficient_financial_history"  # fail closed
        assert reasons["SDIL"] == "severe_dilution"
        assert reasons["ACCT"] == "earnings_cash_mismatch"
        assert set(result.candidates["ticker"]) == {"STBL"}

    def test_missing_core_fields_fail_closed(self, settings: Settings) -> None:
        candidates = pd.DataFrame([{"ticker": "HOLEY"}])
        history = _history("HOLEY", 6, revenue=[1_000e6] * 5 + [None])
        result = run_financial_hard_filters(candidates, history, settings.hard_filters)
        assert _reasons(result.rejected)["HOLEY"] == "missing_core_financials"

    def test_no_fundamentals_at_all_fails_closed(self, settings: Settings) -> None:
        candidates = pd.DataFrame([{"ticker": "VOID"}])
        result = run_financial_hard_filters(candidates, pd.DataFrame(), settings.hard_filters)
        assert _reasons(result.rejected)["VOID"] == "insufficient_financial_history"

    def test_persistent_negative_fcf(self, settings: Settings) -> None:
        candidates = pd.DataFrame([{"ticker": "BURN"}])
        history = _history("BURN", 6, ocf=20e6, capex=80e6)  # FCF < 0 every year
        result = run_financial_hard_filters(candidates, history, settings.hard_filters)
        assert _reasons(result.rejected)["BURN"] == "persistent_negative_fcf"

    def test_healthy_company_passes(self, settings: Settings) -> None:
        candidates = pd.DataFrame([{"ticker": "FINE"}])
        result = run_financial_hard_filters(
            candidates, _history("FINE", 8), settings.hard_filters
        )
        assert result.rejected.empty
