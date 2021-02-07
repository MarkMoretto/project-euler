
"""
Purpose: Project euler problem
Date created: 2021-01-31

Problen Number: 745
Name: Sum of Squares
URL: https://projecteuler.net/problem=745

Contributor(s):
    Mark M.

Description:

"""

from functools import lru_cache as cache

MOD = 1000000007


@cache(maxsize=None)
def squared(num):
    return num * num


@cache(maxsize=None)
def g(n):
    max_sq = 1
    for i in range(1, n//2 + 1):
        sq = squared(i)
        if n % sq == 0 and sq <= n:
            max_sq = sq
    return max_sq


def S(N):
    tot = 0
    for i in range(1, N + 1):
        tot += (g(i) % MOD)
    return tot



# def factor_gen(number):
#     return filter(lambda q: number % q == 0 and (q * q) <= number, range(1, number))

if __name__ == "__main__":
    number = int(1e14)
    res = S(number)
    print(f"The result is: {res}")
