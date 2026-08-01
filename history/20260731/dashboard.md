# Weekly US Stock Screen — 2026-07-31

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-07-31**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 515 | - |
| step2_hard_filters | 515 | 306 | adr_excluded: 33, persistent_negative_fcf: 22, interest_coverage: 18 |
| step3_standardize | 306 | 306 | - |
| step4_specialist_models | 93 | 58 | asset_management_model_not_supported: 17, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 306 | 300 | no_normalized_earnings: 6 |
| step5_quality_risk | 300 | 292 | - |
| step6_scenario_valuation | 292 | 268 | insufficient_post_valuation_model_confidence: 17, roic_not_meaningful:meaningless_capital: 6, invalid_valuation_output: 1 |
| step7_risk_adjusted_ranking | 326 | 326 | - |

## Eligible Candidates (11)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | OMC | 12.5% | 30.5% | 20.9% | 37.3% | 0.0% | 0% | 0.83 | 0.68 |
| 2 | UHS | 10.7% | 27.5% | 10.8% | 37.1% | 1.2% | 0% | 0.78 | 0.77 |
| 3 | FOXA | 8.8% | 28.0% | 9.8% | 37.7% | 2.2% | 0% | 0.89 | 0.68 |
| 4 | VICI | 8.7% | 30.2% | 13.8% | 30.2% | 0.0% | 0% | 0.51 | 0.48 |
| 5 | TTD | 6.4% | 27.2% | 7.6% | 35.6% | 4.4% | 0% | 0.91 | 0.71 |
| 6 | ARE | 6.3% | 25.1% | 16.0% | 25.1% | 0.0% | 0% | 0.69 | 0.48 |
| 7 | CMCSA | 3.5% | 19.6% | 14.5% | 23.8% | 0.0% | 0% | 0.76 | 0.46 |
| 8 | CPT | 1.4% | 21.8% | 8.7% | 21.8% | 3.3% | 0% | 0.57 | 0.48 |
| 9 | BXP | 1.3% | 19.5% | 9.7% | 19.5% | 2.3% | 0% | 0.65 | 0.48 |
| 10 | HUM | 0.8% | 19.0% | 8.5% | 27.1% | 3.5% | 0% | 0.76 | 0.61 |
| 11 | ELV | 0.5% | 13.6% | 11.5% | 19.6% | 0.5% | 0% | 0.82 | 0.67 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | OMC | 12.5% | 30.5% | 20.9% | 37.3% | 0.0% | 0% | 0.83 | 0.68 |
| 2 | UHS | 10.7% | 27.5% | 10.8% | 37.1% | 1.2% | 0% | 0.78 | 0.77 |
| 3 | FOXA | 8.8% | 28.0% | 9.8% | 37.7% | 2.2% | 0% | 0.89 | 0.68 |
| 4 | VICI | 8.7% | 30.2% | 13.8% | 30.2% | 0.0% | 0% | 0.51 | 0.48 |
| 5 | TTD | 6.4% | 27.2% | 7.6% | 35.6% | 4.4% | 0% | 0.91 | 0.71 |
| 6 | ARE | 6.3% | 25.1% | 16.0% | 25.1% | 0.0% | 0% | 0.69 | 0.48 |
| 7 | CMCSA | 3.5% | 19.6% | 14.5% | 23.8% | 0.0% | 0% | 0.76 | 0.46 |
| 8 | CPT | 1.4% | 21.8% | 8.7% | 21.8% | 3.3% | 0% | 0.57 | 0.48 |
| 9 | BXP | 1.3% | 19.5% | 9.7% | 19.5% | 2.3% | 0% | 0.65 | 0.48 |
| 10 | HUM | 0.8% | 19.0% | 8.5% | 27.1% | 3.5% | 0% | 0.76 | 0.61 |
| 11 | ELV | 0.5% | 13.6% | 11.5% | 19.6% | 0.5% | 0% | 0.82 | 0.67 |
| 12 | AVB | -1.3% | 20.0% | 6.8% | 20.0% | 5.2% | 0% | 0.56 | 0.48 |
| 13 | CTSH | -2.1% | 16.0% | 6.5% | 22.3% | 5.5% | 0% | 0.85 | 0.87 |
| 14 | UDR | -2.6% | 20.3% | 5.4% | 20.3% | 6.6% | 0% | 0.52 | 0.48 |
| 15 | EQR | -2.9% | 18.0% | 6.2% | 22.6% | 5.8% | 0% | 0.59 | 0.48 |
| 16 | MO | -4.4% | 17.6% | 2.4% | 25.4% | 9.6% | 0% | 0.98 | 0.93 |
| 17 | ZTS | -4.7% | 16.3% | 3.4% | 23.4% | 8.6% | 0% | 0.98 | 0.90 |
| 18 | GIS | -6.3% | 18.9% | 1.1% | 28.1% | 10.9% | 0% | 0.81 | 0.67 |
| 19 | CPAY | -7.3% | 14.8% | 2.4% | 21.9% | 9.6% | 0% | 0.99 | 0.84 |
| 20 | HPQ | -7.5% | 4.5% | 4.5% | 9.5% | 7.5% | 0% | 0.97 | 0.67 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | CI | 31.5% | 35.2% | -9.7% | 65.3% | 75% | 214% |
| 2 | OMC | 29.8% | 30.5% | 20.9% | 37.3% | 100% | 182% |
| 3 | VICI | 26.1% | 30.2% | 13.8% | 30.2% | 100% | 274% |
| 4 | FOXA | 25.9% | 28.0% | 9.8% | 37.7% | 75% | 113% |
| 5 | UHS | 25.7% | 27.5% | 10.8% | 37.1% | 75% | 91% |
| 6 | TTD | 24.4% | 27.2% | 7.6% | 35.6% | 75% | 91% |
| 7 | ARE | 22.8% | 25.1% | 16.0% | 25.1% | 100% | 206% |
| 8 | REGN | 19.6% | 21.5% | -2.4% | 37.9% | 75% | 74% |
| 9 | CMCSA | 19.4% | 19.6% | 14.5% | 23.8% | 100% | 70% |
| 10 | EOG | 18.7% | 20.5% | -5.8% | 39.7% | 75% | 73% |
| 11 | APA | 18.6% | 20.9% | -7.2% | 39.8% | 75% | 105% |
| 12 | CPT | 18.5% | 21.8% | 8.7% | 21.8% | 75% | 168% |
| 13 | HUM | 18.4% | 19.0% | 8.5% | 27.1% | 75% | 64% |
| 14 | CHTR | 17.6% | 48.1% | -95.0% | 69.2% | 75% | 323% |
| 15 | FISV | 17.3% | 26.9% | -35.0% | 50.4% | 75% | 107% |
| 16 | BXP | 17.0% | 19.5% | 9.7% | 19.5% | 75% | 144% |
| 17 | GIS | 16.7% | 18.9% | 1.1% | 28.1% | 75% | 60% |
| 18 | AVB | 16.7% | 20.0% | 6.8% | 20.0% | 75% | 149% |
| 19 | UDR | 16.6% | 20.3% | 5.4% | 20.3% | 75% | 152% |
| 20 | EQR | 16.2% | 18.0% | 6.2% | 22.6% | 75% | 129% |

## Week-over-week

Previous run: 2026-07-24

- Entered Robust Top: GIS, MO
- Exited Robust Top: ADBE, HCA
- Entered Upside Top: APA, EQR, HUM, REGN
- Exited Upside Top: CTSH, HCA, LDOS, ZTS

Largest robust-rank moves:

- PCAR: 239 → 132 (+107)
- SWK: 186 → 118 (+68)
- FLEX: 274 → 214 (+60)
- VZ: 55 → 100 (-45)
- ABT: 152 → 196 (-44)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| OMC | bear | 25% | 18.2% | 12.8% | 6.8% | 148.50 | 20.9% | 174% |
| OMC | base | 50% | 25.0% | 14.6% | 6.8% | 221.82 | 30.5% | 305% |
| OMC | bull | 25% | 30.4% | 15.9% | 6.8% | 289.51 | 37.3% | 426% |
| UHS | bear | 25% | 1.9% | 8.9% | 8.3% | 174.25 | 10.8% | 56% |
| UHS | base | 50% | 7.1% | 10.7% | 17.2% | 321.04 | 27.5% | 216% |
| UHS | bull | 25% | 11.3% | 12.1% | 19.5% | 452.88 | 37.1% | 354% |
| FOXA | bear | 25% | -1.0% | 17.5% | 6.9% | 64.79 | 9.8% | 51% |
| FOXA | base | 50% | 4.9% | 20.1% | 54.4% | 124.15 | 28.0% | 225% |
| FOXA | bull | 25% | 9.5% | 22.0% | 60.0% | 173.31 | 37.7% | 364% |
| TTD | bear | 25% | 13.5% | 13.1% | 9.7% | 16.85 | 7.6% | 40% |
| TTD | base | 50% | 19.8% | 17.1% | 41.0% | 34.43 | 27.2% | 222% |
| TTD | bull | 25% | 24.8% | 20.7% | 44.1% | 45.57 | 35.6% | 334% |
| CMCSA | bear | 25% | -6.6% | 16.1% | 6.5% | 30.93 | 14.5% | 79% |
| CMCSA | base | 50% | 0.8% | 18.7% | 6.5% | 40.82 | 19.6% | 143% |
| CMCSA | bull | 25% | 6.6% | 20.4% | 6.5% | 52.84 | 23.8% | 218% |
| HUM | bear | 25% | 13.3% | 2.5% | 8.0% | 377.26 | 8.5% | 51% |
| HUM | base | 50% | 19.1% | 3.7% | 8.0% | 596.36 | 19.0% | 140% |
| HUM | bull | 25% | 23.7% | 4.8% | 8.0% | 835.05 | 27.1% | 236% |
| ELV | bear | 25% | -0.8% | 4.9% | 7.2% | 449.92 | 11.5% | 63% |
| ELV | base | 50% | 5.4% | 5.9% | 7.2% | 506.91 | 13.6% | 92% |
| ELV | bull | 25% | 10.3% | 6.6% | 7.2% | 661.34 | 19.6% | 150% |
| CTSH | bear | 25% | -0.4% | 12.8% | 8.7% | 50.31 | 6.5% | 31% |
| CTSH | base | 50% | 4.6% | 15.0% | 13.9% | 71.83 | 16.0% | 102% |
| CTSH | bull | 25% | 8.6% | 16.6% | 14.8% | 91.01 | 22.3% | 164% |
| MO | bear | 25% | -2.2% | 48.7% | 6.8% | 55.60 | 2.4% | 11% |
| MO | base | 50% | 1.2% | 54.9% | 45.6% | 103.25 | 17.6% | 115% |
| MO | bull | 25% | 4.0% | 60.1% | 46.5% | 138.76 | 25.4% | 193% |
| ZTS | bear | 25% | 0.9% | 32.2% | 7.7% | 62.82 | 3.4% | 16% |
| ZTS | base | 50% | 5.1% | 36.0% | 24.5% | 105.10 | 16.3% | 106% |
| ZTS | bull | 25% | 8.4% | 39.1% | 24.8% | 137.47 | 23.4% | 174% |
| GIS | bear | 25% | -8.0% | 14.7% | 6.5% | 27.15 | 1.1% | 5% |
| GIS | base | 50% | -2.2% | 17.0% | 10.1% | 57.05 | 18.9% | 118% |
| GIS | bull | 25% | 2.4% | 18.6% | 11.0% | 82.87 | 28.1% | 218% |
| CPAY | bear | 25% | 7.7% | 39.8% | 7.8% | 299.03 | 2.4% | 11% |
| CPAY | base | 50% | 13.4% | 44.0% | 30.0% | 497.02 | 14.8% | 97% |
| CPAY | bull | 25% | 17.9% | 47.4% | 30.3% | 651.90 | 21.9% | 164% |
| HPQ | bear | 25% | -3.6% | 5.7% | 9.4% | 22.94 | 5.9% | 27% |
| HPQ | base | 50% | 1.8% | 6.6% | 9.4% | 20.60 | 4.5% | 26% |
| HPQ | bull | 25% | 6.2% | 7.3% | 9.4% | 26.58 | 9.5% | 62% |

**Scenario order inversions** (named bear/base/bull intrinsic value is not monotone — this is economic, not a bug):
- HPQ: growth destroys value: forward ROIC 2.0% at/below WACC 9.4%, so higher-growth scenarios reinvest below the cost of capital and are worth less than the bear case

## Boundary Assumptions & Valuation Alerts

- OMC — bounds: base_growth_cap_hit;reinvestment_cap_hit;intrinsic_2x_price
- UHS — bounds: share_change_floor_hit
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit;intrinsic_2x_price
- VICI — bounds: specialist_model_v1
- ARE — bounds: specialist_model_v1
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;wacc_floor_hit;reinvestment_cap_hit
- CPT — bounds: specialist_model_v1
- BXP — bounds: specialist_model_v1
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- AVB — bounds: specialist_model_v1
- UDR — bounds: specialist_model_v1
- EQR — bounds: specialist_model_v1
- GIS — bounds: wacc_floor_hit
- HPQ — bounds: forward_roic_floor_hit;reinvestment_cap_hit

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| ORCL | drawdown_from_high | nan% | -47% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| GLW | drawdown_from_high | nan% | -46% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| MRVL | drawdown_from_high | nan% | -41% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| QCOM | drawdown_from_high | nan% | -41% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| SMCI | drawdown_from_high | nan% | -43% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| CHRW | weekly_drop | -29% | nan% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- OMC: incremental_roic_below_wacc
- VICI: nan
- TTD: heavy_sbc
- ARE: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- CPT: nan
- BXP: nan
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- ELV: incremental_roic_below_wacc
- AVB: nan
- UDR: nan
- EQR: nan
- GIS: elevated_leverage, thin_interest_coverage
- CPAY: thin_interest_coverage
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
- NDAQ Nasdaq, Inc. — financial_sector_model_not_supported
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- NTRS Northern Trust Corporation — asset_management_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- ORCL Oracle Corporation — material_event_requires_reunderwriting
- GLW Corning Inc — material_event_requires_reunderwriting
- MRVL Marvell Technology, Inc. — material_event_requires_reunderwriting
- QCOM QUALCOMM Incorporated — material_event_requires_reunderwriting
- SMCI Super Micro Computer, Inc. — material_event_requires_reunderwriting
- CHRW C.H. Robinson Worldwide, Inc. — material_event_requires_reunderwriting
- XOM Exxon Mobil Corporation — insufficient_model_confidence
- CVX Chevron Corporation — insufficient_model_confidence
- MPC Marathon Petroleum Corporation — insufficient_model_confidence
- PSX Phillips 66 — insufficient_model_confidence
- CCL Carnival Corporation & plc — insufficient_model_confidence
- NRG NRG Energy, Inc. — insufficient_model_confidence
- MOS The Mosaic Company — insufficient_model_confidence
- TSLA Tesla, Inc. — insufficient_model_confidence
- LHX L3Harris Technologies, Inc. — invalid_valuation_output
- GDDY GoDaddy Inc. — roic_not_meaningful:meaningless_capital
- BKNG Booking Holdings Inc. — roic_not_meaningful:meaningless_capital
- FTNT Fortinet, Inc. — roic_not_meaningful:meaningless_capital
- ABNB Airbnb, Inc. — roic_not_meaningful:meaningless_capital
- EXPE Expedia Group, Inc. — roic_not_meaningful:meaningless_capital
- VRSN VeriSign, Inc. — roic_not_meaningful:meaningless_capital
- COP ConocoPhillips — insufficient_post_valuation_model_confidence
- VLO Valero Energy Corporation — insufficient_post_valuation_model_confidence
- FCX Freeport-McMoRan Inc. — insufficient_post_valuation_model_confidence
- RCL Royal Caribbean Cruises Ltd. — insufficient_post_valuation_model_confidence
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
- AMD Advanced Micro Devices, Inc. — insufficient_post_valuation_model_confidence
- APP AppLovin Corporation — insufficient_post_valuation_model_confidence
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
