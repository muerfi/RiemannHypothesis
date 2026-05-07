"""Compute finite lists of non-trivial zeta zeros."""

from __future__ import annotations

from importlib import import_module
from pathlib import Path
from typing import Sequence

from riemann_lab.utils.paths import LEGACY_ZERO_DATA_PATH, resolve_output_path
from riemann_lab.utils.precision import DEFAULT_PRECISION, mpmath_available, precision_context
from riemann_lab.utils.validation import require_positive_int


def _load_reference_zeros() -> list[complex]:
    """Load the bundled first ten reference zeros for fallback demos."""

    from riemann_lab.zeros.verify import load_zeros

    if not LEGACY_ZERO_DATA_PATH.exists():
        return []
    return load_zeros(LEGACY_ZERO_DATA_PATH)


def compute_nontrivial_zeros(count: int, precision: int = DEFAULT_PRECISION) -> list[complex]:
    """Return the first ``count`` non-trivial zeros as numerical approximations.

    With :mod:`mpmath` installed, zeros are computed using ``mpmath.zetazero``
    in the standard ordering by positive imaginary part.  If mpmath is not
    available, the function can return the bundled first ten reference zeros for
    small educational demonstrations and raises a clear error for larger
    requests.  A finite list is a numerical experiment, not a proof of RH.
    """

    n = require_positive_int(count, "count")
    if mpmath_available():
        mpmath = import_module("mpmath")
        with precision_context(precision):
            return [mpmath.zetazero(k) for k in range(1, n + 1)]
    reference = _load_reference_zeros()
    if len(reference) >= n:
        return reference[:n]
    raise ModuleNotFoundError(
        "mpmath is required to compute zeros beyond the bundled reference fixture; "
        "install the package dependencies with `pip install -e .`."
    )


def _number_to_string(value: float, digits: int) -> str:
    """Format a real number using mpmath when available, else Python formatting."""

    if mpmath_available():
        mpmath = import_module("mpmath")
        return str(mpmath.nstr(value, digits))
    return f"{float(value):.{min(digits, 17)}g}"


def format_zero(index: int, zero: complex, digits: int = 30) -> str:
    """Format a zero for human-readable logs or data files."""

    z = complex(zero)
    return f"Zero {index}: s = {_number_to_string(z.real, digits)} + {_number_to_string(z.imag, digits)}j"


def write_zeros(zeros: Sequence[complex], path: str | Path | None = None, digits: int = 30) -> Path:
    """Write zeros to a text file under ``artifacts/`` unless a path is supplied."""

    output_path = resolve_output_path(path, "zeros", "zeros_found.txt")
    with output_path.open("w", encoding="utf8") as handle:
        handle.write(f"First {len(zeros)} non-trivial zeros of the Riemann zeta function.\n")
        handle.write("These are finite numerical approximations, not a proof of RH.\n")
        for index, zero in enumerate(zeros, start=1):
            handle.write(format_zero(index, zero, digits=digits) + "\n")
    return output_path
