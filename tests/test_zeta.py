"""Tests for numerical zeta-function evaluation helpers."""

from __future__ import annotations

import math

import pytest

mpmath = pytest.importorskip("mpmath")

from riemann_lab.utils.precision import precision_context
from riemann_lab.zeta.critical_line import evaluate_zeta_on_critical_line
from riemann_lab.zeta.evaluation import evaluate_zeta


def test_evaluate_zeta_real_reference_values() -> None:
    """ζ(2) and ζ(0) match classical finite numerical reference values."""

    zeta_two = evaluate_zeta(2, precision=80)
    zeta_zero = evaluate_zeta(0, precision=80)

    assert float(mpmath.re(zeta_two)) == pytest.approx(math.pi**2 / 6, rel=0, abs=1e-15)
    assert abs(float(mpmath.im(zeta_two))) < 1e-70
    assert float(mpmath.re(zeta_zero)) == pytest.approx(-0.5, rel=0, abs=1e-70)
    assert abs(float(mpmath.im(zeta_zero))) < 1e-70


def test_evaluate_zeta_on_critical_line_matches_direct_evaluation() -> None:
    """The critical-line helper evaluates ζ(1/2 + it), not a different point."""

    with precision_context(90):
        height = mpmath.nstr(mpmath.im(mpmath.zetazero(1)), 80)
        direct_point = mpmath.mpc("0.5", height)

    via_helper = evaluate_zeta_on_critical_line(height, precision=80)
    direct = evaluate_zeta(direct_point, precision=80)

    assert abs(via_helper - direct) < mpmath.mpf("1e-70")
    assert abs(via_helper) < mpmath.mpf("1e-60")
