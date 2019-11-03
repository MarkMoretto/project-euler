
"""
Purpose: Project Euler problems
Date created: 2019-11-03
Contributor(s): Mark M.

ID: 6
Title: Sum square difference
URI: https://projecteuler.net/problem=6

Status: Complete!


Desc: 
    The sum of the squares of the first ten natural numbers is,
    1**2 + 2**2 + ... + 10**2 = 385
    
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)**2 = 55**2 = 3025
    
    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 − 385 = 2640.
    
    Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum.
"""

import numpy as np
from functools import reduce


def sum_square(n):
    base = 0
    for i in np.arange(1, n + 1):
        base = base + i**2
        yield base


def square_sum(n):
    base = np.zeros(n, dtype=np.int32)
    for i in np.arange(1, n + 1):
        base[i-1] += i
        yield np.sum(base) ** 2


def sq_diffs(n):
    # Max value of the sequences
    ssq = reduce(max, [i for i in sum_square(n)])
    sqs = reduce(max, [i for i in square_sum(n)])
    return sqs - ssq


if __name__ == '__main__':
    N = 100

    res = sq_diffs(N)
    msg = f'The difference between the sum of the squares of the first one'
    msg += f'hundred natural numbers\nand the square of the sum is: {res}'
    print(msg)





