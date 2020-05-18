
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

import cython
import numpy as np
from math import gcd
import itertools as ittr
from sympy.ntheory import totient


cdef:
    int MOD = np.uint32(1e9+7)
    long[:] f_num_rng, k_rng, sq
    unsigned long f_tot
    double g_tot

cdef double f(long n):
    
    f_tot = 0
    
    f_num_rng = np.arange(0, n)
        
    for i in ittr.product(f_num_rng, repeat=6):  
        sq = np.square(np.array(i))
        if np.gcd(sq.sum(), np.power(n, 2)) == 1:
            f_tot += 1
    return f_tot


cdef double g_worker(long k_val):
    cdef double numerator, denominator
    numerator = f(k_val)
    denominator = np.power(k_val, 2) * totient(k_val)
    return numerator / denominator


cdef double G(long gn):
    g_tot = 0.
    k_rng = np.arange(1, gn + 1)
    
    for k in k_rng:
        g_tot += (g_worker(k) % MOD)

    return g_tot



cdef long N = np.uint32(1e5)
cdef g_res

g_res = G(N)

print(g_res)