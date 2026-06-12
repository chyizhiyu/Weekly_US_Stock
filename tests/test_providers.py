"""Provider contracts: point-in-time discipline and pure payload transforms."""

from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from tests.conftest import AS_OF
from weekly_us_stock.providers.base import PointInTimeUnavailable
from weekly_us_stock.providers.fmp import (
    FMPProvider,
    build_ttm_row,
    classify_security,
    normalize_exchange,
    transform_batch_eod,
    transform_profile_bulk,
    transform_screener,
    transform_statements,
    transform_treasury,
)
from weekly_us_stock.providers.fred import transform_observations
from weekly_us_stock.providers.polygon import transform_grouped
from weekly_us_stock.providers.sample import SampleDataProvider
from weekly_us_stock.steps.step3_standardize import standardize_fundamentals


class TestNoLookAheadBias:
    """The sample CSVs deliberately contain future-dated rows; every loader
    must hide them at the requested as_of."""

    def test_prices_never_leak_past_as_of(self, sample_provider: SampleDataProvider) -> None:
        prices = sample_provider.load_prices(None, AS_OF, lookback_days=60)
        assert not prices.empty
        assert prices["trade_date"].max() <= pd.Timestamp(AS_OF)
        # The same CSV does contain later sessions, visible at a later as_of.
        later = sample_provider.load_prices(None, date(2026, 1, 16), lookback_days=60)
        assert later["trade_date"].max() > pd.Timestamp(AS_OF)

    def test_unfiled_fiscal_year_is_invisible(
        self, sample_provider: SampleDataProvider
    ) -> None:
        # FY2025 was filed 2026-02-20: invisible on 2026-01-09, visible later.
        before = sample_provider.load_fundamentals(["STBL"], AS_OF)
        assert before["fiscal_year"].max() == 2024
        after = sample_provider.load_fundamentals(["STBL"], date(2026, 3, 1))
        assert after["fiscal_year"].max() == 2025

    def test_future_estimate_snapshot_is_invisible(
        self, sample_provider: SampleDataProvider
    ) -> None:
        # STBL has a second estimate snapshot dated 2026-01-14 with 5x revenue.
        estimates = sample_provider.load_estimates(["STBL"], AS_OF)
        assert (estimates["as_of"] <= pd.Timestamp(AS_OF)).all()
        fy2025 = estimates.loc[estimates["fiscal_year"] == 2025, "revenue_mean"].iloc[0]
        assert fy2025 < 50e9  # the 5x-scaled future snapshot would be ~46e9 * 5

    def test_future_macro_observation_is_invisible(
        self, sample_provider: SampleDataProvider
    ) -> None:
        macro = sample_provider.load_macro(AS_OF)
        value = macro.loc[macro["series"] == "risk_free_10y", "value"].iloc[0]
        assert value == 0.043  # not the 0.099 row dated 2026-01-12

    def test_standardize_re_enforces_filing_dates(
        self, sample_provider: SampleDataProvider
    ) -> None:
        # Even if a provider misbehaved, step 3 re-applies the filing gate.
        leaked = sample_provider.load_fundamentals(["STBL"], date(2026, 3, 1))
        cleaned = standardize_fundamentals(leaked, AS_OF)
        assert cleaned["fiscal_year"].max() == 2024

    def test_provenance_columns_present(self, sample_provider: SampleDataProvider) -> None:
        for frame in [
            sample_provider.fetch_universe(AS_OF),
            sample_provider.load_prices(["STBL"], AS_OF, 10),
            sample_provider.load_fundamentals(["STBL"], AS_OF),
        ]:
            for column in ["as_of", "source", "fetched_at"]:
                assert column in frame.columns


class TestFMPTransforms:
    def test_classify_security(self) -> None:
        assert classify_security("AAPL", "Apple Inc.", is_etf=False, is_fund=False) == (
            "common_stock"
        )
        assert classify_security("SPY", "SPDR S&P 500", is_etf=True, is_fund=False) == "etf"
        assert (
            classify_security("ACQ", "Horizon Acquisition Corp", is_etf=False, is_fund=False)
            == "spac"
        )
        assert classify_security("ABC-WT", "ABC Warrant", is_etf=False, is_fund=False) == (
            "warrant"
        )
        assert (
            classify_security("XYZ-PA", "XYZ Preferred Series A", is_etf=False, is_fund=False)
            == "preferred"
        )

    def test_normalize_exchange(self) -> None:
        assert normalize_exchange("NYSE American") == "AMEX"
        assert normalize_exchange("PNK") == "OTC"
        assert normalize_exchange("NASDAQ Global Select") == "NASDAQ"

    def test_transform_screener_and_statements(self) -> None:
        screener = transform_screener(
            [
                {
                    "symbol": "AAPL",
                    "companyName": "Apple Inc.",
                    "exchangeShortName": "NASDAQ",
                    "sector": "Technology",
                    "industry": "Consumer Electronics",
                    "country": "US",
                    "marketCap": 3e12,
                    "beta": 1.2,
                    "isEtf": False,
                    "isFund": False,
                }
            ],
            "2026-01-09T00:00:00+00:00",
            AS_OF,
        )
        assert screener.iloc[0]["security_type"] == "common_stock"
        assert not screener.iloc[0]["is_adr"]

        statements = transform_statements(
            income=[
                {
                    "symbol": "AAPL",
                    "fiscalYear": "2024",
                    "date": "2024-09-28",
                    "filingDate": "2024-11-01",
                    "revenue": 391e9,
                    "grossProfit": 180e9,
                    "operatingIncome": 123e9,
                    "netIncome": 93e9,
                    "incomeBeforeTax": 110e9,
                    "incomeTaxExpense": 17e9,
                    "interestExpense": 0,
                    "weightedAverageShsOutDil": 15.4e9,
                }
            ],
            balance=[
                {
                    "fiscalYear": "2024",
                    "totalDebt": 106e9,
                    "cashAndShortTermInvestments": 65e9,
                    "totalStockholdersEquity": 57e9,
                }
            ],
            cashflow=[
                {
                    "fiscalYear": "2024",
                    "operatingCashFlow": 118e9,
                    "capitalExpenditure": -9.4e9,
                    "depreciationAndAmortization": 11.4e9,
                    "stockBasedCompensation": 11.7e9,
                    "commonDividendsPaid": -15.2e9,
                    "commonStockRepurchased": -94.9e9,
                }
            ],
            fetched_at="2026-01-09T00:00:00+00:00",
            as_of=AS_OF,
        )
        row = statements.iloc[0]
        assert row["filing_date"] == "2024-11-01"
        assert row["fiscal_year"] == 2024
        assert row["capex"] == 9.4e9  # absolute value
        assert row["buybacks"] == 94.9e9  # sign flipped to positive spend
        assert row["dividends_paid"] == 15.2e9
        assert row["effective_tax_rate"] == 17e9 / 110e9


def test_fmp_refuses_historical_snapshot_requests() -> None:
    # Estimates and the active-listings universe are CURRENT snapshots: a
    # historical as_of through them would be silent look-ahead/survivorship
    # bias. The provider must refuse before any HTTP happens.
    provider = FMPProvider("test-key", min_request_interval=0.0)
    with pytest.raises(PointInTimeUnavailable):
        provider.load_estimates(["AAPL"], date(2020, 1, 3))
    with pytest.raises(PointInTimeUnavailable):
        provider.fetch_universe(date(2020, 1, 3))


def _quarter(symbol: str, q_date: str, filing: str, revenue: float) -> dict:
    return {
        "symbol": symbol,
        "date": q_date,
        "filingDate": filing,
        "fiscalYear": q_date[:4],
        "revenue": revenue,
        "grossProfit": revenue * 0.4,
        "operatingIncome": revenue * 0.2,
        "netIncome": revenue * 0.15,
        "incomeBeforeTax": revenue * 0.19,
        "incomeTaxExpense": revenue * 0.04,
        "interestExpense": revenue * 0.005,
        "weightedAverageShsOutDil": 100e6 - 1e6 * int(q_date[5:7]),
    }


def test_fmp_build_ttm_row() -> None:
    quarters = [
        ("2025-12-31", "2026-01-05", 110e9),  # filed before as_of? no - see below
        ("2025-09-30", "2025-11-01", 105e9),
        ("2025-06-30", "2025-08-01", 100e9),
        ("2025-03-31", "2025-05-01", 95e9),
        ("2024-12-31", "2025-02-01", 90e9),
    ]
    income = [_quarter("AAPL", d, f, r) for d, f, r in quarters]
    cashflow = [
        {
            "date": d,
            "filingDate": f,
            "operatingCashFlow": r * 0.2,
            "capitalExpenditure": -r * 0.05,
            "depreciationAndAmortization": r * 0.04,
            "stockBasedCompensation": r * 0.02,
            "commonDividendsPaid": -r * 0.01,
            "commonStockRepurchased": -r * 0.03,
            "commonStockIssuance": 0.0,
        }
        for d, f, r in quarters
    ]
    balance = [
        {"date": d, "filingDate": f, "totalDebt": 100e9, "cashAndShortTermInvestments": 60e9,
         "totalStockholdersEquity": 70e9}
        for d, f, _ in quarters
    ]
    frame = build_ttm_row(income, balance, cashflow, "now", as_of=date(2026, 1, 9))
    row = frame.iloc[0]
    # Four most recent FILED quarters: Q4'25 (filed 01-05) .. Q1'25.
    assert row["revenue"] == pytest.approx((110 + 105 + 100 + 95) * 1e9)
    assert row["is_ttm"]
    assert row["filing_date"] == "2026-01-05"
    assert row["shares_diluted"] == pytest.approx(100e6 - 12e6)  # latest quarter
    assert row["capex"] == pytest.approx((110 + 105 + 100 + 95) * 1e9 * 0.05)
    # Fewer than four filed quarters -> empty (caller anchors on annuals).
    short = build_ttm_row(income[:3], balance[:3], cashflow[:3], "now", date(2026, 1, 9))
    assert short.empty


def test_sample_ttm_hides_future_filing(sample_provider) -> None:
    ttm = sample_provider.load_ttm(["STBL"], AS_OF)
    assert len(ttm) == 1
    # The absurd 9.9x window filed 2026-02-10 must be invisible on 2026-01-09.
    assert ttm.iloc[0]["filing_date"] == pd.Timestamp("2025-11-14")
    later = sample_provider.load_ttm(["STBL"], date(2026, 3, 1))
    assert later.iloc[0]["filing_date"] == pd.Timestamp("2026-02-10")


def test_fmp_batch_eod_transform() -> None:
    frame = transform_batch_eod(
        [{"symbol": "AAPL", "date": "2026-01-09", "close": 295.0, "volume": 40_000_000}],
        trade_date=date(2026, 1, 9),
        fetched_at="now",
        as_of=AS_OF,
    )
    row = frame.iloc[0]
    assert row["dollar_volume"] == 295.0 * 40_000_000
    assert row["source"] == "fmp:batch-eod"


def test_fmp_profile_bulk_transform() -> None:
    csv_text = (
        "symbol,price,marketCap,beta,averageVolume,ipoDate,isEtf,isActivelyTrading,isAdr,isFund\n"
        'AAPL,295.63,4342023054280,1.086,45584055,1980-12-12,false,true,false,false\n'
        'TSM,200.0,1000000000000,1.2,30000000,1997-10-08,false,true,true,false\n'
    )
    frame = transform_profile_bulk(csv_text).set_index("ticker")
    assert frame.loc["AAPL", "listing_date_profile"] == "1980-12-12"
    assert not frame.loc["AAPL", "is_adr_profile"]
    assert frame.loc["TSM", "is_adr_profile"]
    assert frame.loc["AAPL", "shares_outstanding_profile"] == pytest.approx(
        4342023054280 / 295.63
    )


def test_fmp_treasury_transform() -> None:
    frame = transform_treasury(
        [
            {"date": "2026-01-08", "year10": "4.30", "month1": "5.1"},
            {"date": "2026-01-09", "year10": None},
        ],
        fetched_at="now",
    )
    assert len(frame) == 1  # rows without a 10y value are dropped
    assert frame.iloc[0]["value"] == 0.043
    assert frame.iloc[0]["source"] == "fmp:treasury"


def test_polygon_grouped_transform() -> None:
    frame = transform_grouped(
        {"results": [{"T": "AAPL", "c": 230.0, "v": 50_000_000}]},
        trade_date=date(2026, 1, 9),
        fetched_at="2026-01-09T21:30:00+00:00",
        as_of=AS_OF,
    )
    row = frame.iloc[0]
    assert row["dollar_volume"] == 230.0 * 50_000_000
    assert row["source"] == "polygon:grouped-daily"


def test_fred_observation_transform() -> None:
    observations = [
        {"date": "2026-01-08", "value": "4.30"},
        {"date": "2026-01-09", "value": "."},
    ]
    frame = transform_observations(
        {"observations": observations}, series="risk_free_10y", fetched_at="now"
    )
    assert len(frame) == 1  # the "." placeholder is dropped
    assert frame.iloc[0]["value"] == 0.043
