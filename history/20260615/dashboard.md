# Weekly US Stock Screen — 2026-06-15

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-06-15**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 514 | - |
| step2_hard_filters | 514 | 321 | persistent_negative_fcf: 22, interest_coverage: 21, adr_excluded: 18 |
| step3_standardize | 321 | 321 | - |
| step4_normalized_model | 321 | 314 | no_normalized_earnings: 7 |
| step5_quality_risk | 314 | 306 | - |
| step6_scenario_valuation | 306 | 278 | insufficient_post_valuation_model_confidence: 20, roic_not_meaningful:meaningless_capital: 6, irr_below_solver_bound: 1 |
| step7_risk_adjusted_ranking | 278 | 278 | - |

## Eligible Candidates (7)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 16.1% | 33.0% | 15.3% | 42.9% | 0.0% | 0% | 0.78 | 0.77 |
| 2 | FOXA | 12.4% | 32.2% | 12.6% | 42.4% | 0.0% | 0% | 0.90 | 0.62 |
| 3 | KLAC | 11.9% | 29.4% | 15.7% | 37.7% | 0.0% | 0% | 0.97 | 0.68 |
| 4 | OMC | 8.4% | 26.5% | 17.3% | 32.9% | 0.0% | 0% | 0.80 | 0.58 |
| 5 | TTD | 6.0% | 27.3% | 7.1% | 35.7% | 4.9% | 0% | 0.91 | 0.71 |
| 6 | CTSH | 4.8% | 19.7% | 10.0% | 26.0% | 2.0% | 0% | 0.87 | 0.87 |
| 7 | CMCSA | 2.9% | 18.2% | 14.7% | 23.7% | 0.0% | 0% | 0.76 | 0.46 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Worst Hurdle Gap | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 16.1% | 33.0% | 15.3% | 42.9% | 0.0% | 0% | 0.78 | 0.77 |
| 2 | FOXA | 12.4% | 32.2% | 12.6% | 42.4% | 0.0% | 0% | 0.90 | 0.62 |
| 3 | KLAC | 11.9% | 29.4% | 15.7% | 37.7% | 0.0% | 0% | 0.97 | 0.68 |
| 4 | OMC | 8.4% | 26.5% | 17.3% | 32.9% | 0.0% | 0% | 0.80 | 0.58 |
| 5 | TTD | 6.0% | 27.3% | 7.1% | 35.7% | 4.9% | 0% | 0.91 | 0.71 |
| 6 | CTSH | 4.8% | 19.7% | 10.0% | 26.0% | 2.0% | 0% | 0.87 | 0.87 |
| 7 | CMCSA | 2.9% | 18.2% | 14.7% | 23.7% | 0.0% | 0% | 0.76 | 0.46 |
| 8 | ADBE | -0.7% | 17.6% | 6.9% | 23.9% | 5.1% | 0% | 0.98 | 0.79 |
| 9 | CPAY | -1.5% | 18.5% | 5.1% | 26.0% | 6.9% | 0% | 0.99 | 0.84 |
| 10 | ELV | -2.2% | 11.7% | 9.8% | 17.8% | 2.2% | 0% | 0.84 | 0.67 |
| 11 | HPQ | -3.9% | 8.1% | 8.1% | 13.2% | 3.9% | 0% | 0.97 | 0.67 |
| 12 | HUM | -4.1% | 16.4% | 5.2% | 25.0% | 6.8% | 0% | 0.66 | 0.60 |
| 13 | ZTS | -4.2% | 16.9% | 3.5% | 24.2% | 8.5% | 0% | 0.98 | 0.90 |
| 14 | GIS | -4.3% | 15.6% | 4.8% | 19.9% | 7.2% | 0% | 0.83 | 0.80 |
| 15 | MO | -4.8% | 18.5% | 1.5% | 27.5% | 10.5% | 0% | 0.96 | 0.89 |
| 16 | ACN | -5.2% | 13.9% | 5.1% | 19.0% | 6.9% | 0% | 0.99 | 0.88 |
| 17 | IT | -6.8% | 19.0% | -0.0% | 30.5% | 12.0% | 0% | 0.91 | 0.74 |
| 18 | EOG | -7.2% | 26.0% | -0.9% | 46.0% | 12.9% | 0% | 0.83 | 0.40 |
| 19 | LEN | -10.9% | 8.8% | 1.1% | 19.8% | 10.9% | 0% | 0.49 | 0.43 |
| 20 | INTU | -10.9% | 11.9% | 1.1% | 17.9% | 10.9% | 0% | 0.95 | 0.83 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | UHS | 31.1% | 33.0% | 15.3% | 42.9% | 100% | 132% |
| 2 | FOXA | 29.9% | 32.2% | 12.6% | 42.4% | 100% | 150% |
| 3 | KLAC | 28.1% | 29.4% | 15.7% | 37.7% | 100% | 76% |
| 4 | OMC | 25.8% | 26.5% | 17.3% | 32.9% | 100% | 142% |
| 5 | FISV | 24.9% | 32.7% | -22.1% | 56.3% | 75% | 159% |
| 6 | TTD | 24.4% | 27.3% | 7.1% | 35.7% | 75% | 95% |
| 7 | EOG | 24.3% | 26.0% | -0.9% | 46.0% | 75% | 118% |
| 8 | CTSH | 18.9% | 19.7% | 10.0% | 26.0% | 75% | 53% |
| 9 | CMCSA | 18.7% | 18.2% | 14.7% | 23.7% | 100% | 62% |
| 10 | IT | 17.1% | 19.0% | -0.0% | 30.5% | 75% | 47% |
| 11 | CPAY | 17.0% | 18.5% | 5.1% | 26.0% | 75% | 52% |
| 12 | ADBE | 16.5% | 17.6% | 6.9% | 23.9% | 75% | 25% |
| 13 | MO | 16.5% | 18.5% | 1.5% | 27.5% | 75% | 58% |
| 14 | LDOS | 15.8% | 18.9% | -6.2% | 31.6% | 75% | 62% |
| 15 | HUM | 15.8% | 16.4% | 5.2% | 25.0% | 75% | 48% |
| 16 | ZTS | 15.4% | 16.9% | 3.5% | 24.2% | 75% | 41% |
| 17 | GIS | 14.0% | 15.6% | 4.8% | 19.9% | 75% | 38% |
| 18 | KDP | 13.6% | 16.1% | -8.3% | 30.5% | 75% | 51% |
| 19 | ACN | 13.0% | 13.9% | 5.1% | 19.0% | 75% | 19% |
| 20 | ELV | 12.7% | 11.7% | 9.8% | 17.8% | 25% | 25% |

## Week-over-week

**comparison_baseline_reset** — previous run: 2026-06-12.
The universe or result-affecting config changed (changed: config); entered/exited/rank-change deltas are suppressed because they would be meaningless against a different baseline.

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| UHS | bear | 25% | 1.7% | 8.9% | 8.0% | 181.89 | 15.3% | 84% |
| UHS | base | 50% | 6.9% | 10.7% | 17.2% | 338.42 | 33.0% | 282% |
| UHS | bull | 25% | 11.0% | 12.1% | 19.6% | 479.14 | 42.9% | 450% |
| FOXA | bear | 25% | -1.1% | 17.5% | 6.5% | 69.31 | 12.6% | 69% |
| FOXA | base | 50% | 4.7% | 20.1% | 54.7% | 137.04 | 32.2% | 278% |
| FOXA | bull | 25% | 9.3% | 22.0% | 60.0% | 193.42 | 42.4% | 444% |
| KLAC | bear | 25% | 7.9% | 32.5% | 11.9% | 292.81 | 15.7% | 85% |
| KLAC | base | 50% | 14.6% | 37.6% | 58.4% | 451.55 | 29.4% | 221% |
| KLAC | bull | 25% | 19.9% | 41.9% | 60.0% | 589.70 | 37.7% | 331% |
| OMC | bear | 25% | 18.4% | 12.7% | 6.5% | 125.03 | 17.3% | 132% |
| OMC | base | 50% | 25.0% | 14.6% | 6.5% | 185.39 | 26.5% | 241% |
| OMC | bull | 25% | 30.3% | 15.9% | 6.5% | 240.10 | 32.9% | 340% |
| TTD | bear | 25% | 13.6% | 13.1% | 9.3% | 17.90 | 7.1% | 37% |
| TTD | base | 50% | 19.9% | 17.1% | 41.0% | 37.53 | 27.3% | 224% |
| TTD | bull | 25% | 24.9% | 20.7% | 44.1% | 49.80 | 35.7% | 338% |
| CTSH | bear | 25% | 0.1% | 12.9% | 8.3% | 54.42 | 10.0% | 52% |
| CTSH | base | 50% | 4.9% | 15.0% | 14.2% | 77.65 | 19.7% | 133% |
| CTSH | bull | 25% | 8.8% | 16.6% | 15.0% | 97.98 | 26.0% | 201% |
| CMCSA | bear | 25% | -6.1% | 16.1% | 6.5% | 30.83 | 14.7% | 80% |
| CMCSA | base | 50% | 1.2% | 18.7% | 6.5% | 38.92 | 18.2% | 135% |
| CMCSA | bull | 25% | 7.0% | 20.4% | 6.5% | 52.41 | 23.7% | 217% |
| ADBE | bear | 25% | 8.7% | 29.7% | 11.0% | 174.99 | 6.9% | 34% |
| ADBE | base | 50% | 13.2% | 33.6% | 57.2% | 257.20 | 17.6% | 114% |
| ADBE | bull | 25% | 16.9% | 36.9% | 58.3% | 320.95 | 23.9% | 174% |
| CPAY | bear | 25% | 7.7% | 39.8% | 7.5% | 316.22 | 5.1% | 25% |
| CPAY | base | 50% | 13.3% | 44.0% | 30.0% | 537.81 | 18.5% | 129% |
| CPAY | bull | 25% | 17.9% | 47.4% | 30.3% | 711.23 | 26.0% | 209% |
| ELV | bear | 25% | -1.3% | 4.9% | 7.0% | 451.76 | 9.8% | 52% |
| ELV | base | 50% | 4.9% | 5.9% | 7.0% | 502.43 | 11.7% | 76% |
| ELV | bull | 25% | 9.9% | 6.6% | 7.0% | 660.46 | 17.8% | 132% |
| HPQ | bear | 25% | -3.6% | 5.7% | 8.9% | 24.63 | 9.8% | 49% |
| HPQ | base | 50% | 1.8% | 6.6% | 8.9% | 22.78 | 8.1% | 49% |
| HPQ | bull | 25% | 6.2% | 7.3% | 8.9% | 29.35 | 13.2% | 93% |
| HUM | bear | 25% | 12.7% | 2.5% | 7.9% | 338.61 | 5.2% | 29% |
| HUM | base | 50% | 19.3% | 3.7% | 7.9% | 561.04 | 16.4% | 115% |
| HUM | bull | 25% | 24.6% | 4.8% | 7.9% | 801.45 | 25.0% | 208% |
| ZTS | bear | 25% | 0.9% | 32.2% | 7.4% | 65.90 | 3.5% | 16% |
| ZTS | base | 50% | 5.3% | 36.0% | 24.5% | 112.76 | 16.9% | 111% |
| ZTS | bull | 25% | 8.8% | 39.1% | 24.8% | 148.95 | 24.2% | 185% |
| GIS | bear | 25% | -6.5% | 14.8% | 6.5% | 30.35 | 4.8% | 22% |
| GIS | base | 50% | -1.3% | 17.0% | 6.5% | 47.17 | 15.6% | 88% |
| GIS | bull | 25% | 2.8% | 18.6% | 6.5% | 57.70 | 19.9% | 133% |
| MO | bear | 25% | -2.4% | 46.5% | 6.5% | 55.10 | 1.5% | 7% |
| MO | base | 50% | 1.2% | 54.9% | 44.3% | 110.23 | 18.5% | 123% |
| MO | bull | 25% | 4.1% | 62.0% | 46.0% | 155.04 | 27.5% | 219% |
| ACN | bear | 25% | 2.4% | 13.4% | 9.4% | 139.16 | 5.1% | 25% |
| ACN | base | 50% | 7.2% | 14.7% | 18.8% | 196.00 | 13.9% | 86% |
| ACN | bull | 25% | 11.1% | 15.8% | 18.8% | 237.80 | 19.0% | 130% |
| IT | bear | 25% | -2.1% | 13.0% | 8.0% | 99.52 | -0.0% | -0% |
| IT | base | 50% | 3.3% | 17.1% | 47.6% | 209.51 | 19.0% | 129% |
| IT | bull | 25% | 7.6% | 20.7% | 51.6% | 314.15 | 30.5% | 255% |
| EOG | bear | 25% | -6.3% | 22.4% | 6.7% | 95.31 | -0.9% | -4% |
| EOG | base | 50% | 17.2% | 32.4% | 12.9% | 288.02 | 26.0% | 214% |
| EOG | bull | 25% | 36.1% | 41.1% | 14.2% | 629.55 | 46.0% | 580% |
| LEN | bear | 25% | -10.7% | 9.7% | 9.9% | 61.44 | 1.1% | 5% |
| LEN | base | 50% | 2.1% | 13.8% | 9.9% | 82.83 | 8.8% | 54% |
| LEN | bull | 25% | 12.3% | 16.7% | 9.9% | 138.92 | 19.8% | 157% |
| INTU | bear | 25% | 10.6% | 22.4% | 8.9% | 198.43 | 1.1% | 5% |
| INTU | base | 50% | 15.8% | 25.9% | 16.8% | 314.78 | 11.9% | 74% |
| INTU | bull | 25% | 20.0% | 28.8% | 17.3% | 401.52 | 17.9% | 125% |

**Scenario order inversions** (named bear/base/bull intrinsic value is not monotone — this is economic, not a bug):
- HPQ: growth destroys value: forward ROIC 2.0% at/below WACC 8.9%, so higher-growth scenarios reinvest below the cost of capital and are worth less than the bear case

## Boundary Assumptions & Valuation Alerts

- UHS — bounds: share_change_floor_hit;intrinsic_2x_price
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit;wacc_floor_hit;intrinsic_2x_price
- KLAC — bounds: forward_roic_cap_hit
- OMC — bounds: base_growth_cap_hit;reinvestment_cap_hit;intrinsic_2x_price
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;wacc_floor_hit;reinvestment_cap_hit
- ADBE — bounds: share_change_floor_hit
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HPQ — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- GIS — bounds: wacc_floor_hit
- EOG — bounds: reinvestment_cap_hit;intrinsic_2x_price
- LEN — bounds: forward_roic_floor_hit;reinvestment_cap_hit

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| CHTR | drawdown_from_high | nan% | -41% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| SMCI | weekly_drop | -34% | nan% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- OMC: incremental_roic_below_wacc
- TTD: heavy_sbc
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- ADBE: heavy_sbc
- CPAY: thin_interest_coverage
- ELV: incremental_roic_below_wacc
- HPQ: incremental_roic_below_wacc
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- GIS: elevated_leverage, incremental_roic_below_wacc
- EOG: cyclical_revenue
- LEN: weak_cash_conversion, incremental_roic_below_wacc
- INTU: heavy_sbc

## Watchlist (not rankable under the general model)

- BRK-B Berkshire Hathaway Inc. — insurance_model_not_supported
- JPM JPMorgan Chase & Co. — bank_model_not_supported
- V Visa Inc. — consumer_finance_model_not_supported
- MA Mastercard Incorporated — consumer_finance_model_not_supported
- BAC Bank of America Corporation — bank_model_not_supported
- MS Morgan Stanley — asset_management_model_not_supported
- GS The Goldman Sachs Group, Inc. — asset_management_model_not_supported
- WFC Wells Fargo & Company — bank_model_not_supported
- C Citigroup Inc. — bank_model_not_supported
- AXP American Express Company — consumer_finance_model_not_supported
- BLK BlackRock, Inc. — asset_management_model_not_supported
- SCHW The Charles Schwab Corporation — asset_management_model_not_supported
- WELL Welltower Inc. — reit_model_not_supported
- BX Blackstone Inc. — asset_management_model_not_supported
- PLD Prologis, Inc. — reit_model_not_supported
- SPGI S&P Global Inc. — financial_sector_model_not_supported
- COF Capital One Financial Corporation — consumer_finance_model_not_supported
- PGR The Progressive Corporation — insurance_model_not_supported
- PNC The PNC Financial Services Group, Inc. — bank_model_not_supported
- USB U.S. Bancorp — bank_model_not_supported
- KKR KKR & Co. Inc. — asset_management_model_not_supported
- AMT American Tower Corporation — reit_model_not_supported
- MRSH Marsh & McLennan Companies, Inc. — insurance_model_not_supported
- MCO Moody's Corporation — financial_sector_model_not_supported
- ICE Intercontinental Exchange, Inc. — financial_sector_model_not_supported
- APO Apollo Global Management, Inc. — asset_management_model_not_supported
- AON Aon plc — insurance_model_not_supported
- SPG Simon Property Group, Inc. — reit_model_not_supported
- TRV The Travelers Companies, Inc. — insurance_model_not_supported
- DLR Digital Realty Trust, Inc. — reit_model_not_supported
- TFC Truist Financial Corporation — bank_model_not_supported
- AFL Aflac Incorporated — insurance_model_not_supported
- O Realty Income Corporation — reit_model_not_supported
- ALL The Allstate Corporation — insurance_model_not_supported
- MET MetLife, Inc. — insurance_model_not_supported
- PSA Public Storage — reit_model_not_supported
- AJG Arthur J. Gallagher & Co. — insurance_model_not_supported
- STT State Street Corporation — asset_management_model_not_supported
- MSCI MSCI Inc. — financial_sector_model_not_supported
- ARES Ares Management Corporation — asset_management_model_not_supported
- AMP Ameriprise Financial, Inc. — asset_management_model_not_supported
- VTR Ventas, Inc. — reit_model_not_supported
- AIG American International Group, Inc. — insurance_model_not_supported
- CCI Crown Castle Inc. — reit_model_not_supported
- PRU Prudential Financial, Inc. — insurance_model_not_supported
- IRM Iron Mountain Incorporated — reit_model_not_supported
- HIG The Hartford Financial Services Group, Inc. — insurance_model_not_supported
- MTB M&T Bank Corporation — bank_model_not_supported
- RJF Raymond James Financial, Inc. — asset_management_model_not_supported
- VICI VICI Properties Inc. — reit_model_not_supported
- CFG Citizens Financial Group, Inc. — bank_model_not_supported
- AVB AvalonBay Communities, Inc. — reit_model_not_supported
- WRB W. R. Berkley Corporation — insurance_model_not_supported
- SYF Synchrony Financial — consumer_finance_model_not_supported
- EQR Equity Residential — reit_model_not_supported
- RF Regions Financial Corporation — bank_model_not_supported
- KEY KeyCorp — bank_model_not_supported
- L Loews Corporation — insurance_model_not_supported
- BRO Brown & Brown, Inc. — insurance_model_not_supported
- ESS Essex Property Trust, Inc. — reit_model_not_supported
- INVH Invitation Homes Inc. — reit_model_not_supported
- KIM Kimco Realty Corporation — reit_model_not_supported
- BEN Franklin Resources, Inc. — asset_management_model_not_supported
- MAA Mid-America Apartment Communities, Inc. — reit_model_not_supported
- GPN Global Payments Inc. — consumer_finance_model_not_supported
- DOC Healthpeak Properties, Inc. — reit_model_not_supported
- EG Everest Re Group, Ltd. — insurance_model_not_supported
- GL Globe Life Inc. — insurance_model_not_supported
- IVZ Invesco Ltd. — asset_management_model_not_supported
- AIZ Assurant, Inc. — insurance_model_not_supported
- UDR UDR, Inc. — reit_model_not_supported
- CPT Camden Property Trust — reit_model_not_supported
- FRT Federal Realty Investment Trust — reit_model_not_supported
- BXP BXP, Inc. — reit_model_not_supported
- ARE Alexandria Real Estate Equities, Inc. — reit_model_not_supported
- FDS FactSet Research Systems Inc. — financial_sector_model_not_supported
- EQIX Equinix, Inc. — reit_model_not_supported
- CME CME Group Inc. — financial_sector_model_not_supported
- HOOD Robinhood Markets, Inc. — asset_management_model_not_supported
- NDAQ Nasdaq, Inc. — financial_sector_model_not_supported
- FITB Fifth Third Bancorp — bank_model_not_supported
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- IBKR Interactive Brokers Group, Inc. — bank_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- HBAN Huntington Bancshares Incorporated — bank_model_not_supported
- ACGL Arch Capital Group Ltd. — insurance_model_not_supported
- CINF Cincinnati Financial Corporation — insurance_model_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- INSM Insmed Incorporated — preprofit_biotech_not_supported
- SBAC SBA Communications Corporation — reit_model_not_supported
- MRNA Moderna, Inc. — preprofit_biotech_not_supported
- HST Host Hotels & Resorts, Inc. — reit_model_not_supported
- REG Regency Centers Corporation — reit_model_not_supported
- ERIE Erie Indemnity Company — insurance_model_not_supported
- CHTR Charter Communications, Inc. — material_event_requires_reunderwriting
- SMCI Super Micro Computer, Inc. — material_event_requires_reunderwriting
- XOM Exxon Mobil Corporation — insufficient_model_confidence
- CVX Chevron Corporation — insufficient_model_confidence
- COP ConocoPhillips — insufficient_model_confidence
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
- VLO Valero Energy Corporation — insufficient_post_valuation_model_confidence
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
- MU Micron Technology, Inc. — insufficient_post_valuation_model_confidence
- AMD Advanced Micro Devices, Inc. — insufficient_post_valuation_model_confidence
- APP AppLovin Corporation — insufficient_post_valuation_model_confidence
- STLD Steel Dynamics, Inc. — insufficient_post_valuation_model_confidence
- APA APA Corporation — insufficient_post_valuation_model_confidence

## Data Gaps and Model Limitations

- Stocks missing core financials were rejected (fail closed), never estimated.
- Banks, insurers, REITs and pre-profit biotech are watchlisted: the general
  owner-earnings DCF does not apply and no substitute model is forced on them.
- Scenario set is discrete (bear/base/bull); worst-case stress metrics are
  deterministic bear/base/bull stress labels, not calibrated CVaR.
- Ad-hoc market closures are not in the calendar; freshness checks catch them.
