# Weekly US Stock Screen — 2026-07-17

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-07-17**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 515 | - |
| step2_hard_filters | 515 | 308 | adr_excluded: 33, persistent_negative_fcf: 22, interest_coverage: 19 |
| step3_standardize | 308 | 308 | - |
| step4_specialist_models | 92 | 58 | asset_management_model_not_supported: 16, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 308 | 301 | no_normalized_earnings: 7 |
| step5_quality_risk | 301 | 293 | - |
| step6_scenario_valuation | 293 | 266 | insufficient_post_valuation_model_confidence: 19, roic_not_meaningful:meaningless_capital: 6, irr_below_solver_bound: 1 |
| step7_risk_adjusted_ranking | 324 | 324 | - |

## Eligible Candidates (11)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 14.9% | 31.4% | 14.0% | 41.2% | 0.0% | 0% | 0.78 | 0.77 |
| 2 | FOXA | 10.6% | 29.4% | 10.7% | 39.3% | 1.3% | 0% | 0.90 | 0.68 |
| 3 | VICI | 9.7% | 32.2% | 14.5% | 32.2% | 0.0% | 0% | 0.49 | 0.48 |
| 4 | CTSH | 9.0% | 22.3% | 12.7% | 28.5% | 0.0% | 0% | 0.87 | 0.87 |
| 5 | OMC | 7.2% | 24.4% | 15.4% | 30.7% | 0.0% | 0% | 0.80 | 0.58 |
| 6 | ARE | 7.1% | 26.8% | 17.3% | 26.8% | 0.0% | 0% | 0.68 | 0.48 |
| 7 | TTD | 6.9% | 27.8% | 7.6% | 36.1% | 4.4% | 0% | 0.91 | 0.71 |
| 8 | CMCSA | 3.0% | 18.4% | 14.9% | 23.7% | 0.0% | 0% | 0.76 | 0.46 |
| 9 | BXP | 2.8% | 20.8% | 10.5% | 20.8% | 1.5% | 0% | 0.64 | 0.48 |
| 10 | CPT | 2.6% | 23.1% | 9.2% | 23.1% | 2.8% | 0% | 0.55 | 0.48 |
| 11 | ELV | 1.5% | 14.3% | 12.2% | 20.5% | 0.0% | 0% | 0.83 | 0.67 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 14.9% | 31.4% | 14.0% | 41.2% | 0.0% | 0% | 0.78 | 0.77 |
| 2 | FOXA | 10.6% | 29.4% | 10.7% | 39.3% | 1.3% | 0% | 0.90 | 0.68 |
| 3 | VICI | 9.7% | 32.2% | 14.5% | 32.2% | 0.0% | 0% | 0.49 | 0.48 |
| 4 | CTSH | 9.0% | 22.3% | 12.7% | 28.5% | 0.0% | 0% | 0.87 | 0.87 |
| 5 | OMC | 7.2% | 24.4% | 15.4% | 30.7% | 0.0% | 0% | 0.80 | 0.58 |
| 6 | ARE | 7.1% | 26.8% | 17.3% | 26.8% | 0.0% | 0% | 0.68 | 0.48 |
| 7 | TTD | 6.9% | 27.8% | 7.6% | 36.1% | 4.4% | 0% | 0.91 | 0.71 |
| 8 | CMCSA | 3.0% | 18.4% | 14.9% | 23.7% | 0.0% | 0% | 0.76 | 0.46 |
| 9 | BXP | 2.8% | 20.8% | 10.5% | 20.8% | 1.5% | 0% | 0.64 | 0.48 |
| 10 | CPT | 2.6% | 23.1% | 9.2% | 23.1% | 2.8% | 0% | 0.55 | 0.48 |
| 11 | ELV | 1.5% | 14.3% | 12.2% | 20.5% | 0.0% | 0% | 0.83 | 0.67 |
| 12 | AVB | -0.7% | 21.0% | 7.0% | 21.0% | 5.0% | 0% | 0.54 | 0.48 |
| 13 | UDR | -1.9% | 21.6% | 5.5% | 21.6% | 6.5% | 0% | 0.49 | 0.48 |
| 14 | ZTS | -2.7% | 17.5% | 4.3% | 24.8% | 7.7% | 0% | 0.98 | 0.90 |
| 15 | CPAY | -4.0% | 16.9% | 3.9% | 24.2% | 8.1% | 0% | 0.99 | 0.84 |
| 16 | HPQ | -4.7% | 7.3% | 7.3% | 12.4% | 4.7% | 0% | 0.97 | 0.67 |
| 17 | EQR | -5.1% | 16.1% | 4.9% | 23.7% | 7.1% | 0% | 0.60 | 0.48 |
| 18 | HUM | -5.6% | 15.4% | 4.3% | 23.9% | 7.7% | 0% | 0.66 | 0.60 |
| 19 | HST | -6.8% | 13.5% | 4.5% | 13.5% | 7.5% | 0% | 0.66 | 0.48 |
| 20 | INVH | -7.0% | 15.6% | 3.3% | 15.6% | 8.7% | 0% | 0.57 | 0.48 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | UHS | 29.5% | 31.4% | 14.0% | 41.2% | 100% | 119% |
| 2 | VICI | 27.8% | 32.2% | 14.5% | 32.2% | 100% | 304% |
| 3 | FOXA | 27.2% | 29.4% | 10.7% | 39.3% | 75% | 126% |
| 4 | TTD | 24.8% | 27.8% | 7.6% | 36.1% | 75% | 96% |
| 5 | ARE | 24.4% | 26.8% | 17.3% | 26.8% | 100% | 227% |
| 6 | OMC | 23.7% | 24.4% | 15.4% | 30.7% | 100% | 121% |
| 7 | FISV | 22.2% | 30.2% | -25.0% | 53.4% | 75% | 135% |
| 8 | EOG | 21.6% | 23.4% | -3.5% | 43.0% | 75% | 96% |
| 9 | CTSH | 21.5% | 22.3% | 12.7% | 28.5% | 100% | 65% |
| 10 | CPT | 19.7% | 23.1% | 9.2% | 23.1% | 75% | 183% |
| 11 | CMCSA | 18.9% | 18.4% | 14.9% | 23.7% | 100% | 64% |
| 12 | BXP | 18.3% | 20.8% | 10.5% | 20.8% | 75% | 158% |
| 13 | LDOS | 17.7% | 20.8% | -4.6% | 33.7% | 75% | 74% |
| 14 | UDR | 17.6% | 21.6% | 5.5% | 21.6% | 75% | 165% |
| 15 | AVB | 17.5% | 21.0% | 7.0% | 21.0% | 75% | 159% |
| 16 | IT | 16.1% | 17.9% | -0.8% | 29.4% | 75% | 40% |
| 17 | ZTS | 16.0% | 17.5% | 4.3% | 24.8% | 75% | 44% |
| 18 | CPAY | 15.5% | 16.9% | 3.9% | 24.2% | 75% | 42% |
| 19 | ELV | 15.3% | 14.3% | 12.2% | 20.5% | 100% | 41% |
| 20 | GIS | 15.3% | 17.3% | -0.1% | 26.5% | 75% | 50% |

## Week-over-week

Previous run: 2026-07-10

- Entered Robust Top: HST, INVH
- Exited Robust Top: ACN, IT
- Entered Upside Top: ELV, ZTS
- Exited Upside Top: ACN, APA

Largest robust-rank moves:

- ABT: 183 → 141 (+42)
- ATO: 289 → 315 (-26)
- ISRG: 187 → 166 (+21)
- CDW: 98 → 81 (+17)
- JBHT: 229 → 246 (-17)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| UHS | bear | 25% | 1.7% | 8.9% | 8.1% | 178.46 | 14.0% | 76% |
| UHS | base | 50% | 6.9% | 10.7% | 17.2% | 330.85 | 31.4% | 261% |
| UHS | bull | 25% | 11.0% | 12.1% | 19.6% | 467.86 | 41.2% | 420% |
| FOXA | bear | 25% | -1.0% | 17.5% | 6.7% | 66.99 | 10.7% | 57% |
| FOXA | base | 50% | 4.8% | 20.1% | 54.6% | 130.11 | 29.4% | 242% |
| FOXA | bull | 25% | 9.4% | 22.0% | 60.0% | 182.42 | 39.3% | 390% |
| CTSH | bear | 25% | -0.0% | 12.8% | 8.6% | 52.46 | 12.7% | 67% |
| CTSH | base | 50% | 4.8% | 15.0% | 14.2% | 73.89 | 22.3% | 156% |
| CTSH | bull | 25% | 8.7% | 16.6% | 15.0% | 92.75 | 28.5% | 229% |
| OMC | bear | 25% | 18.4% | 12.7% | 6.6% | 121.37 | 15.4% | 112% |
| OMC | base | 50% | 25.0% | 14.6% | 6.6% | 180.51 | 24.4% | 213% |
| OMC | bull | 25% | 30.3% | 15.9% | 6.6% | 234.06 | 30.7% | 304% |
| TTD | bear | 25% | 13.5% | 13.1% | 9.5% | 17.54 | 7.6% | 40% |
| TTD | base | 50% | 19.8% | 17.1% | 41.0% | 36.47 | 27.8% | 229% |
| TTD | bull | 25% | 24.8% | 20.7% | 44.1% | 48.29 | 36.1% | 344% |
| CMCSA | bear | 25% | -6.0% | 16.1% | 6.5% | 30.91 | 14.9% | 81% |
| CMCSA | base | 50% | 1.2% | 18.7% | 6.5% | 38.98 | 18.4% | 136% |
| CMCSA | bull | 25% | 6.9% | 20.4% | 6.5% | 52.21 | 23.7% | 218% |
| ELV | bear | 25% | -0.9% | 4.9% | 7.1% | 463.80 | 12.2% | 68% |
| ELV | base | 50% | 5.4% | 5.9% | 7.1% | 525.00 | 14.3% | 98% |
| ELV | bull | 25% | 10.4% | 6.6% | 7.1% | 686.96 | 20.5% | 159% |
| ZTS | bear | 25% | 1.0% | 32.2% | 7.5% | 65.11 | 4.3% | 20% |
| ZTS | base | 50% | 5.1% | 36.0% | 24.5% | 110.17 | 17.5% | 117% |
| ZTS | bull | 25% | 8.4% | 39.1% | 24.8% | 144.59 | 24.8% | 190% |
| CPAY | bear | 25% | 7.7% | 39.8% | 7.6% | 309.18 | 3.9% | 19% |
| CPAY | base | 50% | 13.3% | 44.0% | 30.0% | 520.90 | 16.9% | 115% |
| CPAY | bull | 25% | 17.9% | 47.4% | 30.3% | 686.54 | 24.2% | 189% |
| HPQ | bear | 25% | -3.6% | 5.7% | 9.1% | 23.96 | 9.1% | 44% |
| HPQ | base | 50% | 1.8% | 6.6% | 9.1% | 21.90 | 7.3% | 44% |
| HPQ | bull | 25% | 6.2% | 7.3% | 9.1% | 28.24 | 12.4% | 86% |
| HUM | bear | 25% | 12.4% | 2.5% | 7.8% | 342.31 | 4.3% | 24% |
| HUM | base | 50% | 19.0% | 3.7% | 7.8% | 567.58 | 15.4% | 106% |
| HUM | bull | 25% | 24.3% | 4.8% | 7.8% | 811.09 | 23.9% | 195% |

**Scenario order inversions** (named bear/base/bull intrinsic value is not monotone — this is economic, not a bug):
- HPQ: growth destroys value: forward ROIC 2.0% at/below WACC 9.1%, so higher-growth scenarios reinvest below the cost of capital and are worth less than the bear case

## Boundary Assumptions & Valuation Alerts

- UHS — bounds: share_change_floor_hit;intrinsic_2x_price
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit;intrinsic_2x_price
- VICI — bounds: specialist_model_v1
- OMC — bounds: base_growth_cap_hit;reinvestment_cap_hit;intrinsic_2x_price
- ARE — bounds: specialist_model_v1
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;wacc_floor_hit;reinvestment_cap_hit
- BXP — bounds: specialist_model_v1
- CPT — bounds: specialist_model_v1
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- AVB — bounds: specialist_model_v1
- UDR — bounds: specialist_model_v1
- HPQ — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- EQR — bounds: specialist_model_v1
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HST — bounds: specialist_model_v1
- INVH — bounds: specialist_model_v1

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| ORCL | drawdown_from_high | nan% | -49% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| IBM | weekly_drop | -27% | nan% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| CHTR | drawdown_from_high | nan% | -46% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| SMCI | drawdown_from_high | nan% | -49% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- VICI: nan
- OMC: incremental_roic_below_wacc
- ARE: nan
- TTD: heavy_sbc
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- BXP: nan
- CPT: nan
- ELV: incremental_roic_below_wacc
- AVB: nan
- UDR: nan
- CPAY: thin_interest_coverage
- HPQ: incremental_roic_below_wacc
- EQR: nan
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- HST: nan
- INVH: nan

## Watchlist (not rankable under the general model)

- V Visa Inc. — consumer_finance_model_not_supported
- MA Mastercard Incorporated — consumer_finance_model_not_supported
- MS Morgan Stanley — asset_management_model_not_supported
- GS The Goldman Sachs Group, Inc. — asset_management_model_not_supported
- AXP American Express Company — consumer_finance_model_not_supported
- SCHW The Charles Schwab Corporation — asset_management_model_not_supported
- BLK BlackRock, Inc. — asset_management_model_not_supported
- BX Blackstone Inc. — asset_management_model_not_supported
- SPGI S&P Global Inc. — financial_sector_model_not_supported
- COF Capital One Financial Corporation — consumer_finance_model_not_supported
- KKR KKR & Co. Inc. — asset_management_model_not_supported
- MCO Moody's Corporation — financial_sector_model_not_supported
- ICE Intercontinental Exchange, Inc. — financial_sector_model_not_supported
- APO Apollo Global Management, Inc. — asset_management_model_not_supported
- STT State Street Corporation — asset_management_model_not_supported
- AMP Ameriprise Financial, Inc. — asset_management_model_not_supported
- MSCI MSCI Inc. — financial_sector_model_not_supported
- ARES Ares Management Corporation — asset_management_model_not_supported
- RJF Raymond James Financial, Inc. — asset_management_model_not_supported
- SYF Synchrony Financial — consumer_finance_model_not_supported
- GPN Global Payments Inc. — consumer_finance_model_not_supported
- BEN Franklin Resources, Inc. — asset_management_model_not_supported
- IVZ Invesco Ltd. — asset_management_model_not_supported
- FDS FactSet Research Systems Inc. — financial_sector_model_not_supported
- HOOD Robinhood Markets, Inc. — asset_management_model_not_supported
- CME CME Group Inc. — financial_sector_model_not_supported
- NDAQ Nasdaq, Inc. — financial_sector_model_not_supported
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- ORCL Oracle Corporation — material_event_requires_reunderwriting
- IBM International Business Machines Corporation — material_event_requires_reunderwriting
- CHTR Charter Communications, Inc. — material_event_requires_reunderwriting
- SMCI Super Micro Computer, Inc. — material_event_requires_reunderwriting
- XOM Exxon Mobil Corporation — insufficient_model_confidence
- CVX Chevron Corporation — insufficient_model_confidence
- VLO Valero Energy Corporation — insufficient_model_confidence
- MPC Marathon Petroleum Corporation — insufficient_model_confidence
- PSX Phillips 66 — insufficient_model_confidence
- CCL Carnival Corporation & plc — insufficient_model_confidence
- MOS The Mosaic Company — insufficient_model_confidence
- TSLA Tesla, Inc. — insufficient_model_confidence
- GM General Motors Company — irr_below_solver_bound
- LHX L3Harris Technologies, Inc. — invalid_valuation_output
- BKNG Booking Holdings Inc. — roic_not_meaningful:meaningless_capital
- FTNT Fortinet, Inc. — roic_not_meaningful:meaningless_capital
- ABNB Airbnb, Inc. — roic_not_meaningful:meaningless_capital
- EXPE Expedia Group, Inc. — roic_not_meaningful:meaningless_capital
- VRSN VeriSign, Inc. — roic_not_meaningful:meaningless_capital
- CSGP CoStar Group, Inc. — roic_not_meaningful:meaningless_capital
- COP ConocoPhillips — insufficient_post_valuation_model_confidence
- FCX Freeport-McMoRan Inc. — insufficient_post_valuation_model_confidence
- RCL Royal Caribbean Cruises Ltd. — insufficient_post_valuation_model_confidence
- CI Cigna Corporation — insufficient_post_valuation_model_confidence
- TRGP Targa Resources Corp. — insufficient_post_valuation_model_confidence
- OXY Occidental Petroleum Corporation — insufficient_post_valuation_model_confidence
- NUE Nucor Corporation — insufficient_post_valuation_model_confidence
- XYZ Block, Inc. — insufficient_post_valuation_model_confidence
- IR Ingersoll Rand Inc. — insufficient_post_valuation_model_confidence
- DVN Devon Energy Corporation — insufficient_post_valuation_model_confidence
- IFF International Flavors & Fragrances Inc. — insufficient_post_valuation_model_confidence
- CF CF Industries Holdings, Inc. — insufficient_post_valuation_model_confidence
- BLDR Builders FirstSource, Inc. — insufficient_post_valuation_model_confidence
- NVDA NVIDIA Corporation — insufficient_post_valuation_model_confidence
- MU Micron Technology, Inc. — insufficient_post_valuation_model_confidence
- AMD Advanced Micro Devices, Inc. — insufficient_post_valuation_model_confidence
- APP AppLovin Corporation — insufficient_post_valuation_model_confidence
- STLD Steel Dynamics, Inc. — insufficient_post_valuation_model_confidence
- APA APA Corporation — insufficient_post_valuation_model_confidence

## Data Gaps and Model Limitations

- Stocks missing core financials were rejected (fail closed), never estimated.
- Banks, insurers and REITs use conservative specialist models; rows with
  incomplete specialist inputs stay watchlisted instead of entering ranking.
- Asset managers, consumer-finance names, other financials and pre-profit
  biotech remain watchlisted until dedicated models exist.
- Scenario set is discrete (bear/base/bull); worst-case stress metrics are
  deterministic bear/base/bull stress labels, not calibrated CVaR.
- Ad-hoc market closures are not in the calendar; freshness checks catch them.
