"""Internal rate of return for a short annual cash-flow stream.

Bisection on net present value: dependency-free, deterministic, and easy to
audit. The solver distinguishes WHY a rate could not be returned so callers can
fail closed instead of treating a bound-saturated or non-finite result as a
precise expected return (see P0-1):

- ``valid``              a sign change exists inside the band; rate is precise.
- ``no_root``            no sign change found inside the band (non-monotonic).
- ``below_lower_bound``  NPV is negative even at LOWER_BOUND -> IRR < -95%.
- ``above_upper_bound``  NPV is positive even at UPPER_BOUND -> IRR > 200%
                         (per the cap comment: a data artifact, not a return).
- ``non_finite_input``   a cash flow or intermediate NPV is NaN/Infinity.
- ``degenerate_input``   fewer than two flows, or no negative entry outlay.

``solve_irr`` keeps the old ``float | None`` contract (rate only when valid).
"""

from __future__ import annotations

import math
from collections.abc import Sequence
from typing import Literal, NamedTuple

LOWER_BOUND = -0.95
# 200%/yr caps the solver: anything beyond that is a data artifact (broken
# share counts, giant negative net debt), not an investable expected return.
UPPER_BOUND = 2.0

IrrStatus = Literal[
    "valid",
    "no_root",
    "below_lower_bound",
    "above_upper_bound",
    "non_finite_input",
    "degenerate_input",
]


class IrrSolution(NamedTuple):
    rate: float | None
    status: IrrStatus


def net_present_value(rate: float, cashflows: Sequence[float]) -> float:
    return sum(cf / (1.0 + rate) ** t for t, cf in enumerate(cashflows))


def solve_irr_detailed(
    cashflows: Sequence[float],
    *,
    tolerance: float = 1e-7,
    max_iterations: int = 200,
) -> IrrSolution:
    if any(not math.isfinite(cf) for cf in cashflows):
        return IrrSolution(None, "non_finite_input")
    if len(cashflows) < 2 or cashflows[0] >= 0:
        return IrrSolution(None, "degenerate_input")

    low, high = LOWER_BOUND, UPPER_BOUND
    npv_low = net_present_value(low, cashflows)
    npv_high = net_present_value(high, cashflows)
    if not (math.isfinite(npv_low) and math.isfinite(npv_high)):
        return IrrSolution(None, "non_finite_input")
    # NPV decreases in the discount rate: npv_low is the high end of NPV.
    if npv_low < 0 and npv_high < 0:
        return IrrSolution(None, "below_lower_bound")  # root sits below -95%
    if npv_low > 0 and npv_high > 0:
        return IrrSolution(None, "above_upper_bound")  # root sits above 200%

    for _ in range(max_iterations):
        mid = (low + high) / 2.0
        npv_mid = net_present_value(mid, cashflows)
        if not math.isfinite(npv_mid):
            return IrrSolution(None, "non_finite_input")
        if abs(npv_mid) < tolerance:
            return IrrSolution(mid, "valid")
        if (npv_mid > 0) == (npv_low > 0):
            low, npv_low = mid, npv_mid
        else:
            high = mid
    return IrrSolution((low + high) / 2.0, "valid")


def solve_irr(
    cashflows: Sequence[float],
    *,
    tolerance: float = 1e-7,
    max_iterations: int = 200,
) -> float | None:
    """Backwards-compatible wrapper: returns a rate only when it is precise."""

    solution = solve_irr_detailed(
        cashflows, tolerance=tolerance, max_iterations=max_iterations
    )
    return solution.rate if solution.status == "valid" else None
