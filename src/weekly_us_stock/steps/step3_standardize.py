"""Step 3: standardize financial, market and estimate data.

Coerces dtypes, deduplicates fiscal years, enforces point-in-time discipline
(filing_date <= as_of) once more at the pipeline boundary, and extracts the
risk-free rate. Providers already filter by as_of; this is the belt to their
suspenders so a misbehaving provider cannot leak future data downstream.
"""

from __future__ import annotations

from datetime import date

import pandas as pd

_NUMERIC_FUNDAMENTAL_FIELDS = [
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
]


def standardize_fundamentals(fundamentals: pd.DataFrame, as_of: date) -> pd.DataFrame:
    if fundamentals.empty:
        return fundamentals
    frame = fundamentals.copy()
    frame["filing_date"] = pd.to_datetime(frame["filing_date"], errors="coerce")
    frame["fiscal_end"] = pd.to_datetime(frame["fiscal_end"], errors="coerce")
    frame = frame.loc[frame["filing_date"].notna()]
    frame = frame.loc[frame["filing_date"] <= pd.Timestamp(as_of)]
    for column in _NUMERIC_FUNDAMENTAL_FIELDS:
        if column in frame:
            frame[column] = pd.to_numeric(frame[column], errors="coerce")
    frame = (
        frame.sort_values(["ticker", "fiscal_year", "filing_date"])
        .groupby(["ticker", "fiscal_year"], as_index=False)
        .tail(1)
    )
    return frame.reset_index(drop=True)


def standardize_estimates(estimates: pd.DataFrame, as_of: date) -> pd.DataFrame:
    if estimates.empty:
        return estimates
    frame = estimates.copy()
    frame["as_of"] = pd.to_datetime(frame["as_of"], errors="coerce")
    frame = frame.loc[frame["as_of"].notna() & (frame["as_of"] <= pd.Timestamp(as_of))]
    numeric_columns = [
        "revenue_mean", "revenue_low", "revenue_high", "eps_mean", "eps_low", "eps_high",
    ]
    for column in numeric_columns:
        if column in frame:
            frame[column] = pd.to_numeric(frame[column], errors="coerce")
    return frame.reset_index(drop=True)


def extract_risk_free(macro: pd.DataFrame, fallback: float) -> tuple[float, str]:
    """Return (risk_free_rate, source_label)."""

    if macro.empty or "series" not in macro:
        return fallback, "config:fallback"
    rows = macro.loc[macro["series"] == "risk_free_10y"]
    if rows.empty:
        return fallback, "config:fallback"
    row = rows.iloc[-1]
    value = float(row["value"])
    if not 0.0 <= value <= 0.20:
        return fallback, "config:fallback(out-of-range)"
    return value, str(row.get("source", "unknown"))
