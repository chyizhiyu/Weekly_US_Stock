"""Funnel ledger: every universe ticker gets exactly one final disposition.

Guards the audit-trail invariant the sample e2e cannot exercise — in particular
that step-6 skips (incomplete valuation inputs), routed to the watchlist, are
accounted for and never left ``unaccounted``.
"""

from __future__ import annotations

import pandas as pd

from weekly_us_stock.reports.funnel import build_funnel_ledger


def _universe(tickers: list[str]) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "ticker": tickers,
            "name": [f"{t} Inc" for t in tickers],
            "sector": ["Tech"] * len(tickers),
            "industry": ["Software"] * len(tickers),
        }
    )


def test_funnel_accounts_for_every_universe_ticker() -> None:
    universe = _universe(["AAA", "BBB", "CCC", "DDD"])
    hard = pd.DataFrame(
        [{"ticker": "BBB", "rejection_reason": "market_cap",
          "all_rejection_reasons": "market_cap;liquidity"}]
    )
    norm = pd.DataFrame([{"ticker": "CCC", "rejection_reason": "insufficient_confidence"}])
    watchlist = pd.DataFrame(
        [{"ticker": "DDD", "watchlist_reason": "incomplete_valuation_inputs"}]
    )
    ranked = pd.DataFrame([{"ticker": "AAA", "rank": 1, "eligible": True}])

    ledger = build_funnel_ledger(universe, hard, norm, watchlist, ranked)

    assert len(ledger) == 4
    assert ledger["ticker"].nunique() == 4
    assert int((ledger["final_bucket"] == "unaccounted").sum()) == 0
    assert dict(zip(ledger["ticker"], ledger["final_bucket"], strict=True)) == {
        "AAA": "eligible",
        "BBB": "hard_filter_rejected",
        "CCC": "normalization_rejected",
        "DDD": "watchlist",
    }


def test_funnel_buckets_incomplete_input_skip_via_watchlist() -> None:
    universe = _universe(["SKIP"])
    empty = pd.DataFrame()
    watchlist = pd.DataFrame(
        [{"ticker": "SKIP", "watchlist_reason": "incomplete_valuation_inputs"}]
    )

    ledger = build_funnel_ledger(universe, empty, empty, watchlist, empty)

    row = ledger.iloc[0]
    assert row["final_bucket"] == "watchlist"
    assert row["decision_stage"] == "step6_valuation_inputs"
    assert row["decision_reason"] == "incomplete_valuation_inputs"
