"""Random-matrix comparison curves for zero-spacing analogies.

These functions provide reference curves often used in discussions of zeta-zero
spacing statistics.  They are analogies/comparisons for finite samples, not
proofs of the Riemann Hypothesis.
"""

from __future__ import annotations

import numpy as np


def wigner_surmise_gue(spacings) -> np.ndarray:
    """Return the GUE Wigner-surmise density ``p(s) = 32 s² exp(-4s²/π)/π²``."""

    s = np.asarray(spacings, dtype=float)
    return (32 / np.pi**2) * s**2 * np.exp((-4 / np.pi) * s**2)


def poisson_spacing_density(spacings) -> np.ndarray:
    """Return the Poisson nearest-neighbor spacing density ``exp(-s)``."""

    s = np.asarray(spacings, dtype=float)
    return np.exp(-s)
