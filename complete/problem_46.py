
"""
Purpose: Project euler problem
Date created: 2021-04-03

Problen Number: 46
Name: Goldbach's other conjecture
URL: https://projecteuler.net/problem=46

Contributor(s):
    Mark M.
"""

try:
    from functools import cache
except ImportError:
    from functools import lru_cache as cache

from pathlib import Path
toplevel_folder = Path().absolute().parent


def get_primes_to_100k(file_subpath: str) -> set:
    datapath = toplevel_folder.joinpath(file_subpath)

    with datapath.open(mode="r") as f:
        data = f.read()

    return tuple(sorted(map(int, data.strip().split("\n"))))




def isqrt(n: int) -> int:
    return int(n ** 0.5)



def is_even(n: int) -> bool:
    """Return True if integer is even, False otherwise."""
    return not n & 1

def is_odd(n: int) -> bool:
    """Return False if integer is even, True otherwise."""
    return not is_even(n)


known_primes: tuple = get_primes_to_100k("primes-to-100k.txt")



@cache(maxsize=10000)
def is_prime(n: int) -> bool:

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



def test_is_prime(max_n: int = 5):
    for i in range(-1, max_n + 1):
        print(i, " -> ", is_prime(i))


def is_composite(n: int) -> bool:
    """Determine if integer number is composite value."""
    return not is_prime(n)

def is_odd_composite(n: int) -> bool:
    """Return True if integer number is a composite
    and is odd.
    """
    return is_composite(n) and is_odd(n)


@cache(maxsize=1000)
def twice_square(n: int):
    return 2 * n ** 2


if __name__ == "__main__":
    ddict = {}
    x = 2
    running = True
    while running:

        if is_odd_composite(x):
            match_found = False
            for p in range(2, x):
                if is_prime(p):
                    for e in range(1, isqrt(x)):
                        if p + twice_square(e) == x:
                            match_found = True
                            break
                    if match_found:
                        break
            # Set running to whatever match_found current is.
            # Should break if no match found.
            ddict[x] = match_found
            running = match_found
    
        x += 1

    res = [k for k, v in ddict.items() if v == False][0]
    print(f"Goldbach's other conjecture fails for composite number: {res}")

