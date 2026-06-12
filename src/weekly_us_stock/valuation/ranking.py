"""Risk-adjusted ranking (Layer 4).

Two rankings are published side by side:
- Upside Ranking: expected 5y IRR, descending.
- Robust Ranking: risk-adjusted return under one of two configurable
  formulas whose weights are investor risk preferences (NOT factor weights):

  formula = "penalized_expected" (default, the project spec's decomposition):
    robust_return = expected_irr
                    - downside_aversion       * expected_shortfall (CVaR)
                    - ambiguity_aversion      * model_uncertainty
                    - permanent_loss_penalty  * permanent_loss_weight

  formula = "median_cvar" (single-penalty variant: the three penalty inputs
  are correlated because all derive partly from the bear scenario, so this
  mode subtracts only the tail term and reports the rest for sizing):
    robust_return = median_irr - downside_aversion * expected_shortfall

Every component stays in the output either way, so a rank can always be
traced back to its inputs; nothing is compressed into an opaque score.
The bear/base/bull weights are analyst-set scenario weights, not calibrated
probabilities — see the report disclaimers.
"""

from __future__ import annotations

import pandas as pd

from weekly_us_stock.config import RiskPreferenceSettings


def add_robust_components(
    frame: pd.DataFrame, prefs: RiskPreferenceSettings
) -> pd.DataFrame:
    result = frame.copy()
    result["downside_penalty"] = prefs.downside_aversion * result["expected_shortfall"]
    result["ambiguity_penalty"] = prefs.ambiguity_aversion * result["model_uncertainty"]
    result["permanent_loss_penalty"] = (
        prefs.permanent_loss_penalty * result["permanent_loss_probability"]
    )
    if prefs.formula == "median_cvar":
        result["robust_return"] = result["median_irr"] - result["downside_penalty"]
    else:
        result["robust_return"] = (
            result["expected_irr"]
            - result["downside_penalty"]
            - result["ambiguity_penalty"]
            - result["permanent_loss_penalty"]
        )
    return result


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
