"""Normalized operating model per company (Layer 2).

Works on one ticker's annual fundamentals (point-in-time filtered upstream).
Normalization anchors profitability at full-cycle medians with one-off items
stripped out, so peak-cycle earnings cannot masquerade as cheapness and
one-time gains do not inflate earning power. SBC is treated as a real expense
when computing owner cash flow.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import pandas as pd

from weekly_us_stock.config import NormalizationSettings


@dataclass(slots=True)
class _Anchor:
    """The CURRENT operating snapshot the valuation hangs off: either the
    latest annual report or, preferably, a trailing-twelve-month row."""

    source: str
    revenue: float | None
    gross_profit: float
    operating_income: float
    one_off: float
    shares: float | None
    total_debt: float
    cash: float
    total_equity: float
    depreciation: float
    ocf: float
    interest_expense: float | None  # None == unknown, never assumed zero
    dividends_paid: float
    buybacks: float
    filing_date: str
    cashflow_period_semantics: str
    ttm_cashflow_status: str

    @classmethod
    def from_row(cls, row: pd.Series | dict) -> _Anchor:
        def _value(key: str, default: float | None = 0.0) -> float | None:
            raw = row.get(key) if isinstance(row, dict) else row.get(key)
            if raw is None or (isinstance(raw, float) and math.isnan(raw)):
                return default
            try:
                return float(raw)
            except (TypeError, ValueError):
                return default

        filing = row.get("filing_date")
        filing_text = str(filing.date()) if hasattr(filing, "date") else str(filing)
        is_ttm = bool(row.get("is_ttm")) if "is_ttm" in row else False
        cashflow_period_semantics = str(
            row.get("cashflow_period_semantics") or ("unknown" if is_ttm else "annual")
        )
        ttm_cashflow_status = str(
            row.get("ttm_cashflow_status") or ("unverified" if is_ttm else "annual_anchor")
        )
        return cls(
            source="ttm" if is_ttm else "annual",
            revenue=_value("revenue", None),
            gross_profit=_value("gross_profit") or 0.0,
            operating_income=_value("operating_income") or 0.0,
            one_off=_value("one_off_items") or 0.0,
            shares=_value("shares_diluted", None),
            total_debt=_value("total_debt") or 0.0,
            cash=_value("cash") or 0.0,
            total_equity=_value("total_equity") or 0.0,
            depreciation=_value("depreciation") or 0.0,
            ocf=_value("ocf") or 0.0,
            interest_expense=_value("interest_expense", None),
            dividends_paid=_value("dividends_paid") or 0.0,
            buybacks=_value("buybacks") or 0.0,
            filing_date=filing_text,
            cashflow_period_semantics=cashflow_period_semantics,
            ttm_cashflow_status=ttm_cashflow_status,
        )


def normalize_company(
    fundamentals: pd.DataFrame,
    settings: NormalizationSettings,
    ttm_row: pd.Series | dict | None = None,
) -> dict[str, float | int | bool | None] | None:
    """Return Layer-2 metrics for one company, or None when the history is too
    short to estimate normalized earnings (caller fails closed).

    Annual history drives everything cyclical (median margins, volatility,
    growth). When a trailing-twelve-month row is supplied it becomes the
    CURRENT anchor — revenue level, today's margin, share count, capital
    structure — so a weekly screen does not lag reality by most of a year.
    """

    frame = fundamentals.dropna(subset=["revenue"]).sort_values("fiscal_year")
    frame = frame.tail(settings.lookback_years).reset_index(drop=True)
    if len(frame) < settings.min_years_for_normalization:
        return None

    revenue = frame["revenue"].astype(float)
    one_offs = frame["one_off_items"].fillna(0.0).astype(float)
    adj_operating_income = frame["operating_income"].astype(float) - one_offs
    adj_margin = adj_operating_income / revenue

    latest = frame.iloc[-1]
    anchor = _Anchor.from_row(ttm_row) if ttm_row is not None else _Anchor.from_row(latest)
    latest_revenue = anchor.revenue
    if latest_revenue is None or latest_revenue <= 0:
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
    latest_shares = anchor.shares if anchor.shares and anchor.shares > 0 else float(shares.iloc[-1])
    if latest_shares <= 0:
        return None

    growth = revenue.pct_change().dropna()
    years_span = int(frame["fiscal_year"].iloc[-1] - frame["fiscal_year"].iloc[0])
    revenue_cagr = _cagr(float(revenue.iloc[0]), float(revenue.iloc[-1]), years_span)

    invested_capital = (
        frame["total_equity"].astype(float)
        + frame["total_debt"].fillna(0.0).astype(float)
        - frame["cash"].fillna(0.0).astype(float)
    )
    adj_nopat_series = adj_operating_income * (1.0 - tax_rate)
    anchor_adj_op = anchor.operating_income - anchor.one_off
    anchor_capital = anchor.total_equity + anchor.total_debt - anchor.cash
    roic = _safe_ratio(anchor_adj_op * (1.0 - tax_rate), anchor_capital)
    incremental_roic = _incremental_roic(adj_nopat_series, invested_capital)

    net_debt = anchor.total_debt - anchor.cash
    ebitda = anchor_adj_op + anchor.depreciation
    interest_coverage = (
        anchor_adj_op / anchor.interest_expense
        if anchor.interest_expense is not None and anchor.interest_expense > 0
        else None
    )
    net_debt_to_ebitda = net_debt / ebitda if ebitda > 0 else None

    recent = frame.tail(3)
    sbc_intensity = float((recent["sbc"].fillna(0.0) / recent["revenue"]).median())
    net_share_change_cagr = _cagr(
        float(shares.iloc[max(len(shares) - 4, 0)]), latest_shares, min(3, len(shares) - 1)
    )
    ocf_to_net_income = _ocf_to_net_income(recent)
    margin_signal = adj_margin
    ocf_margin_signal = frame["ocf"].astype(float) / revenue
    if anchor.source == "ttm":
        # Confidence must judge the CURRENT valuation anchor. Appending TTM as
        # the latest observation lets _mad_anomaly compare it with annual
        # history while still excluding it from the robust baseline.
        margin_signal = pd.concat(
            [margin_signal, pd.Series([anchor_adj_op / latest_revenue])],
            ignore_index=True,
        )
        ocf_margin_signal = pd.concat(
            [ocf_margin_signal, pd.Series([anchor.ocf / latest_revenue])],
            ignore_index=True,
        )
    margin_mad_z = _mad_anomaly(margin_signal, settings.one_off_mad_abs_floor)
    ocf_margin_mad_z = _mad_anomaly(ocf_margin_signal, settings.one_off_mad_abs_floor)
    one_off_suspected = _one_off_suspected(margin_mad_z, ocf_margin_mad_z, settings)

    return {
        "years_of_data": int(len(frame)),
        "latest_fiscal_year": int(latest["fiscal_year"]),
        "anchor_source": anchor.source,
        "latest_filing_date": anchor.filing_date,
        "cashflow_period_semantics": anchor.cashflow_period_semantics,
        "ttm_cashflow_status": anchor.ttm_cashflow_status,
        "revenue": latest_revenue,
        "revenue_cagr": revenue_cagr,
        "revenue_volatility": float(growth.std(ddof=0)) if len(growth) > 1 else 0.0,
        "gross_margin": _safe_ratio(anchor.gross_profit, latest_revenue),
        "current_operating_margin": anchor_adj_op / latest_revenue,
        "reported_operating_income": anchor.operating_income,
        "one_off_items_latest": anchor.one_off,
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
        "total_debt": anchor.total_debt,
        "interest_expense_known": anchor.interest_expense is not None,
        "interest_coverage": interest_coverage,
        "net_debt_to_ebitda": net_debt_to_ebitda,
        "sbc_intensity": sbc_intensity,
        "margin_mad_z": margin_mad_z,
        "ocf_margin_mad_z": ocf_margin_mad_z,
        "one_off_suspected": one_off_suspected,
        "dividends_paid": anchor.dividends_paid,
        "buybacks": anchor.buybacks,
        "net_share_change_cagr": net_share_change_cagr,
        "ocf_to_net_income": ocf_to_net_income,
        "shares_diluted": latest_shares,
    }


def _mad_anomaly(series: pd.Series, abs_floor: float) -> float:
    """Signed deviation of the latest point from its EX-LATEST history, in
    robust MAD units. The latest period is excluded so a one-off cannot
    contaminate the baseline it is judged against; a near-zero MAD falls back
    to an absolute floor. Returns 0.0 when history is too short."""

    values = series.dropna().astype(float)
    if len(values) < 4:
        return 0.0
    history = values.iloc[:-1]
    median = float(history.median())
    mad = float((history - median).abs().median())
    scale = max(1.4826 * mad, abs_floor)
    return (float(values.iloc[-1]) - median) / scale


def _one_off_suspected(
    margin_z: float, ocf_z: float, settings: NormalizationSettings
) -> bool:
    """A latest-period operating-margin spike is read as a likely one-off only
    when OCF/revenue does NOT corroborate it (same direction, comparable
    magnitude), so a real cash-backed operating improvement is not flagged."""

    if abs(margin_z) <= settings.one_off_mad_threshold:
        return False
    corroborated = (margin_z > 0) == (ocf_z > 0) and abs(ocf_z) >= max(
        settings.one_off_corroboration_z,
        settings.one_off_corroboration_ratio * abs(margin_z),
    )
    return not corroborated


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
        # A shrinking capital base makes the incremental return undefined.
        # Returning None (not an optimistic constant) lets the scenario engine
        # fall back to the level ROIC instead of inventing a high number.
        return None
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
