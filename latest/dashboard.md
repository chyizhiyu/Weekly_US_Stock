# Weekly US Stock Screen — 2026-07-02

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-07-02**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 512 | - |
| step2_hard_filters | 512 | 307 | adr_excluded: 31, interest_coverage: 22, persistent_negative_fcf: 21 |
| step3_standardize | 307 | 307 | - |
| step4_specialist_models | 90 | 56 | asset_management_model_not_supported: 16, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 307 | 300 | no_normalized_earnings: 7 |
| step5_quality_risk | 300 | 291 | - |
| step6_scenario_valuation | 291 | 265 | insufficient_post_valuation_model_confidence: 18, roic_not_meaningful:meaningless_capital: 6, irr_below_solver_bound: 1 |
| step7_risk_adjusted_ranking | 321 | 321 | - |

## Eligible Candidates (10)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 13.7% | 29.8% | 12.7% | 39.6% | 0.0% | 0% | 0.78 | 0.77 |
| 2 | FOXA | 12.8% | 31.1% | 11.8% | 41.3% | 0.2% | 0% | 0.90 | 0.68 |
| 3 | CTSH | 11.6% | 25.3% | 15.1% | 31.8% | 0.0% | 0% | 0.87 | 0.87 |
| 4 | VICI | 10.2% | 33.2% | 14.8% | 33.2% | 0.0% | 0% | 0.47 | 0.48 |
| 5 | OMC | 7.9% | 25.7% | 16.6% | 32.0% | 0.0% | 0% | 0.80 | 0.58 |
| 6 | ARE | 6.4% | 25.4% | 16.1% | 25.4% | 0.0% | 0% | 0.68 | 0.48 |
| 7 | TTD | 6.3% | 27.5% | 7.3% | 35.9% | 4.7% | 0% | 0.91 | 0.71 |
| 8 | ACN | 5.6% | 20.1% | 10.5% | 25.3% | 1.5% | 0% | 0.99 | 0.88 |
| 9 | CMCSA | 3.0% | 18.4% | 14.9% | 23.8% | 0.0% | 0% | 0.76 | 0.46 |
| 10 | BXP | 2.6% | 20.7% | 10.5% | 20.7% | 1.5% | 0% | 0.64 | 0.48 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 13.7% | 29.8% | 12.7% | 39.6% | 0.0% | 0% | 0.78 | 0.77 |
| 2 | FOXA | 12.8% | 31.1% | 11.8% | 41.3% | 0.2% | 0% | 0.90 | 0.68 |
| 3 | CTSH | 11.6% | 25.3% | 15.1% | 31.8% | 0.0% | 0% | 0.87 | 0.87 |
| 4 | VICI | 10.2% | 33.2% | 14.8% | 33.2% | 0.0% | 0% | 0.47 | 0.48 |
| 5 | OMC | 7.9% | 25.7% | 16.6% | 32.0% | 0.0% | 0% | 0.80 | 0.58 |
| 6 | ARE | 6.4% | 25.4% | 16.1% | 25.4% | 0.0% | 0% | 0.68 | 0.48 |
| 7 | TTD | 6.3% | 27.5% | 7.3% | 35.9% | 4.7% | 0% | 0.91 | 0.71 |
| 8 | ACN | 5.6% | 20.1% | 10.5% | 25.3% | 1.5% | 0% | 0.99 | 0.88 |
| 9 | CMCSA | 3.0% | 18.4% | 14.9% | 23.8% | 0.0% | 0% | 0.76 | 0.46 |
| 10 | BXP | 2.6% | 20.7% | 10.5% | 20.7% | 1.5% | 0% | 0.64 | 0.48 |
| 11 | AVB | -0.8% | 21.0% | 6.9% | 21.0% | 5.1% | 0% | 0.54 | 0.48 |
| 12 | ZTS | -0.8% | 18.8% | 5.1% | 26.2% | 6.9% | 0% | 0.98 | 0.90 |
| 13 | HPQ | -1.2% | 10.8% | 10.8% | 15.9% | 1.2% | 0% | 0.97 | 0.67 |
| 14 | CPAY | -1.5% | 18.5% | 5.1% | 26.0% | 6.9% | 0% | 0.99 | 0.84 |
| 15 | UDR | -3.2% | 20.5% | 4.7% | 20.5% | 7.3% | 0% | 0.50 | 0.48 |
| 16 | ELV | -3.3% | 10.7% | 8.7% | 16.8% | 3.3% | 0% | 0.83 | 0.67 |
| 17 | ADBE | -3.8% | 15.8% | 5.2% | 22.1% | 6.8% | 0% | 0.98 | 0.78 |
| 18 | APA | -4.7% | 25.2% | 2.6% | 44.8% | 9.4% | 0% | 0.72 | 0.35 |
| 19 | IT | -4.9% | 20.3% | 1.0% | 31.9% | 11.0% | 0% | 0.91 | 0.74 |
| 20 | EQR | -5.5% | 15.9% | 4.7% | 23.5% | 7.3% | 0% | 0.60 | 0.48 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | FOXA | 28.8% | 31.1% | 11.8% | 41.3% | 75% | 141% |
| 2 | VICI | 28.6% | 33.2% | 14.8% | 33.2% | 100% | 320% |
| 3 | UHS | 28.0% | 29.8% | 12.7% | 39.6% | 100% | 108% |
| 4 | OMC | 25.0% | 25.7% | 16.6% | 32.0% | 100% | 134% |
| 5 | TTD | 24.5% | 27.5% | 7.3% | 35.9% | 75% | 96% |
| 6 | APA | 24.5% | 25.2% | 2.6% | 44.8% | 75% | 153% |
| 7 | CTSH | 24.4% | 25.3% | 15.1% | 31.8% | 100% | 85% |
| 8 | EOG | 23.8% | 25.7% | -1.5% | 45.5% | 75% | 115% |
| 9 | ARE | 23.1% | 25.4% | 16.1% | 25.4% | 100% | 210% |
| 10 | FISV | 22.1% | 29.8% | -24.3% | 53.0% | 75% | 134% |
| 11 | ACN | 19.0% | 20.1% | 10.5% | 25.3% | 75% | 48% |
| 12 | CMCSA | 18.9% | 18.4% | 14.9% | 23.8% | 100% | 64% |
| 13 | IT | 18.4% | 20.3% | 1.0% | 31.9% | 75% | 54% |
| 14 | BXP | 18.1% | 20.7% | 10.5% | 20.7% | 75% | 156% |
| 15 | AVB | 17.5% | 21.0% | 6.9% | 21.0% | 75% | 159% |
| 16 | ZTS | 17.2% | 18.8% | 5.1% | 26.2% | 75% | 51% |
| 17 | LDOS | 17.1% | 20.3% | -5.1% | 33.1% | 75% | 70% |
| 18 | CPAY | 17.0% | 18.5% | 5.1% | 26.0% | 75% | 52% |
| 19 | UDR | 16.5% | 20.5% | 4.7% | 20.5% | 75% | 154% |
| 20 | MO | 15.2% | 17.1% | 0.4% | 26.1% | 75% | 50% |

## Week-over-week

Previous run: 2026-07-02

- Entered Robust Top: APA, ZTS
- Exited Robust Top: CPT, HUM
- Entered Upside Top: APA, MO, ZTS
- Exited Upside Top: ADBE, CPT, EQR

Largest robust-rank moves:

- KLAC: 247 → 222 (+25)
- CDW: 96 → 79 (+17)
- JBL: 236 → 219 (+17)
- TER: 265 → 248 (+17)
- AMAT: 246 → 230 (+16)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| UHS | bear | 25% | 1.7% | 8.9% | 8.1% | 177.84 | 12.7% | 67% |
| UHS | base | 50% | 6.9% | 10.7% | 17.2% | 329.48 | 29.8% | 243% |
| UHS | bull | 25% | 11.0% | 12.1% | 19.6% | 465.79 | 39.6% | 394% |
| FOXA | bear | 25% | -1.0% | 17.5% | 6.5% | 69.06 | 11.8% | 63% |
| FOXA | base | 50% | 4.7% | 20.1% | 54.7% | 136.25 | 31.1% | 264% |
| FOXA | bull | 25% | 9.3% | 22.0% | 60.0% | 192.14 | 41.3% | 424% |
| CTSH | bear | 25% | 0.0% | 12.9% | 8.3% | 54.47 | 15.1% | 83% |
| CTSH | base | 50% | 4.9% | 15.0% | 14.2% | 77.82 | 25.3% | 186% |
| CTSH | bull | 25% | 8.8% | 16.6% | 15.0% | 98.27 | 31.8% | 270% |
| OMC | bear | 25% | 18.4% | 12.7% | 6.6% | 123.76 | 16.6% | 124% |
| OMC | base | 50% | 25.0% | 14.6% | 6.6% | 183.69 | 25.7% | 230% |
| OMC | bull | 25% | 30.3% | 15.9% | 6.6% | 237.99 | 32.0% | 326% |
| TTD | bear | 25% | 13.6% | 13.1% | 9.4% | 17.86 | 7.3% | 38% |
| TTD | base | 50% | 19.8% | 17.1% | 41.0% | 37.39 | 27.5% | 226% |
| TTD | bull | 25% | 24.8% | 20.7% | 44.1% | 49.61 | 35.9% | 341% |
| ACN | bear | 25% | 2.1% | 13.4% | 9.4% | 144.38 | 10.5% | 55% |
| ACN | base | 50% | 6.9% | 14.7% | 18.9% | 203.06 | 20.1% | 137% |
| ACN | bull | 25% | 10.8% | 15.8% | 19.0% | 246.05 | 25.3% | 193% |
| CMCSA | bear | 25% | -6.1% | 16.1% | 6.5% | 30.82 | 14.9% | 81% |
| CMCSA | base | 50% | 1.2% | 18.7% | 6.5% | 38.95 | 18.4% | 136% |
| CMCSA | bull | 25% | 7.0% | 20.4% | 6.5% | 52.39 | 23.8% | 219% |
| ZTS | bear | 25% | 0.9% | 32.2% | 7.4% | 66.14 | 5.1% | 25% |
| ZTS | base | 50% | 5.3% | 36.0% | 24.5% | 113.29 | 18.8% | 128% |
| ZTS | bull | 25% | 8.8% | 39.1% | 24.8% | 149.72 | 26.2% | 207% |
| HPQ | bear | 25% | -3.6% | 5.7% | 8.8% | 25.03 | 13.2% | 69% |
| HPQ | base | 50% | 1.8% | 6.6% | 8.8% | 23.29 | 10.8% | 70% |
| HPQ | bull | 25% | 6.2% | 7.3% | 8.8% | 30.00 | 15.9% | 119% |
| CPAY | bear | 25% | 7.7% | 39.8% | 7.5% | 315.42 | 5.1% | 25% |
| CPAY | base | 50% | 13.3% | 44.0% | 30.0% | 535.90 | 18.5% | 129% |
| CPAY | bull | 25% | 17.9% | 47.4% | 30.3% | 708.45 | 26.0% | 209% |
| ELV | bear | 25% | -1.3% | 4.9% | 7.0% | 448.75 | 8.7% | 45% |
| ELV | base | 50% | 4.9% | 5.9% | 7.0% | 498.19 | 10.7% | 68% |
| ELV | bull | 25% | 9.9% | 6.6% | 7.0% | 654.94 | 16.8% | 121% |
| ADBE | bear | 25% | 8.6% | 29.7% | 11.0% | 173.89 | 5.2% | 25% |
| ADBE | base | 50% | 13.3% | 33.6% | 57.2% | 256.42 | 15.8% | 99% |
| ADBE | bull | 25% | 17.1% | 36.9% | 58.3% | 320.98 | 22.1% | 157% |
| APA | bear | 25% | -13.0% | 21.1% | 6.5% | 29.11 | 2.6% | 11% |
| APA | base | 50% | 10.7% | 31.8% | 6.5% | 81.74 | 25.2% | 218% |
| APA | bull | 25% | 29.7% | 40.8% | 6.5% | 177.83 | 44.8% | 588% |
| IT | bear | 25% | -2.2% | 13.0% | 8.0% | 99.26 | 1.0% | 4% |
| IT | base | 50% | 3.2% | 17.1% | 47.6% | 209.66 | 20.3% | 141% |
| IT | bull | 25% | 7.5% | 20.7% | 51.6% | 314.90 | 31.9% | 274% |

**Scenario order inversions** (named bear/base/bull intrinsic value is not monotone — this is economic, not a bug):
- HPQ: growth destroys value: forward ROIC 2.0% at/below WACC 8.8%, so higher-growth scenarios reinvest below the cost of capital and are worth less than the bear case

## Boundary Assumptions & Valuation Alerts

- UHS — bounds: share_change_floor_hit;intrinsic_2x_price
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit;intrinsic_2x_price
- VICI — bounds: specialist_model_v1
- OMC — bounds: base_growth_cap_hit;reinvestment_cap_hit;intrinsic_2x_price
- ARE — bounds: specialist_model_v1
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;wacc_floor_hit;reinvestment_cap_hit
- BXP — bounds: specialist_model_v1
- AVB — bounds: specialist_model_v1
- HPQ — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- UDR — bounds: specialist_model_v1
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- ADBE — bounds: share_change_floor_hit
- APA — bounds: wacc_floor_hit;reinvestment_cap_hit;intrinsic_2x_price
- EQR — bounds: specialist_model_v1

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| ORCL | drawdown_from_high | nan% | -43% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| HON | weekly_drop;drawdown_from_high | -50% | -51% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| CHTR | drawdown_from_high | nan% | -44% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| SMCI | drawdown_from_high | nan% | -43% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- VICI: nan
- OMC: incremental_roic_below_wacc
- ARE: nan
- TTD: heavy_sbc
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- BXP: nan
- AVB: nan
- HPQ: incremental_roic_below_wacc
- CPAY: thin_interest_coverage
- UDR: nan
- ELV: incremental_roic_below_wacc
- ADBE: heavy_sbc
- APA: cyclical_revenue, incremental_roic_below_wacc
- EQR: nan

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
- MCO Moody's Corporation — financial_sector_model_not_supported
- KKR KKR & Co. Inc. — asset_management_model_not_supported
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
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- ORCL Oracle Corporation — material_event_requires_reunderwriting
- HON Honeywell International Inc. — material_event_requires_reunderwriting
- CHTR Charter Communications, Inc. — material_event_requires_reunderwriting
- SMCI Super Micro Computer, Inc. — material_event_requires_reunderwriting
- XOM Exxon Mobil Corporation — insufficient_model_confidence
- CVX Chevron Corporation — insufficient_model_confidence
- COP ConocoPhillips — insufficient_model_confidence
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

## Data Gaps and Model Limitations

- Stocks missing core financials were rejected (fail closed), never estimated.
- Banks, insurers and REITs use conservative specialist models; rows with
  incomplete specialist inputs stay watchlisted instead of entering ranking.
- Asset managers, consumer-finance names, other financials and pre-profit
  biotech remain watchlisted until dedicated models exist.
- Scenario set is discrete (bear/base/bull); worst-case stress metrics are
  deterministic bear/base/bull stress labels, not calibrated CVaR.
- Ad-hoc market closures are not in the calendar; freshness checks catch them.
