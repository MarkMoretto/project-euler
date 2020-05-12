
"""
Purpose: Projec Euler exercise
Date created: 2020-05-03

Problen Number: 714
Name: Duodigits
URL: https://projecteuler.net/problem=714


Contributor(s):
    Mark M.

Description:
    We call a natural number a duodigit if its decimal representation uses no more than
    two different digits. For example, 12, 110 and 33333 are duodigits, while 102 is not.
    It can be shown that every natural number has duodigit multiples. Let d(n) be the
    smallest (positive) multiple of the number n that happens to be a duodigit.
    For example:
        d(12) = 12,
        d(102) = 1122,
        d(103) = 515,
        d(290) = 11011010 and
        d(317) = 211122.
    
    Let D(k)=∑n=1k d(n). You are given:
        D(110) = 11047,
        D(150) = 53312 and
        D(500) = 29570988.
    
    Find D(50000).
    Give your answer in scientific notation rounded to 13 significant digits (12 after
    the decimal point). If, for example, we had asked for D(500) instead, the answer
    format would have been 2.957098800000e7.
"""

import numba
# import itertools as ittr
from decimal import getcontext

getcontext().prec = 12




def setlen(q):
    ns = str(q)
    return len(set(ns))


# @numba.njit(fastmath=True)
def d(n):
    res = 0
    i = 0
    while True:
        i += n
        if setlen(i) <= 2:
            res = i
            break
    return res


def run_tests():
    assert (d(102) == 1122), "Test error: d(102)"
    assert (d(103) == 515), "Test error: d(103)"
    assert (d(290) == 11011010), "Test error: d(290)"


# @numba.njit(fastmath=True, parallel=True)
def D(N):
    nmax = N + 1
    tot = 0
    q = 0
    for q in numba.prange(2, N)
        tmp = d(q)
        tot += tmp
    return tot * 1.





D(110)




# def d(n):
#     res = 0
#     g_cnt = ittr.count(start=n, step=n)
#     for c in g_cnt:
#         if setlen(c) <= 2:
#             res = c
#             break
#     return res













