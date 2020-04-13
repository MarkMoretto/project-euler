
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
    
    For example, 90 = 2 × 3 × 3 × 5,
    then replacing the primes, 2 × 2 × 2 × 2 = 16,
    hence f(90) = 16.
    
    Let S(N) = ∑n = 1Nf(n).

    You are given S(108) = 9613563919.
    
    Find S(1014).
"""

import os
os.environ["NUMBA_THREADING_LAYER"] = "tbb"
os.environ["NUMBA_ENABLE_AVX"] = "1"


import numpy as np

from numba import (
        njit,
        prange,
        vectorize,
        cuda,
        )



@njit(["float64(int64)"], fastmath=True)
def f(n):
    """Prime decomposition function."""

    result = 1.
    two = 2.

    while n % 2 == 0:
        result *= two
        n /= 2

    max_n = np.int64(n ** 0.5 + 1)
    for i in range(3, max_n, 2):
        while n % i == 0:
            result *= two
            n /= i

    if n > 2:
        result *= two
    return np.float64(result)



@njit(["uint64(int64)"], fastmath=True, parallel=True)
def S(N):
    tot = np.float64(0)
    N += 1
    for i in prange(1, N):
        tot += f(i)
    return tot



if __name__ == "__main__":

    # Expected test results for a given integer
    expected = {
            "1e7": np.uint64(746246327),
            "1e8": np.uint64(9613563919),
            }

    test_str = "1e7"
    test_value = int(eval(f"{test_str}"))
    res = S(test_value)

    print(f"{res}")

    if expected[test_str] == res:
        print("Result matches expected!")




"""
# Possible caching

import tempfile as tf
td = tf.TemporaryDirectory(prefix="NumbaCache")
os.environ["NUMBA_CACHE_DIR"] = td.name
os.environ["CACHE_DIR"] = td.name

td.cleanup()
"""

# @jit(["int64[:](float64)", "int32[:](float32)"])
# def p(num):
#     out = [i for i in pd(num)]
#     xyz = np.full((4,1), 2)
#     return out


# @jit(["int64(int64[:])"])
# @generated_jit
# def reducer(x):
#     a = x[0]
#     if x.size > 1:
#         for i in x[1:]:
#             a *= i
#     return a

# tst1 = np.array([2,2,2,2], dtype=np.uint64)
# reducer(tst1)


# @numba.vectorize(["float64(int64)"], target='parallel')
# @numba.njit
# def f(n):
#     result = 1
#     if n > 1:
#         xyz = np.array([i for i in p(n)])
#         # result = np.multiply.reduce(xyz)
#         result = reducer(xyz)
#     return np.float64(result)


"""
import concurrent.futures

CPU_COUNT = mp.cpu_count()
N_WORKERS = int((CPU_COUNT / 2) * 5)

def Scf(N):
    tot = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=N_WORKERS) as executor:
        futures_dict = {executor.submit(f, i):i for i in range(1, N + 1)}
        for n in concurrent.futures.as_completed(futures_dict):
            err_n = futures_dict[n]
            try:
                tot += n.result()
            except Exception as e:
                print(f"Exception generated by {err_n}: {e}")
    return tot

# res = Scf(int(1e7))
"""