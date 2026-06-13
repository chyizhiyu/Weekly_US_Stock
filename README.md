# Weekly US Stock

美股周度自动筛选系统：每周六北京时间 08:00，在 **S&P 500 与 Nasdaq-100 当前成分股的并集**
（默认股票池；`config/default.yaml` 的 `universe.index_membership` 置空 `[]` 时扫描全美股市场
NYSE / Nasdaq / NYSE American）中，经四层决策结构生成风险调整后的候选股票排名，并通过 OpenClaw
将中文摘要发送到飞书。目标不是扫描所有低价股，而是在高质量成分股中寻找**因暂时性问题或市场错价
而具备风险调整后回报潜力**的公司。

> **本项目只负责筛选、研究和输出报告。不执行真实交易，不生成下单指令。**
> 筛选分数只用于缩小股票池；最终排名基于概率估值（Bear/Base/Bull）与风险调整回报，
> 而不是固定因子加权总分。**"被排名"不等于"具备投资资格"**：报告首先展示满足最低门槛的
> 达标候选（不足则如实显示"本周无达标候选"，绝不凑数）。

## 四层决策结构

1. **Layer 1 可投资性硬过滤（不可补偿）**：证券类型（剔除 ETF/ETN/基金/SPAC/权证/优先股/OTC，
   ADR 可配置）、上市年限 ≥3 年、市值与流动性、**价格新鲜度**、连续亏损与长期负 FCF、偿债能力、
   严重股权稀释、会计质量（OCF/净利润）、数据完整性——核心数据缺失或报价陈旧一律 fail closed 剔除，禁止猜测。
2. **Layer 2 正常化经营模型**：年度全周期中位利润率正常化盈利（剔除一次性损益、SBC 计为真实费用），
   **TTM（最近四个已披露季度）作为当前锚点**——收入水平、当前利润率、当前流通股数、资本结构
   都来自 TTM，排名不滞后于最新季报。ROIC / 增量 ROIC / WACC、净负债与利息覆盖、
   回购/分红/稀释、分析师预期分散度、周期性与盈利质量。增量 ROIC 在资本基数收缩时标记为
   不可估计（绝不赋固定高值）。**整个金融板块**（银行/保险/REIT/资产管理/消费信贷/其他金融）
   及未盈利生物科技路由到**观察名单**，不强行套用通用 DCF。模型置信度低于阈值的个股同样进观察名单。
3. **Layer 3 情景估值**：每家公司 Bear/Base/Bull 三情景（收入增长、利润率、再投资 = g/ROIC、
   终值 = NOPAT×(1−g/ROIC_t)/(WACC−g)），输出预期 IRR、中位 IRR、P10/P90、达标权重、
   永久亏损权重、Expected Shortfall (CVaR)、内在价值区间、模型/数据置信度。
   **情景权重为人工设定（默认 25/50/25），不是校准概率**——所有 W(...) 指标是情景加权值，
   应当作压力标签阅读；概率校准（Monte Carlo + 滚动回测）在路线图中。
   增量 ROIC ≤ WACC 时增长不创造价值（终值自动塌缩为 NOPAT/WACC）。
   护城河证据只影响回报持续期、利润率稳定性、情景宽度和模型置信度，不是加分项。
4. **Layer 4 风险调整排名**：同时输出两个榜单——
   - `upside_ranking.csv`：按预期 IRR 排名；
   - `robust_ranking.csv`：默认 `formula: hurdle_cvar`——
     `robust_return = 数据置信×模型置信 × max(中位IRR − hurdle, 0) −
     downside_aversion × 门槛相对CVaR`，其中门槛相对 CVaR = 最差情景尾部的
     `max(0, hurdle − IRR)` 均值（Bear 赚 7% 但门槛 12% 仍计 5 个点的缺口）；
     单一下行惩罚，不重复扣减。可切换 `penalized_expected`（原任务书三项分解）
     或 `median_cvar`。
   每只股票同时给出三个独立维度（绝不压缩成单一总分）：
   **Business Quality**（financial_persistence_score，历史财务持续性）、
   **Valuation**（中位 IRR 相对门槛的超额）、**Evidence Confidence**（数据×模型置信度）。
   风险参数代表投资人风险偏好，在 `config/default.yaml` 中配置，所有分项保留在输出中可审计。

**重大事件闸门**：单周下跌 ≥25% 或距 60 日高点回撤 ≥40% 的个股（核心合同丢失、
指引下调、监管冲击在价格上的影子）自动移入 `material_event_requires_reunderwriting`
事件观察名单——价格已反映坏消息而财报还没有时，绝不按事件前的盈利能力排名。
**时间一致性**：`run_metadata.json` 的 `time_consistency` 块记录 price_as_of、
estimate_as_of、财报年龄（中位/最大）、TTM 锚定覆盖率、事件检查时间；财报超过
150 天或缺少 TTM 窗口的个股数据置信度自动下调。
**重复经济实体**：GOOG/GOOGL、BRK-A/B 等多股权类别只保留流动性最高的一条。

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

每次运行输出到 `runs/YYYYMMDD/`。报告明确区分以下受众，绝不混为一榜：

| 文件 | 含义 |
|---|---|
| `eligible_candidates.csv` | **达标候选**：估值有限、`robust_return>0`、`median_irr>门槛`（可配更严：p10、达标权重等）。报告首先展示这一组 |
| `robust_ranking.csv` | 完整 Robust 排名（含不达标名，带 `eligible` 标记，供研究/审计） |
| `upside_ranking.csv` / `research_queue.csv` | **高分散度研究队列**，明确标注"仅研究、非可执行" |
| `turnaround_watchlist.csv` | 重大事件反转观察名单（状态机 + 重新进入排名所需证据） |
| `invalid_or_watchlist.csv` | 不支持模型的行业 / 数据或估值异常 / 重大事件，统一观察名单 |
| `invalid_valuations.csv` | 非有限或求解边界饱和的估值（fail closed 剔除，附原因） |
| `roic_routed.csv` | ROIC 无经济意义（负投入资本等），待专用模型 |
| `paper_portfolio.csv` | 前向纸面组合入场快照（点时入场价，供未来样本外验证） |
| `run_manifest.json` / `run_metadata.json` | 自描述归档：股票池/配置指纹、各类计数、产物清单 |

另有 `hard_filter_candidates.csv`、`normalized_financials.csv`、`scenario_valuations.csv`、
`dashboard.md`、`feishu_summary.md`、`result.json` 等。

## 数据源

| Provider | 用途 | 凭证 |
|---|---|---|
| FMP（stable API） | 股票列表（company-screener + profile-bulk）、财报、分析师预期、全市场日线（batch-eod）、无风险利率（treasury-rates） | `FMP_API_KEY`（生产必需，仅此一个即可完整运行） |
| Polygon | 日线的可选替代源 | `POLYGON_API_KEY`（可选；缺失时用 FMP batch-eod，等价数据不算降级） |
| FRED | 无风险利率的可选替代源 | `FRED_API_KEY`（可选；缺失时用 FMP treasury-rates） |
| SEC EDGAR | 财报抽样校验 | `SEC_USER_AGENT`（含联系方式的 UA 字符串） |
| Sample | 离线测试/CI | 无 |

注意：2025-08-31 后注册的 FMP 账号只能使用 stable API（`/stable/...`），本项目即按此实现；
旧版 `/api/v3` 端点对新账号返回 403 Legacy Endpoint。

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
  scripts/openclaw_trigger_actions.sh
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

## 安全与诚实性边界

- **生产 fail closed**：`auto`/`fmp` 模式缺少凭证直接报错退出（退出码 78），绝不静默
  切换到样本数据发布；样本 Provider 只能显式指定。
- **指数股票池 fail closed**：配置了 `index_membership` 时，成分集合为空、任一指数接口
  失败、或成分数量低于下限，都会以 `IndexUniverseUnavailable`（退出码 78）中止，绝不静默
  退回全市场。股票池与全市场 ticker 经统一规范化匹配（`BRK.B`/`BRK-B` 等不会被漏掉），
  无法匹配的成分会被记录。
- **指数成分是当前快照，不能直接用于历史回放**：`sp500-constituent`/`nasdaq-constituent`
  返回的是**当前**成分，用它回测过去会引入幸存者偏差（漏掉后来退市/剔除的票）。**历史回测
  必须使用已归档的点时（point-in-time）成分集合**——每次运行的成分、配置指纹、资格结果与
  排名都归档在 `runs/YYYYMMDD/`（`run_manifest.json` + `paper_portfolio.csv`），供前向样本外
  验证；在积累足够历史前，情景权重只是人工设定的压力标签，**不是校准概率**。
- **历史回放防泄漏**：FMP 的股票列表与分析师预期是当前快照，请求 7 天前的 `as_of`
  会被 `PointInTimeUnavailable` 拒绝——回测必须使用有历史快照的数据源，否则就是
  未来数据泄漏 + 幸存者偏差。
- **估值结果 fail closed**：非有限值（NaN/Infinity）或 IRR 触及求解上下界（200% / -95%）的
  估值不进入任何榜单，改入观察名单并附原因；负/无意义 ROIC 不再被静默当作 +2% 估值。
- 价格陈旧（>3 个交易日）个股被硬过滤剔除，不参与排名。

## 已知限制与路线图

- 金融板块（含资产管理、消费信贷）暂无专用估值模型，全部进观察名单；
  **路线图**：分别实现银行（超额股本回报）、保险、REIT（FFO）、资管/信贷模型。
- 情景为离散三态、权重人工设定；**路线图**：Monte Carlo 联合抽样（增长/利润率/ROIC/WACC/稀释，
  保留相关性）、按确定性等价回报排名、滚动回测做概率校准（Top decile 收益、最大回撤、换手率）。
- `financial_persistence_score`（刻意不叫护城河分）只衡量历史财务持续性，识别不了
  监管变化、技术替代、客户集中度等结构性威胁——重大事件闸门用价格冲击兜底；
  **路线图**：结构性护城河独立证据项（市占率、留存率、定价权、竞争进入、监管依赖、
  转换成本、网络效应），每项带 score/evidence_source/evidence_date/failure_condition
  和否决机制（如核心客户丢失 → 直接 challenged 进观察名单）；8-K/新闻接入让事件闸门
  超越价格代理。
- FMP 财报无法干净拆分非经常性项目，`one_off_items` 在真实数据下为 0（正常化仍通过
  全周期中位利润率实现）；**路线图**：SEC Company Facts 接入生产做多源交叉校验，
  校验失败降低数据置信度。
- 双重股权类别（GOOG/GOOGL、BRK-A/B）目前各自独立出现在榜单/观察名单中，未做合并。
- 交易日历不含临时休市（如全国哀悼日），由数据新鲜度检查兜底。
- LLM 辅助（10-K 风险摘要等）尚未接入；接入时 LLM 不得生成财务数字、不得单独决定排名，
  输出必须带证据来源与置信度。
