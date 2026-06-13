"""Forward archiving for out-of-sample validation (P2-2).

Each run already exports its universe, eligibility splits, watchlists, scenario
assumptions and rankings under runs/YYYYMMDD/. This adds two things that make
the archive usable as a forward (paper-trading) record:

- a paper-portfolio snapshot: the eligible candidates frozen with their entry
  price and key metrics, so 1/3/6/12-month forward and excess returns, drawdown,
  hit rate and turnover can be computed later WITHOUT look-ahead - the entry was
  fixed with only point-in-time data;
- a run manifest tying the artifacts to the universe/config fingerprints, so a
  later validation can locate exactly what each run screened and decided.

No real trades are executed and no return is computed here: scenario weights
remain analyst-set, never calibrated probabilities, until enough archived runs
exist to test them out of sample.
"""

from __future__ import annotations

from datetime import date

import pandas as pd

_PORTFOLIO_COLUMNS = [
    "as_of",
    "ticker",
    "rank",
    "entry_price",
    "robust_return",
    "expected_irr",
    "median_irr",
    "p10_irr",
    "p90_irr",
    "business_quality",
    "evidence_confidence",
]

CALIBRATION_NOTE = (
    "Scenario weights are analyst-set, NOT calibrated probabilities. Out-of-sample "
    "validation requires accumulated archived runs (P2-2); do not report W(...) "
    "figures as calibrated until that forward history exists."
)


def build_paper_portfolio(eligible: pd.DataFrame, as_of: date) -> pd.DataFrame:
    """Equal-weight forward entry record for the eligible candidates."""

    if eligible.empty:
        return pd.DataFrame(columns=_PORTFOLIO_COLUMNS)
    rows = [
        {
            "as_of": as_of.isoformat(),
            "ticker": row.get("ticker"),
            "rank": row.get("rank"),
            "entry_price": row.get("price"),
            "robust_return": row.get("robust_return"),
            "expected_irr": row.get("expected_irr"),
            "median_irr": row.get("median_irr"),
            "p10_irr": row.get("p10_irr"),
            "p90_irr": row.get("p90_irr"),
            "business_quality": row.get("business_quality"),
            "evidence_confidence": row.get("evidence_confidence"),
        }
        for _, row in eligible.iterrows()
    ]
    return pd.DataFrame(rows, columns=_PORTFOLIO_COLUMNS)


def build_run_manifest(
    *,
    as_of: date,
    fingerprints: dict,
    counts: dict[str, int],
    artifacts: list[str],
    paper_portfolio_size: int,
) -> dict:
    """A self-describing index of one run's archive for forward validation."""

    return {
        "as_of": as_of.isoformat(),
        **fingerprints,
        "counts": counts,
        "paper_portfolio_size": paper_portfolio_size,
        "artifacts": sorted(set(artifacts)),
        "calibration_note": CALIBRATION_NOTE,
    }
