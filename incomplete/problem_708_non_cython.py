
"""
Purpose: Project Euler problems
Date created: 2020-03-29

ID: 708
Title: Twos are all you need
URI: https://projecteuler.net/problem=708
Status: Complete
Contributor(s): Mark Moretto

Description:
    A positive integer, n, is factorised into prime factors. We define f(n) to be the
    product when each prime factor is replaced with 2. In addition we define f(1)=1.
    
    For example, 90=2×3×3×5, then replacing the primes, 2×2×2×2=16, hence f(90)=16.
    
    Let S(N)=∑n=1Nf(n). You are given S(108)=9613563919.
    
    Find S(1014).
"""


from itertools import count
from array import array
import numpy as np


def w(q):
    return int(np.sqrt(q)) + 1


def pd(n):
    """Prime decomposition function."""
    while n % 2 == 0:
        yield 2
        n /= 2

    q = w(n)
    for i in range(3, q, 2):
        while n % i == 0:
            yield 2
            n /= i

    if n > 2:
        yield 2



def f(n):
    result = 1
    if n > 1:
        xyz = list(pd(n))
        result = np.multiply.reduce(xyz)
    return result



def S(N):
    i = 1
    tot = 0
    while i <= N:
        tot += f(i)
        i += 1
    return tot


if __name__ == "__main__":
    debug = True
    res = 0
    if debug:
        # test = 10000
        test = int(1e6)
        res = S(test)
    else:
        actual = int(1e8)
        res = S(actual)

    print(res)


