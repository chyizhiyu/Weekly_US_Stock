"""One-row-per-ticker ledger explaining the final funnel outcome."""

from __future__ import annotations

import pandas as pd

_OUTPUT_COLUMNS = [
    "ticker",
    "name",
    "sector",
    "industry",
    "final_bucket",
    "decision_stage",
    "decision_reason",
    "rank",
    "eligible",
    "robust_return",
    "expected_irr",
    "median_irr",
    "p10_irr",
    "hurdle_cvar",
    "business_quality",
    "model_confidence",
    "data_confidence",
    "evidence_confidence",
    "catastrophic_tail_floor_applied",
    "catastrophic_tail_scenarios",
]


def build_funnel_ledger(
    universe: pd.DataFrame,
    hard_rejected: pd.DataFrame,
    normalization_rejected: pd.DataFrame,
    watchlist: pd.DataFrame,
    ranked: pd.DataFrame,
) -> pd.DataFrame:
    """Return exactly one final disposition for every ticker in the universe."""

    base_columns = [
        column
        for column in ["ticker", "name", "sector", "industry"]
        if column in universe
    ]
    ledger = universe[base_columns].drop_duplicates(subset=["ticker"]).copy()
    ledger["final_bucket"] = "unaccounted"
    ledger["decision_stage"] = ""
    ledger["decision_reason"] = ""
    for column in _OUTPUT_COLUMNS[7:]:
        ledger[column] = pd.NA
    ledger = ledger.set_index("ticker", drop=False)

    _apply_disposition(
        ledger,
        hard_rejected,
        bucket="hard_filter_rejected",
        stage="step2_hard_filters",
        reason_columns=["all_rejection_reasons", "rejection_reason"],
    )
    _apply_disposition(
        ledger,
        normalization_rejected,
        bucket="normalization_rejected",
        stage="step4_normalized_model",
        reason_columns=["rejection_reason"],
    )

    if not watchlist.empty:
        for _, row in watchlist.iterrows():
            ticker = row.get("ticker")
            if ticker not in ledger.index:
                continue
            reason = row.get("watchlist_reason")
            ledger.at[ticker, "final_bucket"] = "watchlist"
            ledger.at[ticker, "decision_stage"] = _watchlist_stage(str(reason or ""))
            ledger.at[ticker, "decision_reason"] = reason
            _copy_metrics(ledger, ticker, row)

    if not ranked.empty:
        for _, row in ranked.iterrows():
            ticker = row.get("ticker")
            if ticker not in ledger.index:
                continue
            eligible = bool(row.get("eligible", False))
            ledger.at[ticker, "final_bucket"] = "eligible" if eligible else "research_queue"
            ledger.at[ticker, "decision_stage"] = "step7_risk_adjusted_ranking"
            ledger.at[ticker, "decision_reason"] = (
                "eligible" if eligible else row.get("ineligible_reasons")
            )
            _copy_metrics(ledger, ticker, row)

    return ledger.reset_index(drop=True)[_OUTPUT_COLUMNS]


def _apply_disposition(
    ledger: pd.DataFrame,
    rows: pd.DataFrame,
    *,
    bucket: str,
    stage: str,
    reason_columns: list[str],
) -> None:
    if rows.empty:
        return
    for _, row in rows.iterrows():
        ticker = row.get("ticker")
        if ticker not in ledger.index:
            continue
        reason = next(
            (
                row.get(column)
                for column in reason_columns
                if column in row.index and pd.notna(row.get(column)) and str(row.get(column))
            ),
            "",
        )
        ledger.at[ticker, "final_bucket"] = bucket
        ledger.at[ticker, "decision_stage"] = stage
        ledger.at[ticker, "decision_reason"] = reason


def _copy_metrics(ledger: pd.DataFrame, ticker: object, row: pd.Series) -> None:
    for column in _OUTPUT_COLUMNS[7:]:
        if column in row.index and pd.notna(row.get(column)):
            ledger.at[ticker, column] = row.get(column)


def _watchlist_stage(reason: str) -> str:
    if reason == "material_event_requires_reunderwriting":
        return "step2_material_event_gate"
    if reason.endswith("_not_supported"):
        return "step2_model_routing"
    if reason == "insufficient_confidence":
        return "step4_normalized_model"
    if reason == "insufficient_model_confidence":
        return "step5_quality_risk"
    if reason == "incomplete_valuation_inputs":
        return "step6_valuation_inputs"
    return "step6_scenario_valuation"
