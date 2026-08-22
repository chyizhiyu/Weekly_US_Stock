# Weekly US Stock Screen — 2026-08-21

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-08-21**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 517 | - |
| step2_hard_filters | 517 | 308 | adr_excluded: 32, persistent_negative_fcf: 23, interest_coverage: 17 |
| step3_standardize | 308 | 308 | - |
| step4_specialist_models | 94 | 59 | asset_management_model_not_supported: 17, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 308 | 300 | no_normalized_earnings: 8 |
| step5_quality_risk | 300 | 296 | - |
| step6_scenario_valuation | 296 | 270 | insufficient_post_valuation_model_confidence: 19, roic_not_meaningful:meaningless_capital: 5, irr_below_solver_bound: 1 |
| step7_risk_adjusted_ranking | 329 | 329 | - |

## Eligible Candidates (8)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | OMC | 10.5% | 27.5% | 18.2% | 34.2% | 0.0% | 0% | 0.83 | 0.68 |
| 2 | UHS | 9.6% | 26.8% | 10.2% | 36.4% | 1.8% | 0% | 0.78 | 0.77 |
| 3 | VICI | 8.7% | 30.2% | 13.7% | 30.2% | 0.0% | 0% | 0.51 | 0.48 |
| 4 | ARE | 6.0% | 24.5% | 15.4% | 24.5% | 0.0% | 0% | 0.68 | 0.48 |
| 5 | CPT | 2.9% | 23.0% | 9.6% | 23.0% | 2.4% | 0% | 0.56 | 0.48 |
| 6 | FOXA | 2.8% | 23.6% | 6.8% | 32.7% | 5.2% | 0% | 0.91 | 0.69 |
| 7 | BXP | 2.5% | 20.4% | 10.5% | 20.4% | 1.5% | 0% | 0.65 | 0.48 |
| 8 | CMCSA | 1.7% | 16.9% | 11.4% | 21.3% | 0.6% | 0% | 0.76 | 0.46 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | OMC | 10.5% | 27.5% | 18.2% | 34.2% | 0.0% | 0% | 0.83 | 0.68 |
| 2 | UHS | 9.6% | 26.8% | 10.2% | 36.4% | 1.8% | 0% | 0.78 | 0.77 |
| 3 | VICI | 8.7% | 30.2% | 13.7% | 30.2% | 0.0% | 0% | 0.51 | 0.48 |
| 4 | ARE | 6.0% | 24.5% | 15.4% | 24.5% | 0.0% | 0% | 0.68 | 0.48 |
| 5 | CPT | 2.9% | 23.0% | 9.6% | 23.0% | 2.4% | 0% | 0.56 | 0.48 |
| 6 | FOXA | 2.8% | 23.6% | 6.8% | 32.7% | 5.2% | 0% | 0.91 | 0.69 |
| 7 | BXP | 2.5% | 20.4% | 10.5% | 20.4% | 1.5% | 0% | 0.65 | 0.48 |
| 8 | CMCSA | 1.7% | 16.9% | 11.4% | 21.3% | 0.6% | 0% | 0.76 | 0.46 |
| 9 | HUM | -1.0% | 17.8% | 7.5% | 25.9% | 4.5% | 0% | 0.76 | 0.61 |
| 10 | UDR | -2.0% | 20.8% | 5.8% | 20.8% | 6.2% | 0% | 0.51 | 0.48 |
| 11 | ELV | -2.3% | 12.0% | 9.7% | 18.0% | 2.3% | 0% | 0.82 | 0.67 |
| 12 | MO | -2.6% | 18.7% | 3.2% | 26.6% | 8.8% | 0% | 0.98 | 0.92 |
| 13 | VMRK | -2.7% | 18.2% | 6.3% | 22.9% | 5.7% | 0% | 0.59 | 0.48 |
| 14 | CF | -3.6% | 30.7% | 1.6% | 49.0% | 10.4% | 0% | 0.89 | 0.37 |
| 15 | CTSH | -6.4% | 13.6% | 4.2% | 19.9% | 7.8% | 0% | 0.86 | 0.87 |
| 16 | HST | -7.1% | 13.1% | 4.4% | 13.1% | 7.6% | 0% | 0.67 | 0.48 |
| 17 | ZTS | -7.3% | 15.2% | 1.8% | 22.6% | 10.2% | 0% | 0.98 | 0.89 |
| 18 | INVH | -8.3% | 14.3% | 2.6% | 14.3% | 9.4% | 0% | 0.58 | 0.48 |
| 19 | DECK | -8.8% | 13.0% | 2.4% | 19.8% | 9.6% | 0% | 0.96 | 0.75 |
| 20 | EOG | -9.2% | 24.2% | -2.2% | 42.4% | 14.2% | 0% | 0.87 | 0.41 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | CI | 31.9% | 35.5% | -9.3% | 65.7% | 75% | 219% |
| 2 | CF | 28.0% | 30.7% | 1.6% | 49.0% | 75% | 140% |
| 3 | OMC | 26.9% | 27.5% | 18.2% | 34.2% | 100% | 148% |
| 4 | VICI | 26.1% | 30.2% | 13.7% | 30.2% | 100% | 274% |
| 5 | UHS | 25.0% | 26.8% | 10.2% | 36.4% | 75% | 86% |
| 6 | ARE | 22.2% | 24.5% | 15.4% | 24.5% | 100% | 199% |
| 7 | EOG | 22.2% | 24.2% | -2.2% | 42.4% | 75% | 96% |
| 8 | FOXA | 21.7% | 23.6% | 6.8% | 32.7% | 75% | 84% |
| 9 | CPT | 19.6% | 23.0% | 9.6% | 23.0% | 75% | 181% |
| 10 | BXP | 17.9% | 20.4% | 10.5% | 20.4% | 75% | 153% |
| 11 | HUM | 17.2% | 17.8% | 7.5% | 25.9% | 75% | 55% |
| 12 | UDR | 17.1% | 20.8% | 5.8% | 20.8% | 75% | 158% |
| 13 | MO | 16.8% | 18.7% | 3.2% | 26.6% | 75% | 57% |
| 14 | CMCSA | 16.6% | 16.9% | 11.4% | 21.3% | 75% | 52% |
| 15 | FISV | 16.5% | 26.4% | -36.8% | 50.1% | 75% | 103% |
| 16 | CHTR | 16.5% | 46.5% | -95.0% | 67.7% | 75% | 307% |
| 17 | VMRK | 16.4% | 18.2% | 6.3% | 22.9% | 75% | 131% |
| 18 | GIS | 13.9% | 15.9% | -1.4% | 25.0% | 75% | 43% |
| 19 | ZTS | 13.7% | 15.2% | 1.8% | 22.6% | 75% | 30% |
| 20 | ELV | 12.9% | 12.0% | 9.7% | 18.0% | 25% | 25% |

## Week-over-week

Previous run: 2026-08-14

- Entered Robust Top: CF, DECK, VMRK
- Exited Robust Top: AVB, EQR, TTD
- Entered Upside Top: CF, CI, ELV, VMRK
- Exited Upside Top: AVB, CTSH, EQR, TTD

Largest robust-rank moves:

- DE: 321 → 183 (+138)
- FISV: 205 → 247 (-42)
- EL: 292 → 326 (-34)
- FICO: 207 → 230 (-23)
- PFE: 210 → 232 (-22)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| OMC | bear | 25% | 18.2% | 12.8% | 6.9% | 145.18 | 18.2% | 142% |
| OMC | base | 50% | 25.0% | 14.6% | 6.9% | 217.51 | 27.5% | 259% |
| OMC | bull | 25% | 30.4% | 15.9% | 6.9% | 284.29 | 34.2% | 367% |
| UHS | bear | 25% | 1.9% | 8.9% | 8.3% | 178.96 | 10.2% | 52% |
| UHS | base | 50% | 7.1% | 10.7% | 17.2% | 329.70 | 26.8% | 208% |
| UHS | bull | 25% | 11.3% | 12.1% | 19.5% | 465.15 | 36.4% | 343% |
| FOXA | bear | 25% | -1.3% | 17.3% | 6.9% | 67.51 | 6.8% | 34% |
| FOXA | base | 50% | 4.4% | 19.7% | 55.1% | 125.91 | 23.6% | 177% |
| FOXA | bull | 25% | 8.8% | 21.5% | 60.0% | 173.38 | 32.7% | 291% |
| CMCSA | bear | 25% | -6.6% | 16.1% | 6.5% | 30.89 | 11.4% | 60% |
| CMCSA | base | 50% | 0.7% | 18.7% | 6.5% | 40.90 | 16.9% | 117% |
| CMCSA | bull | 25% | 6.6% | 20.4% | 6.5% | 52.77 | 21.3% | 184% |
| HUM | bear | 25% | 13.4% | 2.5% | 8.1% | 372.77 | 7.5% | 43% |
| HUM | base | 50% | 19.1% | 3.7% | 8.1% | 588.39 | 17.8% | 128% |
| HUM | bull | 25% | 23.7% | 4.8% | 8.1% | 823.13 | 25.9% | 220% |
| ELV | bear | 25% | -0.7% | 4.9% | 7.3% | 445.46 | 9.7% | 52% |
| ELV | base | 50% | 5.4% | 5.9% | 7.3% | 501.25 | 12.0% | 78% |
| ELV | bull | 25% | 10.4% | 6.6% | 7.3% | 653.98 | 18.0% | 133% |
| MO | bear | 25% | -2.3% | 48.7% | 6.8% | 55.78 | 3.2% | 15% |
| MO | base | 50% | 1.3% | 54.9% | 45.6% | 104.07 | 18.7% | 124% |
| MO | bull | 25% | 4.1% | 60.1% | 46.5% | 140.25 | 26.6% | 206% |
| CF | bear | 25% | -9.9% | 22.8% | 6.9% | 103.96 | 1.6% | 7% |
| CF | base | 50% | 12.0% | 31.1% | 17.8% | 310.63 | 30.7% | 268% |
| CF | bull | 25% | 29.6% | 38.4% | 19.1% | 630.82 | 49.0% | 632% |
| CTSH | bear | 25% | -0.4% | 12.8% | 8.5% | 51.68 | 4.2% | 20% |
| CTSH | base | 50% | 4.6% | 15.0% | 13.9% | 74.39 | 13.6% | 84% |
| CTSH | bull | 25% | 8.5% | 16.6% | 14.8% | 94.52 | 19.9% | 141% |
| ZTS | bear | 25% | -1.7% | 32.2% | 7.6% | 59.27 | 1.8% | 8% |
| ZTS | base | 50% | 2.9% | 36.0% | 24.3% | 101.41 | 15.2% | 97% |
| ZTS | bull | 25% | 6.6% | 39.1% | 24.5% | 134.40 | 22.6% | 167% |
| DECK | bear | 25% | 7.5% | 15.9% | 10.4% | 68.15 | 2.4% | 11% |
| DECK | base | 50% | 12.3% | 18.9% | 57.8% | 101.37 | 13.0% | 79% |
| DECK | bull | 25% | 16.2% | 21.4% | 60.0% | 129.09 | 19.8% | 136% |
| EOG | bear | 25% | -8.3% | 22.6% | 7.0% | 103.77 | -2.2% | -9% |
| EOG | base | 50% | 13.9% | 32.4% | 14.3% | 300.32 | 24.2% | 190% |
| EOG | bull | 25% | 31.7% | 41.1% | 15.4% | 620.86 | 42.4% | 496% |

## Boundary Assumptions & Valuation Alerts

- OMC — bounds: base_growth_cap_hit;reinvestment_cap_hit;intrinsic_2x_price
- UHS — bounds: share_change_floor_hit
- VICI — bounds: specialist_model_v1
- ARE — bounds: specialist_model_v1
- CPT — bounds: specialist_model_v1
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit
- BXP — bounds: specialist_model_v1
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;wacc_floor_hit;reinvestment_cap_hit
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- UDR — bounds: specialist_model_v1
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- VMRK — bounds: specialist_model_v1
- CF — bounds: share_change_floor_hit;intrinsic_2x_price
- HST — bounds: specialist_model_v1
- INVH — bounds: specialist_model_v1
- DECK — bounds: forward_roic_cap_hit
- EOG — bounds: reinvestment_cap_hit

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| ORCL | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| GLW | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| APP | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| ON | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| TTD | drawdown_from_high | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- OMC: incremental_roic_below_wacc
- VICI: nan
- ARE: nan
- CPT: nan
- BXP: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- UDR: nan
- ELV: incremental_roic_below_wacc
- VMRK: nan
- CF: cyclical_revenue
- HST: nan
- INVH: nan
- EOG: cyclical_revenue

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
- CME CME Group Inc. — financial_sector_model_not_supported
- HOOD Robinhood Markets, Inc. — asset_management_model_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- NDAQ Nasdaq, Inc. — financial_sector_model_not_supported
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- NTRS Northern Trust Corporation — asset_management_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- ORCL Oracle Corporation — material_event_requires_reunderwriting
- GLW Corning Inc — material_event_requires_reunderwriting
- APP AppLovin Corporation — material_event_requires_reunderwriting
- ON ON Semiconductor Corporation — material_event_requires_reunderwriting
- TTD The Trade Desk, Inc. — material_event_requires_reunderwriting
- XOM Exxon Mobil Corporation — insufficient_model_confidence
- CCL Carnival Corporation & plc — insufficient_model_confidence
- NRG NRG Energy, Inc. — insufficient_model_confidence
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
- FCX Freeport-McMoRan Inc. — insufficient_post_valuation_model_confidence
- MPC Marathon Petroleum Corporation — insufficient_post_valuation_model_confidence
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
