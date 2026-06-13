"""P0-4: ranking is not investability - eligible candidates are split out."""

from __future__ import annotations

import pandas as pd

from weekly_us_stock.config import EligibilitySettings
from weekly_us_stock.valuation.eligibility import classify_eligibility


def _ranked() -> pd.DataFrame:
    return pd.DataFrame(
        [
            # clears the bar: positive robust return, median above hurdle
            {"rank": 1, "ticker": "GOOD", "robust_return": 0.05, "median_irr": 0.20,
             "hurdle_rate": 0.12, "expected_irr": 0.18, "p10_irr": 0.02,
             "above_hurdle_weight": 0.80, "model_uncertainty": 0.30, "evidence_confidence": 0.90},
            # high expected IRR but negative robust return + fat tail -> research only
            {"rank": 2, "ticker": "CHTR", "robust_return": -0.73, "median_irr": 0.54,
             "hurdle_rate": 0.12, "expected_irr": 0.60, "p10_irr": -0.95,
             "above_hurdle_weight": 0.50, "model_uncertainty": 1.20, "evidence_confidence": 0.60},
            # positive robust but median below hurdle -> ineligible
            {"rank": 3, "ticker": "LOWMED", "robust_return": 0.01, "median_irr": 0.10,
             "hurdle_rate": 0.12, "expected_irr": 0.11, "p10_irr": 0.0,
             "above_hurdle_weight": 0.40, "model_uncertainty": 0.40, "evidence_confidence": 0.80},
        ]
    )


def test_default_eligibility_splits_actionable_from_research() -> None:
    result = classify_eligibility(_ranked(), EligibilitySettings())
    assert set(result.eligible["ticker"]) == {"GOOD"}
    # CHTR: high expected IRR but negative robust_return -> research queue, not eligible
    assert "CHTR" in set(result.research_queue["ticker"])
    reasons = result.ranked.set_index("ticker")["ineligible_reasons"]
    assert "robust_return<=0" in reasons.loc["CHTR"]
    assert "median_irr<=hurdle" in reasons.loc["LOWMED"]
    assert reasons.loc["GOOD"] == ""


def test_no_eligible_returns_empty_not_padded() -> None:
    frame = _ranked()
    frame["robust_return"] = -1.0  # everyone fails the bar
    result = classify_eligibility(frame, EligibilitySettings())
    assert result.eligible.empty
    assert len(result.research_queue) == 3  # ranked but none actionable; no padding


def test_stricter_optional_rules_apply() -> None:
    lenient = classify_eligibility(_ranked(), EligibilitySettings(min_above_hurdle_weight=0.75))
    assert set(lenient.eligible["ticker"]) == {"GOOD"}  # 0.80 >= 0.75
    strict = classify_eligibility(_ranked(), EligibilitySettings(min_above_hurdle_weight=0.95))
    assert strict.eligible.empty  # GOOD's 0.80 weight now fails the 0.95 bar


def test_empty_ranking_is_safe() -> None:
    result = classify_eligibility(pd.DataFrame(), EligibilitySettings())
    assert result.eligible.empty and result.research_queue.empty
