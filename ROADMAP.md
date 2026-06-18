# Roadmap - intentionally deferred work

This file separates work that was **deliberately deferred** (each with a known
prerequisite or trigger) from anything accidentally missed. Everything under
"Shipped" is done, test-gated and committed; everything under "Deferred" is a
conscious choice, not a gap.

## Shipped
- Cross-platform run-date lock (bounded, fail-closed) + cross-process test + Windows CI.
- SBC: expense-method fade toward an industry peer median; SBC removed from per-share dilution (zero-SBC names provably unchanged).
- FMP one-off detection (MAD vs ex-latest history) -> data-confidence haircut; quarterly YTD cash-flow guard (de-cumulate, else drop to the annual anchor).
- SEC reconciliation (revenue / operating income / net income / shares, same fiscal year) -> soft divergence haircuts confidence, hard divergence routes to the watchlist.
- CVaR honesty: the degenerate 3-point "CVaR" renamed to a deterministic worst-case stress; redundant tail integral removed.
- Event gate: structured events + SEC 8-K detector wired into the pipeline; `material_events.csv` archived.
- Forward validation: point-in-time archive (paper portfolio + fingerprints) + `forward-validate` CLI (rank IC, hit rate, excess, cohorted by config_fingerprint).
- Cross-asset evaluation spine skeleton + equity plugin (shared Layer 4; per-asset Layer 1-3 plugins).
- Financial-sector specialist v1: banks/insurers via justified P/B residual-income proxy; REITs via conservative P/AFFO proxy; incomplete specialist inputs stay watchlisted.

## Deferred (intentional)

### 1. Financial-sector specialist model depth
Banks, insurers and REITs now have conservative v1 specialist models and can
enter ranking when inputs are complete. The intentionally deferred work is model
depth, not basic coverage.
- **Next step (by priority):** banks (ROTCE/TBV, CET1/excess capital, deposit
  beta), REITs (reported AFFO, NAV, same-store NOI, rate sensitivity), insurers
  (combined ratio, underwriting margin, reserve development, statutory capital),
  asset managers (AUM, fee rate, net flows), consumer finance (credit losses and
  funding spread).
- **Why deferred:** the standard FMP statement payload does not expose these
  specialist operating drivers cleanly. v1 is deliberately capped in model
  confidence and should be upgraded only with better fields or forward evidence.

### 2. Estimate-revision events
The event gate covers price shocks + SEC 8-K, but not analyst guidance / estimate
revisions.
- **Prerequisite:** weekly **estimate-snapshot archiving**. The run loads
  estimates but does not archive them, so consecutive snapshots cannot be diffed.
  Add `estimates.csv` to the per-run archive, then a detector that compares
  week-over-week to emit `estimate_revision` events.

### 3. SEC networked end-to-end smoke
The SEC reconciliation and 8-K paths are unit-tested offline with fakes; the live
EDGAR calls (companyfacts / submissions) are never exercised in CI (no network,
no `SEC_USER_AGENT` in the sandbox).
- **Next step:** a one-time manual smoke on a machine with `SEC_USER_AGENT` set,
  against a few known tickers (one with a recent 8-K item 4.02, one clean). This
  is a verification gap, not a code gap.

### 4. Crypto / Pre-IPO-perp asset plugins
The cross-asset spine (`cross_asset/`) is ready and Layer 4 (risk scoring) is
shared; a new asset class needs only a new `AssetModel` plugin supplying Layer 1-3.
- **Why deferred (firm):** the per-asset Layer 2-3 are separate research problems
  - crypto (real yield, MC/TVL, unlock schedules, smart-money flow), perps
  (parent NAV, IPO-conversion probability, settlement). They must wait until the
  equity model has accumulated months of `forward-validate` history and shown the
  ranking actually predicts returns. Extending an unvalidated model only
  multiplies unproven surface area.

### 5. Smaller v1 notes (revisit opportunistically)
- SBC share model: non-SBC "other issuance" is held flat / floored at 0 (no
  M&A-issuance extrapolation); decompose if a cleaner signal appears.
- Forward validation: delisted names are dropped at a horizon (survivorship); the
  production price wiring should use last-available / explicit-loss instead.
- Freeze the benchmark (SPY) entry close in `run_metadata.json` for drift-proof
  excess returns (currently fetched by date at validation time).
