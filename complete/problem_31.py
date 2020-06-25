
"""
Purpose: Project Euler
Date created: 2020-02-11
Updated: 2020-06-24

Contributor(s):
    Mark M.

ID: 31
URI: https://projecteuler.net/problem=31
"""

from array import array


def coin_combos(target, coin_array):
    count = array("L", [1] + ([0] * target))

    target += 1

    for coin in coins:
        for i in range(coin, target):
            count[i] += count[i-coin]
    return count[-1]


if __name__ == "__main__":

    COINS = array("L", [1, 2, 5, 10, 20, 50, 100, 200])

    TARGET_AMT = 200

    res = coin_combos(TARGET_AMT, COINS)

    print(res)