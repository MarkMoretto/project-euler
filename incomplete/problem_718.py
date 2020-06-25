
"""
Purpose: Project Euler exercises
Date created: 2020-06-24

Problen Number: 721
Name: High powers of irrational numbers
URL: https://projecteuler.net/problem=721

Contributor(s):
    Mark M.

Description:
    Consider the equation 17pa+19pb+23pc=n where a, b, c and p are positive
    integers, i.e. a,b,c,p>0.
    
    For a given p
    there are some values of n > 0 for which the equation cannot be solved. We call
    these unreachable values.
    
    Define G(p) to be the sum of all unreachable values of n for the given value of p.
    For example:
        G(1) = 8253; and
        G(2) = 60258000.
    
    Find G(6). Give your answer modulo 1000000007.    
"""

import numpy as np

MOD = 1000000007 # int(1e9)+7





def set_dict(*args):
    dict(a=(aa * A), b=(bb * B), c=(cc * C),)



p = 1
max_n = 2**63-1

# zmatrix = np.zeros((max_n, max_n, max_n), dtype=np.uint64)

A = (17**p)
B = (19**p)
C = (23**p)

unreachable = []

aa, bb, cc = 1, 1, 1
dd = dict(
        a=(aa*A),
        b=(bb*B),
        c=(cc*C),
        )

# Seed initial n with minimum value possible
n = sum(dd.values())


while True:

    aa, bb, cc = 1, 1, 1

    n += 1

    dd = dict(
            a=(aa*A),
            b=(bb*B),
            c=(cc*C),
            )

    while sum(dd.values()) > n:
        unreachable.append(n)
        n += 1

    for a in range(1, max_n):
        worker['a'] =
        for b in range(1, max_n):
            for c in range(1, max_n):
                if ((a*A)+(b*B)+(c*C)) != n:
                    unreachable.append(n)




































# def fexp(base, exp, m=MOD):
#     res = 1
#     if 1 & exp:
#         res = base
#     while exp:
#         exp >>= 1
#         base = (base * base) % m
#         if exp & 1:
#             res = (res * base) % m
#     return res












