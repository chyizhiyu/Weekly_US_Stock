"""Deterministically (re)generate the offline sample dataset.

Run from the repo root:  python scripts/generate_sample_data.py

The dataset is hand-designed so that every pipeline path is exercised at a
known ticker, including look-ahead traps (rows dated after the canonical test
as_of of 2026-01-09 that the providers must hide):

Ranked (general model):
  STBL stable high-ROIC compounder         -> top of Robust ranking
  LOTO high-upside, high-variance lottery  -> top of Upside, penalized in Robust
  CYCP cyclical at peak margins            -> normalized earnings << reported
  DILU heavy SBC + 6%/yr dilution          -> per-share value penalized
  BYBK same economics, net buybacks        -> ranks above DILU
  GROW 25% growth, incremental ROIC < WACC -> low rank despite growth
  VALU moderate-everything value stock
  MEGA stable mega-cap, low growth
  ADRX quality ADR (enters only when universe.include_adrs=true)

Hard-filter rejects:
  SPCX spac | ETFX etf | WRNT warrant | PREF preferred | OTCP otc exchange
  NEWIPO listed <3y | TINY market cap | ILLQ liquidity | LOSS consecutive losses
  DEBT interest coverage | MISS 2y of financials (fail closed)
  SDIL 15%/yr dilution | ACCT OCF/NI accounting mismatch
  NEGM negative normalized margin -> no_normalized_earnings

Watchlist (unsupported industry models):
  BNKA bank | INSU insurer | RLTY REIT | BIOX pre-profit biotech
"""

from __future__ import annotations

import csv
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parents[1] / "data" / "samples"
AS_OF = date(2026, 1, 9)  # canonical Friday used across the test-suite
M = 1_000_000  # company params below are in millions; CSVs carry absolute USD/shares
FETCHED_AT = "2026-01-09T13:00:00+00:00"
SOURCE = "sample"
PRICE_START = date(2025, 9, 15)
PRICE_END = date(2026, 1, 16)  # extends PAST as_of on purpose (leak trap)


@dataclass(slots=True)
class Company:
    ticker: str
    name: str
    exchange: str
    security_type: str
    listing_date: str
    sector: str
    industry: str
    price: float
    dollar_volume: float
    beta: float | None = 1.0
    country: str = "US"
    is_adr: bool = False
    # Fundamentals (omitted -> no statement rows are generated)
    first_fiscal_year: int | None = None
    revenue0: float | None = None
    revenue_growth: float | list[float] | None = None
    revenue_path: list[float] | None = None
    operating_margin: float | list[float] | None = None
    gross_margin: float = 0.40
    sbc_pct: float = 0.01
    capex_pct: float = 0.04
    dep_pct: float = 0.04
    shares0: float | None = None
    share_growth: float = 0.0
    debt_start: float = 0.0
    debt_end: float | None = None
    cash: float = 0.0
    interest_rate: float = 0.045
    equity_start: float = 1000.0
    equity_end: float | None = None
    payout: float = 0.0
    buybacks: float = 0.0
    one_offs: dict[int, float] = field(default_factory=dict)
    ocf_to_ni_override: float | None = None  # forces OCF = ratio * NI
    net_income_margin_override: float | None = None  # for loss-makers
    # Estimates
    estimate_growth: float | None = None
    estimate_dispersion: float = 0.08
    num_analysts: int = 12
    # TTM window growth override (None -> half of the latest annual growth)
    ttm_growth: float | None = None

    @property
    def shares_latest(self) -> float:
        if self.shares0 is None:
            return 0.0
        years = len(self._revenues()) - 2  # growth applied through FY2024
        return self.shares0 * (1.0 + self.share_growth) ** max(years, 0)

    def _revenues(self) -> list[float]:
        if self.revenue_path is not None:
            return list(self.revenue_path)
        if self.revenue0 is None:
            return []
        if isinstance(self.revenue_growth, list):
            values = [self.revenue0]
            for growth in self.revenue_growth:
                values.append(values[-1] * (1.0 + growth))
            return values
        growth = self.revenue_growth or 0.0
        # FY2017..FY2025 when first_fiscal_year=2017 (last row stays unfiled)
        count = 2025 - (self.first_fiscal_year or 2017) + 1
        return [self.revenue0 * (1.0 + growth) ** t for t in range(count)]


COMPANIES: list[Company] = [
    Company(
        ticker="STBL", name="Steadfast Compounders Inc", exchange="NYSE",
        security_type="common_stock", listing_date="1998-05-12",
        sector="Consumer Defensive", industry="Household Products",
        price=52.0, dollar_volume=80e6, beta=0.9,
        first_fiscal_year=2017, revenue0=5000, revenue_growth=0.08,
        operating_margin=0.28, gross_margin=0.60, sbc_pct=0.01,
        capex_pct=0.04, dep_pct=0.04, shares0=520, share_growth=-0.02,
        debt_start=2000, cash=1500, interest_rate=0.04,
        equity_start=8000, equity_end=12500, payout=0.30, buybacks=700,
        estimate_growth=0.07,
    ),
    Company(
        ticker="LOTO", name="Moonshot Dynamics", exchange="NASDAQ",
        security_type="common_stock", listing_date="2015-09-30",
        sector="Technology", industry="Software - Application",
        price=10.0, dollar_volume=60e6, beta=1.8,
        first_fiscal_year=2017, revenue0=300,
        revenue_growth=[0.55, 0.30, 0.65, 0.20, 0.50, 0.28, 0.45, 0.30],
        operating_margin=[-0.02, 0.04, 0.01, 0.10, 0.14, 0.08, 0.16, 0.18, 0.18],
        gross_margin=0.70, sbc_pct=0.06, capex_pct=0.03, dep_pct=0.02,
        shares0=200, share_growth=0.03, debt_start=0, cash=500,
        interest_rate=0.04, equity_start=600, equity_end=1800,
        estimate_growth=0.35, estimate_dispersion=0.50, num_analysts=6,
        ttm_growth=0.02,  # growth stalled in the trailing window: lottery profile

    ),
    Company(
        ticker="CYCP", name="PeakCycle Materials", exchange="NYSE",
        security_type="common_stock", listing_date="2001-03-15",
        sector="Basic Materials", industry="Steel",
        price=16.5, dollar_volume=40e6, beta=1.4,
        first_fiscal_year=2017,
        revenue_path=[3800, 4200, 3600, 3900, 4400, 3700, 4600, 5000, 5100],
        operating_margin=[0.08, 0.06, 0.04, 0.07, 0.09, 0.05, 0.14, 0.16, 0.15],
        gross_margin=0.30, sbc_pct=0.005, capex_pct=0.06, dep_pct=0.06,
        shares0=300, share_growth=0.0, debt_start=1500, cash=500,
        interest_rate=0.05, equity_start=3500, equity_end=5200, payout=0.25,
        one_offs={2024: 120},
        estimate_growth=0.02, estimate_dispersion=0.30,
    ),
    Company(
        ticker="DILU", name="StockComp Software", exchange="NASDAQ",
        security_type="common_stock", listing_date="2014-04-10",
        sector="Technology", industry="Software - Infrastructure",
        price=26.5, dollar_volume=70e6, beta=1.2,
        first_fiscal_year=2017, revenue0=2000, revenue_growth=0.12,
        operating_margin=0.25, gross_margin=0.75, sbc_pct=0.08,
        capex_pct=0.03, dep_pct=0.03, shares0=400, share_growth=0.06,
        debt_start=1000, cash=800, interest_rate=0.05,
        equity_start=3000, equity_end=5500,
        estimate_growth=0.11,
    ),
    Company(
        ticker="BYBK", name="BuybackCo Industrial", exchange="NYSE",
        security_type="common_stock", listing_date="2009-08-20",
        sector="Industrials", industry="Specialty Industrial Machinery",
        price=49.4, dollar_volume=70e6, beta=1.0,
        first_fiscal_year=2017, revenue0=2000, revenue_growth=0.12,
        operating_margin=0.25, gross_margin=0.75, sbc_pct=0.005,
        capex_pct=0.03, dep_pct=0.03, shares0=400, share_growth=-0.03,
        debt_start=1000, cash=800, interest_rate=0.05,
        equity_start=3000, equity_end=5500, payout=0.10, buybacks=600,
        estimate_growth=0.11,
    ),
    Company(
        ticker="GROW", name="EmpireBuilder Logistics", exchange="NYSE",
        security_type="common_stock", listing_date="2012-11-05",
        sector="Industrials", industry="Integrated Freight & Logistics",
        price=28.0, dollar_volume=60e6, beta=1.3,
        first_fiscal_year=2017, revenue0=1000, revenue_growth=0.25,
        operating_margin=0.10, gross_margin=0.35, sbc_pct=0.01,
        capex_pct=0.085, dep_pct=0.06, shares0=250, share_growth=0.0,
        debt_start=1500, debt_end=3500, cash=300, interest_rate=0.045,
        equity_start=2000, equity_end=6000,
        estimate_growth=0.20, estimate_dispersion=0.25,
    ),
    Company(
        ticker="VALU", name="FairValue Brands", exchange="NYSE",
        security_type="common_stock", listing_date="2005-06-22",
        sector="Consumer Cyclical", industry="Apparel Manufacturing",
        price=20.0, dollar_volume=50e6, beta=0.95,
        first_fiscal_year=2017, revenue0=3000, revenue_growth=0.05,
        operating_margin=0.18, gross_margin=0.45, sbc_pct=0.01,
        capex_pct=0.04, dep_pct=0.04, shares0=360, share_growth=-0.01,
        debt_start=1200, cash=600, interest_rate=0.05,
        equity_start=4000, equity_end=5200, payout=0.35, buybacks=150,
        one_offs={2023: 150},
        estimate_growth=0.04,
    ),
    Company(
        ticker="MEGA", name="MegaCap Staples", exchange="NYSE",
        security_type="common_stock", listing_date="1985-01-02",
        sector="Consumer Defensive", industry="Beverages - Non-Alcoholic",
        price=92.0, dollar_volume=300e6, beta=0.7,
        first_fiscal_year=2017, revenue0=45000, revenue_growth=0.03,
        operating_margin=0.20, gross_margin=0.50, sbc_pct=0.005,
        capex_pct=0.035, dep_pct=0.035, shares0=1800, share_growth=-0.015,
        debt_start=20000, cash=8000, interest_rate=0.04,
        equity_start=28000, equity_end=32000, payout=0.55, buybacks=3000,
        estimate_growth=0.03,
    ),
    Company(
        ticker="ADRX", name="Global Semi ADR", exchange="NYSE",
        security_type="common_stock", listing_date="2010-10-10",
        sector="Technology", industry="Semiconductors",
        price=38.0, dollar_volume=90e6, beta=1.1, country="TW", is_adr=True,
        first_fiscal_year=2017, revenue0=8000, revenue_growth=0.07,
        operating_margin=0.22, gross_margin=0.40, sbc_pct=0.015,
        capex_pct=0.05, dep_pct=0.05, shares0=500, share_growth=0.0,
        debt_start=2000, cash=2500, interest_rate=0.04,
        equity_start=9000, equity_end=14000, payout=0.30,
        estimate_growth=0.06,
    ),
    # --- hard-filter rejects ------------------------------------------------
    Company(
        ticker="SPCX", name="Horizon Acquisition Corp", exchange="NASDAQ",
        security_type="spac", listing_date="2024-03-01",
        sector="Financial Services", industry="Shell Companies",
        price=10.0, dollar_volume=8e6,
    ),
    Company(
        ticker="ETFX", name="Total Market ETF", exchange="NYSE",
        security_type="etf", listing_date="2010-01-15",
        sector="", industry="Exchange Traded Fund",
        price=50.0, dollar_volume=500e6,
    ),
    Company(
        ticker="WRNT", name="Moonshot Dynamics Warrant", exchange="NASDAQ",
        security_type="warrant", listing_date="2024-03-01",
        sector="Technology", industry="Software - Application",
        price=1.5, dollar_volume=2e6,
    ),
    Company(
        ticker="PREF", name="Utility Preferred Series A", exchange="NYSE",
        security_type="preferred", listing_date="2018-05-05",
        sector="Utilities", industry="Utilities - Regulated Electric",
        price=25.0, dollar_volume=3e6,
    ),
    Company(
        ticker="OTCP", name="PinkSheet Holdings", exchange="OTC",
        security_type="common_stock", listing_date="2008-01-01",
        sector="Industrials", industry="Conglomerates",
        price=12.0, dollar_volume=6e6,
    ),
    Company(
        ticker="NEWIPO", name="Fresh Float Tech", exchange="NASDAQ",
        security_type="common_stock", listing_date="2024-06-15",
        sector="Technology", industry="Software - Application",
        price=45.0, dollar_volume=100e6,
    ),
    Company(
        ticker="TINY", name="MicroCap Gadgets", exchange="NASDAQ",
        security_type="common_stock", listing_date="2015-02-02",
        sector="Technology", industry="Consumer Electronics",
        price=5.0, dollar_volume=10e6,
        first_fiscal_year=2019, revenue0=120, revenue_growth=0.03,
        operating_margin=0.08, shares0=40, equity_start=80, equity_end=120,
        interest_rate=0.05,
    ),
    Company(
        ticker="ILLQ", name="Illiquid Industries", exchange="NYSE",
        security_type="common_stock", listing_date="2010-09-09",
        sector="Industrials", industry="Metal Fabrication",
        price=10.0, dollar_volume=1e6,
        first_fiscal_year=2019, revenue0=600, revenue_growth=0.02,
        operating_margin=0.12, shares0=80, equity_start=500, equity_end=700,
        interest_rate=0.05,
    ),
    Company(
        ticker="LOSS", name="Perma Loss Retail", exchange="NYSE",
        security_type="common_stock", listing_date="2014-07-07",
        sector="Consumer Cyclical", industry="Department Stores",
        price=8.0, dollar_volume=20e6,
        first_fiscal_year=2019, revenue0=900, revenue_growth=0.0,
        operating_margin=-0.10, shares0=90, equity_start=900, equity_end=400,
        cash=100, interest_rate=0.05,
    ),
    Company(
        ticker="DEBT", name="Leverage Tower Media", exchange="NASDAQ",
        security_type="common_stock", listing_date="2013-03-03",
        sector="Communication Services", industry="Broadcasting",
        price=12.0, dollar_volume=25e6,
        first_fiscal_year=2019, revenue0=1200, revenue_growth=0.0,
        operating_margin=0.20, shares0=70, debt_start=4000, cash=200,
        interest_rate=0.05, equity_start=800, equity_end=900,
        capex_pct=0.05, dep_pct=0.05,
    ),
    Company(
        ticker="MISS", name="Opaque Industrials", exchange="NYSE",
        security_type="common_stock", listing_date="2000-01-01",
        sector="Industrials", industry="Specialty Business Services",
        price=30.0, dollar_volume=40e6,
        first_fiscal_year=2023, revenue0=2200, revenue_growth=0.04,
        operating_margin=0.15, shares0=50, equity_start=2000, equity_end=2200,
        interest_rate=0.05,
    ),
    Company(
        ticker="SDIL", name="Serial Diluter Mining", exchange="AMEX",
        security_type="common_stock", listing_date="2011-04-04",
        sector="Basic Materials", industry="Gold",
        price=15.0, dollar_volume=30e6,
        first_fiscal_year=2019, revenue0=2000, revenue_growth=0.04,
        operating_margin=0.15, shares0=60, share_growth=0.15,
        debt_start=300, cash=400, interest_rate=0.05,
        equity_start=2500, equity_end=4000, capex_pct=0.03, dep_pct=0.03,
    ),
    Company(
        ticker="ACCT", name="Accrual Gymnastics Corp", exchange="NASDAQ",
        security_type="common_stock", listing_date="2009-12-12",
        sector="Industrials", industry="Staffing & Employment Services",
        price=20.0, dollar_volume=35e6,
        first_fiscal_year=2019, revenue0=1500, revenue_growth=0.05,
        operating_margin=0.18, shares0=100, debt_start=400, cash=300,
        interest_rate=0.05, equity_start=1800, equity_end=2400,
        capex_pct=0.01, dep_pct=0.02, ocf_to_ni_override=0.45,
    ),
    Company(
        ticker="NEGM", name="Forever Promotions", exchange="NYSE",
        security_type="common_stock", listing_date="2012-02-02",
        sector="Communication Services", industry="Advertising Agencies",
        price=7.0, dollar_volume=15e6,
        first_fiscal_year=2019, revenue0=800, revenue_growth=0.0,
        operating_margin=[-0.04, 0.03, -0.05, 0.02, -0.03, -0.02, -0.01],
        shares0=100, cash=300, interest_rate=0.05,
        equity_start=700, equity_end=500, capex_pct=0.02, dep_pct=0.02,
    ),
    # --- watchlist routing ----------------------------------------------------
    Company(
        ticker="BNKA", name="First Continental Bank", exchange="NYSE",
        security_type="common_stock", listing_date="1995-05-05",
        sector="Financial Services", industry="Banks - Regional",
        price=40.0, dollar_volume=45e6,
    ),
    Company(
        ticker="INSU", name="Granite Mutual Insurance", exchange="NYSE",
        security_type="common_stock", listing_date="1990-10-10",
        sector="Financial Services", industry="Insurance - Property & Casualty",
        price=55.0, dollar_volume=50e6,
    ),
    Company(
        ticker="RLTY", name="Cornerstone Realty Trust", exchange="NYSE",
        security_type="common_stock", listing_date="2003-03-03",
        sector="Real Estate", industry="REIT - Diversified",
        price=60.0, dollar_volume=40e6,
    ),
    Company(
        ticker="BIOX", name="Helix Therapeutics", exchange="NASDAQ",
        security_type="common_stock", listing_date="2019-06-01",
        sector="Healthcare", industry="Biotechnology",
        price=25.0, dollar_volume=30e6,
        first_fiscal_year=2019, revenue0=30, revenue_growth=0.40,
        operating_margin=-1.50, shares0=80, cash=900, interest_rate=0.04,
        equity_start=1000, equity_end=600, capex_pct=0.02, dep_pct=0.02,
    ),
]

# Shares used for market cap (universe snapshot). For names without statements
# we still need a share count consistent with the intended market cap.
_SNAPSHOT_SHARES: dict[str, float] = {
    "SPCX": 50, "ETFX": 100, "WRNT": 10, "PREF": 20, "OTCP": 60,
    "NEWIPO": 80, "BNKA": 120, "INSU": 150, "RLTY": 100,
}


def _universe_rows() -> list[dict]:
    rows = []
    for company in COMPANIES:
        shares = company.shares_latest or _SNAPSHOT_SHARES.get(company.ticker, 0.0)
        rows.append(
            {
                "ticker": company.ticker,
                "name": company.name,
                "exchange": company.exchange,
                "security_type": company.security_type,
                "is_adr": company.is_adr,
                "listing_date": company.listing_date,
                "sector": company.sector,
                "industry": company.industry,
                "country": company.country,
                "shares_outstanding": round(shares * M, 0),
                "beta": company.beta,
                "as_of": AS_OF.isoformat(),
                "source": SOURCE,
                "fetched_at": FETCHED_AT,
            }
        )
    return rows


def _price_rows() -> list[dict]:
    rows = []
    day = PRICE_START
    days: list[date] = []
    while day <= PRICE_END:
        if day.weekday() < 5:
            days.append(day)
        day += timedelta(days=1)
    for company in COMPANIES:
        volume = company.dollar_volume / company.price
        for index, trade_date in enumerate(days):
            wiggle = 1.0 + 0.003 * ((index % 7) - 3)
            close = round(company.price * wiggle, 4)
            rows.append(
                {
                    "ticker": company.ticker,
                    "trade_date": trade_date.isoformat(),
                    "close": close,
                    "volume": round(volume, 2),
                    "dollar_volume": round(close * volume, 2),
                    "as_of": AS_OF.isoformat(),
                    "source": SOURCE,
                    "fetched_at": FETCHED_AT,
                }
            )
    return rows


def _margin_for(company: Company, index: int) -> float:
    if isinstance(company.operating_margin, list):
        return company.operating_margin[index]
    return float(company.operating_margin or 0.0)


def _interp(start: float, end: float | None, index: int, count: int) -> float:
    target = start if end is None else end
    if count <= 1:
        return target
    return start + (target - start) * index / (count - 1)


def _fundamental_rows() -> list[dict]:
    rows = []
    tax = 0.21
    for company in COMPANIES:
        revenues = company._revenues()
        if not revenues or company.first_fiscal_year is None or company.shares0 is None:
            continue
        count = len(revenues)
        for index, revenue in enumerate(revenues):
            year = company.first_fiscal_year + index
            if year > 2025:
                break
            margin = _margin_for(company, index)
            one_off = company.one_offs.get(year, 0.0)
            operating_income = revenue * margin + one_off
            debt = _interp(company.debt_start, company.debt_end, index, count)
            interest = debt * company.interest_rate
            pretax = operating_income - interest
            if company.net_income_margin_override is not None:
                net_income = revenue * company.net_income_margin_override
            else:
                net_income = pretax * (1 - tax) if pretax > 0 else pretax
            depreciation = revenue * company.dep_pct
            sbc = revenue * company.sbc_pct
            if company.ocf_to_ni_override is not None and net_income > 0:
                ocf = net_income * company.ocf_to_ni_override
            else:
                ocf = net_income + depreciation + sbc
            shares = company.shares0 * (1.0 + company.share_growth) ** index
            equity = _interp(company.equity_start, company.equity_end, index, count)
            filing = date(year + 1, 2, 20)
            rows.append(
                {
                    "ticker": company.ticker,
                    "fiscal_year": year,
                    "fiscal_end": date(year, 12, 31).isoformat(),
                    "filing_date": filing.isoformat(),
                    "revenue": round(revenue * M, 2),
                    "gross_profit": round(revenue * company.gross_margin * M, 2),
                    "operating_income": round(operating_income * M, 2),
                    "one_off_items": round(one_off * M, 2),
                    "net_income": round(net_income * M, 2),
                    "ocf": round(ocf * M, 2),
                    "capex": round(revenue * company.capex_pct * M, 2),
                    "depreciation": round(depreciation * M, 2),
                    "sbc": round(sbc * M, 2),
                    "dividends_paid": round(max(net_income, 0.0) * company.payout * M, 2),
                    "buybacks": round(company.buybacks * M, 2),
                    "share_issuance": round(sbc * M, 2),
                    "shares_diluted": round(shares * M, 0),
                    "total_debt": round(debt * M, 2),
                    "cash": round(company.cash * M, 2),
                    "interest_expense": round(interest * M, 2),
                    "total_equity": round(equity * M, 2),
                    "effective_tax_rate": tax,
                    "is_estimate": False,
                    "as_of": AS_OF.isoformat(),
                    "source": SOURCE,
                    "fetched_at": FETCHED_AT,
                }
            )
    return rows


def _ttm_rows() -> list[dict]:
    """Trailing-twelve-month anchors as of Q3 FY2025 (filed 2025-11-14).

    Flows scale from FY2024 by half of the latest annual growth so the TTM
    anchor sits realistically between FY2024 and FY2025. The peak-margin
    cyclical keeps its FY2024 margin so the normalization tests stay valid.
    A second window filed 2026-02-10 is a look-ahead trap: it must stay
    invisible at the canonical as_of of 2026-01-09.
    """

    rows = []
    tax = 0.21
    for company in COMPANIES:
        revenues = company._revenues()
        if not revenues or company.first_fiscal_year is None or company.shares0 is None:
            continue
        idx = 2024 - company.first_fiscal_year
        if idx < 1 or idx >= len(revenues):
            continue
        if company.ticker in {"TINY", "ILLQ", "LOSS", "DEBT", "MISS", "SDIL", "ACCT", "NEGM",
                              "BIOX"}:
            continue  # rejected/watchlisted upstream; annual fallback suffices
        growth_latest = revenues[idx] / revenues[idx - 1] - 1.0
        if company.ttm_growth is not None:
            growth_latest = company.ttm_growth
        margin = _margin_for(company, idx)
        debt = _interp(company.debt_start, company.debt_end, idx, len(revenues))
        equity = _interp(company.equity_start, company.equity_end, idx, len(revenues))
        for filing, fiscal_end, factor in [
            ("2025-11-14", "2025-09-30", 1.0 + 0.5 * growth_latest),
            ("2026-02-10", "2025-12-31", 9.9),  # absurd future window: must be hidden
        ]:
            revenue = revenues[idx] * factor
            operating_income = revenue * margin
            interest = debt * company.interest_rate
            pretax = operating_income - interest
            net_income = pretax * (1 - tax) if pretax > 0 else pretax
            depreciation = revenue * company.dep_pct
            sbc = revenue * company.sbc_pct
            if company.ocf_to_ni_override is not None and net_income > 0:
                ocf = net_income * company.ocf_to_ni_override
            else:
                ocf = net_income + depreciation + sbc
            shares = company.shares0 * (1.0 + company.share_growth) ** (idx + 0.75)
            rows.append(
                {
                    "ticker": company.ticker,
                    "fiscal_year": "",
                    "fiscal_end": fiscal_end,
                    "filing_date": filing,
                    "revenue": round(revenue * M, 2),
                    "gross_profit": round(revenue * company.gross_margin * M, 2),
                    "operating_income": round(operating_income * M, 2),
                    "one_off_items": 0.0,
                    "net_income": round(net_income * M, 2),
                    "ocf": round(ocf * M, 2),
                    "capex": round(revenue * company.capex_pct * M, 2),
                    "depreciation": round(depreciation * M, 2),
                    "sbc": round(sbc * M, 2),
                    "dividends_paid": round(max(net_income, 0.0) * company.payout * M, 2),
                    "buybacks": round(company.buybacks * M, 2),
                    "share_issuance": round(sbc * M, 2),
                    "shares_diluted": round(shares * M, 0),
                    "total_debt": round(debt * M, 2),
                    "cash": round(company.cash * M, 2),
                    "interest_expense": round(interest * M, 2),
                    "total_equity": round(equity * M, 2),
                    "effective_tax_rate": tax,
                    "is_estimate": False,
                    "is_ttm": True,
                    "as_of": AS_OF.isoformat(),
                    "source": SOURCE,
                    "fetched_at": FETCHED_AT,
                }
            )
    return rows


def _estimate_rows() -> list[dict]:
    rows = []
    for company in COMPANIES:
        if company.estimate_growth is None:
            continue
        revenues = company._revenues()
        latest_revenue = revenues[2024 - (company.first_fiscal_year or 2017)]
        shares = company.shares_latest
        snapshots = [("2026-01-05", 1.0)]
        if company.ticker == "STBL":
            # Future snapshot (after the canonical as_of): providers must hide it.
            snapshots.append(("2026-01-14", 5.0))
        for snapshot_date, scale in snapshots:
            for offset in (1, 2):
                fiscal_year = 2024 + offset
                mean = latest_revenue * M * (1 + company.estimate_growth) ** offset * scale
                spread = mean * company.estimate_dispersion / 2
                eps = mean * 0.12 / (shares * M) if shares else None
                rows.append(
                    {
                        "ticker": company.ticker,
                        "fiscal_year": fiscal_year,
                        "revenue_mean": round(mean, 2),
                        "revenue_low": round(mean - spread, 2),
                        "revenue_high": round(mean + spread, 2),
                        "eps_mean": round(eps, 4) if eps else "",
                        "eps_low": round(eps * 0.9, 4) if eps else "",
                        "eps_high": round(eps * 1.1, 4) if eps else "",
                        "num_analysts": company.num_analysts,
                        "is_estimate": True,
                        "as_of": snapshot_date,
                        "source": SOURCE,
                        "fetched_at": FETCHED_AT,
                    }
                )
    return rows


def _macro_rows() -> list[dict]:
    return [
        {
            "series": "risk_free_10y",
            "value": 0.042,
            "as_of": "2025-12-31",
            "source": SOURCE,
            "fetched_at": FETCHED_AT,
        },
        {
            "series": "risk_free_10y",
            "value": 0.043,
            "as_of": "2026-01-08",
            "source": SOURCE,
            "fetched_at": FETCHED_AT,
        },
        {  # future observation: must be ignored at as_of 2026-01-09... 01-12 > as_of
            "series": "risk_free_10y",
            "value": 0.099,
            "as_of": "2026-01-12",
            "source": SOURCE,
            "fetched_at": FETCHED_AT,
        },
    ]


def _write_csv(filename: str, rows: list[dict]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / filename
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {path} ({len(rows)} rows)")


def main() -> None:
    _write_csv("universe.csv", _universe_rows())
    _write_csv("prices.csv", _price_rows())
    _write_csv("fundamentals.csv", _fundamental_rows())
    _write_csv("ttm.csv", _ttm_rows())
    _write_csv("estimates.csv", _estimate_rows())
    _write_csv("macro.csv", _macro_rows())


if __name__ == "__main__":
    main()
