
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








# # Borrowed from:
# # https://stackoverflow.com/questions/2211990/how-to-implement-an-efficient-infinite-generator-of-prime-numbers-in-python

# def p_sieve():
#     itc = count
#     yield from (2, 3, 5, 7)
#     D = {}
#     ps = p_sieve()
#     ps.__next__()
#     p = ps.__next__()
#     assert p == 3
#     psq = p*p
#     for i in itc(9, 2):
#         if i in D: # composite
#             step = D.pop(i)
#         elif i < psq:   # prime
#             yield i
#             continue
#         else: # composite, = p*p
#             assert i == psq
#             step = 2*p
#             p = ps.__next__()
#             psq = p*p
#         i += step
#         while i in D:
#             i += step
#         D[i] = step


# def x_prime():
#     itc = count
#     p_arr = array("Q")
#     p_arr.append(2)
#     n = 0
#     yield p_arr[0]
#     for i in itc(3, 2):
#         is_prime = True
#         for n in p_arr:
#             if (i % n).__eq__(0):
#                 is_prime = False
#                 break
#             elif (n * n).__gt__(i):
#                 break
#         if is_prime:
#             p_arr.append(i)
#             yield i


# def make_primes(max_n):
#     """Generate list of primes"""
#     # p = p_sieve()
#     p = x_prime()
#     return [p.__next__() for _ in range(max_n)]
#     p.close()

# # primes = array("Q")
# # primes.fromlist(make_primes(10))