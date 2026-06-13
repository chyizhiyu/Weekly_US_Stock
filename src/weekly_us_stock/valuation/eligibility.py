"""Eligibility gate (P0-4): separate 'ranked' from 'worth acting on'.

The robust ranking is a full, auditable ordering. Being ranked does not mean a
name clears the minimum investment bar - filling 20 slots with negative
robust-return names reads as "20 buys". This module flags each ranked name as
eligible or not, with a per-name list of failed rules, and splits out a
research queue (ranked but sub-bar / high-dispersion) so reports never pad.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from weekly_us_stock.config import EligibilitySettings


@dataclass(slots=True)
class EligibilityResult:
    ranked: pd.DataFrame  # all valid ranked names + `eligible` / `ineligible_reasons`
    eligible: pd.DataFrame  # clears every configured rule (actionable)
    research_queue: pd.DataFrame  # ranked but not eligible, expected-IRR sorted


def classify_eligibility(
    robust: pd.DataFrame, settings: EligibilitySettings
) -> EligibilityResult:
    if robust.empty:
        frame = robust.copy()
        frame["eligible"] = pd.Series(dtype=bool)
        frame["ineligible_reasons"] = pd.Series(dtype=str)
        return EligibilityResult(frame, frame, frame)

    frame = robust.copy()
    reasons: list[list[str]] = [[] for _ in range(len(frame))]

    def _fail(violated: pd.Series, label: str) -> None:
        for position, bad in enumerate(violated.to_numpy()):
            if bool(bad):
                reasons[position].append(label)

    if settings.require_robust_return_positive:
        _fail(~(frame["robust_return"] > 0), "robust_return<=0")
    if settings.require_median_above_hurdle:
        _fail(~(frame["median_irr"] > frame["hurdle_rate"]), "median_irr<=hurdle")
    if settings.min_p10_irr is not None:
        _fail(~(frame["p10_irr"] >= settings.min_p10_irr), f"p10_irr<{settings.min_p10_irr}")
    if settings.min_above_hurdle_weight is not None:
        _fail(
            ~(frame["above_hurdle_weight"] >= settings.min_above_hurdle_weight),
            f"above_hurdle_weight<{settings.min_above_hurdle_weight}",
        )
    if settings.max_model_uncertainty is not None:
        _fail(
            ~(frame["model_uncertainty"] <= settings.max_model_uncertainty),
            f"model_uncertainty>{settings.max_model_uncertainty}",
        )
    if settings.min_evidence_confidence is not None:
        _fail(
            ~(frame["evidence_confidence"] >= settings.min_evidence_confidence),
            f"evidence_confidence<{settings.min_evidence_confidence}",
        )

    frame["ineligible_reasons"] = ["; ".join(items) for items in reasons]
    frame["eligible"] = frame["ineligible_reasons"] == ""

    eligible = frame.loc[frame["eligible"]].reset_index(drop=True)
    research = frame.loc[~frame["eligible"]].copy()
    if "expected_irr" in research.columns:
        research = research.sort_values("expected_irr", ascending=False)
    research = research.reset_index(drop=True)
    return EligibilityResult(ranked=frame, eligible=eligible, research_queue=research)
