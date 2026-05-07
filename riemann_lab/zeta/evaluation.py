"""Numerical evaluation of the Riemann zeta function."""

from __future__ import annotations

from mpmath import mpc, zeta

from riemann_lab.utils.precision import DEFAULT_PRECISION, precision_context


def evaluate_zeta(s: complex | float | int | str, precision: int = DEFAULT_PRECISION) -> mpc:
    """Evaluate the Riemann zeta function ``ζ(s)`` at a complex point.

    This is a numerical evaluation using :func:`mpmath.zeta`.  It is useful for
    experimentation and visualization, but it does not by itself establish any
    theorem about the zero set of ``ζ``.

    Parameters
    ----------
    s:
        Complex input value.  Strings accepted by :class:`mpmath.mpc` may be
        used for reproducible high-precision inputs.
    precision:
        Decimal digits used by mpmath during this finite computation.
    """

    with precision_context(precision):
        return zeta(mpc(s))
