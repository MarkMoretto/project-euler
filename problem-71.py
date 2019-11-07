
"""
Purpose: Project Euler problems
Date created: 2019-11-05
Contributor(s): Mark M.

ID: 71
Title: Ordered fractions
URI: https://projecteuler.net/problem=71
Difficulty: 10%

Status: Incomplete

Additional refs:
    mypy -> https://mypy.readthedocs.io/en/latest/

Desc: 
    Consider the fraction, n/d, where n and d are positive integers. If n<d
    and HCF(n,d)=1, it is called a reduced proper fraction.
    
    If we list the set of reduced proper fractions for d ≤ 8 in ascending order
    of size, we get:
    
    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
    5/7, 3/4, 4/5, 5/6, 6/7, 7/8
    
    It can be seen that 2/5 is the fraction immediately to the left of 3/7.
    
    By listing the set of reduced proper fractions for d ≤ 1,000,000 in
    ascending order of size, find the numerator of the fraction immediately to
    the left of 3/7.

"""

import typing as T
import numpy as np

f_vector = T.List[float]
i_vector = T.List[int]

def minmax(x: int, y: int) -> i_vector:
    return sorted([x, y])

#--
def vrange(start: int, stop: int = None, increment: int = 1) -> T.Iterator[int]:

    if increment == 0:
        increment = 1

    if increment > 0:
        if stop is None:
            stop = start
            start = 0

        while start < stop:
            yield start
            start += increment

    elif increment < 0:
        if stop is None:
            stop = 0

        elif start < stop:
            stop = start
            start = stop

        while start > stop:
            yield start
            start += increment

#-- Generate a list of integers
def range_gen(start: int, stop: int = None, increment: int = 1) -> f_vector:
    return [i for i in vrange(start, stop, increment)]

#-- Absolute value
def xABS(n: int) -> int:
    return n * -1 if ((n ^ 1) < 0) else n


def HCF(x: int, y: int) -> T.Iterator[int]:
    x, y = xABS(x), xABS(y)
    if x == 0:
        return y
    while y != 0:
        if x > y:
            x -= y
        else:
            y -= x
    return x

vHCF = np.vectorize(HCF, cache=False)


# def frac_gen(x, y):


#-- Set variables
#-- d = max_value, target = fraction to find, support = minimum fraction
d: int = int(1e2)
target: float = 3/7
support: float = 2/5


#-- Create two lists for numerators and denominators
numer = np.arange(1, int(d) + 1)
denom = np.arange(1, int(d) + 1)
X = np.arange(1, int(d) + 1)

for d in np.array_split(denom, 10):
    for n in np.array_split(numer, 10):


#-- Create vector of fraction strings
frac_str_grid = np.array([f'{n}/{d}' for n in numer for d in denom])


#--Generator



#-- Create fractions vector
#-- Conditions:
#--     1. n / d < 1
#--     2. n / d < target
#--     3. n / d > support

frac_vec = np.array([np.divide(n, d) for n in numer for d in denom \
                      if np.divide(n, d) < 1 \
                      and np.divide(n, d) < target \
                      and np.divide(n, d) > support])



hcf_vec = np.array([vHCF(n, d) for n in numer for d in denom])


#-- Reduce values to between support and target
max_val = max(qrs)
target_rc = frac_str_grid[np.where(qrs == max_val)]













