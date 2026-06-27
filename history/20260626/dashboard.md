# Weekly US Stock Screen — 2026-06-26

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-06-26**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 512 | - |
| step2_hard_filters | 512 | 311 | adr_excluded: 30, persistent_negative_fcf: 22, interest_coverage: 21 |
| step3_standardize | 311 | 311 | - |
| step4_specialist_models | 93 | 58 | asset_management_model_not_supported: 16, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 311 | 304 | no_normalized_earnings: 7 |
| step5_quality_risk | 304 | 295 | - |
| step6_scenario_valuation | 295 | 269 | insufficient_post_valuation_model_confidence: 19, roic_not_meaningful:meaningless_capital: 6, invalid_valuation_output: 1 |
| step7_risk_adjusted_ranking | 327 | 327 | - |

## Eligible Candidates (13)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 16.5% | 33.5% | 15.7% | 43.5% | 0.0% | 0% | 0.79 | 0.77 |
| 2 | CTSH | 13.3% | 27.2% | 16.7% | 33.7% | 0.0% | 0% | 0.87 | 0.87 |
| 3 | VICI | 11.0% | 34.8% | 15.4% | 34.8% | 0.0% | 0% | 0.46 | 0.48 |
| 4 | ACN | 9.1% | 22.3% | 12.4% | 27.7% | 0.0% | 0% | 0.99 | 0.88 |
| 5 | TTD | 8.6% | 29.0% | 8.4% | 37.5% | 3.6% | 0% | 0.91 | 0.71 |
| 6 | OMC | 8.2% | 27.7% | 18.5% | 34.2% | 0.0% | 0% | 0.80 | 0.52 |
| 7 | ARE | 6.1% | 24.8% | 15.3% | 24.8% | 0.0% | 0% | 0.67 | 0.48 |
| 8 | BXP | 4.4% | 22.1% | 11.5% | 22.1% | 0.5% | 0% | 0.64 | 0.48 |
| 9 | CMCSA | 3.3% | 19.0% | 15.7% | 24.5% | 0.0% | 0% | 0.76 | 0.46 |
| 10 | CPT | 2.5% | 23.3% | 9.0% | 23.3% | 3.0% | 0% | 0.54 | 0.48 |
| 11 | CPAY | 2.3% | 20.9% | 6.8% | 28.5% | 5.2% | 0% | 0.99 | 0.84 |
| 12 | AVB | 1.0% | 22.6% | 7.9% | 22.6% | 4.1% | 0% | 0.53 | 0.48 |
| 13 | ADBE | 0.5% | 18.4% | 7.4% | 24.9% | 4.6% | 0% | 0.98 | 0.78 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 16.5% | 33.5% | 15.7% | 43.5% | 0.0% | 0% | 0.79 | 0.77 |
| 2 | CTSH | 13.3% | 27.2% | 16.7% | 33.7% | 0.0% | 0% | 0.87 | 0.87 |
| 3 | VICI | 11.0% | 34.8% | 15.4% | 34.8% | 0.0% | 0% | 0.46 | 0.48 |
| 4 | ACN | 9.1% | 22.3% | 12.4% | 27.7% | 0.0% | 0% | 0.99 | 0.88 |
| 5 | TTD | 8.6% | 29.0% | 8.4% | 37.5% | 3.6% | 0% | 0.91 | 0.71 |
| 6 | OMC | 8.2% | 27.7% | 18.5% | 34.2% | 0.0% | 0% | 0.80 | 0.52 |
| 7 | ARE | 6.1% | 24.8% | 15.3% | 24.8% | 0.0% | 0% | 0.67 | 0.48 |
| 8 | BXP | 4.4% | 22.1% | 11.5% | 22.1% | 0.5% | 0% | 0.64 | 0.48 |
| 9 | CMCSA | 3.3% | 19.0% | 15.7% | 24.5% | 0.0% | 0% | 0.76 | 0.46 |
| 10 | CPT | 2.5% | 23.3% | 9.0% | 23.3% | 3.0% | 0% | 0.54 | 0.48 |
| 11 | CPAY | 2.3% | 20.9% | 6.8% | 28.5% | 5.2% | 0% | 0.99 | 0.84 |
| 12 | AVB | 1.0% | 22.6% | 7.9% | 22.6% | 4.1% | 0% | 0.53 | 0.48 |
| 13 | ADBE | 0.5% | 18.4% | 7.4% | 24.9% | 4.6% | 0% | 0.98 | 0.78 |
| 14 | ZTS | -0.9% | 18.8% | 5.0% | 26.3% | 7.0% | 0% | 0.98 | 0.90 |
| 15 | UDR | -1.1% | 22.5% | 5.9% | 22.5% | 6.1% | 0% | 0.48 | 0.48 |
| 16 | ELV | -1.3% | 12.4% | 10.4% | 18.5% | 1.6% | 0% | 0.84 | 0.67 |
| 17 | HPQ | -1.9% | 10.1% | 10.1% | 15.2% | 1.9% | 0% | 0.97 | 0.67 |
| 18 | IT | -3.7% | 21.1% | 1.5% | 32.8% | 10.5% | 0% | 0.91 | 0.74 |
| 19 | EQR | -3.9% | 17.2% | 5.6% | 25.3% | 6.4% | 0% | 0.59 | 0.48 |
| 20 | HUM | -4.1% | 16.5% | 5.2% | 25.0% | 6.8% | 0% | 0.66 | 0.60 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | UHS | 31.6% | 33.5% | 15.7% | 43.5% | 100% | 137% |
| 2 | VICI | 30.0% | 34.8% | 15.4% | 34.8% | 100% | 346% |
| 3 | OMC | 27.0% | 27.7% | 18.5% | 34.2% | 100% | 155% |
| 4 | CTSH | 26.2% | 27.2% | 16.7% | 33.7% | 100% | 99% |
| 5 | TTD | 26.0% | 29.0% | 8.4% | 37.5% | 75% | 107% |
| 6 | FISV | 24.7% | 32.3% | -21.7% | 55.7% | 75% | 156% |
| 7 | EOG | 24.4% | 26.2% | -0.9% | 46.3% | 75% | 121% |
| 8 | ARE | 22.4% | 24.8% | 15.3% | 24.8% | 100% | 203% |
| 9 | ACN | 21.2% | 22.3% | 12.4% | 27.7% | 100% | 61% |
| 10 | CPT | 19.7% | 23.3% | 9.0% | 23.3% | 75% | 185% |
| 11 | CMCSA | 19.6% | 19.0% | 15.7% | 24.5% | 100% | 68% |
| 12 | BXP | 19.4% | 22.1% | 11.5% | 22.1% | 75% | 171% |
| 13 | CPAY | 19.3% | 20.9% | 6.8% | 28.5% | 75% | 67% |
| 14 | IT | 19.2% | 21.1% | 1.5% | 32.8% | 75% | 59% |
| 15 | LDOS | 19.0% | 22.1% | -3.5% | 35.1% | 75% | 82% |
| 16 | AVB | 18.9% | 22.6% | 7.9% | 22.6% | 75% | 177% |
| 17 | UDR | 18.3% | 22.5% | 5.9% | 22.5% | 75% | 175% |
| 18 | ADBE | 17.3% | 18.4% | 7.4% | 24.9% | 75% | 29% |
| 19 | ZTS | 17.2% | 18.8% | 5.0% | 26.3% | 75% | 52% |
| 20 | EQR | 16.3% | 17.2% | 5.6% | 25.3% | 75% | 121% |

## Week-over-week

Previous run: 2026-06-18

- Entered Robust Top: ACN, ZTS
- Exited Robust Top: FOXA, GIS
- Entered Upside Top: ACN, ZTS
- Exited Upside Top: ACGL, FOXA

Largest robust-rank moves:

- FDX: 265 → 202 (+63)
- DRI: 177 → 125 (+52)
- MDT: 122 → 86 (+36)
- QCOM: 185 → 149 (+36)
- BDX: 326 → 291 (+35)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| UHS | bear | 25% | 1.7% | 8.9% | 7.9% | 184.91 | 15.7% | 87% |
| UHS | base | 50% | 6.9% | 10.7% | 17.2% | 345.17 | 33.5% | 289% |
| UHS | bull | 25% | 11.0% | 12.1% | 19.6% | 489.25 | 43.5% | 461% |
| CTSH | bear | 25% | 0.1% | 12.9% | 8.2% | 55.33 | 16.7% | 95% |
| CTSH | base | 50% | 4.9% | 15.0% | 14.2% | 79.46 | 27.2% | 207% |
| CTSH | bull | 25% | 8.7% | 16.6% | 15.0% | 100.52 | 33.7% | 296% |
| ACN | bear | 25% | 2.1% | 13.4% | 9.2% | 146.39 | 12.4% | 67% |
| ACN | base | 50% | 6.9% | 14.7% | 18.9% | 207.32 | 22.3% | 159% |
| ACN | bull | 25% | 10.9% | 15.8% | 19.0% | 252.13 | 27.7% | 221% |
| TTD | bear | 25% | 13.6% | 13.1% | 9.2% | 18.10 | 8.4% | 45% |
| TTD | base | 50% | 19.9% | 17.1% | 41.0% | 38.11 | 29.0% | 245% |
| TTD | bull | 25% | 24.9% | 20.7% | 44.1% | 50.63 | 37.5% | 367% |
| OMC | bear | 25% | 18.4% | 12.7% | 6.5% | 125.76 | 18.5% | 144% |
| OMC | base | 50% | 25.0% | 14.6% | 6.5% | 186.37 | 27.7% | 259% |
| OMC | bull | 25% | 30.3% | 15.9% | 6.5% | 241.30 | 34.2% | 363% |
| CMCSA | bear | 25% | -6.0% | 16.1% | 6.5% | 30.86 | 15.7% | 86% |
| CMCSA | base | 50% | 1.2% | 18.7% | 6.5% | 38.89 | 19.0% | 143% |
| CMCSA | bull | 25% | 7.0% | 20.4% | 6.5% | 52.44 | 24.5% | 228% |
| CPAY | bear | 25% | 7.7% | 39.8% | 7.3% | 323.19 | 6.8% | 35% |
| CPAY | base | 50% | 13.3% | 44.0% | 30.0% | 554.87 | 20.9% | 152% |
| CPAY | bull | 25% | 17.9% | 47.4% | 30.3% | 736.32 | 28.5% | 240% |
| ADBE | bear | 25% | 8.6% | 29.7% | 10.9% | 176.42 | 7.4% | 37% |
| ADBE | base | 50% | 13.3% | 33.6% | 57.2% | 261.15 | 18.4% | 121% |
| ADBE | bull | 25% | 17.1% | 36.9% | 58.3% | 327.35 | 24.9% | 185% |
| ZTS | bear | 25% | 0.9% | 32.2% | 7.3% | 67.24 | 5.0% | 24% |
| ZTS | base | 50% | 5.3% | 36.0% | 24.5% | 115.88 | 18.8% | 128% |
| ZTS | bull | 25% | 8.8% | 39.1% | 24.8% | 153.45 | 26.3% | 208% |
| ELV | bear | 25% | -1.3% | 4.9% | 6.9% | 458.47 | 10.4% | 56% |
| ELV | base | 50% | 4.9% | 5.9% | 6.9% | 511.87 | 12.4% | 82% |
| ELV | bull | 25% | 9.9% | 6.6% | 6.9% | 672.70 | 18.5% | 139% |
| HPQ | bear | 25% | -3.6% | 5.7% | 8.7% | 25.26 | 12.3% | 63% |
| HPQ | base | 50% | 1.8% | 6.6% | 8.7% | 23.59 | 10.1% | 65% |
| HPQ | bull | 25% | 6.2% | 7.3% | 8.7% | 30.39 | 15.2% | 112% |
| IT | bear | 25% | -2.2% | 13.0% | 7.9% | 101.13 | 1.5% | 7% |
| IT | base | 50% | 3.2% | 17.1% | 47.6% | 214.79 | 21.1% | 149% |
| IT | bull | 25% | 7.5% | 20.7% | 51.6% | 323.21 | 32.8% | 286% |
| HUM | bear | 25% | 12.7% | 2.5% | 7.8% | 342.90 | 5.2% | 29% |
| HUM | base | 50% | 19.3% | 3.7% | 7.8% | 568.58 | 16.5% | 115% |
| HUM | bull | 25% | 24.6% | 4.8% | 7.8% | 812.45 | 25.0% | 209% |

**Scenario order inversions** (named bear/base/bull intrinsic value is not monotone — this is economic, not a bug):
- HPQ: growth destroys value: forward ROIC 2.0% at/below WACC 8.7%, so higher-growth scenarios reinvest below the cost of capital and are worth less than the bear case

## Boundary Assumptions & Valuation Alerts

- UHS — bounds: share_change_floor_hit;intrinsic_2x_price
- VICI — bounds: specialist_model_v1
- TTD — bounds: intrinsic_2x_price
- OMC — bounds: base_growth_cap_hit;wacc_floor_hit;reinvestment_cap_hit;intrinsic_2x_price
- ARE — bounds: specialist_model_v1
- BXP — bounds: specialist_model_v1
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;wacc_floor_hit;reinvestment_cap_hit
- CPT — bounds: specialist_model_v1
- AVB — bounds: specialist_model_v1
- ADBE — bounds: share_change_floor_hit
- UDR — bounds: specialist_model_v1
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HPQ — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- EQR — bounds: specialist_model_v1
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| ORCL | drawdown_from_high | nan% | -40% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| FOXA | weekly_drop | -27% | nan% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| CHTR | drawdown_from_high | nan% | -45% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- VICI: nan
- TTD: heavy_sbc
- OMC: incremental_roic_below_wacc
- ARE: nan
- BXP: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- CPT: nan
- CPAY: thin_interest_coverage
- AVB: nan
- ADBE: heavy_sbc
- UDR: nan
- ELV: incremental_roic_below_wacc
- HPQ: incremental_roic_below_wacc
- EQR: nan
- HUM: thin_interest_coverage, incremental_roic_below_wacc

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
- MCO Moody's Corporation — financial_sector_model_not_supported
- ICE Intercontinental Exchange, Inc. — financial_sector_model_not_supported
- APO Apollo Global Management, Inc. — asset_management_model_not_supported
- STT State Street Corporation — asset_management_model_not_supported
- AMP Ameriprise Financial, Inc. — asset_management_model_not_supported
- MSCI MSCI Inc. — financial_sector_model_not_supported
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
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- INSM Insmed Incorporated — preprofit_biotech_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- ORCL Oracle Corporation — material_event_requires_reunderwriting
- FOXA Fox Corporation — material_event_requires_reunderwriting
- CHTR Charter Communications, Inc. — material_event_requires_reunderwriting
- XOM Exxon Mobil Corporation — insufficient_model_confidence
- CVX Chevron Corporation — insufficient_model_confidence
- COP ConocoPhillips — insufficient_model_confidence
- VLO Valero Energy Corporation — insufficient_model_confidence
- MPC Marathon Petroleum Corporation — insufficient_model_confidence
- PSX Phillips 66 — insufficient_model_confidence
- CCL Carnival Corporation & plc — insufficient_model_confidence
- MOS The Mosaic Company — insufficient_model_confidence
- TSLA Tesla, Inc. — insufficient_model_confidence
- LHX L3Harris Technologies, Inc. — invalid_valuation_output
- BKNG Booking Holdings Inc. — roic_not_meaningful:meaningless_capital
- FTNT Fortinet, Inc. — roic_not_meaningful:meaningless_capital
- ABNB Airbnb, Inc. — roic_not_meaningful:meaningless_capital
- EXPE Expedia Group, Inc. — roic_not_meaningful:meaningless_capital
- VRSN VeriSign, Inc. — roic_not_meaningful:meaningless_capital
- CSGP CoStar Group, Inc. — roic_not_meaningful:meaningless_capital
- PFE Pfizer Inc. — insufficient_post_valuation_model_confidence
- FCX Freeport-McMoRan Inc. — insufficient_post_valuation_model_confidence
- RCL Royal Caribbean Cruises Ltd. — insufficient_post_valuation_model_confidence
- CI Cigna Corporation — insufficient_post_valuation_model_confidence
- TRGP Targa Resources Corp. — insufficient_post_valuation_model_confidence
- NUE Nucor Corporation — insufficient_post_valuation_model_confidence
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
