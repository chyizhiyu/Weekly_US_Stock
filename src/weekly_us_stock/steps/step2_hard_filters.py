"""Step 2: investability hard filters (Layer 1).

Every condition here is NON-COMPENSATORY: no growth or valuation merit can
offset a failed check. Missing core data fails closed — a stock with unknown
financials is rejected, never guessed at. Each rejected row records the first
failed gate in ``rejection_reason`` for backward compatibility and every
failed gate in ``all_rejection_reasons`` for the audit trail.
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
    all_reasons = _empty_reason_lists(frame.index)

    allowed_types = set(universe_settings.allowed_security_types)
    allowed_exchanges = {value.upper() for value in universe_settings.exchanges}

    type_bad = ~frame["security_type"].isin(allowed_types)
    _assign(reasons, type_bad, "security_type", all_reasons)

    exchange_bad = ~frame["exchange"].astype(str).str.upper().isin(allowed_exchanges)
    _assign(reasons, exchange_bad, "exchange_not_allowed", all_reasons)

    if not universe_settings.include_adrs:
        _assign(
            reasons,
            frame["is_adr"].fillna(False).astype(bool),
            "adr_excluded",
            all_reasons,
        )

    listing = pd.to_datetime(frame["listing_date"], errors="coerce")
    min_listing = pd.Timestamp(as_of) - pd.DateOffset(years=hard_filters.min_listing_years)
    _assign(reasons, listing.isna(), "listing_date_missing", all_reasons)
    _assign(reasons, listing > min_listing, "listing_age", all_reasons)

    return _split(frame, reasons, all_reasons)


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
    all_reasons = _empty_reason_lists(frame.index)

    missing_market = frame["price"].isna() | frame["market_cap"].isna()
    _assign(reasons, missing_market, "missing_market_data", all_reasons)
    _assign(reasons, frame["market_cap"] < settings.min_market_cap, "market_cap", all_reasons)
    _assign(
        reasons,
        frame["avg_dollar_volume"].isna()
        | (frame["avg_dollar_volume"] < settings.min_avg_dollar_volume),
        "liquidity",
        all_reasons,
    )
    # Fail closed on stale quotes: an IRR computed off an old price is not a
    # ranking, it is a guess. Degraded runs report these as rejections.
    _assign(
        reasons,
        ~frame["is_price_fresh"].fillna(False).astype(bool),
        "stale_price",
        all_reasons,
    )
    return _split(frame, reasons, all_reasons)


def drop_duplicate_share_classes(candidates: pd.DataFrame) -> FilterFrameResult:
    """One economic entity, one ranking slot: GOOG/GOOGL or BRK-A/BRK-B style
    duplicate listings keep only the most liquid line (exact company-name
    match); the rest are rejected as duplicate_share_class."""

    if candidates.empty or "name" not in candidates:
        return FilterFrameResult(candidates=candidates)
    frame = candidates.copy()
    named = frame["name"].fillna("").astype(str).str.strip()
    duplicated = named.ne("") & named.duplicated(keep=False)
    if not duplicated.any():
        return FilterFrameResult(candidates=frame.reset_index(drop=True))

    liquidity = pd.to_numeric(frame.get("avg_dollar_volume"), errors="coerce").fillna(0.0)
    keep_index = (
        frame.assign(_name=named, _liquidity=liquidity)
        .sort_values("_liquidity", ascending=False)
        .drop_duplicates(subset=["_name"])
        .index
    )
    reasons = pd.Series("", index=frame.index, dtype=str)
    reasons.loc[duplicated & ~frame.index.isin(keep_index)] = "duplicate_share_class"
    return _split(frame, reasons)


def run_financial_hard_filters(
    candidates: pd.DataFrame,
    fundamentals: pd.DataFrame,
    settings: HardFilterSettings,
) -> FilterFrameResult:
    frame = candidates.copy()
    reasons = pd.Series("", index=frame.index, dtype=str)
    all_reasons = _empty_reason_lists(frame.index)

    grouped: dict[str, pd.DataFrame] = (
        {
            ticker: group.sort_values("fiscal_year")
            for ticker, group in fundamentals.groupby("ticker")
        }
        if not fundamentals.empty
        else {}
    )

    for index, row in frame.iterrows():
        failed = _financial_reasons(grouped.get(row["ticker"]), settings)
        if failed:
            reasons.at[index] = failed[0]
            all_reasons.at[index] = failed

    return _split(frame, reasons, all_reasons)


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


def _financial_reasons(history: pd.DataFrame | None, settings: HardFilterSettings) -> list[str]:
    if history is None or len(history) < settings.min_financial_years:
        return ["insufficient_financial_history"]  # fail closed

    recent = history.tail(settings.min_financial_years)
    if recent[_CORE_FIELDS].isna().any().any():
        return ["missing_core_financials"]  # fail closed

    reasons: list[str] = []

    net_income = history["net_income"].astype(float)
    loss_window = net_income.tail(settings.max_consecutive_loss_years)
    if len(loss_window) >= settings.max_consecutive_loss_years and (loss_window < 0).all():
        reasons.append("consecutive_losses")

    # Owner cash flow: SBC is a real expense (the OCF add-back is stripped).
    fcf = (
        history["ocf"].astype(float)
        - history["capex"].fillna(0.0).astype(float)
        - history["sbc"].fillna(0.0).astype(float)
    )
    fcf_window = fcf.tail(settings.max_negative_fcf_years)
    if len(fcf_window) >= settings.max_negative_fcf_years and (fcf_window < 0).all():
        reasons.append("persistent_negative_fcf")

    latest = history.iloc[-1]
    net_debt = float(latest["total_debt"] or 0.0) - float(latest["cash"] or 0.0)
    interest = float(latest["interest_expense"] or 0.0)
    operating_income = float(latest["operating_income"] or 0.0)
    if net_debt > 0 and interest > 0:
        if operating_income / interest < settings.min_interest_coverage:
            reasons.append("interest_coverage")
    ebitda = operating_income + float(latest["depreciation"] or 0.0)
    if net_debt > 0 and ebitda > 0 and net_debt / ebitda > settings.max_net_debt_to_ebitda:
        reasons.append("excessive_leverage")
    if net_debt > 0 and ebitda <= 0:
        reasons.append("negative_ebitda_with_debt")

    shares = history["shares_diluted"].astype(float)
    window = min(3, len(shares) - 1)
    if window >= 1 and shares.iloc[-1 - window] > 0:
        dilution_cagr = (shares.iloc[-1] / shares.iloc[-1 - window]) ** (1.0 / window) - 1.0
        if dilution_cagr > settings.max_share_dilution_cagr_3y:
            reasons.append("severe_dilution")

    profitable = history.tail(3).loc[history.tail(3)["net_income"].astype(float) > 0]
    if not profitable.empty:
        ratio = (profitable["ocf"].astype(float) / profitable["net_income"].astype(float)).median()
        if ratio < settings.min_ocf_to_net_income:
            reasons.append("earnings_cash_mismatch")  # accounting-quality red flag

    return reasons


def combine_results(*results: FilterFrameResult) -> dict[str, int]:
    counts: dict[str, int] = {}
    for result in results:
        for reason, count in result.rejection_counts.items():
            counts[reason] = counts.get(reason, 0) + count
    return counts


def _empty_reason_lists(index: pd.Index) -> pd.Series:
    return pd.Series([[] for _ in range(len(index))], index=index, dtype=object)


def _assign(
    reasons: pd.Series,
    mask: pd.Series,
    reason: str,
    all_reasons: pd.Series | None = None,
) -> None:
    failed = mask.fillna(True).astype(bool)
    if all_reasons is not None:
        for index in all_reasons.index[failed]:
            all_reasons.at[index] = [*all_reasons.at[index], reason]
    reasons.loc[failed & (reasons == "")] = reason


def _split(
    frame: pd.DataFrame,
    reasons: pd.Series,
    all_reasons: pd.Series | None = None,
) -> FilterFrameResult:
    rejected = frame.loc[reasons != ""].copy()
    rejected["rejection_reason"] = reasons.loc[reasons != ""]
    if all_reasons is None:
        rejected["all_rejection_reasons"] = rejected["rejection_reason"]
    else:
        rejected["all_rejection_reasons"] = all_reasons.loc[reasons != ""].map(";".join)
    candidates = frame.loc[reasons == ""].reset_index(drop=True)
    counts = rejected["rejection_reason"].value_counts().to_dict() if not rejected.empty else {}
    return FilterFrameResult(
        candidates=candidates,
        rejected=rejected.reset_index(drop=True),
        rejection_counts={str(k): int(v) for k, v in counts.items()},
    )
