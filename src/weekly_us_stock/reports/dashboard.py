"""Full markdown dashboard for each weekly run."""

from __future__ import annotations

from collections.abc import Sequence

import pandas as pd

from weekly_us_stock.models.screening import DataFreshness, PipelineRequest, StepSummary
from weekly_us_stock.reports.compare import WeekOverWeek


def build_dashboard(
    request: PipelineRequest,
    steps: Sequence[StepSummary],
    robust: pd.DataFrame,
    upside: pd.DataFrame,
    scenarios: pd.DataFrame,
    watchlist: pd.DataFrame,
    comparison: WeekOverWeek,
    freshness: DataFreshness,
    top_n: int,
) -> str:
    lines: list[str] = [
        f"# Weekly US Stock Screen — {request.as_of}",
        "",
        "Research output only. No trading instructions are generated. Screening",
        "scores only narrow the pool; final ordering comes from probabilistic",
        "valuation and risk-adjusted return, never from fixed factor weights.",
        "",
        "## Data Freshness",
        "",
        f"- Expected market data date: **{freshness.expected_as_of}**",
        f"- Fresh price coverage: **{freshness.fresh_price_coverage:.1%}**"
        f" ({freshness.stale_tickers} stale tickers)",
    ]
    if freshness.degraded_sources:
        lines.append("- Degraded sources: " + ", ".join(freshness.degraded_sources))
    for note in freshness.notes:
        lines.append(f"- {note}")

    lines += [
        "",
        "## Funnel",
        "",
        "| Step | Input | Output | Top rejections |",
        "|---|---|---|---|",
    ]
    for step in steps:
        top_reasons = ", ".join(
            f"{reason}: {count}"
            for reason, count in sorted(
                step.rejection_counts.items(), key=lambda item: -item[1]
            )[:3]
        )
        lines.append(
            f"| {step.name} | {step.input_count} | {step.output_count} | {top_reasons or '-'} |"
        )

    lines += _ranking_section("Robust Top 20 (risk-adjusted)", robust, top_n, robust_columns=True)
    lines += _ranking_section("Upside Top 20 (expected IRR)", upside, top_n, robust_columns=False)

    lines += ["", "## Week-over-week"]
    if comparison.has_previous:
        lines += [
            "",
            f"Previous run: {comparison.previous_as_of}",
            "",
            f"- Entered Robust Top: {_fmt_list(comparison.robust_entered)}",
            f"- Exited Robust Top: {_fmt_list(comparison.robust_exited)}",
            f"- Entered Upside Top: {_fmt_list(comparison.upside_entered)}",
            f"- Exited Upside Top: {_fmt_list(comparison.upside_exited)}",
        ]
        movers = _top_movers(comparison.robust_rank_changes)
        if movers:
            lines += ["", "Largest robust-rank moves:", ""]
            lines += [f"- {line}" for line in movers]
    else:
        lines += ["", "First tracked run — no previous ranking to compare against."]

    lines += _scenario_section(robust, scenarios, top_n)

    lines += ["", "## Key Risks and Failure Conditions", ""]
    risk_lines = _risk_lines(robust, top_n)
    lines += risk_lines if risk_lines else ["- No flagged risks among ranked names."]

    lines += ["", "## Watchlist (not rankable under the general model)", ""]
    if watchlist.empty:
        lines.append("- Empty.")
    else:
        for _, row in watchlist.iterrows():
            lines.append(
                f"- {row.get('ticker')} {row.get('name', '')} — {row.get('watchlist_reason')}"
            )

    lines += [
        "",
        "## Data Gaps and Model Limitations",
        "",
        "- Stocks missing core financials were rejected (fail closed), never estimated.",
        "- Banks, insurers, REITs and pre-profit biotech are watchlisted: the general",
        "  owner-earnings DCF does not apply and no substitute model is forced on them.",
        "- Scenario set is discrete (bear/base/bull); a Monte Carlo layer is a planned",
        "  extension and the aggregation already operates on generic distributions.",
        "- Ad-hoc market closures are not in the calendar; freshness checks catch them.",
    ]
    return "\n".join(lines) + "\n"


def _ranking_section(
    title: str, frame: pd.DataFrame, top_n: int, *, robust_columns: bool
) -> list[str]:
    lines = ["", f"## {title}", ""]
    if frame.empty:
        return lines + ["- No candidates survived to ranking."]
    if robust_columns:
        lines += [
            "| # | Ticker | Robust | E[IRR] | P10 | P90 | P(IRR>hurdle) | ES "
            "| P(perm loss) | Conf (model/data) |",
            "|---|---|---|---|---|---|---|---|---|---|",
        ]
    else:
        lines += [
            "| # | Ticker | E[IRR] | Median | P10 | P90 | P(IRR>hurdle) | Upside to base |",
            "|---|---|---|---|---|---|---|---|",
        ]
    for _, row in frame.head(top_n).iterrows():
        if robust_columns:
            lines.append(
                f"| {int(row['rank'])} | {row['ticker']} | {row['robust_return']:.1%} "
                f"| {row['expected_irr']:.1%} | {row['p10_irr']:.1%} | {row['p90_irr']:.1%} "
                f"| {row['prob_above_hurdle']:.0%} | {row['expected_shortfall']:.1%} "
                f"| {row['permanent_loss_probability']:.0%} "
                f"| {row['model_confidence']:.2f}/{row['data_confidence']:.2f} |"
            )
        else:
            upside = row.get("upside_to_base")
            upside_text = f"{upside:.0%}" if pd.notna(upside) else "-"
            lines.append(
                f"| {int(row['rank'])} | {row['ticker']} | {row['expected_irr']:.1%} "
                f"| {row['median_irr']:.1%} | {row['p10_irr']:.1%} | {row['p90_irr']:.1%} "
                f"| {row['prob_above_hurdle']:.0%} | {upside_text} |"
            )
    return lines


def _scenario_section(robust: pd.DataFrame, scenarios: pd.DataFrame, top_n: int) -> list[str]:
    lines = ["", "## Scenarios for Ranked Names (Bear / Base / Bull)", ""]
    if robust.empty or scenarios.empty:
        return lines + ["- No scenario output."]
    lines += [
        "| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share "
        "| IRR 5y | Return 5y |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    ranked = robust.head(top_n)["ticker"].tolist()
    indexed = scenarios.set_index("ticker", drop=False)
    for ticker in ranked:
        rows = indexed.loc[[ticker]] if ticker in indexed.index else pd.DataFrame()
        for _, row in rows.iterrows():
            irr = row.get("irr_5y")
            irr_text = f"{irr:.1%}" if pd.notna(irr) else "n/a"
            lines.append(
                f"| {ticker} | {row['scenario']} | {row['probability']:.0%} "
                f"| {row['revenue_growth_y1']:.1%} | {row['operating_margin']:.1%} "
                f"| {row['terminal_roic']:.1%} | {row['intrinsic_value_per_share']:.2f} "
                f"| {irr_text} | {row['total_return_5y']:.0%} |"
            )
    return lines


def _risk_lines(robust: pd.DataFrame, top_n: int) -> list[str]:
    lines = []
    if robust.empty or "risk_flags" not in robust:
        return lines
    for _, row in robust.head(top_n).iterrows():
        flags = str(row.get("risk_flags") or "").strip()
        if flags:
            lines.append(f"- {row['ticker']}: {flags.replace(';', ', ')}")
    return lines


def _top_movers(changes: pd.DataFrame, limit: int = 5) -> list[str]:
    if changes.empty or "rank_change" not in changes:
        return []
    movers = changes.dropna(subset=["rank_change"]).copy()
    movers = movers.loc[movers["rank_change"] != 0]
    if movers.empty:
        return []
    movers["abs_change"] = movers["rank_change"].abs()
    movers = movers.sort_values("abs_change", ascending=False).head(limit)
    return [
        f"{row['ticker']}: {int(row['previous_rank'])} → {int(row['rank'])}"
        f" ({'+' if row['rank_change'] > 0 else ''}{int(row['rank_change'])})"
        for _, row in movers.iterrows()
    ]


def _fmt_list(values: list[str]) -> str:
    return ", ".join(values) if values else "none"
