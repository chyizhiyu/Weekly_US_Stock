# Weekly US Stock Screen — 2026-07-10

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-07-10**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 515 | - |
| step2_hard_filters | 515 | 309 | adr_excluded: 31, persistent_negative_fcf: 22, interest_coverage: 20 |
| step3_standardize | 309 | 309 | - |
| step4_specialist_models | 92 | 58 | asset_management_model_not_supported: 16, financial_sector_model_not_supported: 8, consumer_finance_model_not_supported: 7 |
| step4_normalized_model | 309 | 302 | no_normalized_earnings: 7 |
| step5_quality_risk | 302 | 294 | - |
| step6_scenario_valuation | 294 | 268 | insufficient_post_valuation_model_confidence: 18, roic_not_meaningful:meaningless_capital: 6, irr_below_solver_bound: 1 |
| step7_risk_adjusted_ranking | 326 | 326 | - |

## Eligible Candidates (11)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 14.0% | 30.3% | 13.1% | 40.0% | 0.0% | 0% | 0.78 | 0.77 |
| 2 | FOXA | 13.3% | 31.4% | 12.4% | 41.5% | 0.0% | 0% | 0.90 | 0.68 |
| 3 | CTSH | 10.3% | 23.9% | 14.1% | 30.1% | 0.0% | 0% | 0.87 | 0.87 |
| 4 | VICI | 10.1% | 33.0% | 15.2% | 33.0% | 0.0% | 0% | 0.49 | 0.48 |
| 5 | ARE | 7.6% | 27.9% | 18.4% | 27.9% | 0.0% | 0% | 0.68 | 0.48 |
| 6 | OMC | 7.1% | 24.3% | 15.3% | 30.6% | 0.0% | 0% | 0.80 | 0.58 |
| 7 | ACN | 5.1% | 19.6% | 10.4% | 24.8% | 1.6% | 0% | 0.99 | 0.88 |
| 8 | TTD | 4.6% | 26.3% | 6.4% | 34.5% | 5.6% | 0% | 0.91 | 0.71 |
| 9 | BXP | 4.2% | 21.9% | 11.5% | 21.9% | 0.5% | 0% | 0.64 | 0.48 |
| 10 | CMCSA | 3.1% | 18.6% | 15.1% | 24.0% | 0.0% | 0% | 0.76 | 0.46 |
| 11 | CPT | 2.5% | 23.1% | 9.2% | 23.1% | 2.8% | 0% | 0.55 | 0.48 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 14.0% | 30.3% | 13.1% | 40.0% | 0.0% | 0% | 0.78 | 0.77 |
| 2 | FOXA | 13.3% | 31.4% | 12.4% | 41.5% | 0.0% | 0% | 0.90 | 0.68 |
| 3 | CTSH | 10.3% | 23.9% | 14.1% | 30.1% | 0.0% | 0% | 0.87 | 0.87 |
| 4 | VICI | 10.1% | 33.0% | 15.2% | 33.0% | 0.0% | 0% | 0.49 | 0.48 |
| 5 | ARE | 7.6% | 27.9% | 18.4% | 27.9% | 0.0% | 0% | 0.68 | 0.48 |
| 6 | OMC | 7.1% | 24.3% | 15.3% | 30.6% | 0.0% | 0% | 0.80 | 0.58 |
| 7 | ACN | 5.1% | 19.6% | 10.4% | 24.8% | 1.6% | 0% | 0.99 | 0.88 |
| 8 | TTD | 4.6% | 26.3% | 6.4% | 34.5% | 5.6% | 0% | 0.91 | 0.71 |
| 9 | BXP | 4.2% | 21.9% | 11.5% | 21.9% | 0.5% | 0% | 0.64 | 0.48 |
| 10 | CMCSA | 3.1% | 18.6% | 15.1% | 24.0% | 0.0% | 0% | 0.76 | 0.46 |
| 11 | CPT | 2.5% | 23.1% | 9.2% | 23.1% | 2.8% | 0% | 0.55 | 0.48 |
| 12 | AVB | -0.7% | 21.0% | 7.0% | 21.0% | 5.0% | 0% | 0.54 | 0.48 |
| 13 | UDR | -2.0% | 21.5% | 5.5% | 21.5% | 6.5% | 0% | 0.49 | 0.48 |
| 14 | ZTS | -2.2% | 17.9% | 4.5% | 25.3% | 7.5% | 0% | 0.98 | 0.90 |
| 15 | CPAY | -2.3% | 18.0% | 4.7% | 25.3% | 7.3% | 0% | 0.99 | 0.84 |
| 16 | ELV | -3.4% | 10.6% | 8.6% | 16.7% | 3.4% | 0% | 0.83 | 0.67 |
| 17 | HPQ | -4.1% | 7.9% | 7.9% | 13.0% | 4.1% | 0% | 0.97 | 0.67 |
| 18 | IT | -4.8% | 20.3% | 1.1% | 31.9% | 10.9% | 0% | 0.91 | 0.74 |
| 19 | HUM | -5.0% | 15.9% | 4.7% | 24.4% | 7.3% | 0% | 0.66 | 0.60 |
| 20 | EQR | -5.1% | 16.2% | 4.9% | 23.7% | 7.1% | 0% | 0.60 | 0.48 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | FOXA | 29.2% | 31.4% | 12.4% | 41.5% | 100% | 141% |
| 2 | VICI | 28.5% | 33.0% | 15.2% | 33.0% | 100% | 316% |
| 3 | UHS | 28.4% | 30.3% | 13.1% | 40.0% | 100% | 111% |
| 4 | ARE | 25.5% | 27.9% | 18.4% | 27.9% | 100% | 243% |
| 5 | OMC | 23.6% | 24.3% | 15.3% | 30.6% | 100% | 120% |
| 6 | TTD | 23.4% | 26.3% | 6.4% | 34.5% | 75% | 86% |
| 7 | APA | 23.4% | 24.3% | 1.3% | 43.5% | 75% | 142% |
| 8 | EOG | 23.1% | 24.9% | -2.0% | 44.8% | 75% | 108% |
| 9 | CTSH | 23.0% | 23.9% | 14.1% | 30.1% | 100% | 74% |
| 10 | FISV | 22.2% | 30.2% | -25.1% | 53.4% | 75% | 135% |
| 11 | CPT | 19.6% | 23.1% | 9.2% | 23.1% | 75% | 182% |
| 12 | BXP | 19.3% | 21.9% | 11.5% | 21.9% | 75% | 169% |
| 13 | CMCSA | 19.1% | 18.6% | 15.1% | 24.0% | 100% | 65% |
| 14 | ACN | 18.6% | 19.6% | 10.4% | 24.8% | 75% | 44% |
| 15 | IT | 18.4% | 20.3% | 1.1% | 31.9% | 75% | 52% |
| 16 | LDOS | 17.6% | 20.7% | -4.7% | 33.6% | 75% | 73% |
| 17 | AVB | 17.5% | 21.0% | 7.0% | 21.0% | 75% | 159% |
| 18 | UDR | 17.5% | 21.5% | 5.5% | 21.5% | 75% | 164% |
| 19 | GIS | 16.5% | 18.6% | 0.9% | 27.8% | 75% | 58% |
| 20 | CPAY | 16.5% | 18.0% | 4.7% | 25.3% | 75% | 48% |

## Week-over-week

Previous run: 2026-07-02

- Entered Robust Top: CPT, HUM
- Exited Robust Top: ADBE, APA
- Entered Upside Top: CPT, GIS
- Exited Upside Top: MO, ZTS

Largest robust-rank moves:

- CDW: 79 → 98 (-19)
- META: 37 → 55 (-18)
- QCOM: 134 → 150 (-16)
- NTAP: 137 → 153 (-16)
- SLB: 176 → 192 (-16)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| UHS | bear | 25% | 1.7% | 8.9% | 8.1% | 177.04 | 13.1% | 70% |
| UHS | base | 50% | 6.9% | 10.7% | 17.2% | 327.73 | 30.3% | 248% |
| UHS | bull | 25% | 11.0% | 12.1% | 19.5% | 463.18 | 40.0% | 400% |
| FOXA | bear | 25% | -1.0% | 17.5% | 6.7% | 67.13 | 12.4% | 67% |
| FOXA | base | 50% | 4.8% | 20.1% | 54.6% | 130.59 | 31.4% | 267% |
| FOXA | bull | 25% | 9.4% | 22.0% | 60.0% | 183.21 | 41.5% | 425% |
| CTSH | bear | 25% | -0.0% | 12.8% | 8.6% | 52.46 | 14.1% | 76% |
| CTSH | base | 50% | 4.9% | 15.0% | 14.2% | 73.93 | 23.9% | 170% |
| CTSH | bull | 25% | 8.8% | 16.6% | 15.0% | 92.83 | 30.1% | 247% |
| OMC | bear | 25% | 18.3% | 12.7% | 6.6% | 121.03 | 15.3% | 111% |
| OMC | base | 50% | 25.0% | 14.6% | 6.6% | 180.05 | 24.3% | 212% |
| OMC | bull | 25% | 30.3% | 15.9% | 6.6% | 233.49 | 30.6% | 303% |
| ACN | bear | 25% | 2.1% | 13.4% | 9.7% | 139.70 | 10.4% | 54% |
| ACN | base | 50% | 6.9% | 14.7% | 18.9% | 194.25 | 19.6% | 133% |
| ACN | bull | 25% | 10.8% | 15.8% | 19.0% | 234.37 | 24.8% | 187% |
| TTD | bear | 25% | 13.5% | 13.1% | 9.5% | 17.50 | 6.4% | 33% |
| TTD | base | 50% | 19.8% | 17.1% | 41.0% | 36.35 | 26.3% | 211% |
| TTD | bull | 25% | 24.8% | 20.7% | 44.1% | 48.12 | 34.5% | 320% |
| CMCSA | bear | 25% | -6.1% | 16.1% | 6.5% | 30.82 | 15.1% | 82% |
| CMCSA | base | 50% | 1.2% | 18.7% | 6.5% | 38.95 | 18.6% | 138% |
| CMCSA | bull | 25% | 7.0% | 20.4% | 6.5% | 52.39 | 24.0% | 222% |
| ZTS | bear | 25% | 0.8% | 32.2% | 7.5% | 64.78 | 4.5% | 21% |
| ZTS | base | 50% | 5.2% | 36.0% | 24.5% | 110.25 | 17.9% | 120% |
| ZTS | bull | 25% | 8.7% | 39.1% | 24.8% | 145.39 | 25.3% | 196% |
| CPAY | bear | 25% | 7.7% | 39.8% | 7.6% | 310.23 | 4.7% | 24% |
| CPAY | base | 50% | 13.3% | 44.0% | 30.0% | 523.42 | 18.0% | 124% |
| CPAY | bull | 25% | 17.9% | 47.4% | 30.3% | 690.21 | 25.3% | 201% |
| ELV | bear | 25% | -1.3% | 4.9% | 7.1% | 444.21 | 8.6% | 45% |
| ELV | base | 50% | 4.9% | 5.9% | 7.1% | 491.76 | 10.6% | 67% |
| ELV | bull | 25% | 9.9% | 6.6% | 7.1% | 646.61 | 16.7% | 120% |
| HPQ | bear | 25% | -3.6% | 5.7% | 9.1% | 24.02 | 9.8% | 48% |
| HPQ | base | 50% | 1.8% | 6.6% | 9.1% | 21.98 | 7.9% | 48% |
| HPQ | bull | 25% | 6.2% | 7.3% | 9.1% | 28.34 | 13.0% | 91% |
| IT | bear | 25% | -2.2% | 13.0% | 8.2% | 96.88 | 1.1% | 5% |
| IT | base | 50% | 3.2% | 17.1% | 47.6% | 203.04 | 20.3% | 140% |
| IT | bull | 25% | 7.5% | 20.7% | 51.6% | 304.19 | 31.9% | 272% |
| HUM | bear | 25% | 12.4% | 2.5% | 7.8% | 341.96 | 4.7% | 26% |
| HUM | base | 50% | 19.0% | 3.7% | 7.8% | 566.97 | 15.9% | 110% |
| HUM | bull | 25% | 24.2% | 4.8% | 7.8% | 810.22 | 24.4% | 201% |

**Scenario order inversions** (named bear/base/bull intrinsic value is not monotone — this is economic, not a bug):
- HPQ: growth destroys value: forward ROIC 2.0% at/below WACC 9.1%, so higher-growth scenarios reinvest below the cost of capital and are worth less than the bear case

## Boundary Assumptions & Valuation Alerts

- UHS — bounds: share_change_floor_hit;intrinsic_2x_price
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit;intrinsic_2x_price
- VICI — bounds: specialist_model_v1
- ARE — bounds: specialist_model_v1
- OMC — bounds: base_growth_cap_hit;reinvestment_cap_hit;intrinsic_2x_price
- BXP — bounds: specialist_model_v1
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;wacc_floor_hit;reinvestment_cap_hit
- CPT — bounds: specialist_model_v1
- AVB — bounds: specialist_model_v1
- UDR — bounds: specialist_model_v1
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HPQ — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- EQR — bounds: specialist_model_v1

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| ORCL | drawdown_from_high | nan% | -42% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| HON | weekly_drop;drawdown_from_high | -51% | -52% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| CHTR | drawdown_from_high | nan% | -46% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| SMCI | drawdown_from_high | nan% | -44% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- VICI: nan
- ARE: nan
- OMC: incremental_roic_below_wacc
- TTD: heavy_sbc
- BXP: nan
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- CPT: nan
- AVB: nan
- UDR: nan
- CPAY: thin_interest_coverage
- ELV: incremental_roic_below_wacc
- HPQ: incremental_roic_below_wacc
- HUM: thin_interest_coverage, incremental_roic_below_wacc
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
- GPN Global Payments Inc. — consumer_finance_model_not_supported
- BEN Franklin Resources, Inc. — asset_management_model_not_supported
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
- SBAC SBA Communications Corporation — specialist_missing_book_or_price
- ORCL Oracle Corporation — material_event_requires_reunderwriting
- HON Honeywell International Inc. — material_event_requires_reunderwriting
- CHTR Charter Communications, Inc. — material_event_requires_reunderwriting
- SMCI Super Micro Computer, Inc. — material_event_requires_reunderwriting
- XOM Exxon Mobil Corporation — insufficient_model_confidence
- CVX Chevron Corporation — insufficient_model_confidence
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
- COP ConocoPhillips — insufficient_post_valuation_model_confidence
- FCX Freeport-McMoRan Inc. — insufficient_post_valuation_model_confidence
- CI Cigna Corporation — insufficient_post_valuation_model_confidence
- RCL Royal Caribbean Cruises Ltd. — insufficient_post_valuation_model_confidence
- TRGP Targa Resources Corp. — insufficient_post_valuation_model_confidence
- OXY Occidental Petroleum Corporation — insufficient_post_valuation_model_confidence
- NUE Nucor Corporation — insufficient_post_valuation_model_confidence
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
