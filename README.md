# Weekly US Stock

美股周度自动筛选系统：每周六北京时间 08:00 扫描全美股市场（NYSE / Nasdaq / NYSE American），
经过四层决策结构生成风险调整后的候选股票排名，并通过 OpenClaw 将中文摘要发送到飞书。

> **本项目只负责筛选、研究和输出报告。不执行真实交易，不生成下单指令。**
> 筛选分数只用于缩小股票池；最终排名基于概率估值（Bear/Base/Bull）与风险调整回报，
> 而不是固定因子加权总分。

## 四层决策结构

1. **Layer 1 可投资性硬过滤（不可补偿）**：证券类型（剔除 ETF/ETN/基金/SPAC/权证/优先股/OTC，
   ADR 可配置）、上市年限 ≥3 年、市值与流动性、连续亏损与长期负 FCF、偿债能力、
   严重股权稀释、会计质量（OCF/净利润）、数据完整性——核心数据缺失一律 fail closed 剔除，禁止猜测。
2. **Layer 2 正常化经营模型**：全周期中位利润率正常化盈利（剔除一次性损益、SBC 计为真实费用）、
   ROIC / 增量 ROIC / WACC、净负债与利息覆盖、回购/分红/稀释、分析师预期分散度、周期性与盈利质量。
   银行/保险/REIT/未盈利生物科技路由到**观察名单**，不强行套用通用 DCF。
3. **Layer 3 概率估值**：每家公司 Bear/Base/Bull 三情景（收入增长、利润率、再投资 = g/ROIC、
   终值 = NOPAT×(1−g/ROIC_t)/(WACC−g)），输出预期 IRR、中位 IRR、P10/P90、P(IRR>hurdle)、
   永久亏损概率、Expected Shortfall (CVaR)、内在价值区间、模型/数据置信度。
   增量 ROIC ≤ WACC 时增长不创造价值（终值自动塌缩为 NOPAT/WACC）。
   护城河证据只影响回报持续期、利润率稳定性、情景宽度和模型置信度，不是加分项。
4. **Layer 4 风险调整排名**：同时输出两个榜单——
   - `upside_ranking.csv`：按预期 IRR 排名；
   - `robust_ranking.csv`：`robust_return = E[IRR] − downside_aversion×ES −
     ambiguity_aversion×模型不确定性 − permanent_loss_penalty×永久亏损概率`。
   三个风险参数代表投资人风险偏好，在 `config/default.yaml` 中配置，所有分项保留在输出中可审计。

## 本地运行

```bash
python -m pip install -e ".[dev]"

# 离线样本数据完整运行（无需任何密钥）
weekly-us-stock run --provider sample --as-of 2026-01-09

# 检查与测试
ruff check .
pytest

# 真实数据（需要 FMP key；Polygon/FRED 可选，缺失时自动降级并在报告中标注）
weekly-us-stock run --provider auto

# 打印本周应使用的数据日（最近一个已收盘的美国交易日，自动处理节假日与夏令时）
weekly-us-stock expected-as-of
```

每次运行输出到 `runs/YYYYMMDD/`：`universe.csv`、`hard_filter_candidates.csv`、
`hard_filter_rejected.csv`、`normalized_financials.csv`、`scenario_valuations.csv`、
`robust_ranking.csv`、`upside_ranking.csv`、`watchlist.csv`、`result.json`、
`dashboard.md`、`feishu_summary.md`、`run_metadata.json`。

## 数据源

| Provider | 用途 | 凭证 |
|---|---|---|
| FMP | 股票列表、财报、分析师预期、报价 | `FMP_API_KEY`（生产必需） |
| Polygon | 全市场日线（流动性/价格） | `POLYGON_API_KEY`（可选，缺失降级为 FMP 报价代理） |
| FRED | 无风险利率 DGS10 | `FRED_API_KEY`（可选，缺失用配置回退值） |
| SEC EDGAR | 财报抽样校验 | `SEC_USER_AGENT`（含联系方式的 UA 字符串） |
| Sample | 离线测试/CI | 无 |

所有数据带 `as_of` / `source` / `fetched_at` / `filing_date` 溯源字段；财报按
`filing_date <= as_of` 点时（point-in-time）过滤，历史回放不会泄漏未来数据。
降级情况写入 `run_metadata.json` 的 `degraded_sources` 并显示在报告中。

本地把密钥放在 `.env`（参考 `.env.example`），**不要提交真实密钥**。

## GitHub Actions

- `.github/workflows/ci.yml`：push/PR 时 `ruff check .` + `pytest` + 离线样本端到端冒烟。
- `.github/workflows/weekly_run.yml`：cron `0 0 * * 6`（UTC 周六 00:00 = 北京时间周六 08:00）。
  运行日期不是"当天"，而是用纽约交易日历解析的**最近一个已收盘交易日**（周五，或节假日时
  往前回退；夏令时/冬令时自动正确）。数据未就绪（价格覆盖率不足）时退出码 75，工作流自动
  等待重试，最终降级运行并在报告中说明。结果发布到 `weekly-us-stock-results` 分支：

```
weekly-us-stock-results/
├── latest/          # feishu_summary.md, dashboard.md, result.json, run_metadata.json, ...
└── history/YYYYMMDD/
```

仓库 Secrets：`FMP_API_KEY`（必需）、`POLYGON_API_KEY`、`FRED_API_KEY`、`SEC_USER_AGENT`（可选）。

## OpenClaw 飞书集成

OpenClaw 主机上每周六北京时间 08:05 执行：

```bash
cd /path/to/Weekly_US_Stock
git pull --ff-only origin main
WEEKLY_US_STOCK_TIMEOUT_SECONDS=7200 \
  scripts/openclaw_wait_for_scheduled_result.sh
```

`openclaw_wait_for_scheduled_result.sh` 轮询 `weekly-us-stock-results` 分支，
用 `weekly_us_stock.tools.verify_result_metadata`（纯标准库，无需安装依赖）校验
`latest/run_metadata.json` 的 `as_of` 等于本周期望交易日、`generated_at` 晚于本周六
00:00 UTC 调度窗口——**过期或错期的结果绝不会被发送**。校验通过后把
`latest/feishu_summary.md` 输出到 stdout，OpenClaw 将其原样回复到当前飞书会话；
失败时输出明确错误原因并以非零码退出。

`scripts/openclaw_trigger_actions.sh` 用一次性 tag（`weekly-us-stock-*`）手动触发
工作流并等待与该次提交精确匹配的结果。

飞书 Token 由 OpenClaw 自身管理，本仓库不存放任何密钥。

## 测试

`pytest` 覆盖：证券类型/市值/流动性过滤、数据缺失 fail closed、未来数据泄漏防护、
一次性收益剔除、周期峰值利润正常化、SBC 稀释与回购的每股价值方向、
增量 ROIC<WACC 的高成长不得高排名、高方差股票在 Robust 榜降权、
NYSE 节假日与夏令时、cron 时区、OpenClaw 过期结果拒发、样本数据离线端到端。

## 已知限制

- 银行/保险/REIT/未盈利生物科技暂无专用估值模型，进入观察名单（不强行排名）。
- 情景为离散三态；Monte Carlo 是计划扩展（聚合层已按通用分布实现）。
- FMP 财报无法干净拆分非经常性项目，`one_off_items` 在真实数据下为 0（正常化仍通过
  全周期中位利润率实现）；SEC Provider 提供抽样校验通道。
- 交易日历不含临时休市（如全国哀悼日），由数据新鲜度检查兜底。
- LLM 辅助（10-K 风险摘要等）尚未接入；接入时 LLM 不得生成财务数字、不得单独决定排名，
  输出必须带证据来源与置信度。
