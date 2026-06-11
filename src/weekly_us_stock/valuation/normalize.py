"""Normalized operating model per company (Layer 2).

Works on one ticker's annual fundamentals (point-in-time filtered upstream).
Normalization anchors profitability at full-cycle medians with one-off items
stripped out, so peak-cycle earnings cannot masquerade as cheapness and
one-time gains do not inflate earning power. SBC is treated as a real expense
when computing owner cash flow.
"""

from __future__ import annotations

import math

import pandas as pd

from weekly_us_stock.config import NormalizationSettings


def normalize_company(
    fundamentals: pd.DataFrame,
    settings: NormalizationSettings,
) -> dict[str, float | int | bool | None] | None:
    """Return Layer-2 metrics for one company, or None when the history is too
    short to estimate normalized earnings (caller fails closed)."""

    frame = fundamentals.dropna(subset=["revenue"]).sort_values("fiscal_year")
    frame = frame.tail(settings.lookback_years).reset_index(drop=True)
    if len(frame) < settings.min_years_for_normalization:
        return None

    revenue = frame["revenue"].astype(float)
    one_offs = frame["one_off_items"].fillna(0.0).astype(float)
    adj_operating_income = frame["operating_income"].astype(float) - one_offs
    adj_margin = adj_operating_income / revenue

    latest = frame.iloc[-1]
    latest_revenue = float(latest["revenue"])
    if latest_revenue <= 0:
        return None

    normalized_margin = float(adj_margin.median())
    normalized_operating_income = normalized_margin * latest_revenue

    tax_rate = _clamped_tax_rate(frame, settings)
    normalized_nopat = normalized_operating_income * (1.0 - tax_rate)

    sbc = frame["sbc"].fillna(0.0).astype(float)
    adj_fcf = frame["ocf"].astype(float) - frame["capex"].fillna(0.0).astype(float) - sbc
    adj_fcf_margin = adj_fcf / revenue
    normalized_fcf = float(adj_fcf_margin.median()) * latest_revenue

    shares = frame["shares_diluted"].astype(float)
    latest_shares = float(shares.iloc[-1])
    if latest_shares <= 0:
        return None

    growth = revenue.pct_change().dropna()
    years_span = int(frame["fiscal_year"].iloc[-1] - frame["fiscal_year"].iloc[0])
    revenue_cagr = _cagr(float(revenue.iloc[0]), latest_revenue, years_span)

    invested_capital = (
        frame["total_equity"].astype(float)
        + frame["total_debt"].fillna(0.0).astype(float)
        - frame["cash"].fillna(0.0).astype(float)
    )
    adj_nopat_series = adj_operating_income * (1.0 - tax_rate)
    roic = _safe_ratio(float(adj_nopat_series.iloc[-1]), float(invested_capital.iloc[-1]))
    incremental_roic = _incremental_roic(adj_nopat_series, invested_capital)

    net_debt = float(latest["total_debt"] or 0.0) - float(latest["cash"] or 0.0)
    ebitda = float(adj_operating_income.iloc[-1]) + float(latest["depreciation"] or 0.0)
    interest_expense = float(latest["interest_expense"] or 0.0)
    interest_coverage = (
        float(adj_operating_income.iloc[-1]) / interest_expense if interest_expense > 0 else None
    )
    net_debt_to_ebitda = net_debt / ebitda if ebitda > 0 else None

    recent = frame.tail(3)
    sbc_intensity = float((recent["sbc"].fillna(0.0) / recent["revenue"]).median())
    net_share_change_cagr = _cagr(
        float(shares.iloc[max(len(shares) - 4, 0)]), latest_shares, min(3, len(shares) - 1)
    )
    ocf_to_net_income = _ocf_to_net_income(recent)

    return {
        "years_of_data": int(len(frame)),
        "latest_fiscal_year": int(latest["fiscal_year"]),
        "latest_filing_date": str(latest["filing_date"].date())
        if hasattr(latest["filing_date"], "date")
        else str(latest["filing_date"]),
        "revenue": latest_revenue,
        "revenue_cagr": revenue_cagr,
        "revenue_volatility": float(growth.std(ddof=0)) if len(growth) > 1 else 0.0,
        "gross_margin": _safe_ratio(float(latest["gross_profit"] or 0.0), latest_revenue),
        "current_operating_margin": float(adj_margin.iloc[-1]),
        "reported_operating_income": float(latest["operating_income"]),
        "one_off_items_latest": float(latest["one_off_items"] or 0.0),
        "normalized_operating_margin": normalized_margin,
        "normalized_operating_income": normalized_operating_income,
        "normalized_nopat": normalized_nopat,
        "normalized_fcf": normalized_fcf,
        "normalized_fcf_per_share": normalized_fcf / latest_shares,
        "margin_volatility": float(adj_margin.std(ddof=0)),
        "tax_rate": tax_rate,
        "roic": roic,
        "incremental_roic": incremental_roic,
        "net_debt": net_debt,
        "interest_coverage": interest_coverage,
        "net_debt_to_ebitda": net_debt_to_ebitda,
        "sbc_intensity": sbc_intensity,
        "dividends_paid": float(latest["dividends_paid"] or 0.0),
        "buybacks": float(latest["buybacks"] or 0.0),
        "net_share_change_cagr": net_share_change_cagr,
        "ocf_to_net_income": ocf_to_net_income,
        "shares_diluted": latest_shares,
    }


def _clamped_tax_rate(frame: pd.DataFrame, settings: NormalizationSettings) -> float:
    rates = frame["effective_tax_rate"].dropna().astype(float)
    rate = float(rates.median()) if not rates.empty else settings.default_tax_rate
    if math.isnan(rate):
        rate = settings.default_tax_rate
    return min(max(rate, settings.min_tax_rate), settings.max_tax_rate)


def _incremental_roic(nopat: pd.Series, invested_capital: pd.Series) -> float | None:
    window = min(4, len(nopat) - 1)
    if window < 2:
        return None
    delta_nopat = float(nopat.iloc[-1] - nopat.iloc[-1 - window])
    delta_capital = float(invested_capital.iloc[-1] - invested_capital.iloc[-1 - window])
    if delta_capital <= 0:
        # Returns grew without net new capital: cap the signal rather than
        # reporting an unbounded ratio.
        return 0.60 if delta_nopat > 0 else None
    return delta_nopat / delta_capital


def _ocf_to_net_income(recent: pd.DataFrame) -> float | None:
    profitable = recent.loc[recent["net_income"].astype(float) > 0]
    if profitable.empty:
        return None
    ratios = profitable["ocf"].astype(float) / profitable["net_income"].astype(float)
    return float(ratios.median())


def _cagr(start: float, end: float, years: int) -> float:
    if years <= 0 or start <= 0 or end <= 0:
        return 0.0
    return (end / start) ** (1.0 / years) - 1.0


def _safe_ratio(numerator: float, denominator: float) -> float | None:
    if denominator is None or denominator == 0 or math.isnan(denominator):
        return None
    return numerator / denominator
