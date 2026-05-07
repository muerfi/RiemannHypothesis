"""Tests for precision validation and command-line smoke behavior."""

from __future__ import annotations

import subprocess
import sys

import pytest

from riemann_lab.utils.precision import current_precision, precision_context, validate_precision


def test_precision_context_restores_global_mpmath_precision() -> None:
    """Temporary precision changes do not leak into later computations."""

    pytest.importorskip("mpmath")
    before = current_precision()
    with precision_context(80):
        assert current_precision() == 80
    assert current_precision() == before


@pytest.mark.parametrize("precision", [0, 1])
def test_validate_precision_rejects_too_small_values(precision: int) -> None:
    """Precision validation fails clearly for unsupported decimal digits."""

    with pytest.raises(ValueError, match="precision must be at least 2"):
        validate_precision(precision)


@pytest.mark.parametrize(
    "args, expected_text",
    [
        (["zeros", "--count", "3", "--precision", "50"], "Finite numerical approximations"),
        (["verify", "--count", "3", "--tolerance", "1e-10"], "not a proof"),
        (["primes", "--limit", "100"], "π(100) = 25"),
        (["spacing", "--count", "4", "--precision", "50"], "Computed 3 consecutive spacings"),
    ],
)
def test_cli_smoke_commands_run_for_small_inputs(args: list[str], expected_text: str) -> None:
    """Small CLI experiments complete and keep finite-experiment language visible."""

    completed = subprocess.run(
        [sys.executable, "-m", "riemann_lab", *args],
        check=True,
        text=True,
        capture_output=True,
    )

    assert expected_text in completed.stdout
    assert completed.stderr == ""
