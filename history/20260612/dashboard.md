# Weekly US Stock Screen — 2026-06-12

Research output only. No trading instructions are generated. Screening
scores only narrow the pool; final ordering comes from scenario
valuation and risk-adjusted return, never from fixed factor weights.
Bear/base/bull weights are ANALYST-SET scenario weights (default
25/50/25), not calibrated probabilities: W(...) columns and P10/P90
are scenario-weighted figures, to be read as stress labels.

## Data Freshness

- Expected market data date: **2026-06-12**
- Fresh price coverage: **100.0%** (0 stale tickers)

## Funnel

| Step | Input | Output | Top rejections |
|---|---|---|---|
| step1_universe | 0 | 514 | - |
| step2_hard_filters | 514 | 321 | persistent_negative_fcf: 22, interest_coverage: 21, adr_excluded: 18 |
| step3_standardize | 321 | 321 | - |
| step4_normalized_model | 321 | 314 | no_normalized_earnings: 7 |
| step5_quality_risk | 314 | 306 | - |
| step6_scenario_valuation | 306 | 268 | irr_below_solver_bound: 31, roic_not_meaningful:meaningless_capital: 6, invalid_valuation_output: 1 |
| step7_risk_adjusted_ranking | 268 | 268 | - |

## Eligible Candidates (5)

The only names presented as actionable research — finite valuation, robust_return > 0, median IRR > hurdle.

## Eligible — risk-adjusted

| # | Ticker | Robust | Med IRR | P10 | P90 | Hurdle CVaR | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 16.0% | 32.8% | 15.2% | 42.8% | 0.0% | 0% | 0.78 | 0.77 |
| 2 | OMC | 11.7% | 29.1% | 20.0% | 35.6% | 0.0% | 0% | 0.82 | 0.68 |
| 3 | FOXA | 5.3% | 26.1% | 7.7% | 35.9% | 4.3% | 0% | 0.90 | 0.68 |
| 4 | CTSH | 3.2% | 18.8% | 9.3% | 24.9% | 2.7% | 0% | 0.87 | 0.87 |
| 5 | CMCSA | 3.1% | 17.8% | 14.1% | 23.2% | 0.0% | 0% | 0.76 | 0.54 |

## Full Robust Ranking (audit — includes ineligible names)

| # | Ticker | Robust | Med IRR | P10 | P90 | Hurdle CVaR | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 16.0% | 32.8% | 15.2% | 42.8% | 0.0% | 0% | 0.78 | 0.77 |
| 2 | OMC | 11.7% | 29.1% | 20.0% | 35.6% | 0.0% | 0% | 0.82 | 0.68 |
| 3 | FOXA | 5.3% | 26.1% | 7.7% | 35.9% | 4.3% | 0% | 0.90 | 0.68 |
| 4 | CTSH | 3.2% | 18.8% | 9.3% | 24.9% | 2.7% | 0% | 0.87 | 0.87 |
| 5 | CMCSA | 3.1% | 17.8% | 14.1% | 23.2% | 0.0% | 0% | 0.76 | 0.54 |
| 6 | ADBE | -0.2% | 17.9% | 7.2% | 24.3% | 4.8% | 0% | 0.98 | 0.79 |
| 7 | CF | -0.4% | 36.3% | 4.3% | 56.5% | 7.7% | 0% | 0.89 | 0.30 |
| 8 | CPAY | -2.0% | 18.2% | 4.8% | 25.5% | 7.2% | 0% | 0.99 | 0.84 |
| 9 | ELV | -2.4% | 11.5% | 9.6% | 17.7% | 2.4% | 0% | 0.84 | 0.67 |
| 10 | ZTS | -4.0% | 16.9% | 3.6% | 24.2% | 8.4% | 0% | 0.98 | 0.90 |
| 11 | HUM | -4.0% | 16.5% | 5.3% | 25.0% | 6.7% | 0% | 0.66 | 0.60 |
| 12 | HPQ | -4.6% | 7.4% | 7.4% | 12.5% | 4.6% | 0% | 0.97 | 0.67 |
| 13 | GIS | -4.7% | 15.4% | 4.6% | 19.7% | 7.4% | 0% | 0.83 | 0.80 |
| 14 | MO | -6.5% | 17.4% | 0.7% | 26.4% | 11.3% | 0% | 0.96 | 0.89 |
| 15 | ACN | -8.3% | 11.4% | 3.7% | 16.3% | 8.3% | 0% | 0.99 | 0.88 |
| 16 | EOG | -8.5% | 24.9% | -1.7% | 44.8% | 13.7% | 0% | 0.83 | 0.40 |
| 17 | APA | -9.3% | 22.5% | -0.9% | 42.4% | 12.9% | 0% | 0.73 | 0.34 |
| 18 | IT | -9.5% | 17.1% | -1.3% | 28.5% | 13.3% | 0% | 0.91 | 0.74 |
| 19 | HCA | -11.2% | 13.8% | -0.7% | 21.5% | 12.7% | 0% | 0.97 | 0.81 |
| 20 | TSN | -11.6% | 12.7% | -0.0% | 25.2% | 12.0% | 0% | 0.61 | 0.58 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | CF | 33.4% | 36.3% | 4.3% | 56.5% | 75% | 199% |
| 2 | FISV | 31.0% | 37.1% | -11.0% | 60.6% | 75% | 211% |
| 3 | UHS | 30.9% | 32.8% | 15.2% | 42.8% | 100% | 130% |
| 4 | CI | 30.3% | 33.8% | -10.1% | 63.7% | 75% | 198% |
| 5 | OMC | 28.5% | 29.1% | 20.0% | 35.6% | 100% | 170% |
| 6 | DVN | 25.5% | 27.9% | -15.4% | 61.7% | 75% | 156% |
| 7 | FOXA | 23.9% | 26.1% | 7.7% | 35.9% | 75% | 104% |
| 8 | EOG | 23.2% | 24.9% | -1.7% | 44.8% | 75% | 110% |
| 9 | APA | 21.6% | 22.5% | -0.9% | 42.4% | 75% | 125% |
| 10 | CMCSA | 18.2% | 17.8% | 14.1% | 23.2% | 100% | 59% |
| 11 | CTSH | 17.9% | 18.8% | 9.3% | 24.9% | 75% | 48% |
| 12 | ADBE | 16.8% | 17.9% | 7.2% | 24.3% | 75% | 26% |
| 13 | CPAY | 16.7% | 18.2% | 4.8% | 25.5% | 75% | 50% |
| 14 | HUM | 15.8% | 16.5% | 5.3% | 25.0% | 75% | 48% |
| 15 | MO | 15.5% | 17.4% | 0.7% | 26.4% | 75% | 52% |
| 16 | ZTS | 15.4% | 16.9% | 3.6% | 24.2% | 75% | 41% |
| 17 | IT | 15.4% | 17.1% | -1.3% | 28.5% | 75% | 37% |
| 18 | LDOS | 14.2% | 17.2% | -7.5% | 29.8% | 75% | 52% |
| 19 | GIS | 13.8% | 15.4% | 4.6% | 19.7% | 75% | 37% |
| 20 | KDP | 13.6% | 16.1% | -8.3% | 30.5% | 75% | 51% |

## Week-over-week

**comparison_baseline_reset** — previous run: 2026-06-12.
The universe or result-affecting config changed (previous run has no universe/config fingerprint); entered/exited/rank-change deltas are suppressed because they would be meaningless against a different baseline.

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| UHS | bear | 25% | 1.7% | 8.9% | 8.0% | 181.43 | 15.2% | 84% |
| UHS | base | 50% | 6.9% | 10.7% | 17.2% | 337.41 | 32.8% | 280% |
| UHS | bull | 25% | 11.0% | 12.1% | 19.6% | 477.63 | 42.8% | 447% |
| OMC | bear | 25% | 18.6% | 12.8% | 6.6% | 140.35 | 20.0% | 162% |
| OMC | base | 50% | 25.0% | 14.6% | 6.6% | 206.92 | 29.1% | 282% |
| OMC | bull | 25% | 30.1% | 15.9% | 6.6% | 267.55 | 35.6% | 392% |
| FOXA | bear | 25% | -1.1% | 17.5% | 6.6% | 68.26 | 7.7% | 39% |
| FOXA | base | 50% | 4.7% | 20.1% | 54.7% | 134.04 | 26.1% | 205% |
| FOXA | bull | 25% | 9.3% | 22.0% | 60.0% | 188.71 | 35.9% | 339% |
| CTSH | bear | 25% | 0.1% | 12.9% | 8.4% | 54.32 | 9.3% | 47% |
| CTSH | base | 50% | 4.9% | 15.0% | 14.2% | 77.46 | 18.8% | 123% |
| CTSH | bull | 25% | 8.8% | 16.6% | 15.0% | 97.71 | 24.9% | 187% |
| CMCSA | bear | 25% | -6.1% | 16.1% | 6.5% | 30.83 | 14.1% | 76% |
| CMCSA | base | 50% | 1.2% | 18.7% | 6.5% | 38.94 | 17.8% | 130% |
| CMCSA | bull | 25% | 7.0% | 20.4% | 6.5% | 52.39 | 23.2% | 210% |
| ADBE | bear | 25% | 8.7% | 29.7% | 11.0% | 174.91 | 7.2% | 35% |
| ADBE | base | 50% | 13.2% | 33.6% | 57.2% | 257.06 | 17.9% | 117% |
| ADBE | bull | 25% | 16.9% | 36.9% | 58.3% | 320.75 | 24.3% | 178% |
| CF | bear | 25% | -10.1% | 22.8% | 6.6% | 99.21 | 4.3% | 20% |
| CF | base | 50% | 14.3% | 31.1% | 16.8% | 327.78 | 36.3% | 356% |
| CF | bull | 25% | 33.8% | 38.4% | 18.0% | 708.04 | 56.5% | 855% |
| CPAY | bear | 25% | 7.7% | 39.8% | 7.5% | 315.43 | 4.8% | 24% |
| CPAY | base | 50% | 13.3% | 44.0% | 30.0% | 535.90 | 18.2% | 125% |
| CPAY | bull | 25% | 17.9% | 47.4% | 30.3% | 708.45 | 25.5% | 203% |
| ELV | bear | 25% | -1.3% | 4.9% | 7.0% | 450.87 | 9.6% | 51% |
| ELV | base | 50% | 4.9% | 5.9% | 7.0% | 501.17 | 11.5% | 75% |
| ELV | bull | 25% | 9.9% | 6.6% | 7.0% | 658.83 | 17.7% | 130% |
| ZTS | bear | 25% | 0.9% | 32.2% | 7.5% | 65.83 | 3.6% | 17% |
| ZTS | base | 50% | 5.3% | 36.0% | 24.5% | 112.58 | 16.9% | 111% |
| ZTS | bull | 25% | 8.8% | 39.1% | 24.8% | 148.69 | 24.2% | 184% |
| HUM | bear | 25% | 12.7% | 2.5% | 7.9% | 338.17 | 5.3% | 29% |
| HUM | base | 50% | 19.3% | 3.7% | 7.9% | 560.26 | 16.5% | 116% |
| HUM | bull | 25% | 24.6% | 4.8% | 7.9% | 800.30 | 25.0% | 209% |
| HPQ | bear | 25% | -3.6% | 5.7% | 8.9% | 24.50 | 9.1% | 44% |
| HPQ | base | 50% | 1.8% | 6.6% | 8.9% | 22.60 | 7.4% | 45% |
| HPQ | bull | 25% | 6.2% | 7.3% | 8.9% | 29.13 | 12.5% | 87% |
| GIS | bear | 25% | -6.5% | 14.8% | 6.5% | 30.35 | 4.6% | 21% |
| GIS | base | 50% | -1.3% | 17.0% | 6.5% | 47.17 | 15.4% | 87% |
| GIS | bull | 25% | 2.8% | 18.6% | 6.5% | 57.70 | 19.7% | 131% |
| MO | bear | 25% | -2.4% | 46.5% | 6.6% | 54.88 | 0.7% | 3% |
| MO | base | 50% | 1.2% | 54.9% | 44.3% | 109.58 | 17.4% | 115% |
| MO | bull | 25% | 4.1% | 62.0% | 46.0% | 154.01 | 26.4% | 206% |
| ACN | bear | 25% | 2.4% | 13.4% | 9.4% | 134.77 | 3.7% | 17% |
| ACN | base | 50% | 7.2% | 14.7% | 18.8% | 184.54 | 11.4% | 65% |
| ACN | bull | 25% | 11.1% | 15.8% | 18.8% | 223.94 | 16.3% | 103% |
| EOG | bear | 25% | -6.3% | 22.4% | 6.7% | 95.02 | -1.7% | -7% |
| EOG | base | 50% | 17.2% | 32.4% | 12.9% | 286.70 | 24.9% | 201% |
| EOG | bull | 25% | 36.1% | 41.1% | 14.2% | 626.34 | 44.8% | 552% |
| APA | bear | 25% | -13.5% | 21.1% | 6.5% | 28.84 | -0.9% | -4% |
| APA | base | 50% | 11.2% | 31.8% | 6.5% | 83.45 | 22.5% | 184% |
| APA | bull | 25% | 31.0% | 40.8% | 6.6% | 185.90 | 42.4% | 528% |
| IT | bear | 25% | -2.0% | 13.0% | 8.1% | 97.45 | -1.3% | -6% |
| IT | base | 50% | 3.3% | 17.1% | 47.6% | 203.24 | 17.1% | 113% |
| IT | bull | 25% | 7.6% | 20.7% | 51.6% | 305.63 | 28.5% | 231% |
| HCA | bear | 25% | 0.8% | 13.3% | 8.2% | 239.82 | -0.7% | -3% |
| HCA | base | 50% | 5.4% | 14.9% | 20.7% | 458.87 | 13.8% | 81% |
| HCA | bull | 25% | 9.1% | 16.2% | 21.1% | 632.73 | 21.5% | 147% |
| TSN | bear | 25% | -3.9% | 4.2% | 6.9% | 42.19 | -0.0% | -0% |
| TSN | base | 50% | 3.8% | 6.7% | 6.9% | 75.92 | 12.7% | 88% |
| TSN | bull | 25% | 10.0% | 8.8% | 6.9% | 132.35 | 25.2% | 226% |

**Scenario order inversions** (named bear/base/bull intrinsic value is not monotone — this is economic, not a bug):
- HPQ: growth destroys value: forward ROIC 2.0% at/below WACC 8.9%, so higher-growth scenarios reinvest below the cost of capital and are worth less than the bear case

## Boundary Assumptions & Valuation Alerts

- UHS — bounds: share_change_floor_hit;intrinsic_2x_price
- OMC — bounds: base_growth_cap_hit;reinvestment_cap_hit;intrinsic_2x_price
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit;intrinsic_2x_price
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;wacc_floor_hit;reinvestment_cap_hit
- ADBE — bounds: share_change_floor_hit
- CF — bounds: share_change_floor_hit;reinvestment_cap_hit;intrinsic_2x_price
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HPQ — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- GIS — bounds: wacc_floor_hit
- EOG — bounds: reinvestment_cap_hit;intrinsic_2x_price
- APA — bounds: wacc_floor_hit;reinvestment_cap_hit;intrinsic_2x_price
- HCA — bounds: share_change_floor_hit
- TSN — bounds: forward_roic_floor_hit;reinvestment_cap_hit

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| CHTR | drawdown_from_high | nan% | -40% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| SMCI | weekly_drop | -34% | nan% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- OMC: incremental_roic_below_wacc
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- ADBE: heavy_sbc
- CF: cyclical_revenue
- CPAY: thin_interest_coverage
- ELV: incremental_roic_below_wacc
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- HPQ: incremental_roic_below_wacc
- GIS: elevated_leverage, incremental_roic_below_wacc
- EOG: cyclical_revenue
- APA: cyclical_revenue, incremental_roic_below_wacc
- HCA: elevated_leverage
- TSN: elevated_leverage, thin_interest_coverage, incremental_roic_below_wacc

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
- PGR The Progressive Corporation — insurance_model_not_supported
- COF Capital One Financial Corporation — consumer_finance_model_not_supported
- PNC The PNC Financial Services Group, Inc. — bank_model_not_supported
- USB U.S. Bancorp — bank_model_not_supported
- AMT American Tower Corporation — reit_model_not_supported
- KKR KKR & Co. Inc. — asset_management_model_not_supported
- MRSH Marsh & McLennan Companies, Inc. — insurance_model_not_supported
- ICE Intercontinental Exchange, Inc. — financial_sector_model_not_supported
- MCO Moody's Corporation — financial_sector_model_not_supported
- APO Apollo Global Management, Inc. — asset_management_model_not_supported
- AON Aon plc — insurance_model_not_supported
- SPG Simon Property Group, Inc. — reit_model_not_supported
- TRV The Travelers Companies, Inc. — insurance_model_not_supported
- DLR Digital Realty Trust, Inc. — reit_model_not_supported
- TFC Truist Financial Corporation — bank_model_not_supported
- AFL Aflac Incorporated — insurance_model_not_supported
- O Realty Income Corporation — reit_model_not_supported
- PSA Public Storage — reit_model_not_supported
- MET MetLife, Inc. — insurance_model_not_supported
- ALL The Allstate Corporation — insurance_model_not_supported
- AJG Arthur J. Gallagher & Co. — insurance_model_not_supported
- STT State Street Corporation — asset_management_model_not_supported
- ARES Ares Management Corporation — asset_management_model_not_supported
- MSCI MSCI Inc. — financial_sector_model_not_supported
- AMP Ameriprise Financial, Inc. — asset_management_model_not_supported
- VTR Ventas, Inc. — reit_model_not_supported
- CCI Crown Castle Inc. — reit_model_not_supported
- AIG American International Group, Inc. — insurance_model_not_supported
- IRM Iron Mountain Incorporated — reit_model_not_supported
- PRU Prudential Financial, Inc. — insurance_model_not_supported
- HIG The Hartford Financial Services Group, Inc. — insurance_model_not_supported
- MTB M&T Bank Corporation — bank_model_not_supported
- VICI VICI Properties Inc. — reit_model_not_supported
- RJF Raymond James Financial, Inc. — asset_management_model_not_supported
- CFG Citizens Financial Group, Inc. — bank_model_not_supported
- AVB AvalonBay Communities, Inc. — reit_model_not_supported
- WRB W. R. Berkley Corporation — insurance_model_not_supported
- EQR Equity Residential — reit_model_not_supported
- RF Regions Financial Corporation — bank_model_not_supported
- SYF Synchrony Financial — consumer_finance_model_not_supported
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
- AIZ Assurant, Inc. — insurance_model_not_supported
- IVZ Invesco Ltd. — asset_management_model_not_supported
- UDR UDR, Inc. — reit_model_not_supported
- CPT Camden Property Trust — reit_model_not_supported
- FRT Federal Realty Investment Trust — reit_model_not_supported
- BXP BXP, Inc. — reit_model_not_supported
- ARE Alexandria Real Estate Equities, Inc. — reit_model_not_supported
- FDS FactSet Research Systems Inc. — financial_sector_model_not_supported
- IBKR Interactive Brokers Group, Inc. — bank_model_not_supported
- EQIX Equinix, Inc. — reit_model_not_supported
- CME CME Group Inc. — financial_sector_model_not_supported
- HOOD Robinhood Markets, Inc. — asset_management_model_not_supported
- NDAQ Nasdaq, Inc. — financial_sector_model_not_supported
- FITB Fifth Third Bancorp — bank_model_not_supported
- COIN Coinbase Global, Inc. — financial_sector_model_not_supported
- ALNY Alnylam Pharmaceuticals, Inc. — preprofit_biotech_not_supported
- PYPL PayPal Holdings, Inc. — consumer_finance_model_not_supported
- HBAN Huntington Bancshares Incorporated — bank_model_not_supported
- ACGL Arch Capital Group Ltd. — insurance_model_not_supported
- CINF Cincinnati Financial Corporation — insurance_model_not_supported
- PFG Principal Financial Group, Inc. — asset_management_model_not_supported
- TROW T. Rowe Price Group, Inc. — asset_management_model_not_supported
- SBAC SBA Communications Corporation — reit_model_not_supported
- INSM Insmed Incorporated — preprofit_biotech_not_supported
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
- T AT&T Inc. — irr_below_solver_bound
- DE Deere & Company — irr_below_solver_bound
- CRM Salesforce, Inc. — irr_below_solver_bound
- SO The Southern Company — irr_below_solver_bound
- WMB The Williams Companies, Inc. — irr_below_solver_bound
- RCL Royal Caribbean Cruises Ltd. — irr_below_solver_bound
- GM General Motors Company — irr_below_solver_bound
- KMI Kinder Morgan, Inc. — irr_below_solver_bound
- TRGP Targa Resources Corp. — irr_below_solver_bound
- CARR Carrier Global Corporation — irr_below_solver_bound
- LHX L3Harris Technologies, Inc. — invalid_valuation_output
- OXY Occidental Petroleum Corporation — irr_below_solver_bound
- DAL Delta Air Lines, Inc. — irr_below_solver_bound
- BDX Becton, Dickinson and Company — irr_below_solver_bound
- CAH Cardinal Health, Inc. — irr_below_solver_bound
- LYV Live Nation Entertainment, Inc. — irr_below_solver_bound
- PEG Public Service Enterprise Group Incorporated — irr_below_solver_bound
- ED Consolidated Edison, Inc. — irr_below_solver_bound
- WEC WEC Energy Group, Inc. — irr_below_solver_bound
- LVS Las Vegas Sands Corp. — irr_below_solver_bound
- NRG NRG Energy, Inc. — irr_below_solver_bound
- IFF International Flavors & Fragrances Inc. — irr_below_solver_bound
- EFX Equifax Inc. — irr_below_solver_bound
- RVTY Revvity, Inc. — irr_below_solver_bound
- CRL Charles River Laboratories International, Inc. — irr_below_solver_bound
- BLDR Builders FirstSource, Inc. — irr_below_solver_bound
- TMUS T-Mobile US, Inc. — irr_below_solver_bound
- AEP American Electric Power Company, Inc. — irr_below_solver_bound
- MCHP Microchip Technology Incorporated — irr_below_solver_bound
- XEL Xcel Energy Inc. — irr_below_solver_bound
- UAL United Airlines Holdings, Inc. — irr_below_solver_bound
- HAS Hasbro, Inc. — irr_below_solver_bound
- BKNG nan — roic_not_meaningful:meaningless_capital
- FTNT nan — roic_not_meaningful:meaningless_capital
- ABNB nan — roic_not_meaningful:meaningless_capital
- EXPE nan — roic_not_meaningful:meaningless_capital
- VRSN nan — roic_not_meaningful:meaningless_capital
- CSGP nan — roic_not_meaningful:meaningless_capital

## Data Gaps and Model Limitations

- Stocks missing core financials were rejected (fail closed), never estimated.
- Banks, insurers, REITs and pre-profit biotech are watchlisted: the general
  owner-earnings DCF does not apply and no substitute model is forced on them.
- Scenario set is discrete (bear/base/bull); a Monte Carlo layer is a planned
  extension and the aggregation already operates on generic distributions.
- Ad-hoc market closures are not in the calendar; freshness checks catch them.
