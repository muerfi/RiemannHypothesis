"""Shared input validation helpers."""

from __future__ import annotations


def require_positive_int(value: int, name: str) -> int:
    """Validate that ``value`` is a positive integer."""

    resolved = int(value)
    if resolved < 1:
        raise ValueError(f"{name} must be a positive integer")
    return resolved


def require_nonnegative_int(value: int, name: str) -> int:
    """Validate that ``value`` is a non-negative integer."""

    resolved = int(value)
    if resolved < 0:
        raise ValueError(f"{name} must be a non-negative integer")
    return resolved


def require_positive_float(value: float, name: str) -> float:
    """Validate that ``value`` is a positive floating-point number."""

    resolved = float(value)
    if resolved <= 0:
        raise ValueError(f"{name} must be positive")
    return resolved
