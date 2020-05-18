
"""
Purpose: Projec Euler exercises
Date created: 2020-05-14

Problen Number: 715
Name: Sextuplet Norms
URL: https://projecteuler.net/problem=715


Contributor(s):
    Mark M.

Description:

Let f(n) be the number of 6-tuples (x1,x2,x3,x4,x5,x6) such that:
    All xi are integers with 0≤xi<n
    gcd(x21+x22+x23+x24+x25+x26, n2)=1

Let G(n)=∑k=1nf(k)k2φ(k) where φ(n) is Euler's totient function.

For example,
G(10)=3053 and
G(105)≡157612967(mod1000000007).

Find G(1012)mod1000000007.
"""

import numpy as np
import itertools as ittr
from functools import partial

MOD = np.int32(1e9+7)


class memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        try:
            args.__hash__()
            if args in self.cache:
                return self.cache[args]
            else:
                value = self.func(*args)
                self.cache[args] = value
                return value
        except TypeError:
            return self.func(args)

    def __repr__(self):
        return self.func.__doc__

    def __get__(self, obj, objtype):
        return partial(self.__call__, obj)


def nproduct(num_range):
    cp = ittr.product(num_range, repeat=6)
    for i in cp:
        yield np.square(np.array(i, dtype=np.uint32))


@memoize
def totient(n):
    return sum(1 for k in np.arange(1, n + 1) if np.gcd(n, k) == 1)


def is_prime(n):
    return totient(n) == n - 1


@memoize
def f(n):
    cp = nproduct(np.arange(0, n))
    return sum(1 for k in cp if np.gcd(k.sum(), np.power(n, 2)) == 1)


def g_worker(k_val):
    return f(k_val) / (np.power(k_val, 2) * totient(k_val))


def G(n):
    tot = 0
    k_rng = np.arange(1, n + 1)
    for k in k_rng:
        tot += (g_worker(k) % MOD)
    return tot



if __name__ == '__main__':
    N = int(1e5)
    res = G(N)
    print(res)
