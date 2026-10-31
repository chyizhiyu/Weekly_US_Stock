# Weekly US Stock Screen — 2026-10-30

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-10-30**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 515 | - |
| step2_hard_filters | 515 | 310 | adr_excluded: 32, persistent_negative_fcf: 23, interest_coverage: 18 |
| step3_standardize | 310 | 310 | - |
| step4_specialist_models | 93 | 58 | asset_management_model_not_supported: 17, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 310 | 301 | no_normalized_earnings: 9 |
| step5_quality_risk | 301 | 296 | - |
| step6_scenario_valuation | 296 | 273 | insufficient_post_valuation_model_confidence: 17, roic_not_meaningful:meaningless_capital: 5, invalid_valuation_output: 1 |
| step7_risk_adjusted_ranking | 331 | 331 | - |

## Eligible Candidates (7)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FOXA | 11.6% | 27.9% | 11.3% | 36.8% | 0.7% | 0% | 0.92 | 0.78 |
| 2 | UHS | 10.0% | 27.9% | 9.9% | 38.1% | 2.1% | 0% | 0.76 | 0.76 |
| 3 | ARE | 9.5% | 31.8% | 22.5% | 31.8% | 0.0% | 0% | 0.69 | 0.48 |
| 4 | VICI | 8.9% | 30.5% | 14.7% | 30.5% | 0.0% | 0% | 0.53 | 0.48 |
| 5 | CMCSA | 4.6% | 20.9% | 14.8% | 23.5% | 0.0% | 0% | 0.76 | 0.51 |
| 6 | BXP | 3.3% | 20.6% | 11.1% | 20.6% | 0.9% | 0% | 0.67 | 0.48 |
| 7 | CPT | 2.6% | 22.1% | 9.8% | 22.1% | 2.2% | 0% | 0.59 | 0.48 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FOXA | 11.6% | 27.9% | 11.3% | 36.8% | 0.7% | 0% | 0.92 | 0.78 |
| 2 | UHS | 10.0% | 27.9% | 9.9% | 38.1% | 2.1% | 0% | 0.76 | 0.76 |
| 3 | ARE | 9.5% | 31.8% | 22.5% | 31.8% | 0.0% | 0% | 0.69 | 0.48 |
| 4 | VICI | 8.9% | 30.5% | 14.7% | 30.5% | 0.0% | 0% | 0.53 | 0.48 |
| 5 | CMCSA | 4.6% | 20.9% | 14.8% | 23.5% | 0.0% | 0% | 0.76 | 0.51 |
| 6 | BXP | 3.3% | 20.6% | 11.1% | 20.6% | 0.9% | 0% | 0.67 | 0.48 |
| 7 | CPT | 2.6% | 22.1% | 9.8% | 22.1% | 2.2% | 0% | 0.59 | 0.48 |
| 8 | VMRK | -1.8% | 18.5% | 7.1% | 22.9% | 4.9% | 0% | 0.60 | 0.48 |
| 9 | OMC | -2.6% | 15.2% | 7.5% | 20.7% | 4.5% | 0% | 0.86 | 0.62 |
| 10 | CF | -2.7% | 31.2% | 2.3% | 49.3% | 9.7% | 0% | 0.89 | 0.36 |
| 11 | UDR | -2.7% | 19.4% | 5.7% | 19.4% | 6.3% | 0% | 0.54 | 0.48 |
| 12 | DECK | -3.9% | 16.5% | 5.1% | 23.7% | 6.9% | 0% | 0.96 | 0.67 |
| 13 | ELV | -4.2% | 10.7% | 7.8% | 16.7% | 4.2% | 0% | 0.84 | 0.67 |
| 14 | HUM | -4.8% | 15.1% | 5.2% | 22.9% | 6.8% | 0% | 0.76 | 0.62 |
| 15 | INVH | -5.7% | 15.8% | 4.4% | 15.8% | 7.6% | 0% | 0.60 | 0.48 |
| 16 | TSN | -6.2% | 15.7% | 3.6% | 28.6% | 8.4% | 0% | 0.60 | 0.58 |
| 17 | CTSH | -7.9% | 12.6% | 3.6% | 18.6% | 8.4% | 0% | 0.85 | 0.87 |
| 18 | HPQ | -7.9% | 4.1% | 4.1% | 10.1% | 7.9% | 0% | 0.97 | 0.67 |
| 19 | ADBE | -8.7% | 12.6% | 2.9% | 18.5% | 9.1% | 0% | 0.98 | 0.79 |
| 20 | O | -9.2% | 14.9% | 1.4% | 14.9% | 10.6% | 0% | 0.54 | 0.48 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | ARE | 29.4% | 31.8% | 22.5% | 31.8% | 100% | 297% |
| 2 | CF | 28.5% | 31.2% | 2.3% | 49.3% | 75% | 141% |
| 3 | CI | 28.4% | 32.1% | -11.8% | 61.4% | 75% | 178% |
| 4 | VICI | 26.5% | 30.5% | 14.7% | 30.5% | 100% | 278% |
| 5 | FOXA | 25.9% | 27.9% | 11.3% | 36.8% | 75% | 108% |
| 6 | UHS | 25.9% | 27.9% | 9.9% | 38.1% | 75% | 97% |
| 7 | CHTR | 23.4% | 55.4% | -95.0% | 77.8% | 75% | 416% |
| 8 | CMCSA | 20.0% | 20.9% | 14.8% | 23.5% | 100% | 77% |
| 9 | CPT | 19.0% | 22.1% | 9.8% | 22.1% | 75% | 172% |
| 10 | BXP | 18.2% | 20.6% | 11.1% | 20.6% | 75% | 155% |
| 11 | VMRK | 16.8% | 18.5% | 7.1% | 22.9% | 75% | 134% |
| 12 | FISV | 16.5% | 26.9% | -38.4% | 50.7% | 75% | 106% |
| 13 | UDR | 16.0% | 19.4% | 5.7% | 19.4% | 75% | 143% |
| 14 | TSN | 15.9% | 15.7% | 3.6% | 28.6% | 75% | 50% |
| 15 | DECK | 15.5% | 16.5% | 5.1% | 23.7% | 75% | 25% |
| 16 | APA | 15.0% | 16.1% | -7.0% | 35.0% | 75% | 66% |
| 17 | OMC | 14.6% | 15.2% | 7.5% | 20.7% | 75% | 115% |
| 18 | HUM | 14.6% | 15.1% | 5.2% | 22.9% | 75% | 37% |
| 19 | INVH | 13.0% | 15.8% | 4.4% | 15.8% | 75% | 108% |
| 20 | EOG | 12.1% | 12.3% | -5.9% | 29.4% | 75% | 25% |

## Week-over-week

Previous run: 2026-10-23

- Entered Robust Top: CTSH, HPQ
- Exited Robust Top: FRT, HST
- Entered Upside Top: APA
- Exited Upside Top: MO

Largest robust-rank moves:

- DVA: 231 → 96 (+135)
- FFIV: 163 → 101 (+62)
- TXT: 104 → 164 (-60)
- CHRW: 193 → 152 (+41)
- ECL: 236 → 273 (-37)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| FOXA | bear | 25% | -1.2% | 19.7% | 7.3% | 73.17 | 11.3% | 59% |
| FOXA | base | 50% | 4.4% | 22.2% | 46.3% | 131.37 | 27.9% | 221% |
| FOXA | bull | 25% | 8.8% | 24.1% | 49.9% | 177.98 | 36.8% | 344% |
| UHS | bear | 25% | 1.5% | 8.8% | 8.0% | 177.31 | 9.9% | 51% |
| UHS | base | 50% | 7.1% | 10.7% | 16.7% | 346.18 | 27.9% | 223% |
| UHS | bull | 25% | 11.5% | 12.1% | 19.0% | 500.14 | 38.1% | 375% |
| CMCSA | bear | 25% | -6.8% | 16.1% | 6.5% | 30.35 | 14.8% | 81% |
| CMCSA | base | 50% | 0.4% | 18.7% | 6.5% | 41.17 | 20.9% | 150% |
| CMCSA | bull | 25% | 6.1% | 20.4% | 6.5% | 50.68 | 23.5% | 215% |
| OMC | bear | 25% | 18.8% | 12.9% | 7.2% | 120.91 | 7.5% | 46% |
| OMC | base | 50% | 25.0% | 14.6% | 7.2% | 174.99 | 15.2% | 110% |
| OMC | bull | 25% | 30.0% | 15.9% | 7.2% | 223.44 | 20.7% | 168% |
| CF | bear | 25% | -10.0% | 22.8% | 7.1% | 101.09 | 2.3% | 10% |
| CF | base | 50% | 12.0% | 31.1% | 17.8% | 297.61 | 31.2% | 274% |
| CF | bull | 25% | 29.6% | 38.4% | 19.1% | 600.10 | 49.3% | 638% |
| DECK | bear | 25% | 7.5% | 15.9% | 10.3% | 67.67 | 5.1% | 24% |
| DECK | base | 50% | 12.3% | 18.9% | 57.8% | 102.50 | 16.5% | 105% |
| DECK | bull | 25% | 16.2% | 21.4% | 60.0% | 131.54 | 23.7% | 173% |
| ELV | bear | 25% | -0.1% | 4.9% | 7.6% | 426.31 | 7.8% | 41% |
| ELV | base | 50% | 6.2% | 5.9% | 7.6% | 489.87 | 10.7% | 68% |
| ELV | bull | 25% | 11.2% | 6.6% | 7.6% | 639.39 | 16.7% | 120% |
| HUM | bear | 25% | 13.8% | 2.5% | 8.3% | 363.66 | 5.2% | 29% |
| HUM | base | 50% | 19.2% | 3.7% | 8.3% | 568.11 | 15.1% | 103% |
| HUM | bull | 25% | 23.5% | 4.8% | 8.3% | 788.45 | 22.9% | 183% |
| TSN | bear | 25% | -4.0% | 4.2% | 7.3% | 48.46 | 3.6% | 18% |
| TSN | base | 50% | 3.4% | 6.8% | 7.3% | 85.29 | 15.7% | 118% |
| TSN | bull | 25% | 9.3% | 8.9% | 7.3% | 148.88 | 28.6% | 278% |
| CTSH | bear | 25% | -0.5% | 12.8% | 8.9% | 52.46 | 3.6% | 17% |
| CTSH | base | 50% | 4.5% | 15.0% | 14.0% | 73.80 | 12.6% | 77% |
| CTSH | bull | 25% | 8.4% | 16.6% | 14.9% | 92.79 | 18.6% | 129% |
| HPQ | bear | 25% | -1.4% | 5.7% | 9.4% | 23.90 | 5.7% | 27% |
| HPQ | base | 50% | 3.9% | 6.6% | 9.4% | 21.02 | 4.1% | 24% |
| HPQ | bull | 25% | 8.1% | 7.3% | 9.4% | 28.81 | 10.1% | 67% |
| ADBE | bear | 25% | 9.1% | 29.7% | 11.6% | 176.19 | 2.9% | 13% |
| ADBE | base | 50% | 13.6% | 33.6% | 58.7% | 254.78 | 12.6% | 75% |
| ADBE | bull | 25% | 17.1% | 36.9% | 59.8% | 315.10 | 18.5% | 124% |

**Scenario order inversions** (named bear/base/bull intrinsic value is not monotone — this is economic, not a bug):
- HPQ: growth destroys value: forward ROIC 2.0% at/below WACC 9.4%, so higher-growth scenarios reinvest below the cost of capital and are worth less than the bear case

## Boundary Assumptions & Valuation Alerts

- FOXA — bounds: share_change_floor_hit;intrinsic_2x_price
- UHS — bounds: share_change_floor_hit
- ARE — bounds: specialist_model_v1
- VICI — bounds: specialist_model_v1
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;reinvestment_cap_hit
- BXP — bounds: specialist_model_v1
- CPT — bounds: specialist_model_v1
- VMRK — bounds: specialist_model_v1
- OMC — bounds: base_growth_cap_hit;share_change_cap_hit;reinvestment_cap_hit;intrinsic_2x_price
- CF — bounds: share_change_floor_hit;intrinsic_2x_price
- UDR — bounds: specialist_model_v1
- DECK — bounds: forward_roic_cap_hit;share_change_floor_hit
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- INVH — bounds: specialist_model_v1
- TSN — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HPQ — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- ADBE — bounds: share_change_floor_hit
- O — bounds: specialist_model_v1

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| NOW | weekly_drop | - | - | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- ARE: nan
- VICI: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- BXP: nan
- CPT: nan
- VMRK: nan
- OMC: ongoing_dilution, incremental_roic_below_wacc
- CF: cyclical_revenue
- UDR: nan
- ELV: incremental_roic_below_wacc
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- INVH: nan
- TSN: thin_interest_coverage, incremental_roic_below_wacc
- HPQ: incremental_roic_below_wacc
- ADBE: heavy_sbc
- O: nan

## Watchlist (not rankable under the general model)

- V Visa Inc. — consumer_finance_model_not_supported
- MA Mastercard Incorporated — consumer_finance_model_not_supported
- MS Morgan Stanley — asset_management_model_not_supported
- GS The Goldman Sachs Group, Inc. — asset_management_model_not_supported
- AXP American Express Company — consumer_finance_model_not_supported
- BLK BlackRock, Inc. — asset_management_model_not_supported
- SCHW The Charles Schwab Corporation — asset_management_model_not_supported
- SPGI S&P Global Inc. — financial_sector_model_not_supported
- BX Blackstone Inc. — asset_management_model_not_supported
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
- GPN Global Payments Inc. — consumer_finance_model_not_supported
- SYF Synchrony Financial — consumer_finance_model_not_supported
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
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- NOW ServiceNow, Inc. — material_event_requires_reunderwriting
- XOM Exxonmobil Holdings Corporation — insufficient_model_confidence
- CCL Carnival Corporation & plc — insufficient_model_confidence
- NRG NRG Energy, Inc. — insufficient_model_confidence
- MOS The Mosaic Company — insufficient_model_confidence
- TSLA Tesla, Inc. — insufficient_model_confidence
- LHX L3Harris Technologies, Inc. — invalid_valuation_output
- BKNG Booking Holdings Inc. — roic_not_meaningful:meaningless_capital
- FTNT Fortinet, Inc. — roic_not_meaningful:meaningless_capital
- ABNB Airbnb, Inc. — roic_not_meaningful:meaningless_capital
- EXPE Expedia Group, Inc. — roic_not_meaningful:meaningless_capital
- VRSN VeriSign, Inc. — roic_not_meaningful:meaningless_capital
- CVX Chevron Corporation — insufficient_post_valuation_model_confidence
- COP ConocoPhillips — insufficient_post_valuation_model_confidence
- MPC Marathon Petroleum Corporation — insufficient_post_valuation_model_confidence
- PSX Phillips 66 — insufficient_post_valuation_model_confidence
- FCX Freeport-McMoRan Inc. — insufficient_post_valuation_model_confidence
- RCL Royal Caribbean Cruises Ltd. — insufficient_post_valuation_model_confidence
- OXY Occidental Petroleum Corporation — insufficient_post_valuation_model_confidence
- NUE Nucor Corporation — insufficient_post_valuation_model_confidence
- DVN Devon Energy Corporation — insufficient_post_valuation_model_confidence
- XYZ Block, Inc. — insufficient_post_valuation_model_confidence
- IFF International Flavors & Fragrances Inc. — insufficient_post_valuation_model_confidence
- NVDA NVIDIA Corporation — insufficient_post_valuation_model_confidence
- MU Micron Technology, Inc. — insufficient_post_valuation_model_confidence
- AMD Advanced Micro Devices, Inc. — insufficient_post_valuation_model_confidence
- APP AppLovin Corporation — insufficient_post_valuation_model_confidence
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
