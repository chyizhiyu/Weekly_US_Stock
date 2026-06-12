"""Layer-4 risk-adjusted ranking: penalties are preferences, not factor weights."""

from __future__ import annotations

import pandas as pd
import pytest

from weekly_us_stock.config import RiskPreferenceSettings
from weekly_us_stock.valuation.ranking import add_robust_components, build_rankings

PREFS = RiskPreferenceSettings()  # default formula: hurdle_cvar


def _metrics() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                # Steady compounder: modest excess over the hurdle, shallow tail.
                "ticker": "COMPOUND",
                "expected_irr": 0.13,
                "median_irr": 0.14,
                "hurdle_rate": 0.12,
                "expected_shortfall": 0.00,
                "hurdle_cvar": 0.02,  # bear lands at 10% vs the 12% hurdle
                "model_uncertainty": 0.05,
                "permanent_loss_weight": 0.0,
                "data_confidence": 0.95,
                "model_confidence": 0.90,
            },
            {
                # Lottery ticket: higher expected IRR, deep hurdle-relative tail.
                "ticker": "LOTTERY",
                "expected_irr": 0.20,
                "median_irr": 0.18,
                "hurdle_rate": 0.12,
                "expected_shortfall": 0.30,
                "hurdle_cvar": 0.42,  # bear at -30% vs the 12% hurdle
                "model_uncertainty": 0.30,
                "permanent_loss_weight": 0.25,
                "data_confidence": 0.70,
                "model_confidence": 0.45,
            },
        ]
    )


def test_hurdle_cvar_formula_is_transparent() -> None:
    scored = add_robust_components(_metrics(), PREFS)
    row = scored.set_index("ticker").loc["LOTTERY"]
    expected = (0.70 * 0.45) * max(0.18 - 0.12, 0.0) - PREFS.downside_aversion * 0.42
    assert row["robust_return"] == pytest.approx(expected)
    # A bear case below the hurdle is penalized even when its IRR is positive.
    compound = scored.set_index("ticker").loc["COMPOUND"]
    assert compound["hurdle_penalty"] > 0
    # Every component stays visible: no opaque composite score.
    for column in [
        "hurdle_penalty",
        "downside_penalty",
        "ambiguity_penalty",
        "permanent_loss_penalty",
        "evidence_confidence",
    ]:
        assert column in scored.columns


def test_penalized_expected_formula_matches_spec_decomposition() -> None:
    prefs = RiskPreferenceSettings(formula="penalized_expected")
    scored = add_robust_components(_metrics(), prefs)
    row = scored.set_index("ticker").loc["LOTTERY"]
    expected = (
        0.20
        - prefs.downside_aversion * 0.30
        - prefs.ambiguity_aversion * 0.30
        - prefs.permanent_loss_penalty * 0.25
    )
    assert row["robust_return"] == pytest.approx(expected)


def test_median_cvar_formula_uses_a_single_penalty() -> None:
    prefs = RiskPreferenceSettings(formula="median_cvar", downside_aversion=1.5)
    scored = add_robust_components(_metrics(), prefs)
    row = scored.set_index("ticker").loc["LOTTERY"]
    assert row["robust_return"] == pytest.approx(0.18 - 1.5 * 0.30)


def test_high_variance_name_is_downweighted_in_robust_ranking_only() -> None:
    robust, upside = build_rankings(_metrics(), PREFS)
    upside_ranks = dict(zip(upside["ticker"], upside["rank"], strict=True))
    robust_ranks = dict(zip(robust["ticker"], robust["rank"], strict=True))
    # The lottery stock wins on expected return...
    assert upside_ranks["LOTTERY"] == 1
    # ...but the stable compounder wins after risk adjustment.
    assert robust_ranks["COMPOUND"] == 1
    assert robust_ranks["LOTTERY"] > robust_ranks["COMPOUND"]


def test_risk_preferences_change_the_ordering() -> None:
    # An investor with no downside aversion ranks on confidence-scaled excess:
    # the lottery stock's bigger excess wins once tail risk stops mattering.
    neutral = RiskPreferenceSettings(downside_aversion=0.0)
    robust, _ = build_rankings(_metrics(), neutral)
    assert robust.iloc[0]["ticker"] == "LOTTERY"


def test_empty_frame_is_handled() -> None:
    robust, upside = build_rankings(pd.DataFrame(), PREFS)
    assert robust.empty and upside.empty
