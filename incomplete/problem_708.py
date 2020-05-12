
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

from __future__ import print_function

def factors(n):
    return [f for i in range(1, int(n**0.5) + 1) if n%i == 0 for f in (i, n//i)]
"""
%load_ext cython
"""

"""
%%cython -a
"""

import numpy as np
# cimport numpy as np
import cython
from cython.parallel import prange

DTYPE = np.intc

# @cython.cfunc
# @cython.returns(cython.double)
# @cython.locals(n=cython.double, res=cython.ulonglong)
# def sqrt_(n):
#     res = n ** (1/2)
#     return res

@cython.cfunc
@cython.returns(cython.ulonglong)
@cython.locals(q=cython.ulonglong, res=cython.ulonglong)
def w(q):
    res = int(np.sqrt(q)) + 1
    return res


@cython.cfunc
@cython.returns(cython.uint)
@cython.locals(n=cython.ulonglong, q=cython.ulonglong, i=cython.ulonglong)
def pd(n):
    """Prime decomposition function."""
    while n % 2 == 0:
        yield 2
        n /= 2

    q = w(n)

    for i in prange(start=3, stop=q, step=2, nogil=True, schedule='guided'):
        while n % i == 0:
            yield 2
            n /= i

    if n > 2:
        yield 2


# @exceptval(-1, check=True)
@cython.cfunc
@cython.returns(cython.ulonglong)
@cython.locals(n=cython.ulonglong, result=cython.ulonglong, xyz=cython.ulong[100])
def f(n):
    result = 1
    if n > 1:
        xyz = list(pd(n))
        result = np.multiply.reduce(xyz)
    return result


@cython.cfunc
@cython.returns(cython.ulonglong)
@cython.locals(N=cython.double,
               n=cython.ulonglong,
               i=cython.ulonglong,
               tot=cython.ulonglong,
               )
def S(N):
    n = N
    i = 1
    tot = 0
    while i <= n:
        tot += f(i)
        i += 1
    return tot


if __name__ == "__main__":
    debug = False
    res = 0
    if debug:
        # test = 10000
        test = int(1e6)
        res = S(test)
    else:
        actual = int(1e8)
        res = S(actual)
    if res:
        print(res)

# test2 = 1000000
# S(test2)

# res = S(1e8) # 9613563919




### Old code

# @cython.locals(x=cython.ulonglong)
# cdef step(x):
#     return 1 + (x<<2) - ((x>>1)<<1)
# def pd(double n) except -1:
#     """Prime decomposition function."""
#     cdef double list res = []
#     cdef double maxq, d, q, res
#     maxq = w(n)
#     d = 1
#     q = 2 if n % 2 == 0 else 3
#     while q <= maxq and n % q != 0:
#         q = step_(d)
#         d += 1
#     res = [q] + pd(n // q) if q <= maxq else [n]
#     return [2 for _ in res]


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


# def sqrt_(n):
#     return n ** (1/2)

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

