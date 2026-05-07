"""Precision helpers for numerical experiments.

The package uses :mod:`mpmath` for high-precision complex arithmetic when it is
installed.  Public functions accept explicit decimal precision so that results
are reproducible and callers do not accidentally depend on a process-wide
default.
"""

from __future__ import annotations

from contextlib import contextmanager, nullcontext
from importlib import import_module, util
from typing import Iterator

DEFAULT_PRECISION = 50


def validate_precision(precision: int | None) -> int:
    """Return a validated decimal precision for mpmath computations."""

    resolved = DEFAULT_PRECISION if precision is None else int(precision)
    if resolved < 2:
        raise ValueError("precision must be at least 2 decimal digits")
    return resolved


def mpmath_available() -> bool:
    """Return ``True`` when :mod:`mpmath` can be imported in this environment."""

    return util.find_spec("mpmath") is not None


@contextmanager
def precision_context(precision: int | None = None) -> Iterator[None]:
    """Temporarily set mpmath decimal precision when mpmath is available."""

    if not mpmath_available():
        with nullcontext():
            yield
        return
    mpmath = import_module("mpmath")
    with mpmath.workdps(validate_precision(precision)):
        yield


def current_precision() -> int | None:
    """Return current mpmath decimal precision, or ``None`` if unavailable."""

    if not mpmath_available():
        return None
    return int(import_module("mpmath").mp.dps)
