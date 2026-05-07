"""Tests for exact and approximate finite prime-counting utilities."""

from __future__ import annotations

import pytest

from riemann_lab.primes.approximations import compare_prime_counting, logarithmic_integral_approximation
from riemann_lab.primes.counting import count_primes, primes_up_to


def test_count_primes_small_reference_values() -> None:
    """Exact finite prime counts match standard small values."""

    assert primes_up_to(1) == []
    assert count_primes(10) == 4
    assert count_primes(100) == 25


def test_logarithmic_integral_approximation_is_finite_and_reasonable() -> None:
    """Li(x) approximation is finite and in the expected range for a small cutoff."""

    approximation = logarithmic_integral_approximation(100, precision=60)

    assert 30.12 < approximation < 30.13
    assert approximation > count_primes(100)


def test_compare_prime_counting_reports_consistent_errors() -> None:
    """Comparison object consistently derives absolute and relative errors."""

    comparison = compare_prime_counting(100, precision=60)

    assert comparison.limit == 100
    assert comparison.exact == 25
    assert comparison.li_approximation == pytest.approx(logarithmic_integral_approximation(100, precision=60))
    assert comparison.absolute_error == pytest.approx(abs(comparison.li_approximation - comparison.exact))
    assert comparison.relative_error == pytest.approx(comparison.absolute_error / comparison.exact)


def test_prime_counting_rejects_invalid_limits() -> None:
    """Negative finite cutoffs are rejected instead of silently coerced."""

    with pytest.raises(ValueError, match="limit must be a non-negative integer"):
        count_primes(-1)
