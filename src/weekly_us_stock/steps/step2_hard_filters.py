"""Step 2: investability hard filters (Layer 1).

Every condition here is NON-COMPENSATORY: no growth or valuation merit can
offset a failed check. Missing core data fails closed — a stock with unknown
financials is rejected, never guessed at. Each rejected row records exactly
one machine-readable ``rejection_reason`` (the first failed gate) for the
audit trail.
"""

from __future__ import annotations

from datetime import date

import pandas as pd

from weekly_us_stock.config import HardFilterSettings, UniverseSettings
from weekly_us_stock.models.screening import FilterFrameResult


def run_security_type_filters(
    universe: pd.DataFrame,
    as_of: date,
    universe_settings: UniverseSettings,
    hard_filters: HardFilterSettings,
) -> FilterFrameResult:
    frame = universe.copy()
    reasons = pd.Series("", index=frame.index, dtype=str)

    allowed_types = set(universe_settings.allowed_security_types)
    allowed_exchanges = {value.upper() for value in universe_settings.exchanges}

    type_bad = ~frame["security_type"].isin(allowed_types)
    _assign(reasons, type_bad, "security_type")

    exchange_bad = ~frame["exchange"].astype(str).str.upper().isin(allowed_exchanges)
    _assign(reasons, exchange_bad, "exchange_not_allowed")

    if not universe_settings.include_adrs:
        _assign(reasons, frame["is_adr"].fillna(False).astype(bool), "adr_excluded")

    listing = pd.to_datetime(frame["listing_date"], errors="coerce")
    min_listing = pd.Timestamp(as_of) - pd.DateOffset(years=hard_filters.min_listing_years)
    _assign(reasons, listing.isna(), "listing_date_missing")
    _assign(reasons, listing > min_listing, "listing_age")

    return _split(frame, reasons)


def run_market_filters(
    candidates: pd.DataFrame,
    snapshot: pd.DataFrame,
    settings: HardFilterSettings,
) -> FilterFrameResult:
    frame = candidates.merge(
        snapshot[
            ["ticker", "price", "price_as_of", "market_cap", "avg_dollar_volume", "is_price_fresh"]
        ],
        on="ticker",
        how="left",
    )
    reasons = pd.Series("", index=frame.index, dtype=str)

    missing_market = frame["price"].isna() | frame["market_cap"].isna()
    _assign(reasons, missing_market, "missing_market_data")
    _assign(reasons, frame["market_cap"] < settings.min_market_cap, "market_cap")
    _assign(
        reasons,
        frame["avg_dollar_volume"].isna()
        | (frame["avg_dollar_volume"] < settings.min_avg_dollar_volume),
        "liquidity",
    )
    # Fail closed on stale quotes: an IRR computed off an old price is not a
    # ranking, it is a guess. Degraded runs report these as rejections.
    _assign(
        reasons,
        ~frame["is_price_fresh"].fillna(False).astype(bool),
        "stale_price",
    )
    return _split(frame, reasons)


def run_financial_hard_filters(
    candidates: pd.DataFrame,
    fundamentals: pd.DataFrame,
    settings: HardFilterSettings,
) -> FilterFrameResult:
    frame = candidates.copy()
    reasons = pd.Series("", index=frame.index, dtype=str)

    grouped: dict[str, pd.DataFrame] = (
        {
            ticker: group.sort_values("fiscal_year")
            for ticker, group in fundamentals.groupby("ticker")
        }
        if not fundamentals.empty
        else {}
    )

    for index, row in frame.iterrows():
        reason = _financial_reason(grouped.get(row["ticker"]), settings)
        if reason:
            reasons.at[index] = reason

    return _split(frame, reasons)


_CORE_FIELDS = [
    "revenue",
    "operating_income",
    "net_income",
    "ocf",
    "capex",
    "shares_diluted",
    "total_debt",
    "cash",
    "total_equity",
]


def _financial_reason(history: pd.DataFrame | None, settings: HardFilterSettings) -> str | None:
    if history is None or len(history) < settings.min_financial_years:
        return "insufficient_financial_history"  # fail closed

    recent = history.tail(settings.min_financial_years)
    if recent[_CORE_FIELDS].isna().any().any():
        return "missing_core_financials"  # fail closed

    net_income = history["net_income"].astype(float)
    loss_window = net_income.tail(settings.max_consecutive_loss_years)
    if len(loss_window) >= settings.max_consecutive_loss_years and (loss_window < 0).all():
        return "consecutive_losses"

    fcf = history["ocf"].astype(float) - history["capex"].fillna(0.0).astype(float)
    fcf_window = fcf.tail(settings.max_negative_fcf_years)
    if len(fcf_window) >= settings.max_negative_fcf_years and (fcf_window < 0).all():
        return "persistent_negative_fcf"

    latest = history.iloc[-1]
    net_debt = float(latest["total_debt"] or 0.0) - float(latest["cash"] or 0.0)
    interest = float(latest["interest_expense"] or 0.0)
    operating_income = float(latest["operating_income"] or 0.0)
    if net_debt > 0 and interest > 0:
        if operating_income / interest < settings.min_interest_coverage:
            return "interest_coverage"
    ebitda = operating_income + float(latest["depreciation"] or 0.0)
    if net_debt > 0 and ebitda > 0 and net_debt / ebitda > settings.max_net_debt_to_ebitda:
        return "excessive_leverage"
    if net_debt > 0 and ebitda <= 0:
        return "negative_ebitda_with_debt"

    shares = history["shares_diluted"].astype(float)
    window = min(3, len(shares) - 1)
    if window >= 1 and shares.iloc[-1 - window] > 0:
        dilution_cagr = (shares.iloc[-1] / shares.iloc[-1 - window]) ** (1.0 / window) - 1.0
        if dilution_cagr > settings.max_share_dilution_cagr_3y:
            return "severe_dilution"

    profitable = history.tail(3).loc[history.tail(3)["net_income"].astype(float) > 0]
    if not profitable.empty:
        ratio = (profitable["ocf"].astype(float) / profitable["net_income"].astype(float)).median()
        if ratio < settings.min_ocf_to_net_income:
            return "earnings_cash_mismatch"  # accounting-quality red flag

    return None


def combine_results(*results: FilterFrameResult) -> dict[str, int]:
    counts: dict[str, int] = {}
    for result in results:
        for reason, count in result.rejection_counts.items():
            counts[reason] = counts.get(reason, 0) + count
    return counts


def _assign(reasons: pd.Series, mask: pd.Series, reason: str) -> None:
    apply_to = mask.fillna(True).astype(bool) & (reasons == "")
    reasons.loc[apply_to] = reason


def _split(frame: pd.DataFrame, reasons: pd.Series) -> FilterFrameResult:
    rejected = frame.loc[reasons != ""].copy()
    rejected["rejection_reason"] = reasons.loc[reasons != ""]
    candidates = frame.loc[reasons == ""].reset_index(drop=True)
    counts = rejected["rejection_reason"].value_counts().to_dict() if not rejected.empty else {}
    return FilterFrameResult(
        candidates=candidates,
        rejected=rejected.reset_index(drop=True),
        rejection_counts={str(k): int(v) for k, v in counts.items()},
    )
