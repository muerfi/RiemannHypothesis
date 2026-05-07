"""Command-line interface for finite Riemann zeta laboratory experiments."""

from __future__ import annotations

import argparse
from collections.abc import Callable

DEFAULT_PRECISION = 50


def _add_count_precision(parser: argparse.ArgumentParser, *, default_count: int) -> None:
    parser.add_argument("--count", type=int, default=default_count, help="Number of finite objects to compute.")
    parser.add_argument("--precision", type=int, default=DEFAULT_PRECISION, help="mpmath decimal digits.")


def cmd_zeros(args: argparse.Namespace) -> int:
    """Compute and display a finite list of non-trivial zeros."""

    from riemann_lab.zeros.compute import compute_nontrivial_zeros, format_zero, write_zeros

    zeros = compute_nontrivial_zeros(args.count, precision=args.precision)
    if args.output:
        output = write_zeros(zeros, args.output, digits=args.precision)
        print(f"Wrote {len(zeros)} finite zero approximations to {output}")
    print("Finite numerical approximations to non-trivial zeros (not a proof of RH):")
    for index, zero in enumerate(zeros, start=1):
        print(format_zero(index, zero, digits=min(args.precision, 50)))
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    """Verify that a finite computed list lies numerically on Re(s)=1/2."""

    from riemann_lab.zeros.verify import verify_zeros_on_critical_line

    result = verify_zeros_on_critical_line(count=args.count, tolerance=args.tolerance, precision=args.precision)
    status = "PASS" if result.verified else "FAIL"
    print(f"{status}: checked {result.count} finite zero approximations")
    print(f"Tolerance: {result.tolerance:g}")
    print(f"Maximum |Re(s)-1/2|: {result.max_real_part_error:.3e}")
    print("Finite numerical verification is not a proof of the Riemann Hypothesis.")
    if result.failures:
        print("Failures:")
        for failure in result.failures:
            print(f"  {failure}")
        return 1
    return 0


def cmd_primes(args: argparse.Namespace) -> int:
    """Compute exact prime counts and a classical smooth approximation."""

    from riemann_lab.primes.approximations import compare_prime_counting

    comparison = compare_prime_counting(args.limit, precision=args.precision)
    print(f"π({comparison.limit}) = {comparison.exact}")
    print(f"Li({comparison.limit}) ≈ {comparison.li_approximation:.6f}")
    print(f"Absolute error: {comparison.absolute_error:.6f}")
    print(f"Relative error: {comparison.relative_error:.6g}")
    return 0


def cmd_spacing(args: argparse.Namespace) -> int:
    """Compute normalized spacings between consecutive zero ordinates."""

    from riemann_lab.zeros.compute import _number_to_string
    from riemann_lab.zeros.spacing import compute_zero_spacings

    result = compute_zero_spacings(count=args.count, precision=args.precision)
    print(f"Computed {len(result.spacings)} consecutive spacings from {len(result.heights)} zeros.")
    print(f"Mean spacing: {result.mean_spacing:.12g}")
    print("First normalized spacings:")
    for value in result.normalized_spacings[: args.show]:
        print(f"  {_number_to_string(value, 12)}")
    print("Random-matrix comparisons are analogies for finite statistics, not proofs.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the top-level argument parser."""

    parser = argparse.ArgumentParser(
        prog="riemann_lab",
        description="Riemann Zeta Computational Observatory: finite numerical experiments only.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    zeros_parser = subparsers.add_parser("zeros", help="Compute non-trivial zero approximations.")
    _add_count_precision(zeros_parser, default_count=20)
    zeros_parser.add_argument("--output", help="Optional path for writing zero approximations.")
    zeros_parser.set_defaults(func=cmd_zeros)

    verify_parser = subparsers.add_parser("verify", help="Check finite zero approximations against Re(s)=1/2.")
    _add_count_precision(verify_parser, default_count=20)
    verify_parser.add_argument("--tolerance", type=float, default=1e-10, help="Allowed |Re(s)-1/2| error.")
    verify_parser.set_defaults(func=cmd_verify)

    primes_parser = subparsers.add_parser("primes", help="Compute π(x) and Li(x) for a finite limit.")
    primes_parser.add_argument("--limit", type=int, default=10_000, help="Upper bound x for π(x).")
    primes_parser.add_argument("--precision", type=int, default=DEFAULT_PRECISION, help="mpmath decimal digits.")
    primes_parser.set_defaults(func=cmd_primes)

    spacing_parser = subparsers.add_parser("spacing", help="Compute zero-spacing statistics.")
    _add_count_precision(spacing_parser, default_count=100)
    spacing_parser.add_argument("--show", type=int, default=10, help="Number of normalized spacings to print.")
    spacing_parser.set_defaults(func=cmd_spacing)

    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the CLI and return a process status code."""

    parser = build_parser()
    args = parser.parse_args(argv)
    func: Callable[[argparse.Namespace], int] = args.func
    return func(args)


if __name__ == "__main__":
    raise SystemExit(main())
