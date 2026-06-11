"""简洁中文飞书摘要。OpenClaw 把这个文件原样回贴到飞书会话。"""

from __future__ import annotations

from collections.abc import Sequence

import pandas as pd

from weekly_us_stock.models.screening import DataFreshness, PipelineRequest, StepSummary
from weekly_us_stock.reports.compare import WeekOverWeek


def build_feishu_summary(
    request: PipelineRequest,
    steps: Sequence[StepSummary],
    robust: pd.DataFrame,
    upside: pd.DataFrame,
    watchlist: pd.DataFrame,
    comparison: WeekOverWeek,
    freshness: DataFreshness,
    top_n: int = 10,
) -> str:
    universe_count = steps[0].output_count if steps else 0
    funnel = " → ".join(str(step.output_count) for step in steps)

    lines = [
        f"美股周度筛选｜数据日 {request.as_of}",
        f"扫描 {universe_count} 只，漏斗：{funnel}",
        _coverage_line(freshness),
        "",
        f"Robust Top {top_n}（风险调整后）:",
    ]
    lines += _candidate_lines(robust, top_n)
    lines += ["", f"Upside Top {top_n}（预期回报）:"]
    lines += _upside_lines(upside, top_n)

    lines += ["", _change_line(comparison)]

    if not watchlist.empty:
        reasons = watchlist["watchlist_reason"].value_counts().to_dict()
        reason_text = "、".join(
            f"{_reason_cn(reason)}{count}只" for reason, count in reasons.items()
        )
        lines += [f"观察名单：{len(watchlist)} 只（{reason_text}）"]

    lines += [
        "",
        "说明：仅研究参考，不构成交易指令。排名来自 Bear/Base/Bull 概率估值与风险调整回报，"
        "硬过滤不可补偿，数据缺失个股已剔除。",
    ]
    return "\n".join(lines) + "\n"


def _coverage_line(freshness: DataFreshness) -> str:
    text = (
        f"数据覆盖：价格新鲜度 {freshness.fresh_price_coverage:.0%}"
        f"（陈旧 {freshness.stale_tickers} 只）"
    )
    if freshness.degraded_sources:
        text += f"；降级数据源 {len(freshness.degraded_sources)} 项"
    return text


def _candidate_lines(robust: pd.DataFrame, top_n: int) -> list[str]:
    if robust.empty:
        return ["- 无入选标的"]
    lines = []
    for _, row in robust.head(top_n).iterrows():
        lines.append(
            f"{int(row['rank'])}. {row['ticker']}"
            f"｜预期IRR {row['expected_irr']:.1%}"
            f"｜P10 {row['p10_irr']:.1%}"
            f"｜达标P {row['prob_above_hurdle']:.0%}"
            f"｜永久亏损P {row['permanent_loss_probability']:.0%}"
        )
    return lines


def _upside_lines(upside: pd.DataFrame, top_n: int) -> list[str]:
    if upside.empty:
        return ["- 无入选标的"]
    lines = []
    for _, row in upside.head(top_n).iterrows():
        lines.append(
            f"{int(row['rank'])}. {row['ticker']}"
            f"｜预期IRR {row['expected_irr']:.1%}"
            f"｜中位 {row['median_irr']:.1%}"
            f"｜P10 {row['p10_irr']:.1%} / P90 {row['p90_irr']:.1%}"
        )
    return lines


def _change_line(comparison: WeekOverWeek) -> str:
    if not comparison.has_previous:
        return "本周为首次运行，无上周对比。"
    entered = "、".join(comparison.robust_entered) or "无"
    exited = "、".join(comparison.robust_exited) or "无"
    return f"对比 {comparison.previous_as_of}：新进 {entered}；退出 {exited}。"


_REASON_CN = {
    "bank_model_not_supported": "银行",
    "insurance_model_not_supported": "保险",
    "reit_model_not_supported": "REIT",
    "preprofit_biotech_not_supported": "未盈利生物科技",
    "insufficient_confidence": "数据置信度不足",
}


def _reason_cn(reason: str) -> str:
    return _REASON_CN.get(reason, reason)
