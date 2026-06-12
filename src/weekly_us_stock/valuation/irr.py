"""Internal rate of return for a short annual cash-flow stream.

Bisection on net present value: dependency-free, deterministic, and easy to
audit. Returns None when no sign change exists in the searched band.
"""

from __future__ import annotations

from collections.abc import Sequence

LOWER_BOUND = -0.95
# 200%/yr caps the solver: anything beyond that is a data artifact (broken
# share counts, giant negative net debt), not an investable expected return.
UPPER_BOUND = 2.0


def net_present_value(rate: float, cashflows: Sequence[float]) -> float:
    return sum(cf / (1.0 + rate) ** t for t, cf in enumerate(cashflows))


def solve_irr(
    cashflows: Sequence[float],
    *,
    tolerance: float = 1e-7,
    max_iterations: int = 200,
) -> float | None:
    if len(cashflows) < 2 or cashflows[0] >= 0:
        return None

    low, high = LOWER_BOUND, UPPER_BOUND
    npv_low = net_present_value(low, cashflows)
    npv_high = net_present_value(high, cashflows)
    if npv_low < 0 and npv_high < 0:
        return None  # total payoff never recovers the entry price in-band
    if npv_low > 0 and npv_high > 0:
        return None

    for _ in range(max_iterations):
        mid = (low + high) / 2.0
        npv_mid = net_present_value(mid, cashflows)
        if abs(npv_mid) < tolerance:
            return mid
        if (npv_mid > 0) == (npv_low > 0):
            low, npv_low = mid, npv_mid
        else:
            high = mid
    return (low + high) / 2.0
