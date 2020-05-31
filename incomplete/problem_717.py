
"""
Purpose: Project Euler exercises
Date created: 2020-05-24

Problen Number: 717
Name: Summation of a Modular Formula
URL: https://projecteuler.net/problem=717

Contributor(s):
    Mark M.
"""

import os
import numpy as np
from math import floor
from functools import partial, lru_cache

DIR = r"C:\Users\Work1\Desktop\Info\PythonFiles\project-euler\incomplete"
os.chdir(DIR)


class memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        try:
            args.__hash__()
            if args in self.cache:
                return self.cache[args]
            else:
                value = self.func(*args)
                self.cache[args] = value
                return value
        except TypeError:
            return self.func(args)

    def __repr__(self):
        return self.func.__doc__

    def __get__(self, obj, objtype):
        return partial(self.__call__, obj)


@memoize
def int_sqrt(n):
    return int(n ** 0.5)


def odd_primes_up_to(n):
    """Generates all primes less than n."""
    # if n <= 2: return
    # yield 2
    F = [True] * n
    seq1 = range(3, int_sqrt(n) + 1, 2)
    seq2 = range(seq1[-1] + 2, n, 2)
    for p in filter(F.__getitem__, seq1):
        yield p
        for q in range(p * p, n, 2 * p):
            F[q] = False
    for p in filter(F.__getitem__, seq2):
        yield p


@memoize
def pow2(n):
    return 1<<n




def f(p):
    pow2p = pow2(p)
    return (pow2(pow2p) // p).__mod__(pow2p)


def g(p):
    return f(p).__mod__(p)


def G(N):
    primes = odd_primes_up_to(N)
    tot = 0
    while primes:
        prime = next(primes)
        tot += g(prime)
    return tot

G(100)









'''
https://cp-algorithms.com/algebra/binary-exp.html
https://cp-algorithms.com/algebra/module-inverse.html
https://cp-algorithms.com/algebra/extended-euclid-algorithm.html
'''

# p = np.float64(3)


# def gcd(a, b):
#     """
#     Greatest common divisor
#     :param: a
#     """
#     while b:
#         a, b = b, a % b
#     return a



# def gcd_ext(a, b, x=0, y=1):
#     """
#     Greatest common divisor
#     """
#     pre_x, pre_y = 1, 0
#     while b:
#         q = a / b
#         x, pre_x = pre_x - q * x, x
#         y, pre_y = pre_y - q * y, y
#         a, b = b, a % b
#     return a, pre_x, pre_y


# a_, b_ = 35, 15


# g, x, m = gcd_ext(a_, b_)

# g, b, x = gcd_ext(a, m, x, y)
# if (g != 1):
#     print("No solution!")
# else:
#     x = (x % m + m) % m
#     print(x)


# def np_gcd_ext(a, b):
#     pre_x = np.float64(1)
#     pre_y = np.float64(0)
#     x = np.float64(0)
#     y = np.float64(1)

#     while b:
#         q = np.divide(a, b)
#         x, pre_x = pre_x - q * x, x
#         y, pre_y = pre_y - q * y, y
#         a, b = b, np.modf(a, b)
#     return a, pre_x, pre_y




