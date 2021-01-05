
"""
Purpose: Project euler problem
Date created: 2020-11-29

Problen Number: 735
Name: Divisors of 2n^2
URL: https://projecteuler.net/problem=735

Contributor(s):
    Mark M.

Description:

"""

import gc
from math import sqrt

try:
    from functools import cache
except ImportError:
    from functools import lru_cache as cache

from itertools import takewhile, compress

gc.enable()


@cache(maxsize=None)
def modcheck(*args):
    return args[0] % args[1] == 0


def g_divisor(N):
    i = 1
    while i < N:
        if modcheck(N, i):
            yield i
        i += 1

@cache(maxsize=None)
def get_numer(N):
    return 2 * N * N

# @cache(maxsize=None)
# def divisors(n):
#     divs = {1, n}
#     numer = get_numer(n)
#     nsq = int(sqrt(numer))
#     for i in range(2, nsq + 1):
#         if modcheck(numer, i):
#             # print(i, n//i)
#             if n//i <= n:
#                 divs.update((i, n//i))
#     return divs


@cache(maxsize=None)
def primes(n):
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2)
    for i in range(3, int(sqrt(n)) + 1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1) // (2*i) + 1)
    return [2, *compress(range(3, n, 2), sieve[1:])]


@cache(maxsize=None)
def factorization(n):
    """ Returns a list of the prime factorization of n """
    pf = []
    for p in primes_list:
      if p * p > n: break
      count = 0
      while not n % p:
        n //= p
        count += 1
      if count > 0:
          pf.append((p, count))
    if n > 1:
        pf.append((n, 1))
    return pf


@cache(maxsize=None)
def divisors(n):
    """ Returns an unsorted list of the divisors of n """
    divs = [1]
    numer = get_numer(n)
    for p, e in factorization(numer):
        divs += [x*p**k for k in range(1, e + 1) for x in divs if x*p**k <= n]
    return divs



@cache(maxsize=None)
def f(n):
    return sum([1 for i in divisors(n)])


def F(N):
    rng = range(1, N + 1)
    return sum([f(i) for i in rng])



assert (F(15) == 63), "Error: F(15) value assertion."


if __name__ == "__main__":
    number = int(10 ** 12)
    primes_list = primes(int(sqrt(number)) + 1)

    res = F(number)
    print(res)




# @cache(maxsize=None)
# def f(n):
#     numer = get_numer(n)
#     gd = g_divisor(numer)
#     tw = takewhile(lambda q: q <= n, gd)
#     return sum([1 for i in tw])

# def divisors(n):
#     divs = [1]
#     if modcheck(n, 2):
#         divs.extend([2])
#     for i in range(3, int(math.sqrt(n)) + 1):
#         if modcheck(n, i):
#             divs.extend([i,n//i])
#     divs.extend([n])
#     return list(set(divs))


# def divisors(n):
#     divs = {1,n}
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if modcheck(n, i):
#             print(i, n//i)
#             divs.update((i,n//i))
#     return divs

# def f(n):
#     numer = 2 * n * n
#     i = 1
#     counter = 0
#     while i <= n:
#         if modcheck(numer, i):
#             counter += 1
#         i += 1
#     return counter


# def F(N):
#     i = 1
#     tot = 0
#     while i <= N:
#         tot += f(i)
#         i += 1
#     return tot