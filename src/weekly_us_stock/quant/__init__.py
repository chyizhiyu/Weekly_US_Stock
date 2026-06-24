"""GNN-Transformer-DRL monthly quantitative trading system.

This subpackage hosts the *new* monthly quant research stack that is layered on
top of the existing weekly screener's FMP plumbing. It is built in six
independently testable stages:

1. ``stage1`` - FMP dual-track timestamp alignment gateway + monthly resampler.
2. ``stage2`` - Markov regime-switching (MRSM) defensive front switch (deferred).
3. ``stage3`` - SSA decomposition + Lambert-W feature de-noising (deferred).
4. ``stage4`` - Combinatorial purged & embargoed cross-validation (deferred).
5. ``stage5`` - GNN-Transformer encoder with Focal-Loss/OHEM head (deferred).
6. ``stage6`` - DRL-PPO allocator + deflated-Sharpe backtest (deferred).

Only Stage 1 is implemented here. Each later stage will consume the aligned
monthly feature matrix produced by ``stage1.pipeline``.
"""

from __future__ import annotations

__all__ = ["stage1"]
