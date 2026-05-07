"""Tests for finite zero computation, verification, and spacing helpers."""

from __future__ import annotations

import math

import pytest

from riemann_lab.zeros.compute import compute_nontrivial_zeros
from riemann_lab.zeros.spacing import compute_zero_spacings
from riemann_lab.zeros.verify import verify_zeros_on_critical_line


def test_compute_small_number_of_nontrivial_zeros() -> None:
    """A small finite request returns finite numerical points in standard order."""

    zeros = compute_nontrivial_zeros(count=3, precision=50)

    assert len(zeros) == 3
    values = [complex(z) for z in zeros]
    assert all(math.isfinite(z.real) and math.isfinite(z.imag) for z in values)
    assert all(z.imag > 0 for z in values)
    assert [z.imag for z in values] == sorted(z.imag for z in values)


def test_computed_zeros_are_numerically_close_to_critical_line() -> None:
    """The finite zero sanity check reports numerical closeness, not a proof."""

    zeros = compute_nontrivial_zeros(count=3, precision=60)
    result = verify_zeros_on_critical_line(zeros, tolerance=1e-12, precision=60)

    assert result.count == 3
    assert result.verified is True
    assert result.failures == ()
    assert result.max_real_part_error <= 1e-12


def test_verify_zeros_reports_failures_for_tolerance_violations() -> None:
    """Tolerance handling is explicit when supplied values miss Re(s)=1/2."""

    result = verify_zeros_on_critical_line([0.5 + 14j, 0.51 + 21j], tolerance=1e-3)

    assert result.count == 2
    assert result.verified is False
    assert result.max_real_part_error == pytest.approx(0.01)
    assert result.failures == (0.51 + 21j,)


def test_compute_zero_spacings_returns_count_minus_one_spacings() -> None:
    """Consecutive zero-spacing output has deterministic size and positive values."""

    result = compute_zero_spacings(count=5, precision=50)

    assert len(result.heights) == 5
    assert len(result.spacings) == 4
    assert len(result.normalized_spacings) == 4
    assert all(spacing > 0 for spacing in result.spacings)
    assert result.mean_spacing > 0
    assert sum(result.normalized_spacings) / len(result.normalized_spacings) == pytest.approx(1.0)


def test_compute_zero_spacings_from_supplied_zeros_is_sorted() -> None:
    """Supplied finite zeros are sorted by height before spacing computation."""

    result = compute_zero_spacings([0.5 + 30j, 0.5 + 10j, 0.5 + 20j])

    assert result.heights == (10.0, 20.0, 30.0)
    assert result.spacings == (10.0, 10.0)
    assert result.mean_spacing == 10.0
    assert result.normalized_spacings == (1.0, 1.0)
