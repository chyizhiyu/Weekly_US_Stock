# Weekly US Stock Screen — 2026-11-27

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-11-27**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 514 | - |
| step2_hard_filters | 514 | 298 | adr_excluded: 32, persistent_negative_fcf: 23, interest_coverage: 18 |
| step3_standardize | 298 | 298 | - |
| step4_specialist_models | 94 | 59 | asset_management_model_not_supported: 17, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 298 | 291 | no_normalized_earnings: 7 |
| step5_quality_risk | 291 | 288 | - |
| step6_scenario_valuation | 288 | 266 | insufficient_post_valuation_model_confidence: 16, roic_not_meaningful:meaningless_capital: 4, invalid_valuation_output: 1 |
| step7_risk_adjusted_ranking | 325 | 325 | - |

## Eligible Candidates (8)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FOX | 14.8% | 30.9% | 14.6% | 39.6% | 0.0% | 0% | 0.94 | 0.78 |
| 2 | VICI | 9.1% | 30.9% | 14.6% | 30.9% | 0.0% | 0% | 0.52 | 0.48 |
| 3 | ARE | 8.4% | 29.4% | 20.4% | 29.4% | 0.0% | 0% | 0.70 | 0.48 |
| 4 | CPT | 4.9% | 24.2% | 11.0% | 24.2% | 1.0% | 0% | 0.57 | 0.48 |
| 5 | CF | 4.7% | 33.5% | 7.4% | 50.4% | 4.6% | 0% | 0.89 | 0.43 |
| 6 | UHS | 3.6% | 23.6% | 6.7% | 33.3% | 5.3% | 0% | 0.76 | 0.77 |
| 7 | BXP | 2.8% | 20.3% | 10.8% | 20.3% | 1.2% | 0% | 0.66 | 0.48 |
| 8 | HUM | 0.1% | 17.6% | 8.6% | 24.9% | 3.4% | 0% | 0.87 | 0.63 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FOX | 14.8% | 30.9% | 14.6% | 39.6% | 0.0% | 0% | 0.94 | 0.78 |
| 2 | VICI | 9.1% | 30.9% | 14.6% | 30.9% | 0.0% | 0% | 0.52 | 0.48 |
| 3 | ARE | 8.4% | 29.4% | 20.4% | 29.4% | 0.0% | 0% | 0.70 | 0.48 |
| 4 | CPT | 4.9% | 24.2% | 11.0% | 24.2% | 1.0% | 0% | 0.57 | 0.48 |
| 5 | CF | 4.7% | 33.5% | 7.4% | 50.4% | 4.6% | 0% | 0.89 | 0.43 |
| 6 | UHS | 3.6% | 23.6% | 6.7% | 33.3% | 5.3% | 0% | 0.76 | 0.77 |
| 7 | BXP | 2.8% | 20.3% | 10.8% | 20.3% | 1.2% | 0% | 0.66 | 0.48 |
| 8 | HUM | 0.1% | 17.6% | 8.6% | 24.9% | 3.4% | 0% | 0.87 | 0.63 |
| 9 | CMCSA | -1.9% | 16.3% | 7.6% | 20.6% | 4.4% | 0% | 0.73 | 0.57 |
| 10 | ELV | -2.8% | 12.3% | 9.0% | 18.1% | 3.0% | 0% | 0.84 | 0.67 |
| 11 | UDR | -3.3% | 19.2% | 5.3% | 19.2% | 6.7% | 0% | 0.54 | 0.48 |
| 12 | VMRK | -3.6% | 17.1% | 5.9% | 21.5% | 6.1% | 0% | 0.60 | 0.48 |
| 13 | APA | -4.7% | 24.8% | 2.3% | 44.9% | 9.7% | 0% | 0.76 | 0.39 |
| 14 | ADBE | -5.2% | 14.7% | 4.7% | 20.8% | 7.3% | 0% | 0.98 | 0.79 |
| 15 | EOG | -5.6% | 20.7% | 2.8% | 38.6% | 9.2% | 0% | 0.87 | 0.41 |
| 16 | DECK | -6.2% | 15.0% | 3.8% | 22.1% | 8.2% | 0% | 0.96 | 0.67 |
| 17 | INVH | -6.4% | 15.5% | 3.9% | 15.5% | 8.1% | 0% | 0.59 | 0.48 |
| 18 | CTSH | -6.8% | 12.7% | 4.5% | 18.4% | 7.5% | 0% | 0.86 | 0.88 |
| 19 | INTU | -6.9% | 14.7% | 2.8% | 21.4% | 9.2% | 0% | 0.97 | 0.83 |
| 20 | OMC | -7.8% | 11.8% | 4.2% | 17.1% | 7.8% | 0% | 0.86 | 0.62 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | CI | 32.1% | 35.5% | -8.0% | 65.1% | 75% | 216% |
| 2 | CF | 31.2% | 33.5% | 7.4% | 50.4% | 75% | 159% |
| 3 | FOX | 29.0% | 30.9% | 14.6% | 39.6% | 100% | 126% |
| 4 | ARE | 27.2% | 29.4% | 20.4% | 29.4% | 100% | 263% |
| 5 | VICI | 26.8% | 30.9% | 14.6% | 30.9% | 100% | 285% |
| 6 | APA | 24.2% | 24.8% | 2.3% | 44.9% | 75% | 137% |
| 7 | UHS | 21.8% | 23.6% | 6.7% | 33.3% | 75% | 66% |
| 8 | CPT | 20.9% | 24.2% | 11.0% | 24.2% | 75% | 195% |
| 9 | EOG | 20.7% | 20.7% | 2.8% | 38.6% | 75% | 80% |
| 10 | BXP | 17.9% | 20.3% | 10.8% | 20.3% | 75% | 152% |
| 11 | HUM | 17.2% | 17.6% | 8.6% | 24.9% | 75% | 52% |
| 12 | UDR | 15.8% | 19.2% | 5.3% | 19.2% | 75% | 141% |
| 13 | VMRK | 15.4% | 17.1% | 5.9% | 21.5% | 75% | 121% |
| 14 | CMCSA | 15.2% | 16.3% | 7.6% | 20.6% | 75% | 45% |
| 15 | DECK | 14.0% | 15.0% | 3.8% | 22.1% | 75% | 19% |
| 16 | ADBE | 13.7% | 14.7% | 4.7% | 20.8% | 75% | 11% |
| 17 | INTU | 13.4% | 14.7% | 2.8% | 21.4% | 75% | 22% |
| 18 | KDP | 13.2% | 15.4% | -7.8% | 29.7% | 75% | 47% |
| 19 | ELV | 12.9% | 12.3% | 9.0% | 18.1% | 75% | 26% |
| 20 | INVH | 12.6% | 15.5% | 3.9% | 15.5% | 75% | 105% |

## Week-over-week

Previous run: 2026-11-20

- Entered Robust Top: none
- Exited Robust Top: none
- Entered Upside Top: ELV, INTU, KDP
- Exited Upside Top: CHTR, CTSH, LDOS

Largest robust-rank moves:

- HPQ: 23 → 318 (-295)
- HD: 131 → 80 (+51)
- ADSK: 190 → 216 (-26)
- QCOM: 151 → 172 (-21)
- SWKS: 143 → 160 (-17)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| FOX | bear | 25% | -1.0% | 19.8% | 7.5% | 76.46 | 14.6% | 80% |
| FOX | base | 50% | 4.4% | 22.2% | 47.7% | 133.04 | 30.9% | 253% |
| FOX | bull | 25% | 8.6% | 24.1% | 50.3% | 177.86 | 39.6% | 382% |
| CF | bear | 25% | -6.3% | 22.8% | 7.1% | 120.59 | 7.4% | 36% |
| CF | base | 50% | 10.9% | 31.1% | 18.7% | 309.66 | 33.5% | 303% |
| CF | bull | 25% | 24.6% | 38.4% | 20.1% | 574.88 | 50.4% | 648% |
| UHS | bear | 25% | 1.9% | 8.8% | 8.3% | 167.48 | 6.7% | 33% |
| UHS | base | 50% | 7.1% | 10.7% | 16.7% | 321.21 | 23.6% | 176% |
| UHS | bull | 25% | 11.3% | 12.1% | 18.9% | 459.29 | 33.3% | 301% |
| HUM | bear | 25% | 14.7% | 2.6% | 8.3% | 416.12 | 8.6% | 51% |
| HUM | base | 50% | 19.3% | 3.7% | 8.3% | 616.00 | 17.6% | 125% |
| HUM | bull | 25% | 23.0% | 4.8% | 8.3% | 834.60 | 24.9% | 206% |
| CMCSA | bear | 25% | -6.9% | 15.0% | 6.7% | 25.27 | 7.6% | 37% |
| CMCSA | base | 50% | 0.3% | 18.4% | 6.7% | 37.74 | 16.3% | 108% |
| CMCSA | bull | 25% | 6.2% | 20.7% | 6.7% | 49.06 | 20.6% | 176% |
| ELV | bear | 25% | 0.4% | 4.9% | 7.6% | 421.61 | 9.0% | 50% |
| ELV | base | 50% | 6.2% | 5.9% | 7.6% | 493.99 | 12.3% | 81% |
| ELV | bull | 25% | 10.9% | 6.6% | 7.6% | 638.53 | 18.1% | 134% |
| APA | bear | 25% | -9.5% | 21.3% | 6.9% | 40.36 | 2.3% | 10% |
| APA | base | 50% | 14.0% | 31.8% | 8.5% | 109.14 | 24.8% | 208% |
| APA | bull | 25% | 32.8% | 40.8% | 8.9% | 240.92 | 44.9% | 578% |
| ADBE | bear | 25% | 9.1% | 29.7% | 11.4% | 179.12 | 4.7% | 22% |
| ADBE | base | 50% | 13.6% | 33.6% | 58.7% | 260.09 | 14.7% | 91% |
| ADBE | bull | 25% | 17.1% | 36.9% | 59.8% | 322.14 | 20.8% | 144% |
| EOG | bear | 25% | -0.9% | 20.2% | 7.2% | 123.70 | 2.8% | 13% |
| EOG | base | 50% | 21.2% | 29.6% | 8.2% | 267.48 | 20.7% | 162% |
| EOG | bull | 25% | 38.9% | 38.1% | 8.3% | 549.82 | 38.6% | 434% |
| DECK | bear | 25% | 7.5% | 15.9% | 10.2% | 68.06 | 3.8% | 17% |
| DECK | base | 50% | 12.3% | 18.9% | 57.8% | 103.31 | 15.0% | 94% |
| DECK | bull | 25% | 16.2% | 21.4% | 60.0% | 132.68 | 22.1% | 158% |
| CTSH | bear | 25% | -0.4% | 12.9% | 8.8% | 53.29 | 4.5% | 21% |
| CTSH | base | 50% | 4.4% | 15.0% | 12.4% | 72.75 | 12.7% | 78% |
| CTSH | bull | 25% | 8.2% | 16.5% | 13.0% | 90.08 | 18.4% | 127% |
| INTU | bear | 25% | 10.9% | 22.6% | 9.1% | 205.77 | 2.8% | 14% |
| INTU | base | 50% | 15.9% | 26.1% | 23.9% | 333.02 | 14.7% | 96% |
| INTU | bull | 25% | 19.9% | 29.1% | 24.4% | 430.44 | 21.4% | 159% |
| OMC | bear | 25% | 18.8% | 12.9% | 7.4% | 114.86 | 4.2% | 24% |
| OMC | base | 50% | 25.0% | 14.6% | 7.4% | 167.08 | 11.8% | 79% |
| OMC | bull | 25% | 30.0% | 15.9% | 7.4% | 213.77 | 17.1% | 129% |

## Boundary Assumptions & Valuation Alerts

- FOX — bounds: share_change_floor_hit;intrinsic_2x_price
- VICI — bounds: specialist_model_v1
- ARE — bounds: specialist_model_v1
- CPT — bounds: specialist_model_v1
- CF — bounds: share_change_floor_hit;intrinsic_2x_price
- UHS — bounds: share_change_floor_hit
- BXP — bounds: specialist_model_v1
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;reinvestment_cap_hit
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- UDR — bounds: specialist_model_v1
- VMRK — bounds: specialist_model_v1
- APA — bounds: reinvestment_cap_hit;intrinsic_2x_price
- ADBE — bounds: share_change_floor_hit
- EOG — bounds: reinvestment_cap_hit
- DECK — bounds: forward_roic_cap_hit;share_change_floor_hit
- INVH — bounds: specialist_model_v1
- OMC — bounds: base_growth_cap_hit;share_change_cap_hit;reinvestment_cap_hit

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| DELL | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| NOW | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| CIEN | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| MU | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| AMAT | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| LRCX | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| MRVL | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| SNDK | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| DDOG | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| LITE | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| TER | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| FLEX | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- VICI: nan
- ARE: nan
- CPT: nan
- CF: cyclical_revenue
- BXP: nan
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- ELV: incremental_roic_below_wacc
- UDR: nan
- VMRK: nan
- APA: cyclical_revenue, incremental_roic_below_wacc
- ADBE: heavy_sbc
- EOG: cyclical_revenue, incremental_roic_below_wacc
- INVH: nan
- INTU: heavy_sbc
- OMC: ongoing_dilution, incremental_roic_below_wacc

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
- KKR KKR & Co. Inc. — asset_management_model_not_supported
- MCO Moody's Corporation — financial_sector_model_not_supported
- APO Apollo Global Management, Inc. — asset_management_model_not_supported
- MSCI MSCI Inc. — financial_sector_model_not_supported
- ARES Ares Management Corporation — asset_management_model_not_supported
- STT State Street Corporation — asset_management_model_not_supported
- AMP Ameriprise Financial, Inc. — asset_management_model_not_supported
- RJF Raymond James Financial, Inc. — asset_management_model_not_supported
- GPN Global Payments Inc. — consumer_finance_model_not_supported
- SYF Synchrony Financial — consumer_finance_model_not_supported
- BEN Franklin Resources, Inc. — asset_management_model_not_supported
- IVZ Invesco Ltd. — asset_management_model_not_supported
- FDS FactSet Research Systems Inc. — financial_sector_model_not_supported
- CME CME Group Inc. — financial_sector_model_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- NDAQ Nasdaq, Inc. — financial_sector_model_not_supported
- HOOD Robinhood Markets, Inc. — asset_management_model_not_supported
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- NTRS Northern Trust Corporation — asset_management_model_not_supported
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- DELL Dell Technologies Inc. — material_event_requires_reunderwriting
- NOW ServiceNow, Inc. — material_event_requires_reunderwriting
- CIEN Ciena Corporation — material_event_requires_reunderwriting
- MU Micron Technology, Inc. — material_event_requires_reunderwriting
- AMAT Applied Materials, Inc. — material_event_requires_reunderwriting
- LRCX Lam Research Corporation — material_event_requires_reunderwriting
- MRVL Marvell Technology, Inc. — material_event_requires_reunderwriting
- SNDK Sandisk Corporation — material_event_requires_reunderwriting
- DDOG Datadog, Inc. — material_event_requires_reunderwriting
- LITE Lumentum Holdings Inc. — material_event_requires_reunderwriting
- TER Teradyne, Inc. — material_event_requires_reunderwriting
- FLEX Flex Ltd. — material_event_requires_reunderwriting
- CCL Carnival Corporation & plc — insufficient_model_confidence
- NRG NRG Energy, Inc. — insufficient_model_confidence
- TSLA Tesla, Inc. — insufficient_model_confidence
- LHX L3Harris Technologies, Inc. — invalid_valuation_output
- IFF International Flavors & Fragrances Inc. — irr_below_solver_bound
- BKNG Booking Holdings Inc. — roic_not_meaningful:meaningless_capital
- ABNB Airbnb, Inc. — roic_not_meaningful:meaningless_capital
- FTNT Fortinet, Inc. — roic_not_meaningful:meaningless_capital
- VRSN VeriSign, Inc. — roic_not_meaningful:meaningless_capital
- XOM Exxonmobil Holdings Corporation — insufficient_post_valuation_model_confidence
- CVX Chevron Corporation — insufficient_post_valuation_model_confidence
- PSX Phillips 66 — insufficient_post_valuation_model_confidence
- RCL Royal Caribbean Cruises Ltd. — insufficient_post_valuation_model_confidence
- FCX Freeport-McMoRan Inc. — insufficient_post_valuation_model_confidence
- NUE Nucor Corporation — insufficient_post_valuation_model_confidence
- OXY Occidental Petroleum Corporation — insufficient_post_valuation_model_confidence
- DVN Devon Energy Corporation — insufficient_post_valuation_model_confidence
- XYZ Block, Inc. — insufficient_post_valuation_model_confidence
- IR Ingersoll Rand Inc. — insufficient_post_valuation_model_confidence
- MOS The Mosaic Company — insufficient_post_valuation_model_confidence
- NVDA NVIDIA Corporation — insufficient_post_valuation_model_confidence
- AMD Advanced Micro Devices, Inc. — insufficient_post_valuation_model_confidence
- APP AppLovin Corporation — insufficient_post_valuation_model_confidence
- STLD Steel Dynamics, Inc. — insufficient_post_valuation_model_confidence
- EXPE Expedia Group, Inc. — insufficient_post_valuation_model_confidence

## Data Gaps and Model Limitations

- Stocks missing core financials were rejected (fail closed), never estimated.
- Banks, insurers and REITs use conservative specialist models; rows with
  incomplete specialist inputs stay watchlisted instead of entering ranking.
- Asset managers, consumer-finance names, other financials and pre-profit
  biotech remain watchlisted until dedicated models exist.
- Scenario set is discrete (bear/base/bull); worst-case stress metrics are
  deterministic bear/base/bull stress labels, not calibrated CVaR.
- Ad-hoc market closures are not in the calendar; freshness checks catch them.
