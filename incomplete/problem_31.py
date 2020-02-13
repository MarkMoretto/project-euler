
"""
Purpose: Project Euler
Date created: 2020-02-11
Contributor(s):
    Mark M.

ID: 31
URI: https://projecteuler.net/problem=31
"""

# import itertools
# import functools

# def list_mul(a, b):
#     b = [b]
#     return [[sum(x * y for x, y in zip(a_r, y_c)) for y_c in zip(*b)] for a_r in a]


coins = [1, 2, 5, 10, 20, 50, 100, 200]
coins = coins[:-1][::-1] # We can add on the single 200 at the start
coindict = {k:v for k, v in enumerate(coins)}
target = 200

max_iters_dict = {c:int(target / c) for c in coins}

counter = 1 # Initial value accounts for coin value of 200
results = []
frmt_wt = list("{:0>7}".format(12))
weights = [0] * len(coins)

"".join([str(i) for i in weights])


weights = [10,2,0,0,0,0,0,]
result = [0] * len(coins)
for k, c in coindict.items():
    for idx, s in enumerate(weights):
        if s <= max_iters_dict[c]: # Check max iterations dictionary
            result[idx] = coindict[idx] * s # Multiply seed by coindict value

"".join([str(i) for i in weights])


# Increment weight set




