"""Layer-4 risk-adjusted ranking: penalties are preferences, not factor weights."""

from __future__ import annotations

import pandas as pd
import pytest

from weekly_us_stock.config import RiskPreferenceSettings
from weekly_us_stock.valuation.ranking import add_robust_components, build_rankings

PREFS = RiskPreferenceSettings()


def _metrics() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                # Steady compounder: decent IRR, almost no tail risk.
                "ticker": "COMPOUND",
                "expected_irr": 0.13,
                "median_irr": 0.13,
                "expected_shortfall": 0.00,
                "model_uncertainty": 0.05,
                "permanent_loss_probability": 0.0,
            },
            {
                # Lottery ticket: higher expected IRR, fat left tail, wide range.
                "ticker": "LOTTERY",
                "expected_irr": 0.20,
                "median_irr": 0.18,
                "expected_shortfall": 0.30,
                "model_uncertainty": 0.30,
                "permanent_loss_probability": 0.25,
            },
        ]
    )


def test_robust_return_formula_is_transparent() -> None:
    scored = add_robust_components(_metrics(), PREFS)
    row = scored.set_index("ticker").loc["LOTTERY"]
    expected = (
        0.20
        - PREFS.downside_aversion * 0.30
        - PREFS.ambiguity_aversion * 0.30
        - PREFS.permanent_loss_penalty * 0.25
    )
    assert row["robust_return"] == pytest.approx(expected)
    # Every penalty stays visible in the output: no opaque composite score.
    for column in ["downside_penalty", "ambiguity_penalty", "permanent_loss_penalty"]:
        assert column in scored.columns


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
    # An investor with no downside aversion ranks purely on expected return.
    neutral = RiskPreferenceSettings(
        downside_aversion=0.0, ambiguity_aversion=0.0, permanent_loss_penalty=0.0
    )
    robust, _ = build_rankings(_metrics(), neutral)
    assert robust.iloc[0]["ticker"] == "LOTTERY"


def test_empty_frame_is_handled() -> None:
    robust, upside = build_rankings(pd.DataFrame(), PREFS)
    assert robust.empty and upside.empty
