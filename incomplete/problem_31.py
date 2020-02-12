
"""
Purpose: Project Euler
Date created: 2020-02-11
Contributor(s):
    Mark M.

ID: 31
URI: https://projecteuler.net/problem=31
"""

import itertools
import functools

coins = [1, 2, 5, 10, 20, 50, 100, 200]
coins = coins[:-1] # We can add on the single 200 at the start
coindict = {k:v for k, v in enumerate(coins)}
target = 200

max_iters_dict = {c:int(target / c) for c in coins}

counter = 0
resulta = list



int_list = [i for i in range(max_iters + 1)][::-1]
tmp = [i for i in itertools.product(int_list, coins)]


# Create matrix
matrix = []
for i in range(5):
    tmp = list()
    for j in range(5):
        tmp.extend([i * j])
    matrix.append(tmp)
