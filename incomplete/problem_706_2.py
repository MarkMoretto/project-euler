
"""
Purpose: Projec Euler 706
Date created: 2020-04-25

https://projecteuler.net/problem=706

Contributor(s):
    Mark M.
"""

from collections import Counter


import numpy as np
import pandas as pd
import numexpr as ne

from dask.distributed import Client, progress

# import numba
pd.set_option("compute.use_numexpr", True)
pd.set_option("mode.chained_assignment", None)

ne.set_num_threads(16)

M = 1000000007



def all_substrings(input_string):
  length = input_string.__len__()
  return [f"{int(input_string[i:j+1])}" for i in range(length) for j in range(i, length)]



# Get list of numbers divisible by 3
d = 6
dx = d - 1
min_n = np.int64(10 ** dx)
max_n = np.int64(10 ** d)
rng = np.arange(min_n, max_n)


# Max number of possible mod 3 values
df = pd.DataFrame(columns=["n", "res",])
df["n"] = np.arange(int(10**5), dtype=np.int32)
df["res"] = np.bool_
df.eval("res = n % 3 == 0", inplace=True)

df3 = df.loc[df.loc[:,"res"] == True, :]
df3["ncat"] = df3["n"].astype(str)

# df3.memory_usage(deep=True) / (2**8 * 2**8)



def mergesum(dataframe):
    return df3.merge(dataframe, how="inner", left_on="ncat", right_on="num").loc[:,"freq"].sum()

def mod3(obj):
    return ne.evaluate(f"{obj} % 3 == 0")

def f(n):
    ss = all_substrings(n)
    freq_df = pd.DataFrame(Counter(ss).items(), columns=["num", "freq"])
    return mod3(mergesum(freq_df))


def eval_f(n):
    return 1 if mod3(n) else 0

# f("2573") == 3


d = 6
min_n = np.int64(10 ** (d - 1))
max_n = np.int64(10 ** d)
rng = np.arange(min_n, max_n)

results = sum([1 for i in rng if f(f"{i}")])





def mod3(obj):
    return obj % 3 == 0

def mod_(a, m):
    return (a % m + m) % m

'''
# def subslices(s):
#     xlen = len(s) + 1
#     outset = set()
#     workset = set()
#     for i in range(n_len):
# [workset.add(int(s[i:j])) for j in range(i, xlen) for i in range(xlen) if i < j]
#     return workset

# ss = "100234"
# xlen = len(ss) + 1
# workset = set()
# [workset.add(int(ss[i:j])) for j in range(i, xlen) for i in range(1,xlen) if i < j]
# [int(ss[i:j]) for i in range(xlen) for j in range(i, xlen) if i < j and int(ss[i:j]) > 0]

# def slices(s):
#     """Return only unique substrings of a numeric string."""
#     n_len = len(s) + 1
#     outset = set()
#     workset = set()
#     for i in range(n_len):
#         [workset.add(int(j) for j in range(i, n_len) if i < j]
#         outset.update(workset)
#     return outset

# slices("2573")
# slices("100234")
'''

def f(iterable):
    res = np.uint64(0)
    n_len = len(iterable) + incr
    rng1 = np.arange(n_len, dtype=np.uint64)
    for i in rng1:
        rng2 = np.arange(i, n_len, dtype=np.uint64)
        for j in rng2:
            if i < j and mod3(iterable[i:j]):
                res += incr
    return np.uint64(res)

# sample = "2573"
# f(sample)


abc = np.array([i for i in sample])
xyz = np.array("".join(abc[:2]), dtype = np.uint64)


def F(d):
    M = 1000000007
    d2 = d - 1
    i = np.uint64(10 ** d2)
    max_n = np.uint64(10 ** d)
    tot = 0
    while i < max_n:
        if mod3(f(str(i))):
            tot += incr
        i += incr
    return tot % 1000000007

F(2)
F(6)



sample = "2573"
abc = np.array(list(sample))
n_len = abc.size + 1
for i in range(n_len):
    for j in range(i, n_len):
        if i < j:
            xyz = np.array("".join(abc[i:j]), dtype = np.uint64)
            if xyz % 3 == 0:
                print(1)

mainset = set()

s = "100001"
n_len = len(s) + 1

nset = set()
for i in range(n_len):
    for j in range(i, n_len):
        if i < j:
            nset.add(int(s[i:j]))



mainset.update(nset)


if len(mainset) == 0:
    mainset = nset
else:
    mainset.add(nset.difference(mainset))
mainset = mainset.union(nset)

