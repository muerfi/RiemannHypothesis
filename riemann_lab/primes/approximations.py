"""Approximate prime-counting functions and comparisons."""

from __future__ import annotations

from dataclasses import dataclass
from importlib import import_module, util
import math

from riemann_lab.primes.counting import count_primes
from riemann_lab.utils.validation import require_nonnegative_int

DEFAULT_PRECISION = 50
LI_TWO = 1.0451637801174928


@dataclass(frozen=True)
class PrimeCountingComparison:
    """Exact and approximate values for ``π(x)`` at one finite cutoff."""

    limit: int
    exact: int
    li_approximation: float
    absolute_error: float
    relative_error: float


def _simpson_integral_from_two(limit: int) -> float:
    """Approximate ``∫_2^x dt/log(t)`` with composite Simpson quadrature."""

    if limit == 2:
        return 0.0
    intervals = max(200, min(20_000, int(limit // 2) * 2))
    if intervals % 2:
        intervals += 1
    a = 2.0
    b = float(limit)
    h = (b - a) / intervals
    total = 1.0 / math.log(a) + 1.0 / math.log(b)
    for i in range(1, intervals):
        t = a + i * h
        total += (4 if i % 2 else 2) / math.log(t)
    return total * h / 3


def logarithmic_integral_approximation(limit: int, precision: int = DEFAULT_PRECISION) -> float:
    """Approximate ``π(x)`` by the logarithmic integral ``Li(x)``.

    ``Li(x)`` is a classical smooth approximation to the prime-counting
    function.  When :mod:`mpmath` is installed, this function uses its
    high-precision implementation.  Otherwise it falls back to a deterministic
    quadrature suitable for small educational CLI examples.
    """

    n = require_nonnegative_int(limit, "limit")
    if n < 2:
        return 0.0
    if util.find_spec("mpmath") is not None:
        mpmath = import_module("mpmath")
        with mpmath.workdps(int(precision)):
            return float(mpmath.li(n))
    return LI_TWO + _simpson_integral_from_two(n)


def compare_prime_counting(limit: int, precision: int = DEFAULT_PRECISION) -> PrimeCountingComparison:
    """Compare exact ``π(x)`` with ``Li(x)`` for a finite cutoff."""

    exact = count_primes(limit)
    approx = logarithmic_integral_approximation(limit, precision=precision)
    abs_error = abs(exact - approx)
    rel_error = abs_error / exact if exact else 0.0
    return PrimeCountingComparison(
        limit=int(limit),
        exact=exact,
        li_approximation=approx,
        absolute_error=abs_error,
        relative_error=rel_error,
    )
