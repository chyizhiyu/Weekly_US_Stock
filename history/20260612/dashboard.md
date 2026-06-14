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
| step2_hard_filters | 514 | 319 | persistent_negative_fcf: 22, interest_coverage: 21, adr_excluded: 18 |
| step3_standardize | 319 | 319 | - |
| step4_normalized_model | 319 | 312 | no_normalized_earnings: 7 |
| step5_quality_risk | 312 | 304 | - |
| step6_scenario_valuation | 304 | 278 | insufficient_post_valuation_model_confidence: 18, roic_not_meaningful:meaningless_capital: 6, irr_below_solver_bound: 1 |
| step7_risk_adjusted_ranking | 278 | 278 | - |

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
| 6 | CPAY | -2.0% | 18.2% | 4.8% | 25.5% | 7.2% | 0% | 0.99 | 0.84 |
| 7 | ELV | -2.4% | 11.5% | 9.6% | 17.7% | 2.4% | 0% | 0.84 | 0.67 |
| 8 | ZTS | -4.0% | 16.9% | 3.6% | 24.2% | 8.4% | 0% | 0.98 | 0.90 |
| 9 | HUM | -4.0% | 16.5% | 5.3% | 25.0% | 6.7% | 0% | 0.66 | 0.60 |
| 10 | HPQ | -4.6% | 7.4% | 7.4% | 12.5% | 4.6% | 0% | 0.97 | 0.67 |
| 11 | GIS | -4.7% | 15.4% | 4.6% | 19.7% | 7.4% | 0% | 0.83 | 0.80 |
| 12 | MO | -6.5% | 17.4% | 0.7% | 26.4% | 11.3% | 0% | 0.96 | 0.89 |
| 13 | ACN | -8.3% | 11.4% | 3.7% | 16.3% | 8.3% | 0% | 0.99 | 0.88 |
| 14 | EOG | -8.5% | 24.9% | -1.7% | 44.8% | 13.7% | 0% | 0.83 | 0.40 |
| 15 | IT | -9.5% | 17.1% | -1.3% | 28.5% | 13.3% | 0% | 0.91 | 0.74 |
| 16 | HCA | -11.2% | 13.8% | -0.7% | 21.5% | 12.7% | 0% | 0.97 | 0.81 |
| 17 | TSN | -11.6% | 12.7% | -0.0% | 25.2% | 12.0% | 0% | 0.61 | 0.58 |
| 18 | PHM | -11.7% | 9.5% | 0.3% | 15.2% | 11.7% | 0% | 0.80 | 0.66 |
| 19 | INTU | -11.9% | 9.4% | 0.1% | 15.4% | 11.9% | 0% | 0.95 | 0.83 |
| 20 | MCK | -13.1% | 13.1% | -2.0% | 21.6% | 14.0% | 0% | 0.96 | 0.77 |

## Upside Ranking — high-dispersion RESEARCH QUEUE (not actionable)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | UHS | 30.9% | 32.8% | 15.2% | 42.8% | 100% | 130% |
| 2 | OMC | 28.5% | 29.1% | 20.0% | 35.6% | 100% | 170% |
| 3 | FOXA | 23.9% | 26.1% | 7.7% | 35.9% | 75% | 104% |
| 4 | EOG | 23.2% | 24.9% | -1.7% | 44.8% | 75% | 110% |
| 5 | FISV | 21.3% | 29.1% | -24.8% | 52.1% | 75% | 127% |
| 6 | CMCSA | 18.2% | 17.8% | 14.1% | 23.2% | 100% | 59% |
| 7 | CTSH | 17.9% | 18.8% | 9.3% | 24.9% | 75% | 48% |
| 8 | CPAY | 16.7% | 18.2% | 4.8% | 25.5% | 75% | 50% |
| 9 | HUM | 15.8% | 16.5% | 5.3% | 25.0% | 75% | 48% |
| 10 | MO | 15.5% | 17.4% | 0.7% | 26.4% | 75% | 52% |
| 11 | ZTS | 15.4% | 16.9% | 3.6% | 24.2% | 75% | 41% |
| 12 | IT | 15.4% | 17.1% | -1.3% | 28.5% | 75% | 37% |
| 13 | LDOS | 14.2% | 17.2% | -7.5% | 29.8% | 75% | 52% |
| 14 | GIS | 13.8% | 15.4% | 4.6% | 19.7% | 75% | 37% |
| 15 | KDP | 13.6% | 16.1% | -8.3% | 30.5% | 75% | 51% |
| 16 | TSN | 12.6% | 12.7% | -0.0% | 25.2% | 75% | 32% |
| 17 | ELV | 12.6% | 11.5% | 9.6% | 17.7% | 25% | 24% |
| 18 | HCA | 12.1% | 13.8% | -0.7% | 21.5% | 75% | 19% |
| 19 | MKC | 12.0% | 14.1% | -4.0% | 23.9% | 75% | 33% |
| 20 | MCK | 11.5% | 13.1% | -2.0% | 21.6% | 75% | 27% |

## Week-over-week

Previous run: 2026-06-12

- Entered Robust Top: none
- Exited Robust Top: none
- Entered Upside Top: none
- Exited Upside Top: none

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
| IT | bear | 25% | -2.0% | 13.0% | 8.1% | 97.45 | -1.3% | -6% |
| IT | base | 50% | 3.3% | 17.1% | 47.6% | 203.24 | 17.1% | 113% |
| IT | bull | 25% | 7.6% | 20.7% | 51.6% | 305.63 | 28.5% | 231% |
| HCA | bear | 25% | 0.8% | 13.3% | 8.2% | 239.82 | -0.7% | -3% |
| HCA | base | 50% | 5.4% | 14.9% | 20.7% | 458.87 | 13.8% | 81% |
| HCA | bull | 25% | 9.1% | 16.2% | 21.1% | 632.73 | 21.5% | 147% |
| TSN | bear | 25% | -3.9% | 4.2% | 6.9% | 42.19 | -0.0% | -0% |
| TSN | base | 50% | 3.8% | 6.7% | 6.9% | 75.92 | 12.7% | 88% |
| TSN | bull | 25% | 10.0% | 8.8% | 6.9% | 132.35 | 25.2% | 226% |
| PHM | bear | 25% | -6.0% | 14.4% | 10.0% | 83.44 | 0.3% | 1% |
| PHM | base | 50% | 2.0% | 18.0% | 10.0% | 119.53 | 9.5% | 54% |
| PHM | bull | 25% | 8.4% | 20.7% | 10.0% | 148.73 | 15.2% | 100% |
| INTU | bear | 25% | 10.6% | 22.4% | 8.9% | 186.32 | 0.1% | 0% |
| INTU | base | 50% | 15.8% | 25.9% | 16.8% | 282.21 | 9.4% | 55% |
| INTU | bull | 25% | 20.0% | 28.8% | 17.3% | 362.39 | 15.4% | 101% |
| MCK | bear | 25% | 6.8% | 1.2% | 6.8% | 529.26 | -2.0% | -9% |
| MCK | base | 50% | 11.1% | 1.4% | 57.8% | 998.24 | 13.1% | 83% |
| MCK | bull | 25% | 14.5% | 1.5% | 60.0% | 1378.34 | 21.6% | 161% |

**Scenario order inversions** (named bear/base/bull intrinsic value is not monotone — this is economic, not a bug):
- HPQ: growth destroys value: forward ROIC 2.0% at/below WACC 8.9%, so higher-growth scenarios reinvest below the cost of capital and are worth less than the bear case

## Boundary Assumptions & Valuation Alerts

- UHS — bounds: share_change_floor_hit;intrinsic_2x_price
- OMC — bounds: base_growth_cap_hit;reinvestment_cap_hit;intrinsic_2x_price
- FOXA — bounds: forward_roic_cap_hit;share_change_floor_hit;intrinsic_2x_price
- CMCSA — bounds: forward_roic_floor_hit;share_change_floor_hit;wacc_floor_hit;reinvestment_cap_hit
- ELV — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HUM — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- HPQ — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- GIS — bounds: wacc_floor_hit
- EOG — bounds: reinvestment_cap_hit;intrinsic_2x_price
- HCA — bounds: share_change_floor_hit
- TSN — bounds: forward_roic_floor_hit;reinvestment_cap_hit
- PHM — bounds: share_change_floor_hit
- MCK — bounds: forward_roic_cap_hit

## Turnaround Watchlist (material events)

| Ticker | Triggers | Wk drop | Drawdown | Status | Evidence needed |
|---|---|---|---|---|---|
| ORCL | weekly_drop | -26% | nan% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| ADBE | weekly_drop | -26% | nan% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| CHTR | drawdown_from_high | nan% | -40% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |
| SMCI | weekly_drop | -35% | nan% | awaiting_new_evidence | a post-event 10-Q/10-K or updated guidance reflecting the event |

## Key Risks and Failure Conditions

- OMC: incremental_roic_below_wacc
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- CPAY: thin_interest_coverage
- ELV: incremental_roic_below_wacc
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- HPQ: incremental_roic_below_wacc
- GIS: elevated_leverage, incremental_roic_below_wacc
- EOG: cyclical_revenue
- HCA: elevated_leverage
- TSN: thin_interest_coverage, incremental_roic_below_wacc
- PHM: incremental_roic_below_wacc
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
- ORCL Oracle Corporation — material_event_requires_reunderwriting
- ADBE Adobe Inc. — material_event_requires_reunderwriting
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
- RCL Royal Caribbean Cruises Ltd. — insufficient_post_valuation_model_confidence
- CI Cigna Corporation — insufficient_post_valuation_model_confidence
- VLO Valero Energy Corporation — insufficient_post_valuation_model_confidence
- NUE Nucor Corporation — insufficient_post_valuation_model_confidence
- TRGP Targa Resources Corp. — insufficient_post_valuation_model_confidence
- OXY Occidental Petroleum Corporation — insufficient_post_valuation_model_confidence
- XYZ Block, Inc. — insufficient_post_valuation_model_confidence
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
- Scenario set is discrete (bear/base/bull); a Monte Carlo layer is a planned
  extension and the aggregation already operates on generic distributions.
- Ad-hoc market closures are not in the calendar; freshness checks catch them.
