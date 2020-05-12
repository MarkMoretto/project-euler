
"""
Purpose: Projec Euler exercise
Date created: 2020-05-02

Problen Number: 710
Name: One Million Members
URL: https://projecteuler.net/problem=710


Contributor(s):
    Mark M.

Description:
    On Sunday 5 April 2020 the Project Euler membership first exceeded one million
    members. We would like to present this problem to celebrate that milestone.
    Thank you to everyone for being a part of Project Euler.
    
    The number 6 can be written as a palindromic sum in exactly eight different ways:
    	(1,1,1,1,1,1),
    	(1,1,2,1,1),
    	(1,2,2,1),
    	(1,4,1),
    	(2,1,1,2),
    	(2,2,2),
    	(3,3),
    	(6)
    
    We shall define a twopal to be a palindromic tuple having at least one element with
    a value of 2. It should also be noted that elements are not restricted to single digits.
    
    For example, (3,2,13,6,13,2,3), is a valid twopal.
    
    If we let t(n) be the number of twopals whose elements sum to n, then it can be seen
    that t(6)=4:
    	(1,1,2,1,1),
    	(1,2,2,1),
    	(2,1,1,2),
    	(2,2,2)
    
    Similarly, t(20)=824.
    
    In searching for the answer to the ultimate question of life, the universe, and
    everything, it can be verified that t(42)=1999923, which happens to be the first
    value of t(n) that exceeds one million.
    
    However, your challenge to the "ultimatest" question of life, the universe, and
    everything is to find the least value of n>42 such that t(n) is divisible by one
    million.   

from functools import reduce
def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i]for i in range(1, int(n**0.5) + 1) if n % i == 0)))    
"""

# import numpy as np
# import numba
#from numba import cuda
from math import log10, ceil
#import cupy as cp

# numba.config.THREADING_LAYER="safe" # Requires Intel TBB to be installed
# numba.config.THREADING_LAYER="tbb"

import itertools as ittr



class DataSet:
    def __init__(self, sequence_of_numbers):
        self._data = sequence_of_numbers




#A002113 = sorted(ittr.chain(map(lambda x:int(str(x)+str(x)[::-1]), range(1, 10**3)), map(lambda x:int(str(x)+str(x)[-2::-1]), range(10**3))))

def is_palindrome(n_string):
    return n_string == n_string[::-1]




# @numba.vectorize(['float64(float64, float64, float64)'], target='parallel')
# @numba.vectorize(['u8(u8, u8, u8)'])
# def trunc(a, amin, amax):
#     if a < amin:
#         a = amin
#     elif a > amax:
#         a = amax
#     return a



# @numba.njit(fastmath=True)
# def reverser(num):
#     """Reverse an integer.
#     Assumes only positive integer being passed."""

#     # Remainder and reverse
#     rem = 0
#     rev = 0
#     while num > 0:
#         rem = num % 10
#         rev = (rev * 10) + rem
#         num = num // 10

#     return rev




# @numba.guvectorize(["(u4[:], u4[:])", "(u8[:], u8[:])"], "()->()", nopython=True)
# @numba.njit(["u4[:](u4[:])", "u8[:](u8[:])"], target="cuda")
# @numba.generated_jit(nopython=True)
# def n_to_vec(n):
#     """"""
#     # Length of numeric variable
#     n_digits = int(ceil(max(log10(n))))

#     for i in numba.prange(n_digits)
    # Return numeric value as vector of digits.
    # y[:] = n // 10 ** cp.arange(n_digits)[:, None] % 10
    # return n // 10 ** cp.arange(n_digits)[:, None] % 10


# n1=433625644
# n_digits = cp.ceil(cp.max(cp.log10(n1))).astype(int)
# n1 // 10 ** cp.arange(n_digits)[:, None] % 10

# n1 = 433625644
# n2 = cp.array(n1)
# n_to_vec(n2)
# reverser(n1)


# @numba.njit
# def is_palindrome(vec):
#     q = cp.array(vec, dtype=cp.uint)
#     return q == q[::-1]

# Create preset
# xyz = cp.arange(3, 41)
# max_n_dict = {n:cp.power(10, n-1)-1 for n in range(2, 40)}


def n_sum(n_string):
    return sum(map(int, list(n_string)))



################################################################
## Testing

n=20
power = pow(10, n - 1)
g_palind = chain(map(lambda x: (str(x)+str(x)[::-1]), range(1, power)), map(lambda x: (str(x)+str(x)[-2::-1]), range(power)))
g_no0 = ittr.filterfalse(lambda x: "0" in x, g_palind)
g_sum6 = ittr.filterfalse(lambda x: n_sum(x) != 6, g_no0)
g_has2 = ittr.filterfalse(lambda x: not "2" in x, g_sum6)
res = list(g_has2)


def pdromes(power):
    return ittr.chain(map(lambda x: (str(x)+str(x)[::-1]), range(1, power)), \
                          map(lambda x: (str(x)+str(x)[-2::-1]), range(power)))

def t(n):
    power = pow(10, n - 1)
    g_palind = ittr.chain(map(lambda x: (str(x)+str(x)[::-1]), range(1, power)), \
                          map(lambda x: (str(x)+str(x)[-2::-1]), range(power)))

    g_1= ittr.filterfalse(lambda x: "0" in x, g_palind)
    g_2 = ittr.filterfalse(lambda x: not "2" in x, g_1)
    g_3 = ittr.filterfalse(lambda x: n_sum(x) != n, g_2)

    return len(list(g_3))

#@numba.njit(fastmath=True, parallel=True)
# def t(n):

#     # Always can have a string of 1s
#     two_count = 1
#     i = 1
#     #max_n = eval(f"int(1e{n-1}) - 1")
#     max_n = cp.power(10, n-1)-1
#     while i <= max_n:
#         j = f"{i}"
#         if "2" in j and not "0" in j:
#             if n_sum(j) == 6:
#                 if is_palindrome(j):
#                     two_count += 1
#         i += 1
#     return two_count

assert (t(6) == 4),"Test err: t(6)"
assert (t(20) == 824),"Test err: t(6)"





# l = np.array([43365644])

# n1=43365644
# base = 10
# n_digits = np.ceil(np.max(np.log(n1) / np.log(base))).astype(int)
# n1 // 10 ** np.arange(n_digits)[:, None] % 10


# def n_to_vec(n, base=10):

#     # Length of numeric variable
#     n_digits = cp.ceil(cp.max(cp.log(n) / cp.log(base))).astype(int)

#     # Return numeric value as vector
#     return n // 10 ** cp.arange(n_digits)[:, None] % 10









# n1 = 12345

# def neg_reverser(num):
#     # Sign indicator
#     wasneg = False

#     # Remainder and reverse
#     rem, rev = 0, 0

#     if num < 0:
#         wasneg = True
#         num *= -1


#     while num > 0:
#         rem = num % 10
#         rev = (rev * 10) + rem
#         num = num // 10
    
#     if wasneg:
#         rev *= -1

#     return rev


# reverser(n1)





