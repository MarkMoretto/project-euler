
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
# from sympy.ntheory import totient


MOD = 999999937
# pow(10, 100, MOD)


def fexp(base, exp, m=MOD):
    res = 1
    if 1 & exp:
        res = base
    while exp:
        exp >>= 1
        base = (base * base) % m
        if exp & 1:
            res = (res * base) % m
    return res






def f(a, n):
    a_root = (a**0.5)
    a_ceil = int(a_root + 1)
    w = (a_ceil + a_root)
    tmp = fexp(w, n)
    return int(tmp)

assert f(5, 2) == 27
assert f(5, 5) == 3935



def G(n):
    tot = 0
    for i in range(1, n):
        tmp = f(i, i*i)
        tot += tmp
    return tot

res = G(1000)
print(res % MOD)

actual = 602145087
expected=163861845





# def prime_factor_gen(n):
#     i = 2
#     while pow(i, 2) <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#             yield i
#     if n > 1:
#         yield n

# def pfactors(n):
#     return [i for i in prime_factor_gen(n)]













