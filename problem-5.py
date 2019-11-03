
"""
Purpose: Project Euler problems
Date created: 2019-11-02

ID: 5
Title: Smallest multiple
URI: https://projecteuler.net/problem=5
Status: Incomplete

Contributor(s): Mark M.

Desc: 
    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.
    
    What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20?
"""

from functools import reduce
import numpy as np
import multiprocessing as mp
from multiprocessing.pool import ThreadPool

def prime_prefilter(iterable):
    return set(reduce(list.__add__, ([i, n//i] for i in iterable if n % i == 0)))


# def const_mod(x): return n % x
def const_mod(x, y): return np.mod(x, y)
v_const_mod = np.vectorize(const_mod)

is_zero = lambda mod: (((mod)^0)==0)
def const_mod(x, y): yield np.mod(x, y)


is_zero = lambda mod: (((mod)^0)==0)


sum(reduce(list.__add__, ([j, 0] for i in  mod_list for j in const_mod(12, i))))

# mod_primes = np.array([2, 3, 5, 7, 11, 13, 17, 19], dtype=np.int32)
mod_list = np.array([i for i in range(20, 1, -1)], dtype=np.int8)


n = 0
res = 0

while res == 0:
    n += 1
    if sum(reduce(list.__add__, ([j, 0] for i in  mod_list for j in const_mod(n, i)))) == 0:
        res += n

    if n % 1e6 == 0:
        print(f'Current n value: {n}')


with ThreadPool(processes=6) as tp:

    while res == 0:
    
        n += 1

        r_data = tp.apply_async(v_const_mod, (n, mod_list, ))

        if np.sum(r_data.get()) == 0:
            res += n


        if n % 1e5 == 0:
            print(f'Current n value: {n}')

    # if np.sum(v_const_mod(n, mod_list)) == 0:
    #     res += n

    if n % 1e5 == 0:
        print(f'Current n value: {n}')


with ThreadPool(processes=6) as pool:


