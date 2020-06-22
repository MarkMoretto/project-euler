
"""
Purpose: Project Euler exercises
Date created: 2020-06-21

Problen Number: 721
Name: High powers of irrational numbers
URL: https://projecteuler.net/problem=721

Contributor(s):
    Mark M.
"""

import numpy as np
from sympy.ntheory import totient


MOD = 999999937

def fworker(A):
    a_root = A**0.5
    ac = int(a_root + 1)
    return a_root + ac


t = fworker(1000)


def f(a, n):
    aa = fworker(a)
    return int(aa**n)

assert f(5, 2) == 27
assert f(5, 5) == 3935



def G(n):
    tot = 0
    for i in range(1, n + 1):
        tmp = f(i, i*i)
        tot = tot + (tmp % MOD)
    return tot

G(1000)
