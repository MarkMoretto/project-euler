
"""
Purpose: Validate various numerical values
Date created: 2021-04-03

Contributor(s):
    Mark M.
"""

__all__ = [
        "isqrt",
        "is_prime",
        "is_composite",
        "totienter",
        ]

from math import gcd

try:
    from functools import cache
except ImportError:
    from functools import lru_cache as cache

from pathlib import Path

toplevel_folder = Path().absolute().parent


def isqrt(n: int) -> int:
    """Quick square root function which returns an integer value."""
    return int(n ** 0.5)


def is_even(n: int) -> bool:
    """Return True if integer is even, False otherwise."""
    return not n & 1


def is_odd(n: int) -> bool:
    """Return False if integer is even, True otherwise."""
    return not is_even(n)


def is_prime(n: int) -> bool:
    """Check if number is prime."""
    if n < 2:
        return False

    if n == 2:
        return True

    if is_even(n):
        return False

    rng = range(3, isqrt(n) + 1, 2)
    for i in rng:
        if n % i == 0:
            return False
    return True


# Assumes there's a list of known primes already.
def get_primes_to_100k(path_to_data: Path) -> set:
    with path_to_data.open(mode="r") as f:
        data = f.read()

    return tuple(sorted(map(int, data.strip().split("\n"))))

known_primes: tuple = get_primes_to_100k(toplevel_folder.joinpath("primes-to-100k.txt"))


@cache(maxsize=1000)
def is_prime_2(n: int) -> bool:

    n = abs(int(n))

    if n < 2:
        return False

    if n == 2:
        return True

    if is_even(n):
        return False

    if n in known_primes:
        return True

    rng = range(3, isqrt(n) + 1, 2)
    for i in rng:
        if n % i == 0:
            return False
    return True


def is_composite(n: int) -> bool:
    """Determine if integer number is composite value."""
    if abs(n) > 1:
        return not is_prime(n)
    return False




def totienter(n):
    """Generate all relatively prime values to n"""
    trng = range(1, n + 1)
    for k in trng:
        if gcd(n, k) == 1:
            yield k
        # k +=1

assert (list(totienter(10)) == [1, 3, 7, 9]), "totient generator error."
