"""Prime-counting functions."""

from __future__ import annotations

from riemann_lab.utils.validation import require_nonnegative_int


def primes_up_to(limit: int) -> list[int]:
    """Return all primes ``p <= limit`` using the Sieve of Eratosthenes."""

    n = require_nonnegative_int(limit, "limit")
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    p = 2
    while p * p <= n:
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
        p += 1
    return [idx for idx, is_prime in enumerate(sieve) if is_prime]


def count_primes(limit: int) -> int:
    """Return ``π(limit)``, the number of primes at most ``limit``.

    This exact finite count is a basic observable in computational number
    theory and provides a reference for approximate prime-counting formulas.
    """

    return len(primes_up_to(limit))
