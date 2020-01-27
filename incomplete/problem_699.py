
"""
Purpose: Project Euler problems
Date created: 2020-01-26

Contributor(s):
    Mark M.

ID: 699
Title: Triffle Numbers
URI: https://projecteuler.net/problem=699
Difficulty: ?

Status: Incomplete

Problem:
    Let σ(n) be the sum of all the divisors of the positive integer n,
    for example: σ(10)=1+2+5+10=18.
    
    Define T(N) to be the sum of all numbers n≤N such that when the fraction
    σ(n)n is written in its lowest form ab, the denominator is a power of 3
    i.e. b=3**k, k>0.
    
    You are given T(100)=270
    and T(10**6)=26089287.
    
    Find T(10**14)
"""

import math
import numpy as np

from fractions import Fraction



def divisor_gen(x):
    start = np.int32(1)
    incr = np.int32(1)
    for i in range(start, x + incr):
        if x % i == 0:
            yield i

def sum_divisors(n):
    yield np.sum([i for i in divisor_gen(n)])

def np_log(n, base=3):
    return np.log(n) / np.log(base)


incr = np.int64(1)

def T(N):
    n_limit = np.int64(N)
    n_list = list()
    n = np.int64(0)
    while n <= n_limit:
        n += incr
        numer = sum_divisors(n).__next__()
        frac = Fraction(numer, n)
        res = np_log(frac.denominator)
        if res != 0.:
            if np_log(frac.denominator) % 1. == 0.:
                n_list.append(n)
    return sum(n_list)



assert (T(100) == 270), "Fail: T(100) test"


T(int(1e6))






"""
### Initial T() -
incr = np.int64(1)
n_limit = np.int64(N)

n_list = list()
n = np.int64(0)
while n <= n_limit:
    n += incr
    numer = sum_divisors(n).__next__()
    frac = Fraction(numer, n)
    # print(f"n: {n}, numer: {numer},  {frac}, {np_log(frac.denominator)}")
    res = np_log(frac.denominator)
    if res != 0.:
        if np_log(frac.denominator) % 1. == 0.:
            n_list.append(n)



rng = np.arange(1, 21, dtype=np.int64)
tst1 = [[sum_divisors(i).__next__(), i] for i in rng]

[np.gcd(np.array(sum_divisors(i).__next__()), np.array(i)) for i in rng]

tst3 = [Fraction(sum_divisors(i).__next__(), i) for i in rng]

for i in rng:
    numer = np.array(sum_divisors(i).__next__())
    denom = i
    gcd = np.gcd(np.array(sum_divisors(i).__next__()), np.array(i))
    x = numer / gcd
    y = denom / gcd
    print(f"i: {i}, Numer: {numer}, Denom: {denom}, gcd: {gcd}, frac: ({x}, {y})")



while n <= n_limit:
    n += incr
    numer = np.array(sum_divisors(i).__next__())
    gcd = np.gcd(np.array(numer), np.array(n))
    x = n / gcd
    y = denom / gcd
    if np_log(n / gcd) == 0.:
        n_list.append(n)
    n += incr


for i in rng:
    numer = np.array(sum_divisors(i).__next__())
    denom = i
    gcd = np.gcd(np.array(sum_divisors(i).__next__()), np.array(i))
    y = denom / gcd
    if np_log(y) == 0.:

    print(f"Log base 3 of denominator: {np_log(y)}")

def T(N):
    pass

"""
















