
"""
Purpose: Project Euler problems
Date created: 2020-04-13

ID: 711
Title: Binary Blackboard
URI: https://projecteuler.net/problem=711
Status: Incomplete
Contributor(s): Mark Moretto

Description:
    Oscar and Eric play the following game. First, they agree on a positive
    integer n, and they begin by writing its binary representation on a blackboard.
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



# sum(map(int, list(bin(2).replace("0b",""))))

n = 5
two_n = 2 ** n
rng = np.arange(n, two_n + 1)
# np.cumsum(np.arange(n, two_n + 1))
col_str = "n, i, ni_sum, n_gap, i_ones, ones_cumsum"
def format_print(token_string, width=4):
    h = token_string.split(",")
    out = "".join([f"{{{i.strip()}:>{width}}}" for i in h])
    print(f'print(f"{out}")')

tot_n = n

ones_cumsum = 0
for i in rng:
    ni_sum = n + i
    if i >= n and ni_sum <= two_n:
        n_gap = i - n
        i_ones = count_ones(i)
        if n_parity(i_ones) < 0:
            ones_cumsum += i_ones
            print(f"{n:>4}{i:>4}{ni_sum:>4}{n_gap:>4}{i_ones:>4}{ones_cumsum:>4}")


tot_ones = 0
n_sum = 0
i = n

ddict = dict(oscar=[], eric=[])

# Seed initial turn by Oscar

bin_ones = count_ones(i)
tot_ones += bin_ones
n_sum += i
n_gap = two_n - n_sum
i += 1


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
        ddict["eric"].append(n)

ddict["oscar"].append(n)



    bin_ones = count_ones(i)
    print(f"{i}: {bin_str(i)}, {bin_ones}")
    tot += count_ones(i)
    n_sum += i
    n_gap = two_n - n_sum
    i += 1




print(f"\nSum of all n: {tot}")
print(f"\nn_sum final: {n_sum}")

