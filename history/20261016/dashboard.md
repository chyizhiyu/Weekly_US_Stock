# Weekly US Stock Screen — 2026-10-16

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-10-16**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 515 | - |
| step2_hard_filters | 515 | 310 | adr_excluded: 32, persistent_negative_fcf: 23, interest_coverage: 18 |
| step3_standardize | 310 | 310 | - |
| step4_specialist_models | 94 | 59 | asset_management_model_not_supported: 17, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 310 | 301 | no_normalized_earnings: 9 |
| step5_quality_risk | 301 | 296 | - |
| step6_scenario_valuation | 296 | 269 | insufficient_post_valuation_model_confidence: 19, roic_not_meaningful:meaningless_capital: 6, irr_below_solver_bound: 1 |
| step7_risk_adjusted_ranking | 328 | 328 | - |

## Eligible Candidates (7)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ARE | 8.7% | 30.0% | 21.1% | 30.0% | 0.0% | 0% | 0.70 | 0.48 |
| 2 | VICI | 8.5% | 29.7% | 14.8% | 29.7% | 0.0% | 0% | 0.54 | 0.48 |
| 3 | UHS | 5.6% | 24.3% | 8.1% | 33.9% | 3.9% | 0% | 0.78 | 0.76 |
| 4 | CMCSA | 5.1% | 21.9% | 15.9% | 24.8% | 0.0% | 0% | 0.76 | 0.51 |
| 5 | BXP | 4.3% | 21.2% | 11.9% | 21.2% | 0.1% | 0% | 0.67 | 0.48 |
| 6 | FOXA | 2.1% | 22.7% | 6.8% | 31.4% | 5.2% | 0% | 0.90 | 0.69 |
| 7 | CPT | 2.1% | 21.4% | 9.6% | 21.4% | 2.4% | 0% | 0.60 | 0.48 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ARE | 8.7% | 30.0% | 21.1% | 30.0% | 0.0% | 0% | 0.70 | 0.48 |
| 2 | VICI | 8.5% | 29.7% | 14.8% | 29.7% | 0.0% | 0% | 0.54 | 0.48 |
| 3 | UHS | 5.6% | 24.3% | 8.1% | 33.9% | 3.9% | 0% | 0.78 | 0.76 |
| 4 | CMCSA | 5.1% | 21.9% | 15.9% | 24.8% | 0.0% | 0% | 0.76 | 0.51 |
| 5 | BXP | 4.3% | 21.2% | 11.9% | 21.2% | 0.1% | 0% | 0.67 | 0.48 |
| 6 | FOXA | 2.1% | 22.7% | 6.8% | 31.4% | 5.2% | 0% | 0.90 | 0.69 |
| 7 | CPT | 2.1% | 21.4% | 9.6% | 21.4% | 2.4% | 0% | 0.60 | 0.48 |
| 8 | VMRK | -2.6% | 17.7% | 6.7% | 21.8% | 5.3% | 0% | 0.61 | 0.48 |
| 9 | CF | -2.8% | 31.0% | 2.3% | 48.8% | 9.7% | 0% | 0.89 | 0.36 |
| 10 | UDR | -2.9% | 18.9% | 5.8% | 18.9% | 6.2% | 0% | 0.56 | 0.48 |
| 11 | ELV | -5.0% | 9.3% | 7.0% | 15.1% | 5.0% | 0% | 0.81 | 0.67 |
| 12 | HUM | -5.2% | 14.9% | 5.0% | 22.6% | 7.0% | 0% | 0.76 | 0.62 |
| 13 | TSN | -5.6% | 16.0% | 4.1% | 29.0% | 7.9% | 0% | 0.60 | 0.58 |
| 14 | DECK | -6.2% | 14.6% | 3.9% | 21.5% | 8.1% | 0% | 0.96 | 0.75 |
| 15 | INVH | -7.5% | 14.3% | 3.4% | 14.3% | 8.6% | 0% | 0.61 | 0.48 |
| 16 | ADBE | -8.2% | 12.8% | 3.2% | 18.7% | 8.8% | 0% | 0.98 | 0.79 |
| 17 | OMC | -8.4% | 11.6% | 3.6% | 17.3% | 8.4% | 0% | 0.83 | 0.61 |
| 18 | HST | -9.3% | 10.7% | 2.7% | 10.7% | 9.3% | 0% | 0.69 | 0.48 |
| 19 | HPQ | -9.3% | 2.7% | 2.7% | 8.7% | 9.3% | 0% | 0.97 | 0.67 |
| 20 | O | -10.0% | 13.8% | 1.1% | 13.8% | 10.9% | 0% | 0.55 | 0.48 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | CF | 28.3% | 31.0% | 2.3% | 48.8% | 75% | 137% |
| 2 | ARE | 27.8% | 30.0% | 21.1% | 30.0% | 100% | 272% |
| 3 | CI | 27.1% | 30.8% | -13.1% | 59.8% | 75% | 163% |
| 4 | VICI | 26.0% | 29.7% | 14.8% | 29.7% | 100% | 268% |
| 5 | UHS | 22.7% | 24.3% | 8.1% | 33.9% | 75% | 69% |
| 6 | CHTR | 22.4% | 53.9% | -95.0% | 76.6% | 75% | 393% |
| 7 | CMCSA | 21.1% | 21.9% | 15.9% | 24.8% | 100% | 85% |
| 8 | FOXA | 20.9% | 22.7% | 6.8% | 31.4% | 75% | 73% |
| 9 | BXP | 18.9% | 21.2% | 11.9% | 21.2% | 75% | 161% |
| 10 | CPT | 18.5% | 21.4% | 9.6% | 21.4% | 75% | 164% |
| 11 | FISV | 16.5% | 27.6% | -40.8% | 51.7% | 75% | 111% |
| 12 | TSN | 16.3% | 16.0% | 4.1% | 29.0% | 75% | 51% |
| 13 | VMRK | 16.0% | 17.7% | 6.7% | 21.8% | 75% | 126% |
| 14 | UDR | 15.6% | 18.9% | 5.8% | 18.9% | 75% | 138% |
| 15 | HUM | 14.3% | 14.9% | 5.0% | 22.6% | 75% | 35% |
| 16 | DECK | 13.6% | 14.6% | 3.9% | 21.5% | 75% | 17% |
| 17 | EOG | 12.2% | 12.4% | -5.7% | 29.4% | 75% | 25% |
| 18 | ADBE | 11.9% | 12.8% | 3.2% | 18.7% | 75% | 2% |
| 19 | MKC | 11.8% | 13.4% | -1.7% | 22.2% | 75% | 26% |
| 20 | LEN | 11.8% | 13.9% | -0.7% | 20.1% | 75% | 9% |

## Week-over-week

Previous run: 2026-10-09

- Entered Robust Top: HPQ, O, TSN
- Exited Robust Top: CTSH, GIS, MKC
- Entered Upside Top: ADBE, LEN, TSN
- Exited Upside Top: CTSH, GIS, ZTS

Largest robust-rank moves:

- JBHT: 198 → 227 (-29)
- AMAT: 208 → 182 (+26)
- LRCX: 225 → 199 (+26)
- ANET: 214 → 190 (+24)
- AKAM: 246 → 223 (+23)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| UHS | bear | 25% | 1.6% | 8.8% | 8.5% | 170.38 | 8.1% | 40% |
| UHS | base | 50% | 7.1% | 10.7% | 17.2% | 313.46 | 24.3% | 182% |
| UHS | bull | 25% | 11.4% | 12.1% | 19.5% | 443.23 | 33.9% | 307% |
| CMCSA | bear | 25% | -6.9% | 16.1% | 6.6% | 29.62 | 15.9% | 88% |
| CMCSA | base | 50% | 0.4% | 18.7% | 6.6% | 40.43 | 21.9% | 162% |
| CMCSA | bull | 25% | 6.3% | 20.4% | 6.6% | 50.60 | 24.8% | 235% |
| FOXA | bear | 25% | -1.4% | 17.3% | 7.5% | 61.63 | 6.8% | 33% |
| FOXA | base | 50% | 4.4% | 19.7% | 54.7% | 110.71 | 22.7% | 165% |
| FOXA | bull | 25% | 8.9% | 21.5% | 60.0% | 150.46 | 31.4% | 270% |
| CF | bear | 25% | -10.2% | 22.8% | 7.2% | 98.47 | 2.3% | 10% |
| CF | base | 50% | 11.8% | 31.1% | 17.9% | 286.92 | 31.0% | 270% |
| CF | bull | 25% | 29.4% | 38.4% | 19.1% | 575.25 | 48.8% | 627% |
| ELV | bear | 25% | -0.8% | 4.8% | 7.8% | 418.27 | 7.0% | 36% |
| ELV | base | 50% | 5.4% | 5.9% | 7.8% | 462.85 | 9.3% | 57% |
| ELV | bull | 25% | 10.4% | 6.6% | 7.8% | 604.16 | 15.1% | 105% |
| HUM | bear | 25% | 13.7% | 2.5% | 8.4% | 356.31 | 5.0% | 28% |
| HUM | base | 50% | 19.1% | 3.7% | 8.4% | 555.89 | 14.9% | 101% |
| HUM | bull | 25% | 23.5% | 4.8% | 8.4% | 771.03 | 22.6% | 179% |
| TSN | bear | 25% | -3.9% | 4.2% | 7.4% | 47.20 | 4.1% | 20% |
| TSN | base | 50% | 3.5% | 6.8% | 7.4% | 82.84 | 16.0% | 122% |
| TSN | bull | 25% | 9.4% | 8.9% | 7.4% | 145.01 | 29.0% | 285% |
| DECK | bear | 25% | 7.5% | 15.9% | 10.5% | 67.48 | 3.9% | 18% |
| DECK | base | 50% | 12.3% | 18.9% | 57.8% | 100.03 | 14.6% | 91% |
| DECK | bull | 25% | 16.2% | 21.4% | 60.0% | 127.20 | 21.5% | 151% |
| ADBE | bear | 25% | 9.1% | 29.7% | 11.7% | 173.77 | 3.2% | 15% |
| ADBE | base | 50% | 13.6% | 33.6% | 58.7% | 250.30 | 12.8% | 77% |
| ADBE | bull | 25% | 17.1% | 36.9% | 59.8% | 309.22 | 18.7% | 125% |
| OMC | bear | 25% | 18.6% | 12.8% | 7.3% | 97.59 | 3.6% | 21% |
| OMC | base | 50% | 25.0% | 14.6% | 7.3% | 145.62 | 11.6% | 78% |
| OMC | bull | 25% | 30.1% | 15.9% | 7.3% | 189.32 | 17.3% | 131% |
| HPQ | bear | 25% | -1.4% | 5.7% | 9.6% | 23.24 | 4.1% | 19% |
| HPQ | base | 50% | 3.9% | 6.6% | 9.6% | 20.17 | 2.7% | 16% |
| HPQ | bull | 25% | 8.1% | 7.3% | 9.6% | 27.73 | 8.7% | 56% |

**Scenario order inversions** (named bear/base/bull intrinsic value is not monotone — this is economic, not a bug):
- HPQ: growth destroys value: forward ROIC 2.0% at/below WACC 9.6%, so higher-growth scenarios reinvest below the cost of capital and are worth less than the bear case

## Boundary Assumptions & Valuation Alerts

- ARE — bounds: specialist_model_v1
- VICI — bounds: specialist_model_v1
- UHS — bounds: share_change_floor_hit
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;reinvestment_cap_hit
- BXP — bounds: specialist_model_v1
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit
- CPT — bounds: specialist_model_v1
- VMRK — bounds: specialist_model_v1
- CF — bounds: share_change_floor_hit;intrinsic_2x_price
- UDR — bounds: specialist_model_v1
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- TSN — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- DECK — bounds: forward_roic_cap_hit
- INVH — bounds: specialist_model_v1
- ADBE — bounds: share_change_floor_hit
- OMC — bounds: base_growth_cap_hit;share_change_cap_hit;reinvestment_cap_hit
- HST — bounds: specialist_model_v1
- HPQ — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- O — bounds: specialist_model_v1

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| FICO | drawdown_from_high | nan% | -42% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| TER | weekly_drop | -28% | nan% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- ARE: nan
- VICI: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- BXP: nan
- CPT: nan
- VMRK: nan
- CF: cyclical_revenue
- UDR: nan
- ELV: incremental_roic_below_wacc
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- TSN: thin_interest_coverage, incremental_roic_below_wacc
- INVH: nan
- ADBE: heavy_sbc
- OMC: ongoing_dilution, incremental_roic_below_wacc
- HST: nan
- HPQ: incremental_roic_below_wacc
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
- COF Capital One Financial Corporation — consumer_finance_model_not_supported
- BX Blackstone Inc. — asset_management_model_not_supported
- ICE Intercontinental Exchange, Inc. — financial_sector_model_not_supported
- MCO Moody's Corporation — financial_sector_model_not_supported
- KKR KKR & Co. Inc. — asset_management_model_not_supported
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
- CME CME Group Inc. — financial_sector_model_not_supported
- HOOD Robinhood Markets, Inc. — asset_management_model_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- NDAQ Nasdaq, Inc. — financial_sector_model_not_supported
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- NTRS Northern Trust Corporation — asset_management_model_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- FICO Fair Isaac Corporation — material_event_requires_reunderwriting
- TER Teradyne, Inc. — material_event_requires_reunderwriting
- XOM Exxonmobil Holdings Corporation — insufficient_model_confidence
- CVX Chevron Corporation — insufficient_model_confidence
- PSX Phillips 66 — insufficient_model_confidence
- CCL Carnival Corporation & plc — insufficient_model_confidence
- MOS The Mosaic Company — insufficient_model_confidence
- GM General Motors Company — irr_below_solver_bound
- LHX L3Harris Technologies, Inc. — invalid_valuation_output
- FTNT Fortinet, Inc. — roic_not_meaningful:meaningless_capital
- BKNG Booking Holdings Inc. — roic_not_meaningful:meaningless_capital
- ABNB Airbnb, Inc. — roic_not_meaningful:meaningless_capital
- EXPE Expedia Group, Inc. — roic_not_meaningful:meaningless_capital
- VRSN VeriSign, Inc. — roic_not_meaningful:meaningless_capital
- DPZ Domino's Pizza, Inc. — roic_not_meaningful:meaningless_capital
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
- LITE Lumentum Holdings Inc. — insufficient_post_valuation_model_confidence
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
