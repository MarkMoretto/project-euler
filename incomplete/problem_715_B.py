
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

import cupy as cp
import numpy as np
import itertools as ittr
import numba
from math import gcd

MOD = cp.uint32(1e9+7)


import numpy as np
from math import gcd
import itertools as ittr
from sympy.ntheory import totient

MOD = np.uint32(1e9+7)





n = 3
tot = 0
num_rng = np.arange(0, n)
    
for i in ittr.product(num_rng, repeat=6):  
    sq = np.square(np.array(i))
    # print(i, sq)
    if np.gcd(sq.sum(), np.power(n, 2)) == 1:
        tot += 1










# y = cp.zeros((6,1))
# z = y[:]

@numba.jit
def sq_product(n):

    for x in numba.prange(0, n):
        for prod in ittr.product(num_range, repeat=6):
            return cp.square(cp.array(i, dtype=cp.uint32))



@numba.njit(parallel = True)
def totient(n):
    tot = 0
    for k in numba.prange(1, n + 1):
        if gcd(n, k) == 1:
            tot += 1
    return tot




@numba.jit
def f(n):
    tot = 0
    num_range = np.arange(0, n, dtype=cp.uint32)
    for p in ittr.product(num_range, repeat=6):
        k = cp.square(cp.array(p, dtype=cp.uint32))
        nn = cp.power(p, 2)
        if gcd(k.sum(), nn) == 1:
            tot += 1
    return tot


@numba.njit
def g_worker(k_val):
    return f(k_val) / (cp.power(k_val, 2) * totient(k_val))


@numba.njit
def G(n):
    tot = 0
    tmp =
    for k in numba.prange(1, n + 1):
        tot += (g_worker(k) % MOD)
    return tot



if __name__ == '__main__':
    N = int(10)
    res = G(N)
    print(res)