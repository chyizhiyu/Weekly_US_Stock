# Weekly US Stock Screen — 2026-10-23

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-10-23**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 515 | - |
| step2_hard_filters | 515 | 305 | adr_excluded: 32, persistent_negative_fcf: 23, interest_coverage: 18 |
| step3_standardize | 305 | 305 | - |
| step4_specialist_models | 93 | 58 | asset_management_model_not_supported: 17, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 305 | 296 | no_normalized_earnings: 9 |
| step5_quality_risk | 296 | 291 | - |
| step6_scenario_valuation | 291 | 266 | insufficient_post_valuation_model_confidence: 19, roic_not_meaningful:meaningless_capital: 5, invalid_valuation_output: 1 |
| step7_risk_adjusted_ranking | 324 | 324 | - |

## Eligible Candidates (7)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | VICI | 8.9% | 30.5% | 15.1% | 30.5% | 0.0% | 0% | 0.53 | 0.48 |
| 2 | ARE | 8.5% | 29.7% | 20.6% | 29.7% | 0.0% | 0% | 0.70 | 0.48 |
| 3 | FOXA | 8.5% | 25.9% | 9.7% | 34.6% | 2.3% | 0% | 0.91 | 0.78 |
| 4 | UHS | 5.6% | 24.4% | 8.1% | 33.9% | 3.9% | 0% | 0.78 | 0.76 |
| 5 | CMCSA | 4.8% | 21.3% | 15.1% | 24.1% | 0.0% | 0% | 0.76 | 0.51 |
| 6 | BXP | 3.3% | 20.5% | 11.2% | 20.5% | 0.8% | 0% | 0.67 | 0.48 |
| 7 | CPT | 1.7% | 21.3% | 9.2% | 21.3% | 2.8% | 0% | 0.59 | 0.48 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | VICI | 8.9% | 30.5% | 15.1% | 30.5% | 0.0% | 0% | 0.53 | 0.48 |
| 2 | ARE | 8.5% | 29.7% | 20.6% | 29.7% | 0.0% | 0% | 0.70 | 0.48 |
| 3 | FOXA | 8.5% | 25.9% | 9.7% | 34.6% | 2.3% | 0% | 0.91 | 0.78 |
| 4 | UHS | 5.6% | 24.4% | 8.1% | 33.9% | 3.9% | 0% | 0.78 | 0.76 |
| 5 | CMCSA | 4.8% | 21.3% | 15.1% | 24.1% | 0.0% | 0% | 0.76 | 0.51 |
| 6 | BXP | 3.3% | 20.5% | 11.2% | 20.5% | 0.8% | 0% | 0.67 | 0.48 |
| 7 | CPT | 1.7% | 21.3% | 9.2% | 21.3% | 2.8% | 0% | 0.59 | 0.48 |
| 8 | CF | -2.3% | 31.5% | 2.6% | 49.5% | 9.4% | 0% | 0.89 | 0.36 |
| 9 | VMRK | -2.8% | 17.6% | 6.5% | 21.9% | 5.5% | 0% | 0.61 | 0.48 |
| 10 | OMC | -3.5% | 14.6% | 6.9% | 19.9% | 5.1% | 0% | 0.86 | 0.62 |
| 11 | UDR | -3.6% | 18.7% | 5.2% | 18.7% | 6.8% | 0% | 0.55 | 0.48 |
| 12 | ELV | -5.5% | 9.6% | 6.5% | 15.4% | 5.5% | 0% | 0.84 | 0.67 |
| 13 | HUM | -5.7% | 14.6% | 4.7% | 22.3% | 7.3% | 0% | 0.76 | 0.62 |
| 14 | DECK | -5.7% | 15.0% | 4.7% | 21.6% | 7.3% | 0% | 0.96 | 0.52 |
| 15 | TSN | -6.4% | 15.6% | 3.6% | 28.4% | 8.4% | 0% | 0.60 | 0.58 |
| 16 | INVH | -7.4% | 14.5% | 3.4% | 14.5% | 8.6% | 0% | 0.60 | 0.48 |
| 17 | HST | -9.6% | 10.5% | 2.4% | 10.5% | 9.6% | 0% | 0.68 | 0.48 |
| 18 | O | -9.7% | 14.3% | 1.2% | 14.3% | 10.8% | 0% | 0.54 | 0.48 |
| 19 | ADBE | -10.5% | 10.9% | 1.5% | 16.8% | 10.5% | 0% | 0.98 | 0.79 |
| 20 | FRT | -10.7% | 10.9% | 1.3% | 10.9% | 10.7% | 0% | 0.64 | 0.48 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | CF | 28.8% | 31.5% | 2.6% | 49.5% | 75% | 143% |
| 2 | ARE | 27.4% | 29.7% | 20.6% | 29.7% | 100% | 266% |
| 3 | CI | 27.2% | 30.9% | -12.9% | 60.0% | 75% | 165% |
| 4 | VICI | 26.7% | 30.5% | 15.1% | 30.5% | 100% | 279% |
| 5 | FOXA | 24.0% | 25.9% | 9.7% | 34.6% | 75% | 94% |
| 6 | CHTR | 23.6% | 55.6% | -95.0% | 78.2% | 75% | 419% |
| 7 | UHS | 22.7% | 24.4% | 8.1% | 33.9% | 75% | 70% |
| 8 | CMCSA | 20.5% | 21.3% | 15.1% | 24.1% | 100% | 80% |
| 9 | CPT | 18.3% | 21.3% | 9.2% | 21.3% | 75% | 163% |
| 10 | BXP | 18.2% | 20.5% | 11.2% | 20.5% | 75% | 154% |
| 11 | FISV | 16.0% | 26.7% | -39.7% | 50.5% | 75% | 104% |
| 12 | VMRK | 15.9% | 17.6% | 6.5% | 21.9% | 75% | 125% |
| 13 | TSN | 15.8% | 15.6% | 3.6% | 28.4% | 75% | 48% |
| 14 | UDR | 15.3% | 18.7% | 5.2% | 18.7% | 75% | 135% |
| 15 | DECK | 14.1% | 15.0% | 4.7% | 21.6% | 75% | 20% |
| 16 | HUM | 14.0% | 14.6% | 4.7% | 22.3% | 75% | 33% |
| 17 | OMC | 14.0% | 14.6% | 6.9% | 19.9% | 75% | 109% |
| 18 | EOG | 12.0% | 12.3% | -5.8% | 29.3% | 75% | 25% |
| 19 | INVH | 11.7% | 14.5% | 3.4% | 14.5% | 75% | 97% |
| 20 | MO | 11.3% | 13.0% | -1.5% | 20.6% | 75% | 25% |

## Week-over-week

Previous run: 2026-10-16

- Entered Robust Top: FRT
- Exited Robust Top: HPQ
- Entered Upside Top: INVH, MO, OMC
- Exited Upside Top: ADBE, LEN, MKC

Largest robust-rank moves:

- NWSA: 244 → 173 (+71)
- HON: 212 → 153 (+59)
- ABT: 196 → 152 (+44)
- JBHT: 227 → 192 (+35)
- GPC: 142 → 109 (+33)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| FOXA | bear | 25% | -1.2% | 19.7% | 7.4% | 72.18 | 9.7% | 50% |
| FOXA | base | 50% | 4.4% | 22.2% | 46.3% | 128.91 | 25.9% | 199% |
| FOXA | bull | 25% | 8.8% | 24.1% | 49.9% | 174.35 | 34.6% | 313% |
| UHS | bear | 25% | 1.6% | 8.9% | 8.5% | 172.72 | 8.1% | 40% |
| UHS | base | 50% | 7.1% | 10.7% | 17.2% | 318.41 | 24.4% | 183% |
| UHS | bull | 25% | 11.4% | 12.1% | 19.5% | 450.52 | 33.9% | 309% |
| CMCSA | bear | 25% | -7.0% | 16.1% | 6.6% | 29.95 | 15.1% | 83% |
| CMCSA | base | 50% | 0.4% | 18.7% | 6.6% | 40.93 | 21.3% | 155% |
| CMCSA | bull | 25% | 6.3% | 20.4% | 6.6% | 50.89 | 24.1% | 224% |
| CF | bear | 25% | -10.1% | 22.8% | 7.1% | 100.00 | 2.6% | 12% |
| CF | base | 50% | 11.9% | 31.1% | 17.8% | 293.33 | 31.5% | 278% |
| CF | bull | 25% | 29.5% | 38.4% | 19.1% | 590.22 | 49.5% | 644% |
| OMC | bear | 25% | 18.9% | 12.9% | 7.3% | 119.43 | 6.9% | 43% |
| OMC | base | 50% | 25.0% | 14.6% | 7.3% | 172.40 | 14.6% | 105% |
| OMC | bull | 25% | 29.9% | 15.9% | 7.3% | 219.56 | 19.9% | 160% |
| ELV | bear | 25% | 0.0% | 4.9% | 7.6% | 422.09 | 6.5% | 34% |
| ELV | base | 50% | 6.1% | 5.9% | 7.6% | 485.82 | 9.6% | 60% |
| ELV | bull | 25% | 10.9% | 6.6% | 7.6% | 630.74 | 15.4% | 107% |
| HUM | bear | 25% | 13.7% | 2.5% | 8.4% | 360.45 | 4.7% | 26% |
| HUM | base | 50% | 19.2% | 3.7% | 8.4% | 562.76 | 14.6% | 98% |
| HUM | bull | 25% | 23.5% | 4.8% | 8.4% | 780.83 | 22.3% | 176% |
| DECK | bear | 25% | 7.5% | 15.9% | 10.4% | 66.73 | 4.7% | 22% |
| DECK | base | 50% | 12.3% | 18.9% | 57.8% | 97.67 | 15.0% | 91% |
| DECK | bull | 25% | 16.2% | 21.4% | 60.0% | 123.49 | 21.6% | 149% |
| TSN | bear | 25% | -4.0% | 4.2% | 7.4% | 47.85 | 3.6% | 17% |
| TSN | base | 50% | 3.4% | 6.8% | 7.4% | 84.10 | 15.6% | 117% |
| TSN | bull | 25% | 9.3% | 8.9% | 7.4% | 147.02 | 28.4% | 276% |
| ADBE | bear | 25% | 9.1% | 29.7% | 11.7% | 174.85 | 1.5% | 7% |
| ADBE | base | 50% | 13.6% | 33.6% | 58.7% | 252.33 | 10.9% | 64% |
| ADBE | bull | 25% | 17.1% | 36.9% | 59.8% | 311.87 | 16.8% | 109% |

## Boundary Assumptions & Valuation Alerts

- VICI — bounds: specialist_model_v1
- ARE — bounds: specialist_model_v1
- FOXA — bounds: share_change_floor_hit
- UHS — bounds: share_change_floor_hit
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;reinvestment_cap_hit
- BXP — bounds: specialist_model_v1
- CPT — bounds: specialist_model_v1
- CF — bounds: share_change_floor_hit;intrinsic_2x_price
- VMRK — bounds: specialist_model_v1
- OMC — bounds: base_growth_cap_hit;share_change_cap_hit;reinvestment_cap_hit;intrinsic_2x_price
- UDR — bounds: specialist_model_v1
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- DECK — bounds: forward_roic_cap_hit
- TSN — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- INVH — bounds: specialist_model_v1
- HST — bounds: specialist_model_v1
- O — bounds: specialist_model_v1
- ADBE — bounds: share_change_floor_hit
- FRT — bounds: specialist_model_v1

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| CIEN | weekly_drop | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| FIX | weekly_drop | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| AMAT | weekly_drop | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| LRCX | weekly_drop | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| KLAC | weekly_drop | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| LITE | weekly_drop | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| FLEX | weekly_drop | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- VICI: nan
- ARE: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- BXP: nan
- CPT: nan
- CF: cyclical_revenue
- VMRK: nan
- OMC: ongoing_dilution, incremental_roic_below_wacc
- UDR: nan
- ELV: incremental_roic_below_wacc
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- TSN: thin_interest_coverage, incremental_roic_below_wacc
- INVH: nan
- HST: nan
- O: nan
- ADBE: heavy_sbc
- FRT: nan

## Watchlist (not rankable under the general model)

- V Visa Inc. — consumer_finance_model_not_supported
- MA Mastercard Incorporated — consumer_finance_model_not_supported
- MS Morgan Stanley — asset_management_model_not_supported
- GS The Goldman Sachs Group, Inc. — asset_management_model_not_supported
- AXP American Express Company — consumer_finance_model_not_supported
- BLK BlackRock, Inc. — asset_management_model_not_supported
- SCHW The Charles Schwab Corporation — asset_management_model_not_supported
- BX Blackstone Inc. — asset_management_model_not_supported
- SPGI S&P Global Inc. — financial_sector_model_not_supported
- COF Capital One Financial Corporation — consumer_finance_model_not_supported
- ICE Intercontinental Exchange, Inc. — financial_sector_model_not_supported
- MCO Moody's Corporation — financial_sector_model_not_supported
- KKR KKR & Co. Inc. — asset_management_model_not_supported
- APO Apollo Global Management, Inc. — asset_management_model_not_supported
- STT State Street Corporation — asset_management_model_not_supported
- MSCI MSCI Inc. — financial_sector_model_not_supported
- AMP Ameriprise Financial, Inc. — asset_management_model_not_supported
- ARES Ares Management Corporation — asset_management_model_not_supported
- RJF Raymond James Financial, Inc. — asset_management_model_not_supported
- SYF Synchrony Financial — consumer_finance_model_not_supported
- GPN Global Payments Inc. — consumer_finance_model_not_supported
- BEN Franklin Resources, Inc. — asset_management_model_not_supported
- IVZ Invesco Ltd. — asset_management_model_not_supported
- FDS FactSet Research Systems Inc. — financial_sector_model_not_supported
- CME CME Group Inc. — financial_sector_model_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- HOOD Robinhood Markets, Inc. — asset_management_model_not_supported
- NDAQ Nasdaq, Inc. — financial_sector_model_not_supported
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- NTRS Northern Trust Corporation — asset_management_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- CIEN Ciena Corporation — material_event_requires_reunderwriting
- FIX Comfort Systems USA, Inc. — material_event_requires_reunderwriting
- AMAT Applied Materials, Inc. — material_event_requires_reunderwriting
- LRCX Lam Research Corporation — material_event_requires_reunderwriting
- KLAC KLA Corporation — material_event_requires_reunderwriting
- LITE Lumentum Holdings Inc. — material_event_requires_reunderwriting
- FLEX Flex Ltd. — material_event_requires_reunderwriting
- XOM Exxonmobil Holdings Corporation — insufficient_model_confidence
- CVX Chevron Corporation — insufficient_model_confidence
- PSX Phillips 66 — insufficient_model_confidence
- CCL Carnival Corporation & plc — insufficient_model_confidence
- MOS The Mosaic Company — insufficient_model_confidence
- LHX L3Harris Technologies, Inc. — invalid_valuation_output
- FTNT Fortinet, Inc. — roic_not_meaningful:meaningless_capital
- BKNG Booking Holdings Inc. — roic_not_meaningful:meaningless_capital
- ABNB Airbnb, Inc. — roic_not_meaningful:meaningless_capital
- EXPE Expedia Group, Inc. — roic_not_meaningful:meaningless_capital
- VRSN VeriSign, Inc. — roic_not_meaningful:meaningless_capital
- COP ConocoPhillips — insufficient_post_valuation_model_confidence
- MPC Marathon Petroleum Corporation — insufficient_post_valuation_model_confidence
- VLO Valero Energy Corporation — insufficient_post_valuation_model_confidence
- FCX Freeport-McMoRan Inc. — insufficient_post_valuation_model_confidence
- RCL Royal Caribbean Cruises Ltd. — insufficient_post_valuation_model_confidence
- OXY Occidental Petroleum Corporation — insufficient_post_valuation_model_confidence
- NUE Nucor Corporation — insufficient_post_valuation_model_confidence
- DVN Devon Energy Corporation — insufficient_post_valuation_model_confidence
- XYZ Block, Inc. — insufficient_post_valuation_model_confidence
- IR Ingersoll Rand Inc. — insufficient_post_valuation_model_confidence
- IFF International Flavors & Fragrances Inc. — insufficient_post_valuation_model_confidence
- NVDA NVIDIA Corporation — insufficient_post_valuation_model_confidence
- TSLA Tesla, Inc. — insufficient_post_valuation_model_confidence
- MU Micron Technology, Inc. — insufficient_post_valuation_model_confidence
- AMD Advanced Micro Devices, Inc. — insufficient_post_valuation_model_confidence
- APP AppLovin Corporation — insufficient_post_valuation_model_confidence
- REGN Regeneron Pharmaceuticals, Inc. — insufficient_post_valuation_model_confidence
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
