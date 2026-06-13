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
| step2_hard_filters | 514 | 322 | persistent_negative_fcf: 22, interest_coverage: 21, adr_excluded: 18 |
| step3_standardize | 322 | 322 | - |
| step4_normalized_model | 322 | 315 | no_normalized_earnings: 7 |
| step5_quality_risk | 315 | 307 | - |
| step6_scenario_valuation | 307 | 307 | - |
| step7_risk_adjusted_ranking | 307 | 307 | - |

## Robust Top 20 (risk-adjusted)

| # | Ticker | Robust | Med IRR | P10 | P90 | Hurdle CVaR | W(perm loss) | Quality | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | UHS | 18.8% | 34.0% | 16.2% | 44.3% | 0.0% | 0% | 0.78 | 0.85 |
| 2 | OMC | 14.6% | 29.3% | 20.1% | 35.9% | 0.0% | 0% | 0.82 | 0.84 |
| 3 | FOXA | 8.7% | 27.1% | 7.9% | 37.3% | 4.1% | 0% | 0.90 | 0.85 |
| 4 | CMCSA | 6.6% | 20.0% | 14.9% | 26.3% | 0.0% | 0% | 0.76 | 0.83 |
| 5 | CTSH | 3.6% | 19.1% | 9.4% | 25.4% | 2.6% | 0% | 0.87 | 0.87 |
| 6 | CF | 1.4% | 38.0% | 3.9% | 60.1% | 8.1% | 0% | 0.89 | 0.37 |
| 7 | ADBE | -0.3% | 17.8% | 6.6% | 24.4% | 5.4% | 0% | 0.98 | 0.88 |
| 8 | CPAY | -1.6% | 18.7% | 4.7% | 26.4% | 7.3% | 0% | 0.99 | 0.84 |
| 9 | ELV | -1.8% | 12.4% | 9.8% | 19.0% | 2.2% | 0% | 0.84 | 0.83 |
| 10 | HUM | -2.9% | 17.1% | 5.4% | 25.9% | 6.6% | 0% | 0.66 | 0.74 |
| 11 | HPQ | -3.8% | 8.2% | 8.2% | 14.0% | 3.8% | 0% | 0.97 | 0.83 |
| 12 | ZTS | -4.0% | 17.4% | 3.2% | 24.9% | 8.8% | 0% | 0.98 | 0.90 |
| 13 | GIS | -4.1% | 16.2% | 4.1% | 21.2% | 7.9% | 0% | 0.83 | 0.89 |
| 14 | MO | -6.8% | 17.7% | 0.1% | 26.9% | 11.9% | 0% | 0.96 | 0.89 |
| 15 | ACN | -8.5% | 11.5% | 3.5% | 16.4% | 8.5% | 0% | 0.99 | 0.88 |
| 16 | EOG | -8.5% | 25.8% | -2.7% | 46.9% | 14.7% | 0% | 0.83 | 0.45 |
| 17 | IT | -10.4% | 17.7% | -2.6% | 29.6% | 14.6% | 0% | 0.91 | 0.74 |
| 18 | HCA | -11.2% | 15.1% | -1.9% | 23.7% | 13.9% | 0% | 0.97 | 0.89 |
| 19 | APA | -11.4% | 22.5% | -3.5% | 43.9% | 15.5% | 0% | 0.73 | 0.39 |
| 20 | TSN | -11.6% | 12.9% | -0.2% | 25.7% | 12.2% | 0% | 0.61 | 0.71 |

## Upside Top 20 (expected IRR)

| # | Ticker | E[IRR] | Median | P10 | P90 | W(IRR>hurdle) | Upside to base |
|---|---|---|---|---|---|---|---|
| 1 | LHX | 93.7% | -12.7% | -12.7% | 200.0% | 50% | -66% |
| 2 | CF | 35.0% | 38.0% | 3.9% | 60.1% | 75% | 199% |
| 3 | FISV | 33.2% | 40.8% | -14.8% | 66.2% | 75% | 211% |
| 4 | UHS | 32.2% | 34.0% | 16.2% | 44.3% | 100% | 130% |
| 5 | CI | 32.0% | 36.2% | -13.4% | 68.8% | 75% | 198% |
| 6 | OMC | 28.7% | 29.3% | 20.1% | 35.9% | 100% | 170% |
| 7 | DVN | 26.0% | 28.8% | -17.1% | 63.4% | 75% | 156% |
| 8 | FOXA | 24.8% | 27.1% | 7.9% | 37.3% | 75% | 104% |
| 9 | EOG | 23.9% | 25.8% | -2.7% | 46.9% | 75% | 110% |
| 10 | CHTR | 22.6% | 54.3% | -95.0% | 76.9% | 75% | 349% |
| 11 | APA | 21.3% | 22.5% | -3.5% | 43.9% | 75% | 125% |
| 12 | CMCSA | 20.3% | 20.0% | 14.9% | 26.3% | 100% | 59% |
| 13 | CTSH | 18.3% | 19.1% | 9.4% | 25.4% | 75% | 48% |
| 14 | CPAY | 17.1% | 18.7% | 4.7% | 26.4% | 75% | 50% |
| 15 | ADBE | 16.7% | 17.8% | 6.6% | 24.4% | 75% | 23% |
| 16 | HUM | 16.4% | 17.1% | 5.4% | 25.9% | 75% | 48% |
| 17 | ZTS | 15.7% | 17.4% | 3.2% | 24.9% | 75% | 41% |
| 18 | MO | 15.6% | 17.7% | 0.1% | 26.9% | 75% | 52% |
| 19 | IT | 15.6% | 17.7% | -2.6% | 29.6% | 75% | 37% |
| 20 | LDOS | 14.5% | 17.9% | -9.0% | 31.1% | 75% | 52% |

## Week-over-week

Previous run: 2026-06-12

- Entered Robust Top: ACN, APA, CPAY, ELV, EOG, GIS, HCA, HPQ, HUM, IT, MO, TSN, ZTS
- Exited Robust Top: ALSN, CRI, DOX, EEFT, HLF, HRB, INVA, MMS, MOH, NSP, OPFI, SMPL, TNET
- Entered Upside Top: ADBE, APA, CHTR, CMCSA, CPAY, CTSH, EOG, FOXA, HUM, IT, LDOS, MO, ZTS
- Exited Upside Top: ALSN, CQP, EEFT, GRNT, HLF, HRB, HRMY, INVA, IRWD, NSP, OPFI, SMPL, TNET

Largest robust-rank moves:

- LHX: 867 → 307 (+560)
- MCHP: 861 → 306 (+555)
- CRM: 856 → 305 (+551)
- GM: 849 → 304 (+545)
- XEL: 842 → 303 (+539)

## Scenarios for Ranked Names (Bear / Base / Bull)

| Ticker | Scenario | P | Growth y1 | Margin | Terminal ROIC | Value/share | IRR 5y | Return 5y |
|---|---|---|---|---|---|---|---|---|
| UHS | bear | 25% | 1.7% | 8.9% | 8.0% | 181.43 | 16.2% | 100% |
| UHS | base | 50% | 6.9% | 10.7% | 17.2% | 337.41 | 34.0% | 301% |
| UHS | bull | 25% | 11.0% | 12.1% | 19.6% | 477.63 | 44.3% | 483% |
| OMC | bear | 25% | 18.6% | 12.8% | 6.6% | 140.35 | 20.1% | 164% |
| OMC | base | 50% | 25.0% | 14.6% | 6.6% | 206.92 | 29.3% | 286% |
| OMC | bull | 25% | 30.1% | 15.9% | 6.6% | 267.55 | 35.9% | 398% |
| FOXA | bear | 25% | -1.1% | 17.5% | 6.6% | 68.26 | 7.9% | 45% |
| FOXA | base | 50% | 4.7% | 20.1% | 54.7% | 134.04 | 27.1% | 221% |
| FOXA | bull | 25% | 9.3% | 22.0% | 60.0% | 188.71 | 37.3% | 367% |
| CMCSA | bear | 25% | -6.1% | 16.1% | 6.5% | 30.83 | 14.9% | 90% |
| CMCSA | base | 50% | 1.2% | 18.7% | 6.5% | 38.94 | 20.0% | 167% |
| CMCSA | bull | 25% | 7.0% | 20.4% | 6.5% | 52.39 | 26.3% | 275% |
| CTSH | bear | 25% | 0.1% | 12.9% | 8.4% | 54.32 | 9.4% | 51% |
| CTSH | base | 50% | 4.9% | 15.0% | 14.2% | 77.46 | 19.1% | 127% |
| CTSH | bull | 25% | 8.8% | 16.6% | 15.0% | 97.71 | 25.4% | 195% |
| CF | bear | 25% | -10.1% | 22.8% | 6.6% | 99.21 | 3.9% | 20% |
| CF | base | 50% | 14.3% | 31.1% | 16.8% | 327.78 | 38.0% | 393% |
| CF | bull | 25% | 33.8% | 38.4% | 18.0% | 708.04 | 60.1% | 1021% |
| ADBE | bear | 25% | 7.9% | 29.7% | 11.0% | 170.83 | 6.6% | 35% |
| ADBE | base | 50% | 12.4% | 33.6% | 57.2% | 250.36 | 17.8% | 118% |
| ADBE | bull | 25% | 16.1% | 36.9% | 58.3% | 312.23 | 24.4% | 182% |
| CPAY | bear | 25% | 7.7% | 39.8% | 7.5% | 315.43 | 4.7% | 26% |
| CPAY | base | 50% | 13.3% | 44.0% | 30.0% | 535.90 | 18.7% | 133% |
| CPAY | bull | 25% | 17.9% | 47.4% | 30.3% | 708.45 | 26.4% | 217% |
| ELV | bear | 25% | -1.3% | 4.9% | 7.0% | 450.87 | 9.8% | 56% |
| ELV | base | 50% | 4.9% | 5.9% | 7.0% | 501.17 | 12.4% | 87% |
| ELV | bull | 25% | 9.9% | 6.6% | 7.0% | 658.83 | 19.0% | 152% |
| HUM | bear | 25% | 12.7% | 2.5% | 7.9% | 338.17 | 5.4% | 31% |
| HUM | base | 50% | 19.3% | 3.7% | 7.9% | 560.26 | 17.1% | 125% |
| HUM | bull | 25% | 24.6% | 4.8% | 7.9% | 800.30 | 25.9% | 227% |
| HPQ | bear | 25% | -3.6% | 5.7% | 8.9% | 24.50 | 9.1% | 49% |
| HPQ | base | 50% | 1.8% | 6.6% | 8.9% | 22.60 | 8.2% | 55% |
| HPQ | bull | 25% | 6.2% | 7.3% | 8.9% | 29.13 | 14.0% | 108% |
| ZTS | bear | 25% | 0.9% | 32.2% | 7.5% | 65.83 | 3.2% | 16% |
| ZTS | base | 50% | 5.3% | 36.0% | 24.5% | 112.58 | 17.4% | 116% |
| ZTS | bull | 25% | 8.8% | 39.1% | 24.8% | 148.69 | 24.9% | 194% |
| GIS | bear | 25% | -6.5% | 14.8% | 6.5% | 30.35 | 4.1% | 21% |
| GIS | base | 50% | -1.3% | 17.0% | 6.5% | 47.17 | 16.2% | 101% |
| GIS | bull | 25% | 2.8% | 18.6% | 6.5% | 57.70 | 21.2% | 157% |
| MO | bear | 25% | -2.4% | 46.5% | 6.6% | 54.88 | 0.1% | 1% |
| MO | base | 50% | 1.2% | 54.9% | 44.3% | 109.58 | 17.7% | 118% |
| MO | bull | 25% | 4.1% | 62.0% | 46.0% | 154.01 | 26.9% | 214% |
| ACN | bear | 25% | 2.4% | 13.4% | 9.4% | 134.76 | 3.5% | 17% |
| ACN | base | 50% | 7.2% | 14.7% | 18.8% | 184.53 | 11.5% | 65% |
| ACN | bull | 25% | 11.1% | 15.8% | 18.8% | 223.92 | 16.4% | 104% |
| EOG | bear | 25% | -6.3% | 22.4% | 6.7% | 95.02 | -2.7% | -12% |
| EOG | base | 50% | 17.2% | 32.4% | 12.9% | 286.70 | 25.8% | 220% |
| EOG | bull | 25% | 36.1% | 41.1% | 14.2% | 626.34 | 46.9% | 626% |
| IT | bear | 25% | -2.0% | 13.0% | 8.1% | 97.45 | -2.6% | -12% |
| IT | base | 50% | 3.3% | 17.1% | 47.6% | 203.24 | 17.7% | 120% |
| IT | bull | 25% | 7.6% | 20.7% | 51.6% | 305.63 | 29.6% | 248% |
| HCA | bear | 25% | 0.8% | 13.3% | 8.2% | 239.82 | -1.9% | -9% |
| HCA | base | 50% | 5.4% | 14.9% | 20.7% | 458.87 | 15.1% | 99% |
| HCA | bull | 25% | 9.1% | 16.2% | 21.1% | 632.73 | 23.7% | 185% |
| APA | bear | 25% | -16.2% | 21.1% | 6.5% | 25.73 | -3.5% | -14% |
| APA | base | 50% | 11.2% | 31.8% | 6.5% | 83.41 | 22.5% | 184% |
| APA | bull | 25% | 33.1% | 40.8% | 6.6% | 196.25 | 43.9% | 563% |
| TSN | bear | 25% | -3.9% | 4.2% | 6.9% | 42.19 | -0.2% | -1% |
| TSN | base | 50% | 3.8% | 6.7% | 6.9% | 75.92 | 12.9% | 92% |
| TSN | bull | 25% | 10.0% | 8.8% | 6.9% | 132.35 | 25.7% | 236% |

## Key Risks and Failure Conditions

- OMC: incremental_roic_below_wacc
- CMCSA: thin_interest_coverage, incremental_roic_below_wacc
- CF: cyclical_revenue
- ADBE: heavy_sbc
- CPAY: thin_interest_coverage
- ELV: incremental_roic_below_wacc
- HUM: thin_interest_coverage, incremental_roic_below_wacc
- HPQ: incremental_roic_below_wacc
- GIS: elevated_leverage, incremental_roic_below_wacc
- EOG: cyclical_revenue
- HCA: elevated_leverage
- APA: cyclical_revenue, incremental_roic_below_wacc
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
- SMCI Super Micro Computer, Inc. — material_event_requires_reunderwriting
- XOM Exxon Mobil Corporation — insufficient_model_confidence
- CVX Chevron Corporation — insufficient_model_confidence
- COP ConocoPhillips — insufficient_model_confidence
- MPC Marathon Petroleum Corporation — insufficient_model_confidence
- PSX Phillips 66 — insufficient_model_confidence
- CCL Carnival Corporation & plc — insufficient_model_confidence
- MOS The Mosaic Company — insufficient_model_confidence
- TSLA Tesla, Inc. — insufficient_model_confidence

## Data Gaps and Model Limitations

- Stocks missing core financials were rejected (fail closed), never estimated.
- Banks, insurers, REITs and pre-profit biotech are watchlisted: the general
  owner-earnings DCF does not apply and no substitute model is forced on them.
- Scenario set is discrete (bear/base/bull); a Monte Carlo layer is a planned
  extension and the aggregation already operates on generic distributions.
- Ad-hoc market closures are not in the calendar; freshness checks catch them.
