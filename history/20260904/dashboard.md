# Weekly US Stock Screen — 2026-09-04

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-09-04**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 517 | - |
| step2_hard_filters | 517 | 311 | adr_excluded: 32, persistent_negative_fcf: 23, interest_coverage: 16 |
| step3_standardize | 311 | 311 | - |
| step4_specialist_models | 94 | 59 | asset_management_model_not_supported: 17, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 311 | 304 | no_normalized_earnings: 7 |
| step5_quality_risk | 304 | 300 | - |
| step6_scenario_valuation | 300 | 274 | insufficient_post_valuation_model_confidence: 19, roic_not_meaningful:meaningless_capital: 5, irr_below_solver_bound: 1 |
| step7_risk_adjusted_ranking | 333 | 333 | - |

## Eligible Candidates (9)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 11.6% | 28.2% | 11.3% | 37.9% | 0.7% | 0% | 0.78 | 0.76 |
| 2 | OMC | 11.5% | 28.9% | 19.5% | 35.7% | 0.0% | 0% | 0.83 | 0.68 |
| 3 | TTD | 10.0% | 31.0% | 9.3% | 41.0% | 2.7% | 0% | 0.91 | 0.67 |
| 4 | VICI | 8.9% | 30.5% | 14.3% | 30.5% | 0.0% | 0% | 0.52 | 0.48 |
| 5 | ARE | 6.1% | 24.7% | 15.6% | 24.7% | 0.0% | 0% | 0.68 | 0.48 |
| 6 | FOXA | 4.8% | 24.9% | 7.8% | 34.0% | 4.2% | 0% | 0.91 | 0.69 |
| 7 | CPT | 3.1% | 23.1% | 9.8% | 23.1% | 2.2% | 0% | 0.57 | 0.48 |
| 8 | BXP | 2.3% | 20.2% | 10.3% | 20.2% | 1.7% | 0% | 0.65 | 0.48 |
| 9 | CMCSA | 2.2% | 17.2% | 11.8% | 21.5% | 0.2% | 0% | 0.76 | 0.46 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 11.6% | 28.2% | 11.3% | 37.9% | 0.7% | 0% | 0.78 | 0.76 |
| 2 | OMC | 11.5% | 28.9% | 19.5% | 35.7% | 0.0% | 0% | 0.83 | 0.68 |
| 3 | TTD | 10.0% | 31.0% | 9.3% | 41.0% | 2.7% | 0% | 0.91 | 0.67 |
| 4 | VICI | 8.9% | 30.5% | 14.3% | 30.5% | 0.0% | 0% | 0.52 | 0.48 |
| 5 | ARE | 6.1% | 24.7% | 15.6% | 24.7% | 0.0% | 0% | 0.68 | 0.48 |
| 6 | FOXA | 4.8% | 24.9% | 7.8% | 34.0% | 4.2% | 0% | 0.91 | 0.69 |
| 7 | CPT | 3.1% | 23.1% | 9.8% | 23.1% | 2.2% | 0% | 0.57 | 0.48 |
| 8 | BXP | 2.3% | 20.2% | 10.3% | 20.2% | 1.7% | 0% | 0.65 | 0.48 |
| 9 | CMCSA | 2.2% | 17.2% | 11.8% | 21.5% | 0.2% | 0% | 0.76 | 0.46 |
| 10 | UDR | -1.2% | 21.3% | 6.4% | 21.3% | 5.6% | 0% | 0.52 | 0.48 |
| 11 | VMRK | -2.3% | 18.4% | 6.6% | 23.1% | 5.4% | 0% | 0.59 | 0.48 |
| 12 | ELV | -2.8% | 11.5% | 9.2% | 17.5% | 2.8% | 0% | 0.82 | 0.67 |
| 13 | HUM | -3.0% | 16.3% | 6.3% | 24.1% | 5.7% | 0% | 0.76 | 0.62 |
| 14 | MO | -5.1% | 17.3% | 2.1% | 25.1% | 9.9% | 0% | 0.98 | 0.92 |
| 15 | CF | -5.1% | 29.3% | 0.5% | 47.6% | 11.5% | 0% | 0.89 | 0.36 |
| 16 | HST | -5.7% | 14.0% | 5.4% | 14.0% | 6.6% | 0% | 0.67 | 0.48 |
| 17 | DECK | -6.0% | 14.8% | 4.0% | 21.6% | 8.0% | 0% | 0.96 | 0.75 |
| 18 | ZTS | -6.5% | 15.7% | 2.2% | 23.1% | 9.8% | 0% | 0.98 | 0.89 |
| 19 | INVH | -6.7% | 15.4% | 3.6% | 15.4% | 8.4% | 0% | 0.59 | 0.48 |
| 20 | CTSH | -6.9% | 13.3% | 3.9% | 19.6% | 8.1% | 0% | 0.86 | 0.87 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | CI | 31.1% | 34.7% | -9.9% | 64.7% | 75% | 209% |
| 2 | OMC | 28.3% | 28.9% | 19.5% | 35.7% | 100% | 164% |
| 3 | TTD | 28.1% | 31.0% | 9.3% | 41.0% | 75% | 115% |
| 4 | CF | 26.7% | 29.3% | 0.5% | 47.6% | 75% | 128% |
| 5 | VICI | 26.5% | 30.5% | 14.3% | 30.5% | 100% | 279% |
| 6 | UHS | 26.4% | 28.2% | 11.3% | 37.9% | 75% | 95% |
| 7 | EOG | 23.2% | 25.3% | -1.0% | 43.3% | 75% | 104% |
| 8 | FOXA | 22.9% | 24.9% | 7.8% | 34.0% | 75% | 92% |
| 9 | ARE | 22.4% | 24.7% | 15.6% | 24.7% | 100% | 202% |
| 10 | CPT | 19.7% | 23.1% | 9.8% | 23.1% | 75% | 182% |
| 11 | BXP | 17.7% | 20.2% | 10.3% | 20.2% | 75% | 151% |
| 12 | UDR | 17.6% | 21.3% | 6.4% | 21.3% | 75% | 163% |
| 13 | CMCSA | 16.9% | 17.2% | 11.8% | 21.5% | 75% | 54% |
| 14 | VMRK | 16.6% | 18.4% | 6.6% | 23.1% | 75% | 133% |
| 15 | FISV | 16.4% | 26.2% | -36.9% | 49.9% | 75% | 102% |
| 16 | CHTR | 15.8% | 45.6% | -95.0% | 66.8% | 75% | 295% |
| 17 | HUM | 15.7% | 16.3% | 6.3% | 24.1% | 75% | 45% |
| 18 | MO | 15.4% | 17.3% | 2.1% | 25.1% | 75% | 49% |
| 19 | GIS | 14.9% | 17.0% | -0.5% | 26.2% | 75% | 49% |
| 20 | TSN | 14.4% | 14.3% | 2.3% | 26.8% | 75% | 41% |

## Week-over-week

Previous run: 2026-08-28

- Entered Robust Top: CTSH
- Exited Robust Top: EOG
- Entered Upside Top: GIS, TSN
- Exited Upside Top: ELV, ZTS

Largest robust-rank moves:

- CIEN: 289 → 253 (+36)
- CARR: 325 → 298 (+27)
- ATO: 297 → 323 (-26)
- FICO: 225 → 200 (+25)
- CLX: 166 → 145 (+21)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| UHS | bear | 25% | 1.7% | 8.9% | 8.3% | 178.47 | 11.3% | 58% |
| UHS | base | 50% | 7.1% | 10.7% | 17.2% | 330.68 | 28.2% | 224% |
| UHS | bull | 25% | 11.4% | 12.1% | 19.5% | 468.69 | 37.9% | 367% |
| OMC | bear | 25% | 18.2% | 12.8% | 6.9% | 145.46 | 19.5% | 157% |
| OMC | base | 50% | 25.0% | 14.6% | 6.9% | 217.88 | 28.9% | 281% |
| OMC | bull | 25% | 30.4% | 15.9% | 6.9% | 284.74 | 35.7% | 395% |
| TTD | bear | 25% | 3.4% | 13.1% | 9.7% | 14.63 | 9.3% | 49% |
| TTD | base | 50% | 12.4% | 17.1% | 40.5% | 30.99 | 31.0% | 265% |
| TTD | bull | 25% | 19.5% | 20.7% | 43.5% | 42.97 | 41.0% | 418% |
| FOXA | bear | 25% | -1.3% | 17.3% | 7.0% | 67.31 | 7.8% | 40% |
| FOXA | base | 50% | 4.4% | 19.7% | 55.1% | 125.37 | 24.9% | 190% |
| FOXA | bull | 25% | 8.9% | 21.5% | 60.0% | 172.55 | 34.0% | 309% |
| CMCSA | bear | 25% | -6.6% | 16.1% | 6.5% | 30.89 | 11.8% | 62% |
| CMCSA | base | 50% | 0.7% | 18.7% | 6.5% | 40.90 | 17.2% | 120% |
| CMCSA | bull | 25% | 6.6% | 20.4% | 6.5% | 52.77 | 21.5% | 187% |
| ELV | bear | 25% | -0.7% | 4.9% | 7.4% | 442.14 | 9.2% | 49% |
| ELV | base | 50% | 5.5% | 5.9% | 7.4% | 497.22 | 11.5% | 74% |
| ELV | bull | 25% | 10.4% | 6.6% | 7.4% | 648.74 | 17.5% | 128% |
| HUM | bear | 25% | 13.8% | 2.5% | 8.1% | 372.94 | 6.3% | 36% |
| HUM | base | 50% | 19.1% | 3.7% | 8.1% | 583.49 | 16.3% | 114% |
| HUM | bull | 25% | 23.4% | 4.8% | 8.1% | 810.30 | 24.1% | 198% |
| MO | bear | 25% | -2.3% | 48.7% | 6.8% | 55.23 | 2.1% | 9% |
| MO | base | 50% | 1.3% | 54.9% | 45.6% | 102.61 | 17.3% | 112% |
| MO | bull | 25% | 4.1% | 60.1% | 46.5% | 138.07 | 25.1% | 189% |
| CF | bear | 25% | -10.3% | 22.8% | 7.0% | 101.97 | 0.5% | 2% |
| CF | base | 50% | 11.6% | 31.1% | 17.8% | 304.50 | 29.3% | 250% |
| CF | bull | 25% | 29.2% | 38.4% | 19.1% | 617.36 | 47.6% | 597% |
| DECK | bear | 25% | 7.5% | 15.9% | 10.4% | 67.99 | 4.0% | 18% |
| DECK | base | 50% | 12.3% | 18.9% | 57.8% | 101.06 | 14.8% | 92% |
| DECK | bull | 25% | 16.2% | 21.4% | 60.0% | 128.65 | 21.6% | 153% |
| ZTS | bear | 25% | -1.8% | 32.2% | 7.7% | 58.72 | 2.2% | 10% |
| ZTS | base | 50% | 2.8% | 36.0% | 24.3% | 100.44 | 15.7% | 100% |
| ZTS | bull | 25% | 6.4% | 39.1% | 24.5% | 133.06 | 23.1% | 172% |
| CTSH | bear | 25% | -0.4% | 12.8% | 8.5% | 51.40 | 3.9% | 18% |
| CTSH | base | 50% | 4.6% | 15.0% | 13.9% | 73.86 | 13.3% | 82% |
| CTSH | bull | 25% | 8.5% | 16.6% | 14.8% | 93.78 | 19.6% | 137% |

## Boundary Assumptions & Valuation Alerts

- UHS — bounds: share_change_floor_hit
- OMC — bounds: base_growth_cap_hit;reinvestment_cap_hit;intrinsic_2x_price
- TTD — bounds: intrinsic_2x_price
- VICI — bounds: specialist_model_v1
- ARE — bounds: specialist_model_v1
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit
- CPT — bounds: specialist_model_v1
- BXP — bounds: specialist_model_v1
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;wacc_floor_hit;reinvestment_cap_hit
- UDR — bounds: specialist_model_v1
- VMRK — bounds: specialist_model_v1
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- CF — bounds: share_change_floor_hit;intrinsic_2x_price
- HST — bounds: specialist_model_v1
- DECK — bounds: forward_roic_cap_hit
- INVH — bounds: specialist_model_v1

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| APP | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| ON | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- OMC: incremental_roic_below_wacc
- TTD: heavy_sbc
- VICI: nan
- ARE: nan
- CPT: nan
- BXP: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- UDR: nan
- VMRK: nan
- ELV: incremental_roic_below_wacc
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- CF: cyclical_revenue
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
- COF Capital One Financial Corporation — consumer_finance_model_not_supported
- SPGI S&P Global Inc. — financial_sector_model_not_supported
- KKR KKR & Co. Inc. — asset_management_model_not_supported
- ICE Intercontinental Exchange, Inc. — financial_sector_model_not_supported
- MCO Moody's Corporation — financial_sector_model_not_supported
- APO Apollo Global Management, Inc. — asset_management_model_not_supported
- STT State Street Corporation — asset_management_model_not_supported
- AMP Ameriprise Financial, Inc. — asset_management_model_not_supported
- ARES Ares Management Corporation — asset_management_model_not_supported
- MSCI MSCI Inc. — financial_sector_model_not_supported
- RJF Raymond James Financial, Inc. — asset_management_model_not_supported
- SYF Synchrony Financial — consumer_finance_model_not_supported
- GPN Global Payments Inc. — consumer_finance_model_not_supported
- BEN Franklin Resources, Inc. — asset_management_model_not_supported
- IVZ Invesco Ltd. — asset_management_model_not_supported
- FDS FactSet Research Systems Inc. — financial_sector_model_not_supported
- HOOD Robinhood Markets, Inc. — asset_management_model_not_supported
- CME CME Group Inc. — financial_sector_model_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- NDAQ Nasdaq, Inc. — financial_sector_model_not_supported
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- NTRS Northern Trust Corporation — asset_management_model_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- APP AppLovin Corporation — material_event_requires_reunderwriting
- ON ON Semiconductor Corporation — material_event_requires_reunderwriting
- XOM Exxon Mobil Corporation — insufficient_model_confidence
- HLT Hilton Worldwide Holdings Inc. — insufficient_model_confidence
- CCL Carnival Corporation & plc — insufficient_model_confidence
- MOS The Mosaic Company — insufficient_model_confidence
- GM General Motors Company — irr_below_solver_bound
- LHX L3Harris Technologies, Inc. — invalid_valuation_output
- BKNG Booking Holdings Inc. — roic_not_meaningful:meaningless_capital
- FTNT Fortinet, Inc. — roic_not_meaningful:meaningless_capital
- ABNB Airbnb, Inc. — roic_not_meaningful:meaningless_capital
- EXPE Expedia Group, Inc. — roic_not_meaningful:meaningless_capital
- VRSN VeriSign, Inc. — roic_not_meaningful:meaningless_capital
- CVX Chevron Corporation — insufficient_post_valuation_model_confidence
- COP ConocoPhillips — insufficient_post_valuation_model_confidence
- MPC Marathon Petroleum Corporation — insufficient_post_valuation_model_confidence
- FCX Freeport-McMoRan Inc. — insufficient_post_valuation_model_confidence
- PSX Phillips 66 — insufficient_post_valuation_model_confidence
- RCL Royal Caribbean Cruises Ltd. — insufficient_post_valuation_model_confidence
- TRGP Targa Resources Corp. — insufficient_post_valuation_model_confidence
- OXY Occidental Petroleum Corporation — insufficient_post_valuation_model_confidence
- NUE Nucor Corporation — insufficient_post_valuation_model_confidence
- DVN Devon Energy Corporation — insufficient_post_valuation_model_confidence
- XYZ Block, Inc. — insufficient_post_valuation_model_confidence
- IR Ingersoll Rand Inc. — insufficient_post_valuation_model_confidence
- IFF International Flavors & Fragrances Inc. — insufficient_post_valuation_model_confidence
- BLDR Builders FirstSource, Inc. — insufficient_post_valuation_model_confidence
- NVDA NVIDIA Corporation — insufficient_post_valuation_model_confidence
- TSLA Tesla, Inc. — insufficient_post_valuation_model_confidence
- AMD Advanced Micro Devices, Inc. — insufficient_post_valuation_model_confidence
- LITE Lumentum Holdings Inc. — insufficient_post_valuation_model_confidence
- STLD Steel Dynamics, Inc. — insufficient_post_valuation_model_confidence

## Data Gaps and Model Limitations

- Stocks missing core financials were rejected (fail closed), never estimated.
- Banks, insurers and REITs use conservative specialist models; rows with
  incomplete specialist inputs stay watchlisted instead of entering ranking.
- Asset managers, consumer-finance names, other financials and pre-profit
  biotech remain watchlisted until dedicated models exist.
- Scenario set is discrete (bear/base/bull); worst-case stress metrics are
  deterministic bear/base/bull stress labels, not calibrated CVaR.
- Ad-hoc market closures are not in the calendar; freshness checks catch them.
