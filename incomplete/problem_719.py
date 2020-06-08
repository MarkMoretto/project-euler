
"""
Purpose: Project Euler exercises
Date created: 2020-06-06

Problen Number: 719
Name: Number Splitting
URL: https://projecteuler.net/problem=719

Contributor(s):
    Mark M.

Logging:
    https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook
"""

__all__ = ["Element", "split_eval", "fsplitter", "sq_eval"]

from os import chdir
PROJ_DIR = r"C:\Users\Work1\Desktop\Info\PythonFiles\project-euler\incomplete"
chdir(PROJ_DIR)


import logging

logger = logging.getLogger('problem_719')

fh = logging.FileHandler(rf"{PROJ_DIR}\logs\pe-719.log")
fh.setLevel(logging.DEBUG)

# Console log handler
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')
formatter.datefmt='%H:%M:%S'
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)




# import numba
import numpy as np

from math import sqrt
import itertools as ittr
from functools import lru_cache

# import multiprocessing as mp
import concurrent.futures as ccf
# from multiprocessing.pool import ThreadPool

# from functools import lru_cache


# Dict = numba.typed.Dict


# Namedtuple to structure the data
#from collections import namedtuple
#Element = namedtuple("Element", "n, nstr, nroot")

class Element:
    """
    Class to hold calculated results from square root evaluation.
    
    Mimics namedtuple without additional import:
        --> Element = namedtuple("Element", "n, nstr, root")
    """
    def __init__(self, n, root):
        self.n = (n).__int__()
        self.nstr = (n).__str__()
        self.root = root

    def __repr__(self):
        nm=self.__class__.__name__
        return f"<{nm} ({self.n}) />"


def fsplitter(s):
    '''Float results'''
    slen = len(s)
    for i in range(1, slen):
        start = s[0:i]
        end = s[i:]
        yield [float(start), float(end)]
        for split in fsplitter(end):
            result = [float(start)]
            result.extend(split)
            yield result



def split_eval(element: Element):
    """Iterate splitter and determine if perfect root found."""
    for el in fsplitter(element.nstr):
        if np.sum(el) == element.root:
            return True
    return False




def sq_eval(n):
    i = 9
    while i <= n:
        i += 1
        tmp_sqrt = np.sqrt(i)
        if np.mod(tmp_sqrt, 1) == 0.0:
            # Returns named tuple (n, nstr, nroot)
            yield Element(n = i, root = tmp_sqrt)



def sqrt_eval(num):
    tmp_sqrt = np.sqrt(num)
    if np.mod(tmp_sqrt, 1) == 0.0:
        # Returns named tuple (n, nstr, nroot)
        return Element(n = num, root = tmp_sqrt)



# def T(N):
#     sq = sq_eval(N)
#     tot = 0
#     for element in sq:
#         if split_eval(element) == True:
#             tot += element.n
#     return tot

def T(N):

    min_n, max_n = 10, N+1
    rng = range(min_n, max_n)

    tot = 0
    with ccf.ThreadPoolExecutor(max_workers=50) as executor:
        future_dict = {executor.submit(sqrt_eval, i):f"{i}" for i in rng}
        for future in ccf.as_completed(future_dict):
            current = future_dict[future] # The value, or current i
            try:
                element = future.result()
                if not element is None:
                    if split_eval(element) == True:
                        tot += element.n
            except Exception as exc:
                print(f'Thread {current} generated an exception: {exc}')

    return tot




if __name__ == "__main__":

    N = int(10**6)
    result = T(N)
    print(result)


    # try:
    #     # Set worker count based on # of CPUs, but don't go nuts.
    #     workers = mp.cpu_count() - 1
    # except NotImplementedError:
    #     workers = 1


    # rng = list(range(2, 11))

    # # k = 100
    # total = []


    # # with mp.Pool(processes=workers) as pool:
    # with ThreadPool(processes = workers) as pool:
    #     # total = pool.map(run_ulam, range(2, 11))

    #     multiple_results = [pool.apply_async(run_ulam, (i,)) for i in range(2, 11)]
    #     # print([res.get() for res in multiple_results])
    #     for res in multiple_results:
    #         total.append(res.get())

    #     print(f"The final sum is: {sum(total)}")


# ns = '6724'

# # https://stackoverflow.com/questions/48734357/how-to-get-every-possible-list-of-substrings-from-a-string-in-python
# # https://docs.python.org/3.7/library/itertools.html

# @numba.vectorize
# def n_sum(iterable):
#     """
#     Sum the total of an iterable of numeric string values.

#     Examples:
#         n_sum('123') == 6
#         n_sum(['6', '724']) == 730
#     """
#     return sum(map(int, list(iterable)))

# @numba.vectorize(["float32(int32)"], nopython=True)
# def SQRT(num):
#     return np.float32(num**0.5)


# @numba.guvectorize(["void(int32[:], int32[:])"], "(n)->()")
# def n_sum(arr, out):
#     """
#     Sum the total of an iterable of numeric string values.
#     """
#     for i in numba.prange(len(arr)):
#         out[0] = out[0] + arr[i]


# tst1 = np.array([6, 724], dtype=np.int32)
# result = np.array([0], dtype=np.int32)
# n_sum(tst1, result)


# n1 = 6724


# From project-euler\incomplete\problem_118.py
# @numba.guvectorize(["void(int32[:], int32[:])"], "(n)->()")
# def splitter(s):
#     tmpout=[]
#     for i in numba.prange(1, len(s)):
#         start = s[0:i]
#         end = s[i:]
#         tmpout.append([int(start), int(end)])
#         for split in splitter(end):
#             result = [int(start)]
#             result.extend(split)
#             tmpout.append(result)
#     return tmpout


# splitter('6724')

# sp1 = splitter('6724')
# n_sum(['6', '724'])


# squares_kv = {}
# @numba.njit
# def perfect_squares(max_value):
#     i = np.int32(9)
#     incr_ = np.int32(1)
#     while i <= max_value:
#         i = i + incr_
#         tmp_sqrt = SQRT(i)
#         if tmp_sqrt % 1 == 0.0:
#             d[i] = tmp_sqrt
# res = perfect_squares(d)



# def splitter(s):
#     '''String results'''
#     slen = len(s)
#     for i in range(1, slen):
#         start = s[0:i]
#         end = s[i:]
#         yield [start, end]
#         for split in splitter(end):
#             result = [start]
#             result.extend(split)
#             yield result


# def isplitter(s):
#     '''Integer results'''
#     slen = len(s)
#     for i in range(1, slen):
#         start = s[0:i]
#         end = s[i:]
#         yield [int(start), int(end)]
#         for split in isplitter(end):
#             result = [int(start)]
#             result.extend(split)
#             yield result



# def fsplitter(s):
#     '''Float results'''
#     slen = len(s)
#     for i in range(1, slen):
#         start = s[0:i]
#         end = s[i:]
#         yield [float(start), float(end)]
#         for split in fsplitter(end):
#             result = [float(start)]
#             result.extend(split)
#             yield result


# @lru_cache(500)
# def perfect_squares(d, n):
#     i = 9
#     while i <= n:
#         i += 1
#         tmp_sqrt = np.sqrt(i)
#         if np.mod(tmp_sqrt, 1) == 0.0:
#             d[f"{i}"] = tmp_sqrt



# With concurrent futures


# @lru_cache(500)
# def sq_eval(n, other: float = 0.0) -> int:
#     tmp_sqrt = np.sqrt(n)
#     if np.mod(tmp_sqrt, 1) == other:
#         return tmp_sqrt


# def perfect_squares_ccf(d: dict, n: int):

#     rng = range(10, n+1)

#     with ccf.ThreadPoolExecutor(max_workers=10) as executor:
#         future_dict = {executor.submit(sq_eval, i):f"{i}" for i in rng}
#         for future in ccf.as_completed(future_dict):
#             current = future_dict[future]
#             try:
#                 res = future.result()
#                 if not res is None:
#                     d[f"{current}"] = res
#             except Exception as exc:
#                 print(f'Thread {current} generated an exception: {exc}')


# squares_kv = {}
# perfect_squares_ccf(squares_kv, 10000)

# N = 10000 # 10**4

# squares_kv = {}
# perfect_squares(squares_kv, N)


# res = set()
# for k, v in squares_kv.items():
#     for el in fsplitter(k):
#         if np.sum(el) == v:
#             res.add(k)


# sum(map(int, res))
