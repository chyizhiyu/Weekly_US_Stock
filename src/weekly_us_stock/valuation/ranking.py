"""Risk-adjusted ranking (Layer 4).

Two rankings are published side by side:
- Upside Ranking: expected 5y IRR, descending.
- Robust Ranking: risk-adjusted return under a configurable formula whose
  weights are investor risk preferences, not factor weights.

The current scenario set is a deterministic bear/base/bull stress grid. With
25/50/25 scenario weights, an alpha=25% CVaR calculation collapses to the bear
point, so the public metric names are explicit worst-case stress terms:

  formula = "hurdle_gap" (default):
    robust_return = data_confidence * model_confidence
                      * max(median_irr - hurdle_rate, 0)
                    - downside_aversion * worst_case_hurdle_gap

  formula = "penalized_expected":
    robust_return = expected_irr
                    - downside_aversion       * worst_case_shortfall
                    - ambiguity_aversion      * model_uncertainty
                    - permanent_loss_penalty  * permanent_loss_weight

  formula = "median_stress":
    robust_return = median_irr - downside_aversion * worst_case_shortfall

Legacy formula names "hurdle_cvar" and "median_cvar" are still accepted and
map to the same formulas. Every component stays in the output regardless of
formula, so a rank can be traced back to its inputs; nothing is compressed into
an opaque score. Bear/base/bull weights are analyst-set scenario weights, not
calibrated probabilities.
"""

from __future__ import annotations

import pandas as pd

from weekly_us_stock.config import RiskPreferenceSettings


def add_robust_components(
    frame: pd.DataFrame, prefs: RiskPreferenceSettings
) -> pd.DataFrame:
    result = frame.copy()
    shortfall = _metric(result, "worst_case_shortfall", "expected_shortfall")
    hurdle_gap = _metric(result, "worst_case_hurdle_gap", "hurdle_cvar")
    result["downside_penalty"] = prefs.downside_aversion * shortfall
    result["ambiguity_penalty"] = prefs.ambiguity_aversion * result["model_uncertainty"]
    result["permanent_loss_penalty"] = (
        prefs.permanent_loss_penalty * result["permanent_loss_weight"]
    )
    result["evidence_confidence"] = result["data_confidence"] * result["model_confidence"]
    if prefs.formula in {"hurdle_gap", "hurdle_cvar"}:
        positive_excess = (result["median_irr"] - result["hurdle_rate"]).clip(lower=0.0)
        result["hurdle_penalty"] = prefs.downside_aversion * hurdle_gap
        result["robust_return"] = (
            result["evidence_confidence"] * positive_excess - result["hurdle_penalty"]
        )
    elif prefs.formula in {"median_stress", "median_cvar"}:
        result["robust_return"] = result["median_irr"] - result["downside_penalty"]
    else:  # penalized_expected
        result["robust_return"] = (
            result["expected_irr"]
            - result["downside_penalty"]
            - result["ambiguity_penalty"]
            - result["permanent_loss_penalty"]
        )
    return result


def _metric(frame: pd.DataFrame, primary: str, legacy: str) -> pd.Series:
    if primary in frame.columns:
        return frame[primary]
    return frame[legacy]


def build_rankings(
    valuations: pd.DataFrame, prefs: RiskPreferenceSettings
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return (robust_ranking, upside_ranking) with 1-based rank columns."""

    if valuations.empty:
        empty = valuations.copy()
        empty["rank"] = pd.Series(dtype=int)
        return empty, empty

    scored = add_robust_components(valuations, prefs)

    robust = scored.sort_values(
        ["robust_return", "expected_irr"], ascending=False
    ).reset_index(drop=True)
    robust.insert(0, "rank", robust.index + 1)

    upside = scored.sort_values(
        ["expected_irr", "median_irr"], ascending=False
    ).reset_index(drop=True)
    upside.insert(0, "rank", upside.index + 1)
    return robust, upside
