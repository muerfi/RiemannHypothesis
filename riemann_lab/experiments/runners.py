"""Small orchestrators for reproducible finite experiments."""

from __future__ import annotations

from dataclasses import dataclass

from riemann_lab.primes.approximations import PrimeCountingComparison, compare_prime_counting
from riemann_lab.zeros.spacing import ZeroSpacingResult, compute_zero_spacings


@dataclass(frozen=True)
class BasicExperimentResult:
    """Container for a compact, finite numerical experiment."""

    prime_counting: PrimeCountingComparison
    zero_spacings: ZeroSpacingResult


def run_basic_experiment(*, prime_limit: int = 10_000, zero_count: int = 100) -> BasicExperimentResult:
    """Run a small reproducible experiment combining primes and zero spacings."""

    return BasicExperimentResult(
        prime_counting=compare_prime_counting(prime_limit),
        zero_spacings=compute_zero_spacings(count=zero_count),
    )
