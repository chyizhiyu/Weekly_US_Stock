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
    eligible: pd.DataFrame,
    watchlist: pd.DataFrame,
    turnaround: pd.DataFrame,
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
    ]
    # P0-4: lead with eligible candidates only; never pad to Top N.
    if eligible.empty:
        lines += ["本周无达标候选（无个股满足：估值有限、robust_return>0、中位IRR>门槛）。"]
    else:
        lines += [f"达标候选 {len(eligible)} 只（估值有限、robust_return>0、中位IRR>门槛）:"]
        lines += _candidate_lines(eligible, top_n)
    lines += ["", f"Upside 研究队列 Top {top_n}（高分散度，仅研究、非可执行）:"]
    lines += _upside_lines(upside, top_n)

    lines += ["", _change_line(comparison)]

    if not watchlist.empty:
        reasons = watchlist["watchlist_reason"].value_counts().to_dict()
        reason_text = "、".join(
            f"{_reason_cn(reason)}{count}只" for reason, count in reasons.items()
        )
        lines += [f"观察名单：{len(watchlist)} 只（{reason_text}）"]
    if not turnaround.empty:
        names = "、".join(
            f"{r['ticker']}({r['status']})" for _, r in turnaround.head(8).iterrows()
        )
        lines += [f"重大事件反转观察：{len(turnaround)} 只 — {names}"]

    lines += [
        "",
        "说明：仅研究参考，不构成交易指令。排名来自 Bear/Base/Bull 三情景估值与风险调整回报；"
        "情景权重为人工设定（默认25/50/25），达标权重、永亏权重等是情景加权值，"
        "并非经过校准的概率。硬过滤不可补偿，数据缺失个股已剔除。",
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
            f"｜中位IRR {row['median_irr']:.1%}"
            f"｜P10 {row['p10_irr']:.1%}"
            f"｜门槛CVaR {row['hurdle_cvar']:.1%}"
            f"｜质量 {row['business_quality']:.2f}"
            f"｜置信 {row['evidence_confidence']:.2f}"
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
    if comparison.baseline_reset:
        return (
            f"对比基准已重置（{comparison.reset_reason}）：股票池或关键配置已变更，"
            "本周不做周环比,以免产生无意义的新进/退出。"
        )
    if not comparison.comparable:
        return "本周为首次运行，无上周对比。"
    entered = "、".join(comparison.robust_entered) or "无"
    exited = "、".join(comparison.robust_exited) or "无"
    return f"对比 {comparison.previous_as_of}：新进 {entered}；退出 {exited}。"


_REASON_CN = {
    "bank_model_not_supported": "银行",
    "insurance_model_not_supported": "保险",
    "reit_model_not_supported": "REIT",
    "asset_management_model_not_supported": "资产管理",
    "consumer_finance_model_not_supported": "消费信贷",
    "financial_sector_model_not_supported": "其他金融",
    "preprofit_biotech_not_supported": "未盈利生物科技",
    "insufficient_confidence": "数据置信度不足",
    "insufficient_model_confidence": "模型置信度不足",
    "insufficient_post_valuation_model_confidence": "估值后模型置信度不足",
    "incomplete_valuation_inputs": "估值输入缺失",
    "material_event_requires_reunderwriting": "重大事件待复核",
}


def _reason_cn(reason: str) -> str:
    return _REASON_CN.get(reason, reason)
