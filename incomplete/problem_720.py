
"""
Purpose: Project Euler exercises
Date created: 2020-06-14

Problen Number: 720
Name: Unpredictable Permutations
URL: https://projecteuler.net/problem=720

Contributor(s):
    Mark M.
"""

import numpy as np
import itertools as ittr
from functools import lru_cache
from copy import deepcopy


MOD = 1000000007


# def ncycles(iterable, n):
#     "Returns the sequence elements n times"
#     return ittr.chain.from_iterable(ittr.repeat(tuple(iterable), n))

a = [1,2,3,4,5,6,7,8]

def lexicographical_permutations(number_string):
    p_len = len(number_string)
    perms = sorted(''.join(chars) for chars in ittr.permutations(number_string, p_len))
    return [list(map(int, x)) for x in perms]

res = lexicographical_permutations("123")

@lru_cache(maxsize=None)

def eval_ijk(I, J, K):
    return I < J < K


def S(num):

    rng = np.arange(1, num + 1)
    p_gen = ittr.permutations(rng, num)
    merge_max = num - 2

    pix = 1
    # for pix, perm in enumerate(p_gen, start=1):
    while True:

        perm = next(p_gen)
        t = list(perm)
        t.extend(t[:2])

        inner = 0
        idx = 0

        while idx < num:
            if inner > 0:
                break

            i = t[idx]
            j = t[idx+1]
            k = t[idx+2]

            # if i < j < k:
            if eval_ijk(i, j, k):
                inner += 1
            idx += 1

        if inner == 0:
            break

        pix += 1

    return pix % MOD

if __name__ == "__main__":
    n = 8
    res = S(n)
    print(f"The first unpredictable permutation of S({n}) is at index: {res}")






N = 9

rng = "".join([f"{i}" for i in range(1, N + 1)])
p_list = lexicographical_permutations(rng)

# p_list = sorted(list(ittr.permutations(rng, N)))
# p_dict = {i:list(p) for i, p in enumerate(ittr.permutations(rng, N), start=1)}


unpredictables = {}
ix = 0
# perms = ittr.permutations(rng, N)
# p_list = sorted(list(ittr.permutations(rng, N)))
# for ix in p_dict.keys():
for perm in p_list:
    ix += 1
    # Add the first two elements to the end of the list
    p = list(deepcopy(perm))
    tmp = p[:2]
    p.extend(tmp)
    sucess_val=0
    # print(p)
    for el in range(N):
        i, j, k = p[el], p[el+1], p[el+2]
        # print(i,j, k)
        # if (i<j<k).all():
        if eval_ijk(i, j, k):
            # print(p)
            sucess_val += 1

    if sucess_val==0:
        unpredictables[ix] = p
        break
        # unpredictables.append(ix)

ukeys = list(unpredictables.keys())

# 3 = 2
# 4 = 3
# 5 = 8
# 6 = 27
# 7 = 127
# 8 = 747


# num = 8
# rng = np.arange(1, num + 1)
# merge_max = num - 2
# perms = [i for i in ittr.permutations(rng, num)]
# tst = perms[746]
# t = list(ncycles(tst, 2))[:-merge_max]

# p_gen = ittr.permutations(rng, num)
# next(p_gen)
# t2 = (1, 2, 3, 4, 5, 7, 6, 8)
# for pix, perm in enumerate(p_gen, start=1):
#     t = list(ncycles(perm, 2))[:-2]
#     inner = 0
#     idx = 0

#     while idx < num:
#         if inner > 0:
#             break

#         i = t[idx]
#         j = t[idx+1]
#         k = t[idx+2]

#         if i < j < k:
#             inner += 1
#         idx += 1

#     if inner == 0:
#         break
















