"""Spacing statistics for finite lists of non-trivial zeta zeros."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from riemann_lab.zeros.compute import compute_nontrivial_zeros
from riemann_lab.utils.precision import DEFAULT_PRECISION
from riemann_lab.utils.validation import require_positive_int


@dataclass(frozen=True)
class ZeroSpacingResult:
    """Consecutive imaginary-part spacings for a finite zero list."""

    heights: tuple[float, ...]
    spacings: tuple[float, ...]
    normalized_spacings: tuple[float, ...]
    mean_spacing: float


def compute_zero_spacings(
    zeros: Sequence[complex] | None = None,
    *,
    count: int | None = None,
    precision: int = DEFAULT_PRECISION,
) -> ZeroSpacingResult:
    """Compute consecutive spacings between zero ordinates.

    The normalized spacings have mean one when at least two zeros are present.
    Comparisons with random-matrix statistics are analogies about observed
    finite data, not a proof or independent evidence for RH.
    """

    if zeros is None:
        zeros = compute_nontrivial_zeros(require_positive_int(count or 2, "count"), precision=precision)
    heights = tuple(sorted(float(complex(z).imag) for z in zeros))
    spacings = tuple(b - a for a, b in zip(heights, heights[1:]))
    mean_spacing = sum(spacings) / len(spacings) if spacings else float("nan")
    normalized = tuple(s / mean_spacing for s in spacings) if spacings and mean_spacing else ()
    return ZeroSpacingResult(
        heights=heights,
        spacings=spacings,
        normalized_spacings=normalized,
        mean_spacing=mean_spacing,
    )
