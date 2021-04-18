
"""
Purpose: Project euler problem
Date created: 2021-04-04

Status: Incomplete

Problen Number: 754
Name: Product of Gauss Factorials
URL: https://projecteuler.net/problem=754

Contributor(s):
    Mark M.
"""

import argparse
from math import gcd
from functools import reduce
import concurrent.futures as ccf

try:
    from functools import cache
except ImportError:
    from functools import lru_cache as cache


MOD: int = 1000000007


parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", type = int,
                    choices=[1, 8],
                    help="Exponent value for 10 ^ n. \
                    This is the limit for the main function.")


def totienter(n):
    """Generate all relatively prime values to n"""
    rng = range(1, n + 1)
    for k in rng:
        if gcd(n, k) == 1:
            yield k


@cache(maxsize=1000)
def g(n):
    return reduce(lambda a, b: a * b, totienter(n))


def G(n):
    tot = 1
    with ccf.ThreadPoolExecutor() as executor:
        the_futures = {executor.submit(g, i):i for i in range(1, n + 1)}
        for fut in ccf.as_completed(the_futures):
            data = fut.result()
            tot *= (data % MOD)
    print(f"The product of Gauss Factorials to {n} is: {tot}")


if __name__ == "__main__":
    args = parser.parse_args()

    multiplier: int = None

    if args.number:
        multiplier = args.number
    else:
        multiplier = 8
    G(10**multiplier)
