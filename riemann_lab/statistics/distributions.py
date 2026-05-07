"""Small statistical helpers for finite experimental samples."""

from __future__ import annotations

import numpy as np


def empirical_histogram(values, bins: int = 30, density: bool = True) -> tuple[np.ndarray, np.ndarray]:
    """Return histogram counts and bin edges for finite numerical data."""

    return np.histogram(np.asarray(values, dtype=float), bins=bins, density=density)
