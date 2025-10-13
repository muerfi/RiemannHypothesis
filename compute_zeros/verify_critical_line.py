"""Utility for validating numerically computed zeros of the Riemann zeta function.

The original script was written as top-level procedural code, which made it
hard to test and reuse.  This refactor turns the logic into small functions,
adds helpful error messages, and exposes a tiny command line interface so the
behaviour can be adjusted without editing the file by hand.  The improvements
make the script safer to run in automated pipelines and easier to maintain.
"""

from __future__ import annotations

from dataclasses import dataclass
import argparse
import re
from pathlib import Path
from typing import Iterable, List, Sequence


BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / "results"
DATA_DIR = BASE_DIR / "data"


@dataclass(frozen=True)
class ZeroComparison:
    """Holds a pair of zeros and their absolute difference."""

    index: int
    computed: complex
    known: complex
    difference: float


ZERO_PATTERN = re.compile(r"s = (.+?) \+ (.+?)j")


def parse_zeros(lines: Iterable[str]) -> List[complex]:
    """Parse zeros from an iterable of lines.

    Parameters
    ----------
    lines:
        The lines containing zero representations of the form
        ``s = 0.5 + 14.1347j``.  Leading header lines are ignored.

    Returns
    -------
    list of complex
        Complex numbers parsed from the input.
    """

    zeros: List[complex] = []
    for line in lines:
        match = ZERO_PATTERN.search(line)
        if not match:
            continue
        real_part = float(match.group(1))
        imag_part = float(match.group(2))
        zeros.append(complex(real_part, imag_part))
    return zeros


def load_zeros(file_path: Path) -> List[complex]:
    """Load zeros from ``file_path``.

    Raises a clear ``FileNotFoundError`` with context if the file is missing so
    that misconfigured runs fail fast.
    """

    if not file_path.exists():
        raise FileNotFoundError(f"Zero data file not found: {file_path}")

    with file_path.open("r", encoding="utf8") as handle:
        # Skip header if present by slicing from the second line onward.
        lines = handle.readlines()
    return parse_zeros(lines[1:]) if lines else []


def verify_critical_line(zeros: Iterable[complex], tolerance: float) -> bool:
    """Return ``True`` when all zeros lie on the critical line within tolerance."""

    expected_real = 0.5
    all_on_line = True
    for zero in zeros:
        if abs(zero.real - expected_real) <= tolerance:
            continue
        print(
            "Zero %s is off the critical line! Real part: %.12f"
            % (zero, zero.real)
        )
        all_on_line = False
    return all_on_line


def compare_with_known(
    computed: Sequence[complex],
    known: Sequence[complex],
    *,
    limit: int,
) -> List[ZeroComparison]:
    """Compare two sequences of zeros and return structured differences."""

    comparisons: List[ZeroComparison] = []
    for index, (comp, known_zero) in enumerate(zip(computed[:limit], known), start=1):
        diff = abs(comp - known_zero)
        comparisons.append(ZeroComparison(index=index, computed=comp, known=known_zero, difference=diff))
    return comparisons


def run_validation(tolerance: float, comparison_limit: int) -> None:
    """Validate computed zeros against the critical line and known values."""

    try:
        computed_zeros = load_zeros(RESULTS_DIR / "zeros_found.txt")
    except FileNotFoundError as exc:
        print(exc)
        return

    try:
        known_zeros = load_zeros(DATA_DIR / "known_zeros.txt")
    except FileNotFoundError as exc:
        print(exc)
        return

    if not computed_zeros:
        print("No computed zeros were found in the results file.")
        return

    on_line = verify_critical_line(computed_zeros, tolerance)
    if on_line:
        print("All computed zeros lie on the critical line (Re(s) = 1/2) within tolerance.")
    else:
        print("Some zeros do not lie on the critical line!")

    print("\nComparing the first %d computed zeros with known zeros:" % comparison_limit)
    for comparison in compare_with_known(computed_zeros, known_zeros, limit=comparison_limit):
        print(
            "Zero {index}: Computed = {computed}, Known = {known}, Difference = {diff:.2e}".format(
                index=comparison.index,
                computed=comparison.computed,
                known=comparison.known,
                diff=comparison.difference,
            )
        )
        if comparison.difference > tolerance:
            print(f"Warning: Large discrepancy for zero {comparison.index}!")


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tolerance",
        type=float,
        default=1e-10,
        help="Allowed deviation from the critical line and known zeros.",
    )
    parser.add_argument(
        "--comparison-limit",
        type=int,
        default=10,
        help="How many zeros to compare with the reference data.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run_validation(tolerance=args.tolerance, comparison_limit=args.comparison_limit)


if __name__ == "__main__":
    main()
      
