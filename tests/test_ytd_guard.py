"""Task #3-B: FMP quarterly YTD-cumulative cash-flow guard."""
from __future__ import annotations

from datetime import date

from weekly_us_stock.providers.fmp import build_ttm_row

_AS_OF = date(2026, 3, 1)
_Q = ["2025-03-31", "2025-06-30", "2025-09-30", "2025-12-31"]
_F = ["2025-05-10", "2025-08-10", "2025-11-10", "2026-02-10"]


def _income() -> list[dict]:
    return [
        {
            "symbol": "TST", "date": d, "filingDate": f, "fiscalYear": 2025,
            "netIncome": 25.0, "revenue": 250.0, "operatingIncome": 40.0,
            "incomeBeforeTax": 30.0, "incomeTaxExpense": 5.0,
            "interestExpense": 2.0, "weightedAverageShsOutDil": 1000.0,
        }
        for d, f in zip(_Q, _F, strict=True)
    ]


def _balance() -> list[dict]:
    return [
        {
            "symbol": "TST", "date": d, "filingDate": f, "fiscalYear": 2025,
            "totalDebt": 500.0, "cashAndShortTermInvestments": 200.0,
            "totalStockholdersEquity": 1000.0,
        }
        for d, f in zip(_Q, _F, strict=True)
    ]


def _cf(ni, ocf, capex, sbc) -> list[dict]:
    return [
        {
            "symbol": "TST", "date": _Q[i], "filingDate": _F[i], "fiscalYear": 2025,
            "netIncome": ni[i], "operatingCashFlow": ocf[i],
            "capitalExpenditure": capex[i], "stockBasedCompensation": sbc[i],
            "depreciationAndAmortization": 0.0, "commonStockRepurchased": 0.0,
            "commonStockIssuance": 0.0, "commonDividendsPaid": 0.0, "netDividendsPaid": 0.0,
        }
        for i in range(4)
    ]


def test_discrete_cashflow_sums_directly() -> None:
    cf = _cf([25, 25, 25, 25], [30, 30, 30, 30], [-10, -10, -10, -10], [5, 5, 5, 5])
    row = build_ttm_row(_income(), _balance(), cf, "now", _AS_OF).iloc[0]
    assert row["cashflow_period_semantics"] == "discrete"
    assert row["ttm_cashflow_status"] == "ok"
    assert row["ocf"] == 120.0 and row["capex"] == 40.0 and row["sbc"] == 20.0


def test_ytd_cashflow_is_decumulated_not_summed() -> None:
    cf = _cf([25, 50, 75, 100], [30, 60, 90, 120], [-10, -20, -30, -40], [5, 10, 15, 20])
    row = build_ttm_row(_income(), _balance(), cf, "now", _AS_OF).iloc[0]
    assert row["cashflow_period_semantics"] == "ytd"
    assert row["ttm_cashflow_status"] == "de_cumulated"
    # de-cumulated to 30+30+30+30, NOT the 300 a naive YTD sum would give
    assert row["ocf"] == 120.0 and row["capex"] == 40.0 and row["sbc"] == 20.0


def test_unreliable_ytd_drops_ttm_for_annual_fallback() -> None:
    cf = _cf([25, 50, 75, 100], [30, 60, 90, 120], [-10, -20, -30, -40], [5, 10, 15, 20])
    cf = [r for r in cf if r["date"] != "2025-09-30"]  # missing Q3 -> cannot de-cumulate
    out = build_ttm_row(_income(), _balance(), cf, "now", _AS_OF)
    assert out.empty


def test_incomplete_discrete_cashflow_drops_ttm_for_annual_fallback() -> None:
    cf = _cf([25, 25, 25, 25], [30, 30, 30, 30], [-10, -10, -10, -10], [5, 5, 5, 5])
    cf = [r for r in cf if r["date"] != "2025-09-30"]
    assert build_ttm_row(_income(), _balance(), cf, "now", _AS_OF).empty


def test_non_numeric_core_cashflow_drops_ttm_for_annual_fallback() -> None:
    cf = _cf([25, 25, 25, 25], [30, 30, 30, 30], [-10, -10, -10, -10], [5, 5, 5, 5])
    cf[2]["operatingCashFlow"] = ""
    assert build_ttm_row(_income(), _balance(), cf, "now", _AS_OF).empty


def test_unknown_cashflow_semantics_drops_ttm_for_annual_fallback() -> None:
    cf = _cf([-25, -25, -25, -25], [30, 30, 30, 30], [-10, -10, -10, -10], [5, 5, 5, 5])
    assert build_ttm_row(_income(), _balance(), cf, "now", _AS_OF).empty
