
"""
Purpose: Projec Euler exercises
Date created: 2020-05-09

Problen Number: 118 (B)
Name: Pandigital prime sets
URL: https://projecteuler.net/problem=118


Contributor(s):
    Mark M.

Description:

    Using all of the digits 1 through 9 and concatenating them freely to form decimal
    integers, different sets can be formed.

    Interestingly with the set {2, 5, 47, 89, 631}, all of the elements belonging to it
    are prime.
    
    How many distinct sets containing each of the digits one through nine exactly once
    contain only prime elements?
"""
# https://stackoverflow.com/questions/19368375/set-partitions-in-python/61141601
# http://code.activestate.com/recipes/117119-sieve-of-eratosthenes/

import gc
# import sys
import concurrent.futures as cf
import os
import math
import h5py
import numpy as np
import pandas as pd
import itertools as ittr
# import collections
# from functools import wraps, partial
from functools import partial

gc.enable()

os.chdir(r"C:\Users\Work1\Desktop\Info\PythonFiles\project-euler")
print(f"Current directory: {os.getcwd()}")
primes_file_loc = r"data\prime-numbers.h5"
primes_dataset = "primes123456789"


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



def sqrt_(n):
    """Simple square root function."""
    return np.float32(n ** 0.5)


def primes_up_to(n):
    """Generates all primes less than n."""
    if n <= 2: return
    yield 2
    F = [True] * n
    seq1 = range(3, int(sqrt_(n)) + 1, 2)
    seq2 = range(seq1[-1] + 2, n, 2)
    for p in filter(F.__getitem__, seq1):
        yield p
        for q in range(p * p, n, 2 * p):
            F[q] = False
    for p in filter(F.__getitem__, seq2):
        yield p

def create_primes_HDF5(num=12345678):
    """
    Create local storage of large prime number set.
    """
    p_list = list(primes_up_to(num))
    
    with h5py.File(primes_file_loc, "w") as f:
        f.create_dataset(primes_dataset, data=p_list)

# https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html#rm-invocation

h5f = h5py.File(primes_file_loc, "r")
p_arr = h5f[primes_dataset][:]
p_arr = p_arr.reshape((-1, 1))
h5f.close()



def reverser(iterable):
    rev = iterable[::-1]
    i = 0
    while True:
        try:
            yield i, rev[i]
            i += 1
        except IndexError:
            break

@memoize
def squashem(iterable):
    if len(iterable) == 1:
        return iterable[0]
    else:
        res = 0
        for i, v in reverser(iterable):
            res += pow(10, i) * v
        return res


@memoize
def splitter(a):
    if not a:
        return [[]]
    elif len(a) == 1:
        return [[a]]
    else:
        return [[a[:i], *s] for i in range(1, len(a) + 1) for s in splitter(a[i:])]


def check_prime(num):
    return num in p_arr


@memoize
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def xrange(limit):
    out = []
    i = 1
    while i <= limit:
        out.append(i)
        i += 1
    return out


# def worker(n):
#     count = np.array([0], dtype=np.uint32)
#     nums = np.arange(1, n + 1, dtype=np.uint32)
#     for perm in ittr.permutations(nums, n):
#         for splt in splitter(perm):
#             tmp = [squashem(i) for i in splt]
#             # with cf.ProcessPoolExecutor() as executor:
#             #     itw = [1 if prime else 0 for prime in executor.map(check_prime, tmp)]
#             with cf.ThreadPoolExecutor(max_workers=8) as executor:
#                 prime_gen = [executor.submit(check_prime, n) for n in tmp]
#                 for future in concurrent.futures.as_completed(prime_gen):

#             # itw = [i for i in tmp if check_prime(i)]
#             # itw_len = len(itw)
#             itw_len = sum(itw)
#             if len(tmp).__eq__(itw_len):
#                 np.add.at(count, [0], 1)
#     return count




# @memoize
def worker(n):
    count = np.array([0], dtype=np.uint32)
    nums = xrange(n)
    for perm in ittr.permutations(nums, n):
        for splt in splitter(perm):
            tmp = [squashem(i) for i in splt]
            itw = [i for i in tmp if check_prime(i)]
            itw_len = len(itw)
            if len(tmp).__eq__(itw_len):
                # count += 1
                np.add.at(count, [0], 1)
    return count



# def run(N):
#     res = []
#     for i in range(1, N + 1):
#         tmp = worker(i)
#         res.append(tmp)
#     return res

# codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
# codeObejct = compile(codeInString, 'sumstring', 'exec')
# exec(codeObejct)




if __name__ == "__main__":
    N = 9
    with cf.ThreadPoolExecutor() as executor:
        worker = executor.submit(worker, N)
        res = worker.result()
        print(f"Result for N = {N}: {res}")

    # rng = xrange(N)
    # res = []
    # with cf.ThreadPoolExecutor() as executor:
    #     workers = [executor.submit(worker, i) for i in rng]
    #     for w in cf.as_completed(workers):
    #         try:
    #             tmp = w.result()
    #             res.append(tmp[0])
    #         except Exception as exc:
    #             print(f'{w} generated an exception: {exc}')
    # print("\n".join([f"{i}" for i in res]))


    # output = run(8)
    # print(max(output))



# run(1) # [0]
# run(2) # [0]
# run(3) # [4]
# run(4) # [18]
# run(5) # [94]
# run(6) # [284]
# run(7) # [4306]
# run(8) # [16228]




"""
@memoize
def worker(n):
    count = np.array([0], dtype=np.uint32)
    nums = np.arange(1, n + 1, dtype=np.uint32)
    for perm in ittr.permutations(nums, n):
        for splt in splitter(perm):
            tmp = [squashem(i) for i in splt]
            itw = [i for i in tmp if check_prime(i)]
            itw_len = len(itw)
            if len(tmp).__eq__(itw_len):
                np.add.at(count, [0], 1)
    return count
"""

# @memoize
# def worker(N):
#     rng = xrange(N)
#     perms = [perm for perm in ittr.permutations(rng, N)]
    
#     splits = [[s for s in splitter(perm)] for perm in perms]
#     splits = [i for j in splits for i in j]
    
#     ints  = [[squashem(q) for q in t] for t in splits]
#     base_dict = enum_dict(ints)

#     prime_dict = {i:[p for p in x if is_prime(p)] for i, x in base_dict.items()}
#     return base_dict, prime_dict


# @memoize
# def run(n):
#     counter = 0
#     based, permd = worker(n)
#     for i, a in based.items():
#         for j, b in permd.items():
#             if i == j and len(a) == len(b):
#                 counter += 1
#     return counter
