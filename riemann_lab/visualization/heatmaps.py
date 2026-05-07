"""Grid data helpers for zeta visualizations."""

from __future__ import annotations

import numpy as np
from mpmath import zeta

from riemann_lab.utils.precision import DEFAULT_PRECISION, precision_context


def zeta_magnitude_grid(
    sigma_min: float = 0.0,
    sigma_max: float = 1.0,
    t_min: float = 0.0,
    t_max: float = 50.0,
    sigma_points: int = 100,
    t_points: int = 200,
    precision: int = DEFAULT_PRECISION,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return ``σ``, ``t``, and ``|ζ(σ+it)|`` arrays for finite visualizations."""

    sigma_values = np.linspace(sigma_min, sigma_max, sigma_points)
    t_values = np.linspace(t_min, t_max, t_points)
    sigma_grid, t_grid = np.meshgrid(sigma_values, t_values)
    magnitude = np.empty_like(sigma_grid, dtype=float)
    with precision_context(precision):
        for i in range(t_points):
            for j in range(sigma_points):
                magnitude[i, j] = float(abs(zeta(complex(sigma_grid[i, j], t_grid[i, j]))))
    return sigma_grid, t_grid, magnitude
