
"""
Purpose: Code Wars - Magnet particules in boxes
Date created: 2020-09-27

https://www.codewars.com/kata/56c04261c3fcf33f2d000534

Contributor(s):
    Mark M.

Description:
"""

from functools import lru_cache


@lru_cache(maxsize=None)
def v(k, n):
    n += 1
    return 1 / (k * (n ** (2 * k)))



def g_(mk, mn):
    K = 1
    while K <= mk:
        N = 1
        while N <= mn:
            yield v(K, N)
            N += 1
        K += 1

# g = g_(1, 10)
# sum(list(g))


def doubles(maxk, maxn):
    g = g_(maxk, maxn)
    res = sum([i for i in g])
    return res


doubles(1, 3)
doubles(1, 10)
doubles(10, 100)
doubles(10, 10000)
