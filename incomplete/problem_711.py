
"""
Purpose: Project Euler problems
Date created: 2020-04-13

ID: 711
Title: Binary Blackboard
URI: https://projecteuler.net/problem=711
Status: Incomplete
Contributor(s): Mark Moretto

https://www.groundai.com/project/two-player-games-for-efficient-non-convex-constrained-optimization/1

Description:
    Oscar and Eric play the following game.

    First, they agree on a positive integer n, and they begin by writing its binary
    representation on a blackboard.

    They then take turns, with Oscar going first, to write a number on the
    blackboard in binary representation, such that the sum of all written numbers
    does not exceed 2n.
    
    The game ends when there are no valid moves left. Oscar wins if the number of
    1s on the blackboard is odd, and Eric wins if it is even.
    
    Let S(N) be the sum of all n≤2N for which Eric can guarantee winning, assuming
    optimal play.
    
    For example, the first few values of n for which Eric can guarantee winning
    are 1, 3, 4, 7, 15, 16. Hence S(4)=46.

    You are also given that S(12)=54532 and S(1234)≡690421393(mod1000000007).
    
    Find S(12345678). Give your answer modulo 1000000007.
"""

import numpy as np
import itertools as ittr
from itertools import combinations_with_replacement as cwr


def mod_check(num):
    return num % 1000000007 == 0


def bin_str(num):
    return bin(num).replace("0b","")


def bin_sum(binary_n_string):
    return sum(map(int, list(binary_n_string)))


def count_ones(num):
    cnt = 0
    while num:
        cnt += (num & 1)
        num >>= 1
    return cnt


def n_parity(N):
    parity = 0
    while N:
        parity = ~parity
        N = N & (N - 1)
    return parity


def format_print(token_string = "n, i, ni_sum, n_gap, i_ones, ones_cumsum", width=4):
    h = token_string.split(",")
    out = "".join([f"{{{i.strip()}:>{width}}}" for i in h])
    print(f'print(f"{out}")')

# # memoize decorator
# # @memoize
# def memoize(f):
#     h = {}
#     def g(*u):
#         if u in h:
#             return h[u]
#         else:
#             r = f(*u)
#             h[u] = r
#             return r
#     return g

# sum(map(int, list(bin(2).replace("0b",""))))

# n = 1
# two_n = 2 ** n
# rng = np.arange(n, two_n + 1)

# np.cumsum(np.arange(n, two_n + 1))



# tot_n = n

# ones_cumsum = 0
# for i in rng:
#     ni_sum = n + i
#     if i >= n and ni_sum <= two_n:
#         n_gap = i - n
#         i_ones = count_ones(i)
#         if n_parity(i_ones) < 0:
#             ones_cumsum += i_ones
#             print(f"{n:>4}{i:>4}{ni_sum:>4}{n_gap:>4}{i_ones:>4}{ones_cumsum:>4}")


# dcols = ["oscar","eric","tot N","ij sum","tot 1s"]
# dcols_len_dict = {k:len(k) + 2 for k in dcols}
# cols_len = sum(dcols_len_dict.values())

# msg = list()
# for i in rng:
#     tot_n = i
#     i_ones = count_ones(i)
#     tot_ones = i_ones
#     for j in rng:
#         tot_n += j
#         j_ones = count_ones(j)
#         if tot_n <= two_n:
#             curr_sum = i + j
#             tot_ones += j_ones
#             msg.append(f"{i:^7}{j:^6}{tot_n:^7}{curr_sum:^8}{tot_ones:^8}")
# for i in rng:
#     tot_n = i
#     i_ones = count_ones(i)
#     tot_ones = i_ones
#     for j in rng[::-1]:
#         tot_n += j
#         j_ones = count_ones(j)
#         if tot_n <= two_n:
#             curr_sum = i + j
#             tot_ones += j_ones
#             msg.append(f"{i:^7}{j:^6}{tot_n:^7}{curr_sum:^8}{tot_ones:^8}")

# print(f"{dcols[0]:^7}{dcols[1]:^6}{dcols[2]:^7}{dcols[3]:^8}{dcols[4]:^8}")
# print("-" * cols_len)
# print("\n".join(msg))


n = 3
two_n = 2 ** n
rng = np.arange(1, two_n + 1)


tot_ones = 0
n_sum = 0
i = n

# ddict = dict(oscar=[], eric=[])

# Seed initial n value

bin_ones = count_ones(i)
tot_ones += bin_ones
n_sum += i
n_gap = two_n - n_sum
i += 1



# Need to find best current score based on this and next move
# Cartesian product with n <= 2 ** n constraint
res = [[o, e] for o in rng for e in rng if sum([o, e]) <= two_n]

# np.array(np.meshgrid(rng, rng)).T.reshape(-1,4)
res2 = np.array(np.meshgrid(rng, rng)).T.reshape(-1,2)
res2 = np.where(sum(res2) <= two_n)

for m in res:
    oscar, eric = m[0], m[1]

    tot_ones = count_ones(i)
    o_ones = count_ones(oscar)
    e_ones = count_ones(eric)
    o_tot_ones = tot_ones + o_ones
    e_tot_ones = o_tot_ones + e_ones
    print(oscar, eric, o_ones, e_ones, o_tot_ones, e_tot_ones,)



for o in rng:
    for e in rng:
        if sum([o, e]) <= two_n:
            



while True:
    if n_gap < i:
        break
    else:
        optimal_i = i
        max_n = n_gap + 1
        for x in range(i, max_n):
            bin_ones = count_ones(x)
            if n_parity(bin_ones) and optimal_i < x:
                optimal_i = x
                tot_ones += bin_ones

        n_sum += x
        n_gap = two_n - n_sum
        i += optimal_i
        # ddict["eric"].append(n)

# ddict["oscar"].append(n)



# bin_ones = count_ones(i)
# print(f"{i}: {bin_str(i)}, {bin_ones}")
# tot += count_ones(i)
# n_sum += i
# n_gap = two_n - n_sum
# i += 1




# print(f"\nSum of all n: {tot}")
# print(f"\nn_sum final: {n_sum}")

