# Weekly US Stock Screen — 2026-06-17

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-06-17**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 513 | - |
| step2_hard_filters | 513 | 321 | persistent_negative_fcf: 22, interest_coverage: 21, adr_excluded: 17 |
| step3_standardize | 321 | 321 | - |
| step4_specialist_models | 96 | 61 | asset_management_model_not_supported: 16, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 321 | 314 | no_normalized_earnings: 7 |
| step5_quality_risk | 314 | 306 | - |
| step6_scenario_valuation | 306 | 279 | insufficient_post_valuation_model_confidence: 19, roic_not_meaningful:meaningless_capital: 6, irr_below_solver_bound: 1 |
| step7_risk_adjusted_ranking | 340 | 340 | - |

## Eligible Candidates (13)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 17.0% | 34.1% | 16.3% | 44.2% | 0.0% | 0% | 0.79 | 0.77 |
| 2 | FOXA | 13.7% | 34.2% | 14.3% | 44.6% | 0.0% | 0% | 0.90 | 0.62 |
| 3 | KLAC | 13.5% | 31.7% | 17.8% | 40.1% | 0.0% | 0% | 0.97 | 0.68 |
| 4 | VICI | 10.2% | 33.2% | 14.7% | 33.2% | 0.0% | 0% | 0.47 | 0.48 |
| 5 | TTD | 8.7% | 29.0% | 8.5% | 37.5% | 3.5% | 0% | 0.91 | 0.71 |
| 6 | OMC | 8.4% | 26.5% | 17.3% | 32.9% | 0.0% | 0% | 0.80 | 0.58 |
| 7 | ARE | 7.2% | 27.1% | 17.6% | 27.1% | 0.0% | 0% | 0.68 | 0.48 |
| 8 | CTSH | 6.7% | 20.8% | 11.0% | 27.1% | 1.0% | 0% | 0.87 | 0.87 |
| 9 | BXP | 5.3% | 23.0% | 12.6% | 23.0% | 0.0% | 0% | 0.64 | 0.48 |
| 10 | CPT | 3.5% | 23.8% | 9.8% | 23.8% | 2.2% | 0% | 0.55 | 0.48 |
| 11 | CMCSA | 3.5% | 19.5% | 16.2% | 24.9% | 0.0% | 0% | 0.76 | 0.46 |
| 12 | ADBE | 1.8% | 19.1% | 8.2% | 25.4% | 3.8% | 0% | 0.98 | 0.79 |
| 13 | AVB | 1.8% | 22.9% | 8.6% | 22.9% | 3.4% | 0% | 0.54 | 0.48 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 17.0% | 34.1% | 16.3% | 44.2% | 0.0% | 0% | 0.79 | 0.77 |
| 2 | FOXA | 13.7% | 34.2% | 14.3% | 44.6% | 0.0% | 0% | 0.90 | 0.62 |
| 3 | KLAC | 13.5% | 31.7% | 17.8% | 40.1% | 0.0% | 0% | 0.97 | 0.68 |
| 4 | VICI | 10.2% | 33.2% | 14.7% | 33.2% | 0.0% | 0% | 0.47 | 0.48 |
| 5 | TTD | 8.7% | 29.0% | 8.5% | 37.5% | 3.5% | 0% | 0.91 | 0.71 |
| 6 | OMC | 8.4% | 26.5% | 17.3% | 32.9% | 0.0% | 0% | 0.80 | 0.58 |
| 7 | ARE | 7.2% | 27.1% | 17.6% | 27.1% | 0.0% | 0% | 0.68 | 0.48 |
| 8 | CTSH | 6.7% | 20.8% | 11.0% | 27.1% | 1.0% | 0% | 0.87 | 0.87 |
| 9 | BXP | 5.3% | 23.0% | 12.6% | 23.0% | 0.0% | 0% | 0.64 | 0.48 |
| 10 | CPT | 3.5% | 23.8% | 9.8% | 23.8% | 2.2% | 0% | 0.55 | 0.48 |
| 11 | CMCSA | 3.5% | 19.5% | 16.2% | 24.9% | 0.0% | 0% | 0.76 | 0.46 |
| 12 | ADBE | 1.8% | 19.1% | 8.2% | 25.4% | 3.8% | 0% | 0.98 | 0.79 |
| 13 | AVB | 1.8% | 22.9% | 8.6% | 22.9% | 3.4% | 0% | 0.54 | 0.48 |
| 14 | UDR | -0.3% | 22.6% | 6.6% | 22.6% | 5.4% | 0% | 0.50 | 0.48 |
| 15 | ELV | -1.4% | 12.3% | 10.4% | 18.4% | 1.6% | 0% | 0.84 | 0.67 |
| 16 | CPAY | -1.6% | 18.5% | 5.0% | 25.9% | 7.0% | 0% | 0.99 | 0.84 |
| 17 | HUM | -2.4% | 17.6% | 6.3% | 26.2% | 5.7% | 0% | 0.66 | 0.60 |
| 18 | ACN | -2.4% | 15.5% | 6.5% | 20.6% | 5.5% | 0% | 0.99 | 0.88 |
| 19 | ZTS | -2.5% | 17.8% | 4.3% | 25.2% | 7.7% | 0% | 0.98 | 0.90 |
| 20 | HPQ | -2.6% | 9.4% | 9.4% | 14.6% | 2.6% | 0% | 0.97 | 0.67 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | UHS | 32.2% | 34.1% | 16.3% | 44.2% | 100% | 141% |
| 2 | FOXA | 31.8% | 34.2% | 14.3% | 44.6% | 100% | 167% |
| 3 | KLAC | 30.4% | 31.7% | 17.8% | 40.1% | 100% | 89% |
| 4 | VICI | 28.6% | 33.2% | 14.7% | 33.2% | 100% | 319% |
| 5 | TTD | 26.0% | 29.0% | 8.5% | 37.5% | 75% | 106% |
| 6 | OMC | 25.8% | 26.5% | 17.3% | 32.9% | 100% | 142% |
| 7 | ARE | 24.7% | 27.1% | 17.6% | 27.1% | 100% | 232% |
| 8 | FISV | 24.2% | 32.1% | -22.8% | 55.5% | 75% | 153% |
| 9 | EOG | 23.9% | 25.6% | -1.2% | 45.5% | 75% | 115% |
| 10 | BXP | 20.4% | 23.0% | 12.6% | 23.0% | 100% | 181% |
| 11 | CPT | 20.3% | 23.8% | 9.8% | 23.8% | 75% | 190% |
| 12 | CMCSA | 20.0% | 19.5% | 16.2% | 24.9% | 100% | 72% |
| 13 | CTSH | 19.9% | 20.8% | 11.0% | 27.1% | 75% | 59% |
| 14 | AVB | 19.3% | 22.9% | 8.6% | 22.9% | 75% | 180% |
| 15 | IT | 19.1% | 21.0% | 1.6% | 32.7% | 75% | 58% |
| 16 | UDR | 18.6% | 22.6% | 6.6% | 22.6% | 75% | 177% |
| 17 | ADBE | 17.9% | 19.1% | 8.2% | 25.4% | 75% | 31% |
| 18 | ACGL | 17.4% | 19.5% | 4.6% | 26.1% | 75% | 143% |
| 19 | LDOS | 17.2% | 20.3% | -5.0% | 33.2% | 75% | 71% |
| 20 | CPAY | 17.0% | 18.5% | 5.0% | 25.9% | 75% | 52% |

## Week-over-week

**comparison_baseline_reset** — previous run: 2026-06-15.
The universe or result-affecting config changed (changed: config); entered/exited/rank-change deltas are suppressed because they would be meaningless against a different baseline.

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| UHS | bear | 25% | 1.7% | 8.9% | 7.9% | 182.67 | 16.3% | 91% |
| UHS | base | 50% | 6.9% | 10.7% | 17.2% | 340.15 | 34.1% | 297% |
| UHS | bull | 25% | 11.0% | 12.1% | 19.6% | 481.73 | 44.2% | 471% |
| FOXA | bear | 25% | -1.1% | 17.5% | 6.5% | 69.31 | 14.3% | 80% |
| FOXA | base | 50% | 4.7% | 20.1% | 54.7% | 137.04 | 34.2% | 305% |
| FOXA | bull | 25% | 9.3% | 22.0% | 60.0% | 193.42 | 44.6% | 482% |
| KLAC | bear | 25% | 7.9% | 32.5% | 11.9% | 292.51 | 17.8% | 99% |
| KLAC | base | 50% | 14.6% | 37.6% | 58.4% | 450.97 | 31.7% | 246% |
| KLAC | bull | 25% | 19.9% | 41.9% | 60.0% | 588.89 | 40.1% | 364% |
| TTD | bear | 25% | 13.6% | 13.1% | 9.4% | 17.89 | 8.5% | 46% |
| TTD | base | 50% | 19.9% | 17.1% | 41.0% | 37.48 | 29.0% | 245% |
| TTD | bull | 25% | 24.9% | 20.7% | 44.1% | 49.74 | 37.5% | 366% |
| OMC | bear | 25% | 18.4% | 12.7% | 6.5% | 124.50 | 17.3% | 132% |
| OMC | base | 50% | 25.0% | 14.6% | 6.5% | 184.70 | 26.5% | 241% |
| OMC | bull | 25% | 30.3% | 15.9% | 6.5% | 239.24 | 32.9% | 340% |
| CTSH | bear | 25% | 0.1% | 12.9% | 8.4% | 54.33 | 11.0% | 58% |
| CTSH | base | 50% | 4.9% | 15.0% | 14.2% | 77.48 | 20.8% | 143% |
| CTSH | bull | 25% | 8.8% | 16.6% | 15.0% | 97.73 | 27.1% | 213% |
| CMCSA | bear | 25% | -6.1% | 16.1% | 6.5% | 30.83 | 16.2% | 90% |
| CMCSA | base | 50% | 1.2% | 18.7% | 6.5% | 38.92 | 19.5% | 148% |
| CMCSA | bull | 25% | 7.0% | 20.4% | 6.5% | 52.41 | 24.9% | 235% |
| ADBE | bear | 25% | 8.8% | 29.7% | 11.0% | 175.53 | 8.2% | 41% |
| ADBE | base | 50% | 13.2% | 33.6% | 57.2% | 257.42 | 19.1% | 126% |
| ADBE | bull | 25% | 16.8% | 36.9% | 58.3% | 320.61 | 25.4% | 189% |
| ELV | bear | 25% | -1.3% | 4.9% | 7.0% | 451.66 | 10.4% | 56% |
| ELV | base | 50% | 4.9% | 5.9% | 7.0% | 502.28 | 12.3% | 81% |
| ELV | bull | 25% | 9.9% | 6.6% | 7.0% | 660.27 | 18.4% | 138% |
| CPAY | bear | 25% | 7.7% | 39.8% | 7.5% | 315.34 | 5.0% | 25% |
| CPAY | base | 50% | 13.3% | 44.0% | 30.0% | 535.68 | 18.5% | 129% |
| CPAY | bull | 25% | 17.9% | 47.4% | 30.3% | 708.12 | 25.9% | 208% |
| HUM | bear | 25% | 12.7% | 2.5% | 7.9% | 338.41 | 6.3% | 36% |
| HUM | base | 50% | 19.3% | 3.7% | 7.9% | 560.70 | 17.6% | 126% |
| HUM | bull | 25% | 24.6% | 4.8% | 7.9% | 800.95 | 26.2% | 224% |
| ACN | bear | 25% | 2.4% | 13.4% | 9.4% | 139.17 | 6.5% | 32% |
| ACN | base | 50% | 7.2% | 14.7% | 18.8% | 196.02 | 15.5% | 98% |
| ACN | bull | 25% | 11.1% | 15.8% | 18.8% | 237.83 | 20.6% | 145% |
| ZTS | bear | 25% | 0.9% | 32.2% | 7.4% | 65.91 | 4.3% | 20% |
| ZTS | base | 50% | 5.3% | 36.0% | 24.5% | 112.77 | 17.8% | 119% |
| ZTS | bull | 25% | 8.8% | 39.1% | 24.8% | 148.97 | 25.2% | 195% |
| HPQ | bear | 25% | -3.6% | 5.7% | 8.8% | 24.80 | 11.5% | 59% |
| HPQ | base | 50% | 1.8% | 6.6% | 8.8% | 22.99 | 9.4% | 59% |
| HPQ | bull | 25% | 6.2% | 7.3% | 8.8% | 29.63 | 14.6% | 106% |

**Scenario order inversions** (named bear/base/bull intrinsic value is not monotone — this is economic, not a bug):
- HPQ: growth destroys value: forward ROIC 2.0% at/below WACC 8.8%, so higher-growth scenarios reinvest below the cost of capital and are worth less than the bear case

## Boundary Assumptions & Valuation Alerts

- UHS — bounds: share_change_floor_hit;intrinsic_2x_price
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit;wacc_floor_hit;intrinsic_2x_price
- KLAC — bounds: forward_roic_cap_hit
- VICI — bounds: specialist_model_v1
- TTD — bounds: intrinsic_2x_price
- OMC — bounds: base_growth_cap_hit;reinvestment_cap_hit;intrinsic_2x_price
- ARE — bounds: specialist_model_v1
- BXP — bounds: specialist_model_v1
- CPT — bounds: specialist_model_v1
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;wacc_floor_hit;reinvestment_cap_hit
- ADBE — bounds: share_change_floor_hit
- AVB — bounds: specialist_model_v1
- UDR — bounds: specialist_model_v1
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HPQ — bounds: forward_roic_floor_hit;reinvestment_cap_hit

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| CHTR | drawdown_from_high | nan% | -46% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| SMCI | weekly_drop;drawdown_from_high | -33% | -41% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- VICI: nan
- TTD: heavy_sbc
- OMC: incremental_roic_below_wacc
- ARE: nan
- BXP: nan
- CPT: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- ADBE: heavy_sbc
- AVB: nan
- UDR: nan
- ELV: incremental_roic_below_wacc
- CPAY: thin_interest_coverage
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- HPQ: incremental_roic_below_wacc

## Watchlist (not rankable under the general model)

- V Visa Inc. — consumer_finance_model_not_supported
- MA Mastercard Incorporated — consumer_finance_model_not_supported
- MS Morgan Stanley — asset_management_model_not_supported
- GS The Goldman Sachs Group, Inc. — asset_management_model_not_supported
- AXP American Express Company — consumer_finance_model_not_supported
- SCHW The Charles Schwab Corporation — asset_management_model_not_supported
- BLK BlackRock, Inc. — asset_management_model_not_supported
- BX Blackstone Inc. — asset_management_model_not_supported
- COF Capital One Financial Corporation — consumer_finance_model_not_supported
- SPGI S&P Global Inc. — financial_sector_model_not_supported
- KKR KKR & Co. Inc. — asset_management_model_not_supported
- APO Apollo Global Management, Inc. — asset_management_model_not_supported
- MCO Moody's Corporation — financial_sector_model_not_supported
- ICE Intercontinental Exchange, Inc. — financial_sector_model_not_supported
- STT State Street Corporation — asset_management_model_not_supported
- MSCI MSCI Inc. — financial_sector_model_not_supported
- AMP Ameriprise Financial, Inc. — asset_management_model_not_supported
- ARES Ares Management Corporation — asset_management_model_not_supported
- RJF Raymond James Financial, Inc. — asset_management_model_not_supported
- SYF Synchrony Financial — consumer_finance_model_not_supported
- BEN Franklin Resources, Inc. — asset_management_model_not_supported
- GPN Global Payments Inc. — consumer_finance_model_not_supported
- IVZ Invesco Ltd. — asset_management_model_not_supported
- FDS FactSet Research Systems Inc. — financial_sector_model_not_supported
- HOOD Robinhood Markets, Inc. — asset_management_model_not_supported
- CME CME Group Inc. — financial_sector_model_not_supported
- NDAQ Nasdaq, Inc. — financial_sector_model_not_supported
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- INSM Insmed Incorporated — preprofit_biotech_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- CHTR Charter Communications, Inc. — material_event_requires_reunderwriting
- SMCI Super Micro Computer, Inc. — material_event_requires_reunderwriting
- XOM Exxon Mobil Corporation — insufficient_model_confidence
- CVX Chevron Corporation — insufficient_model_confidence
- COP ConocoPhillips — insufficient_model_confidence
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
- FCX Freeport-McMoRan Inc. — insufficient_post_valuation_model_confidence
- RCL Royal Caribbean Cruises Ltd. — insufficient_post_valuation_model_confidence
- CI Cigna Corporation — insufficient_post_valuation_model_confidence
- VLO Valero Energy Corporation — insufficient_post_valuation_model_confidence
- NUE Nucor Corporation — insufficient_post_valuation_model_confidence
- TRGP Targa Resources Corp. — insufficient_post_valuation_model_confidence
- OXY Occidental Petroleum Corporation — insufficient_post_valuation_model_confidence
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
