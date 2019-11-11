
"""
Purpose: Project Euler problems
Date created: 2019-11-08
Contributor(s): Mark M.

ID: 76
Title: Counting summations
URI: https://projecteuler.net/problem=76
Difficulty: 10%

Status: Incomplete



Problem:
    It is possible to write five as a sum in exactly six different ways:
    
    4 + 1
    3 + 2
    3 + 1 + 1
    2 + 2 + 1
    2 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1
    
    How many different ways can one hundred be written as a sum of at
    least two positive integers?
"""

from helper_modules import *

import typing as T



def lte_target(tot: int, trgt: int) -> bool:
    """ Is the sum less than or equal to the target?"""
    return True if tot <= trgt else False


def gen_ones(n: int) -> ivector:
    """Return vector of 1s"""
    return [1] * n


def gen_lower_matrix(rows: int, cols: int) -> T.Iterable[int]:
    return [[1 if c <= r else 0 for c in mRANGE(cols)] for r in mRANGE(rows)]


def min_threshold_matrix(it: T.Iterable[N_], threshold: N_ = 1) -> T.Iterable[int]:
    return [row for row in it if mSUM(row) > 1]


def nonzero_len(it: T.Iterable[N_]) -> int:
    return mSUM([1 for i in it if i != 0])



#-- Integers must be positive
#-- Max number of items on a list is the target number (repeating 1s)
N: int = 5


index_range = mRANGE_GEN(1, N) # Range from 1 to N - 1, since N cannot be in a vector
vec_size = mRANGE_GEN(2, N + 1) # Size of initial 1s vector
ii_rng = mRANGE_GEN(N - 1, 0, -1) # Inverse range
iter_range = mRANGE_GEN(2, N)

# lmatrix = min_threshold_matrix(gen_lower_matrix(N,N))

 for i in vec_size:
    base = gen_ones(i)
    for r in index_range: # row
        for c in mRANGE_GEN(i): # columns
            for f in index_range: # row
                base[c] = f
                if mSUM(base) == N:
                    print(r, c, f, k, base, mSUM(base))

                for k in mRANGE_GEN(i): # column
                    base[k] = f
                    if mSUM(base) == N:
                        print(r, c, f, k, base, mSUM(base))


#- Working, but going to try inverse
for i in vec_size:
    base = gen_ones(i)
    for r in index_range: # row
        for c, _ in enum(base): # columns
            base[c] = r
            print(r, c, base, mSUM(base))


            for f in index_range: # row
                for k, _ in enum(base): # column
                    if f != k:
                        base[c] = f
                        if mSUM(base) == N:
                            print(r, c, f, k, base, mSUM(base))

                    if mSUM(base) == N:
                        print(r, c, k, base, mSUM(base))









# # Testing N = 10
# output = []
# for i in vec_size:
#     base = gen_ones(i)
#     for n, _ in enum(base):
#         for j in index_range:
#             if mSUM(base) < N:
#                 base[n] = j
#                 print(f'Base: {base}')
#             print(f'Outside if: {base}')
#     print(f'Outside for: {base}')




# # Works for N = 5
# output = []
# counter = 0
# for i in incr_range:
#     base = gen_ones(i)
#     for x, v in enum(base):
#         if mSUM(base) < N:
#             while mSUM(base) < N:
#                 base[x] += 1
#                 print(f'{base}')
#             print(f'Outside while: {base}')
#         if x==0 or base[x] <= base[x-1]:
#             print(f'Outside while (gte): {base}')
#             if not base in output:
#                 output.append(list(base))
#         if base[x] - 1 > 0:
#             base[x] -= 1















