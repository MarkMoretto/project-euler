"""
Purpose: Project Euler problems
Date created: 2020-04-19

ID: 712
Title: Exponent Difference
URI: https://projecteuler.net/problem=712

Status: Incomplete

Contributor(s): Mark Moretto

Problem:
    For any integer n>0 and prime number p, define νp(n) as the greatest integer r
    such that pr divides n.
    
    Define - 
    
        D(n, m) = ∑|νp(n) − νp(m)|.
        For p, where p is prime.
    
    For example, D(14, 24) = 4.
    
    Furthermore, define
    
        S(N) = ∑ D(n, m).
        For 1 ≤ n and m ≤ N
    
    You are given
    	S(10) = 210 
    	S(10^2) = 37018.
    
    Find S(10^12).
    
    Give your answer modulo 1000000007. 

Notes:
    If x divides y, x is a factor of y, or in other words, y is divisible by x.
    
    Ex -
        3 divides 15 because 15 = 3*5.
        3 is a factor of 15.
"""

from __future__ import division, print_function

import os
os.environ["NUMBA_THREADING_LAYER"] = "tbb"
os.environ["NUMBA_ENABLE_AVX"] = "1"
#os.environ["NUMBA_NUM_THREADS"] = f"{os.cpu_count() - 2}"
os.environ["NUMBA_LOOP_VECTORIZE"] = "1"
os.environ["NUMBA_OPT"] = "3"


import numpy as np
import numba


@numba.njit(["uint64(float64)", "uint32(float32)", "uint64(int64)", "uint32(int32)"])
def csqrt(n):
    return np.uint64((n**0.5) + 0.5)



@numba.njit
def primes_(max_num):
    num = np.uint64(2)
    one_ = np.uint64(1)
    output = []
    while num <= max_num:
        count = np.uint64(0)
        i = np.uint64(2)
        while (i <= num // 2):
            if num % i == 0:
                count += one_
                break
            i += one_

        if count == 0 and num != 1:
            output.append(num)
        num += one_
    return output


# @numba.njit(["int64(float64, int64)"], fastmath=True)
@numba.njit
def vp(num, p):

    r = np.uint64(1)
    max_r = np.uint64(0)

    while r <= num:
        q = p ** r
        if q > 0:
            if num % q == 0:
                if r > max_r:
                    max_r = r
        r += 1
    return max_r


@numba.njit
def D(n, m):

    tot = np.uint64(0)

    max_n = max(n, m)

    primes = primes_(max_n)

    for p in primes:
        tmp = abs(vp(n, p) - vp(m, p))
        tot += tmp
    return tot


@numba.njit(["int64(int64)", "int32(int32)"], fastmath=True, parallel=True)
def S(N):
    mod_ = np.uint64(1e9 + 7)
    one_ = np.uint64(1)
    N += one_
    tot = np.uint64(0)
    for n in numba.prange(1, N):
        for m in numba.prange(1, N):
            tot += D(n, m)
    return tot % mod_



if __name__ == "__main__":
    test = int(1e4)
    res = S(test)
    print(res)





