
"""
Purpose: Compiled problem 708
Date created: 2020-04-02

Contributor(s):
    Mark M.
"""


from functools import reduce

import numpy as np
import bottleneck as bn




def sqrt_(n):
    return n ** (1/2)

def step_(x):
    return 1 + (x<<2) - ((x>>1)<<1)

def maxq_(q):
    return int(np.floor(np.sqrt(q)))


def prime_factors(n):
    cdef int maxq, d, q
    maxq = maxq_(n)
    d = 1
    q = 2 if n % 2 == 0 else 3 
    while q <= maxq and n % q != 0:
        q = step_(d)
        d += 1
    res = [q] + prime_factors(n // q) if q <= maxq else [n]
    return [2 for _ in res]



def f(n):
    cdef int result
    result = 1
    if n > 1:
        result = reduce(np.multiply, prime_factors(n))
    return result


def S(N):
    cdef int i, tot_, incr_
    N = int(N)
    i = 0
    tot_ = 0
    incr_ = 1

    while i <= N:
        tot_ += f(i)
        i += incr_
    return tot_
