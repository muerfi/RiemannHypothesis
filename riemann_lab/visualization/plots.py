"""Data preparation helpers for zeta-zero visualizations."""

from __future__ import annotations

from dataclasses import dataclass

from riemann_lab.zeros.compute import compute_nontrivial_zeros
from riemann_lab.utils.precision import DEFAULT_PRECISION
from riemann_lab.utils.validation import require_positive_int


@dataclass(frozen=True)
class ZeroPlotData:
    """Coordinates for plotting non-trivial zeros against the critical line."""

    real_parts: tuple[float, ...]
    imaginary_parts: tuple[float, ...]
    critical_line: float = 0.5


def generate_zero_plot_data(count: int, precision: int = DEFAULT_PRECISION) -> ZeroPlotData:
    """Generate plotting coordinates for the first ``count`` zeros.

    The resulting coordinates are intended for visualization and teaching.
    Showing finitely many zeros on ``Re(s)=1/2`` is illustrative, not a proof
    that every non-trivial zero lies on the critical line.
    """

    zeros = compute_nontrivial_zeros(require_positive_int(count, "count"), precision=precision)
    return ZeroPlotData(
        real_parts=tuple(float(complex(z).real) for z in zeros),
        imaginary_parts=tuple(float(complex(z).imag) for z in zeros),
    )
