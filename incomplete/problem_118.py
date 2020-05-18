
"""
Purpose: Projec Euler exercises
Date created: 2020-05-09

Problen Number: 118
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

import os
import h5py
import numpy as np
import itertools as ittr
# from copy import deepcopy
import collections
# import functools
from functools import wraps, lru_cache, partial

# namedtuple = collections.namedtuple
# deque = collections.deque

os.chdir(r"C:\Users\Work1\Desktop\Info\PythonFiles\project-euler")

primes_file_loc = r"data\prime-numbers.h5"
primes_dataset = "primes123456789"

# Run primes only if file doesn't already exist


def n_sum(n_string):
    """
    Sum the total of a string of numbers.

    Example:
        n_sum('123') == 6
    """
    return sum(map(int, list(n_string)))

def n_split(n):
    """
    Split integer into collection of non-string digits.

    Example:
        n_split('123') == [1,2,3]
    """
    return list(map(int, list(str(n))))



def get_set(iterable):
    """
    Unravel non-set numeric collection into set collection.

    Example:
        get_set('12333') == {'1', '2', '3'}
    """
    res = set(iterable)
    if len(iterable) > 1:
        res = set([p for q in iterable for p in q])
    return res


def reverser(obj):
    tmp = obj[::-1]
    i = 0
    while True:
        try:
            yield i, tmp[i]
            i += 1
        except IndexError:
            break


def squashem(iterable):
    """Concatenate a set of positive integers into one integer."""
    res = 0
    if len(iterable) == 1:
        res = iterable[0]
    else:
        for i, v in reverser(iterable):
            res += pow(10, i) * v
    return res

# arr = [2,3,4]
# squashem(*arr)

def sqrt_(n):
    return n ** 0.5


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


h5f = h5py.File(primes_file_loc, "r")
p_arr = h5f[primes_dataset][:]
h5f.close()



# https://stackoverflow.com/questions/15585493/store-the-cache-to-a-file-functools-lru-cache-in-python-3-2


def cached(func):
    func.cache = {}
    @wraps(func)
    def wrapper(*args):
        try:
            return func.cache[args]
        except KeyError:
            func.cache[args] = result = func(*args)
            return result   
    return wrapper


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



# @cached
@memoize
def splitter(s):
    for i in range(1, len(s)):
        start = s[0:i]
        end = s[i:]
        yield [start, end]
        for split in splitter(end):
            result = [start]
            result.extend(split)
            yield result

# splitter.cache

def run(n):
    count = np.array([0], dtype=np.uint64)
    nums = np.arange(1, n + 1, dtype=np.uint32)
    for p in ittr.permutations(nums, n):
        perm = "".join(list(map(str, p)))
        for j in splitter(perm):
            t = list(map(int, j))
            itw = list(ittr.takewhile(lambda x: x in p_arr, t))
            itw_len = len(itw)
            if itw_len.__gt__(0):
                if len(t).__eq__(itw_len):
                    np.add.at(count, [0], 1)
    print(count)



if __name__ == "__main__":
    N = 9

    run(N)




# def partitioner(iterable):
#     """
#     Create subsets of integer collection using all values in each result.
#     """
#     if len(iterable) == 1:
#         yield [iterable]
#         return

#     first = iterable[0]
#     for smaller in partitioner(iterable[1:]):
#         for n, subset in enumerate(smaller):
#             yield smaller[:n] + [[first] + subset]  + smaller[n+1:]

#         yield [[first]] + smaller





# def ireduce(iterable):
#     """
#     Create local storage of large prime number set.
#     """
#     for i in iterable:
#         tmp = "".join(list(map(str, i)))
#         yield int(tmp)





# All permutations
# Permutation = namedtuple('Partition', ["index", "items", "length"])
# Partition = namedtuple('Partition', ["index", "items", "length"])


"""
# Working set

nums = list(range(1, 10))
length = len(nums)

perms = list()
for p in ittr.permutations(nums, length):
    tmp = "".join(list(map(str, p)))
    perms.append(tmp)

# All partitions of a
def splitter(s):
    for i in range(1, len(s)):
        start = s[0:i]
        end = s[i:]
        yield [start, end]
        for split in splitter(end):
            result = [start]
            result.extend(split)
            yield result



partitions = list()
ix = 0

for i in perms:
    for j in splitter(i):

        t = list(map(int, j))

        itw = list(ittr.takewhile(lambda x: x in p_arr, t))

        t_len, itw_len = len(t), len(itw)

        if itw_len.__gt__(0):
            if t_len.__eq__(itw_len):
                print(t, itw)
"""
# All partitions of a


# N = 4
# nums = [1,2,3,4]
# nums = np.arange(1, N + 1, dtype=np.uint32)











"""
count = 0
for p in ittr.permutations(nums, N):
    perm = "".join(list(map(str, p)))
    for j in splitter(perm):
        parts = list(map(int, j))
        itw = sum([1 for q in parts if q in p_arr])
        if itw.__gt__(0):
            if len(t).__eq__(itw):
                count += 1
                
"""









'''
results = list()
nums = list(range(1, 10))
num_set = set(nums)
length = len(nums)
target_sum = sum(nums)

partitions = list(partitioner(nums))
spartitions = [[j for j in ireduce(p)] for p in partitions]

twofivefour = [v for i, v in enumerate(partitions) if \
            partitions[i][0][0] == 2 \
            and partitions[i][1][0] == 5 \
            and partitions[i][1][0] == 4 \
            ]
twostart = [i for i in partitions if i[0] == 2 and i[1] == 5 and i[2] == 47]

[2,5,47,89,631] in spartitions


for i, v in enumerate(partitions[:10]):
    for j, ele in enumerate(v):
        tmp = "".join(list(map(str, ele)))
        print(i, j, v, ele, tmp)



for p in partitioner(nums):
    ir = list(ireduce(p))
    tw = list(ittr.takewhile(lambda x: x in p_arr, ir))
    len_ir, len_tw = len(ir), len(tw)
    if len(tw) > 1:
        if len_ir == len_tw:
            results.append(tw)


#     print(tw)
# if sum([1 for i in ittr.chain.from_iterable(tw)]) == length:
#     results.append(tw)
#     print(tw)
#     break


# results = list()
# nums = list(range(1, 4))
# num_set = set(nums)
# length = len(nums)
# target_sum = sum(nums)
# for p in partitioner(nums):
#     ir_gntr = ireduce(p)
#     tw = list(ittr.takewhile(lambda x: x in p_arr, ir_gntr))
#     print(tw)
#     if len(tw) > 1:
#         if sum([1 for i in ittr.chain.from_iterable(tw)]) == length:
#             results.append(tw)
#             print(tw)
#             break



sum(list(ireduce(tst2)))



tst2 = [[1], [3], [4], [5], [6], [7], [8], [2, 9]]
ntst = list(range(1, 10))
partitions = list(partitioner(ntst))
int_lists = partitioner(ntst)
# ntst = list(range(1, 6))
# partitions = list(partitioner(ntst))
# tst1 = [[1], [2, 3], [4]]
# [q for p in partitions for q in p]




def sorted_k_partitions(seq, k):
    """Returns a list of all unique k-partitions of `seq`.

    Each partition is a list of parts, and each part is a tuple.

    The parts in each individual partition will be sorted in shortlex
    order (i.e., by length first, then lexicographically).

    The overall list of partitions will then be sorted by the length
    of their first part, the length of their second part, ...,
    the length of their last part, and then lexicographically.
    """
    n = len(seq)
    groups = []  # a list of lists, currently empty

    def generate_partitions(i):
        if i >= n:
            yield list(map(tuple, groups))
        else:
            if n - i > k - len(groups):
                for group in groups:
                    group.append(seq[i])
                    yield from generate_partitions(i + 1)
                    group.pop()

            if len(groups) < k:
                groups.append([seq[i]])
                yield from generate_partitions(i + 1)
                groups.pop()

    result = generate_partitions(0)

    # Sort the parts in each partition in shortlex order
    result = [sorted(ps, key = lambda p: (len(p), p)) for ps in result]
    # Sort partitions by the length of each part, then lexicographically.
    result = sorted(result, key = lambda ps: (*map(len, ps), ps))

    return result

result = list()
nums = list(range(1, 6))
for n in nums:
    for m in sorted_k_partitions(nums, n):
        result.append(m)


i_res = [[j for j in ireduce(p)] for p in result]

p_res = list(partitioner(nums))
# Sort the parts in each partition in shortlex order
p_res = [sorted(ps, key = lambda p: (len(p), p)) for ps in p_res]
# Sort partitions by the length of each part, then lexicographically.
p_res = sorted(p_res, key = lambda ps: (*map(len, ps), ps))

i_res = [[j for j in ireduce(p)] for p in p_res]


# def partitioner(collection):
#     if len(collection) == 1:
#         yield [collection]
#         return
#     first = collection[0]
#     for smaller in partitioner(collection[1:]):
#         for n, subset in enumerate(smaller):
#             yield smaller[:n] + [[first] + subset]  + smaller[n+1:]
#         yield [[first]] + smaller
'''