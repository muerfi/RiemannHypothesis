"""Riemann Zeta Computational Observatory.

``riemann_lab`` is a reproducible computational laboratory for finite
experiments with the Riemann zeta function, prime-counting functions, and
statistics of known non-trivial zeros.  The package is educational and
experimental: numerical verification of finitely many zeros is not a proof of
the Riemann Hypothesis, and exploratory analogies or machine-learning
experiments should not be read as mathematical evidence.
"""

__version__ = "0.1.0"

__all__ = [
    "compare_prime_counting",
    "compute_nontrivial_zeros",
    "compute_zero_spacings",
    "count_primes",
    "evaluate_zeta",
    "evaluate_zeta_on_critical_line",
    "generate_zero_plot_data",
    "logarithmic_integral_approximation",
    "verify_zeros_on_critical_line",
]

_LAZY_EXPORTS = {
    "compare_prime_counting": "riemann_lab.primes.approximations",
    "compute_nontrivial_zeros": "riemann_lab.zeros.compute",
    "compute_zero_spacings": "riemann_lab.zeros.spacing",
    "count_primes": "riemann_lab.primes.counting",
    "evaluate_zeta": "riemann_lab.zeta.evaluation",
    "evaluate_zeta_on_critical_line": "riemann_lab.zeta.critical_line",
    "generate_zero_plot_data": "riemann_lab.visualization.plots",
    "logarithmic_integral_approximation": "riemann_lab.primes.approximations",
    "verify_zeros_on_critical_line": "riemann_lab.zeros.verify",
}


def __getattr__(name: str):
    """Lazily import public helpers so optional dependencies load only when used."""

    if name not in _LAZY_EXPORTS:
        raise AttributeError(f"module 'riemann_lab' has no attribute {name!r}")
    from importlib import import_module

    module = import_module(_LAZY_EXPORTS[name])
    value = getattr(module, name)
    globals()[name] = value
    return value
