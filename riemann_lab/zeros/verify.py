"""Finite verification helpers for computed zeta zeros."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable, Sequence

from riemann_lab.utils.precision import DEFAULT_PRECISION
from riemann_lab.utils.validation import require_positive_float, require_positive_int

ZERO_PATTERN = re.compile(
    r"s\s*=\s*\(?\s*([+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)\s*\+\s*([+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)j\s*\)?"
)


@dataclass(frozen=True)
class ZeroVerification:
    """Result for a finite critical-line check.

    ``verified`` means every supplied numerical zero has real part within the
    stated tolerance of ``1/2``.  It is not a proof of RH or a statement about
    zeros outside the supplied finite list.
    """

    count: int
    tolerance: float
    verified: bool
    max_real_part_error: float
    failures: tuple[complex, ...]


def parse_zeros(lines: Iterable[str]) -> list[complex]:
    """Parse lines containing values of the form ``s = 0.5 + 14.13j``."""

    zeros: list[complex] = []
    for line in lines:
        match = ZERO_PATTERN.search(line)
        if match:
            zeros.append(complex(float(match.group(1)), float(match.group(2))))
    return zeros


def load_zeros(path: str | Path) -> list[complex]:
    """Load zero approximations from a text file."""

    with Path(path).expanduser().open("r", encoding="utf8") as handle:
        return parse_zeros(handle)


def verify_zeros_on_critical_line(
    zeros: Sequence[complex] | None = None,
    *,
    count: int | None = None,
    tolerance: float = 1e-10,
    precision: int = DEFAULT_PRECISION,
) -> ZeroVerification:
    """Check that a finite list of numerical zeros has ``Re(s)≈1/2``.

    If ``zeros`` is omitted, the first ``count`` zeros are computed or, when
    mpmath is unavailable and ``count <= 10``, loaded from the bundled reference
    fixture.  This is a sanity check on numerical output only; finite
    verification is not a proof of RH.
    """

    from riemann_lab.zeros.compute import compute_nontrivial_zeros

    tol = require_positive_float(tolerance, "tolerance")
    if zeros is None:
        zeros = compute_nontrivial_zeros(require_positive_int(count or 1, "count"), precision=precision)
    values = [complex(z) for z in zeros]
    errors = [abs(z.real - 0.5) for z in values]
    failures = tuple(z for z, err in zip(values, errors) if err > tol)
    return ZeroVerification(
        count=len(values),
        tolerance=tol,
        verified=not failures,
        max_real_part_error=max(errors, default=0.0),
        failures=failures,
    )
