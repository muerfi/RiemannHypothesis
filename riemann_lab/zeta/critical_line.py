"""Utilities for evaluating zeta on the critical line ``Re(s)=1/2``."""

from __future__ import annotations

from mpmath import mpc

from riemann_lab.utils.precision import DEFAULT_PRECISION
from riemann_lab.zeta.evaluation import evaluate_zeta


def evaluate_zeta_on_critical_line(t: float | str, precision: int = DEFAULT_PRECISION) -> mpc:
    """Evaluate ``ζ(1/2 + it)`` for a real height ``t``.

    The critical line is central to the Riemann Hypothesis.  This function only
    performs a pointwise numerical evaluation at a requested height; it does not
    verify any interval and does not constitute evidence for a proof.
    """

    return evaluate_zeta(mpc("0.5", t), precision=precision)
