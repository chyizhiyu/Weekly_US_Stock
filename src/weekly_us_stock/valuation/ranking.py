"""Risk-adjusted ranking (Layer 4).

Two rankings are published side by side:
- Upside Ranking: expected 5y IRR, descending.
- Robust Ranking: expected IRR minus explicit risk penalties whose weights are
  investor risk preferences from config (NOT factor weights):

    robust_return = expected_irr
                    - downside_aversion       * expected_shortfall (CVaR)
                    - ambiguity_aversion      * model_uncertainty
                    - permanent_loss_penalty  * permanent_loss_probability

Every component stays in the output so a rank can always be traced back to its
inputs; nothing is compressed into an opaque composite score.
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
