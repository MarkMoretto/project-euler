
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

# https://jakevdp.github.io/blog/2012/08/08/memoryview-benchmarks/

# %load_ext Cython
# import os
# import warnings

# os.environ["MODIN_ENGINE"] = "dask"

# warnings.simplefilter("ignore", FutureWarning)

# # import cython
# import numpy as np
# import modin.pandas as pd
# import pandas as pd

# pd.set_option("compute.use_numexpr", True)
# pd.set_option('display.max_rows', 25)
# pd.set_option('max_colwidth', 60)
# pd.set_option('display.precision', 4)
# pd.set_option('mode.chained_assignment', None)

# import numexpr as ne
# pd.set_option("compute.use_bottleneck", True)

from functools import reduce

import numpy as np
import bottleneck as bn


# def reducer(x):
#     x_len = len(x)
#     if x_len > 0:
#         output = x[0]
#         if x_len > 1:
#             for i in x[1:]:
#                 output *= i
#         return output

# n_list = [2 for i in range(4)]
# reducer(n_list)


def sqrt_(n):
    return n ** (1/2)

def step_(x):
    return 1 + (x<<2) - ((x>>1)<<1)

def maxq_(q):
    return int(np.floor(np.sqrt(q)))


def fac2(n):
    maxq = maxq_(n)
    d = 1
    q = 2 if n % 2 == 0 else 3 
    while q <= maxq and n % q != 0:
        q = step_(d)
        d += 1
    res = [q] + fac2(n // q) if q <= maxq else [n]
    return [2 for _ in res]
    # return [q] + fac(n // q) if q <= maxq else [n]


# def pfs2(n):
#     """
#     Prime factors of n, but only 2 is yielded when a value is found.
#     """
#     while n % 2 == 0:
#         yield 2
#         n /= 2

#     for i in range(3, int(sqrt_(n)) + 1, 2):
#         while n % i == 0:
#             yield 2
#             n /= i

#     if n > 2:
#         yield 2


def f(n):
    result = 1
    if n > 1:
        # result = reducer(p_)
        result = reduce(np.multiply, fac2(n))
    return result


def S(N):
    N = int(N)
    i, tot_, incr_ = int(0), int(0), int(1)
    while i <= N:
        tot_ += f(i)
        i += incr_
    return tot_


if __name__ == "__main__":
    debug = True
    res = 0
    if debug:
        # test = 10000
        test = 1000000
        res = S(test)

    # actual = 1e8
    # res = S(actual)
    if res:
        print(res)

# test2 = 1000000
# S(test2)

# res = S(1e8) # 9613563919





# ### Using numba
# import numba
# from numba.typed import List
# @numba.njit
# def reducer(x):
#     x_len = len(x)
#     if x_len > 0:
#         output = x[0]

#         if x_len > 1:
#             for i in x[1:]:
#                 output *= i
#         return output

# # n_list = [2 for i in numba.prange(4)]
# # reducer(n_list)


# @numba.njit
# def pfs(n):
#     """Prime factors of n."""
#     while n % 2 == 0:
#         yield 2
#         n /= 2

#     max_n = numba.uint64(np.sqrt(n)) + 1
#     for i in numba.prange(3, max_n, 2):
#         while n % i == 0:
#             yield i
#             n /= i

#     if n > 2:
#         yield n


# two_list = List()


# @numba.njit
# def f(n):
#     res = 1
#     if n > 1:
#         p_ = [i for i in pfs(n)]
#         two_list = [2 for i in numba.prange(len(p_))]
#         res = reducer(two_list)
#     return res


# assert (f(90) == 16), "Failed: f(90)"


# rng = List()

# @numba.njit
# def S(N):
#     rng = [i for i in numba.prange(1, N)]
#     res = sum(map(f(i), rng))
#     return res

# test1 = numba.uint64(1000) + numba.uint64(1)
# S(1001)
# S(1e8) # 9613563919



# def ten_exp_format(value = 1e8):
#     print(f"{value:,.0f}")

