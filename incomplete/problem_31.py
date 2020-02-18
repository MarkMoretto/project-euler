
"""
Purpose: Project Euler
Date created: 2020-02-11
Contributor(s):
    Mark M.

ID: 31
URI: https://projecteuler.net/problem=31
"""
import gc
import itertools
import numpy as np
# import functools
gc.enable()

coins = np.array([1, 2, 5, 10, 20, 50, 100, 200], dtype=np.float64)

if __name__ == "__main__":

    # Drop 200; Add initial value to count
    coins = coins[:-1][::-1]
    coindict = {k: v for k, v in enumerate(coins)}
    target = np.float64(200)

    max_iters_dict = {c: int(target / c) for c in coins}

    ranges = [eval(f"range(0, {i+1}, 1)") for i in max_iters_dict.values()]
    # output_list = list(itertools.product(*ranges))

    # base = [0] * len(coins)
    # weights = base.copy()

    counter = 1
    gc.collect()

    rngs = itertools.product(*ranges)

    for wts in rngs:
        res = np.dot(coins, np.array(wts))
        # res = sum([coindict[i] * wt for i, wt in enumerate(wts)])
        if res == target:
            counter += 1

    print(f"The total count is: {counter}")

    # res = 0
    # for i, wt in enumerate(weights):
    #     res += (coindict[i] * wt)
    #     if res == 200:
    #         counter += 1

    # # Increment weights
    # while True:
    #     for i, w in enumerate(weights, 1):
    #         c = coindict[i-1] # Get first coin
    #         if w < max_iters_dict[c]: # If wt less than max
    #             weights[i-1] += 1
    #             break
    #         else:
    #             weights[i] += 1
