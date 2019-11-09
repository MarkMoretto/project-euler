
"""
Purpose: Project Euler problems
Date created: 2019-10-20

Contributor(s): Mark M.

ID: 679
URI: https://projecteuler.net/problem=679
Status: Complete
"""

from sys import getsizeof
from itertools import (
        combinations_with_replacement, permutations
        )


# import multiprocessing as mp
from multiprocessing.pool import ThreadPool


import numpy as np



import gc
gc.enable()


base = {'A','E','F','R'}
kwrds = ['FREE', 'FARE', 'AREA', 'REEF']


thisbytes = lambda x: [str.encode(i) for i in x]
bbase = thisbytes(base)
bkwrds = thisbytes(kwrds)



min_kwrd_len = min(map(len, kwrds))


### Iterable check
isiterable = lambda obj: True if obj.__iter__() else False

combinator = lambda x, n: [''.join(i) for i in combinations_with_replacement(x, n)]

def unique_with_repeat(iterable, n):
    tmp_str = ''.join(iterable)
    for i in combinations_with_replacement(tmp_str, n):
        for x in list(set([''.join(q) for q in permutations(''.join(i), n)])):
            yield x




#------------------------------------------------------
### multiprocessing/multithreading section

def count_keywords(n):
    gc.collect(2)
    for itm in unique_with_repeat(base, n):
        yield sum([1 for x in kwrds if x in itm])


def f_mp(n):
    gc.collect(2)
    print(f'Current n value: {n}\n')
    for i in count_keywords(n):
        if i == len(kwrds):
            return 1



def f(n, num_processes=None):
    if num_processes is None:
        num_processes = mp.cpu_count() - 1
    base_index=len(kwrds)
    tp = ThreadPool(num_processes)

    im = tp.imap_unordered(f_mp, range(base_index, n+1))
    return sum([v for v in im if not v is None])



# f(9)
kwrd_count = f(15)













# def f_mp(n):
#     tot_count = 0
#     print(f'Current n value: {n}\n')
#     value_set = [i for i in unique_with_repeat(base, n)]
#     print(f'Length of unique value set for n {n}: {len(value_set)}\n')
#     for ele in value_set:
#         kwrd_count = sum([1 for i in kwrds if i in ele])
#         if kwrd_count == len(kwrds):
#             tot_count += 1
#     return tot_count




# def f(n):
#     base_index=len(kwrds)
#     tot_count = 0
#     while base_index <= n:
#         print(f'Current n value: {base_index}')
#         value_set = [i for i in unique_with_repeat(base_str, base_index)]
#         print(f'Length of unique value set: {len(value_set)}'
#         for ele in value_set:
#             kwrd_count = sum([1 for i in kwrds if i in ele])
#             if kwrd_count == len(kwrds):
#                 tot_count += 1
#         gc.collect(2)
#         base_index += 1
#     return tot_count
