
"""
Purpose: Project Euler
Date created: 2020-08-10

Problen Number: 367
Name: Bozo sort
URL: https://projecteuler.net/problem=367

Contributor(s):
    Mark M.
"""

import random
from itertools import permutations
from statistics import mean


def is_sorted_incr(L):
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            return False
    return True

def bozosort(L):
    q = 0
    while not is_sorted_incr(L):
        i, j = int(len(L)*random.random()), int(len(L)*random.random())
        L[i], L[j] = L[j], L[i]
        q += 1
    return q


def bozosort3(L):
    q = 0
    sample_rng = list(range(len(L)))
    while not is_sorted_incr(L):
        i, j, k = random.sample(sample_rng, 3)
        L[i], L[j], L[k] = L[j], L[i], L[k]
        q += 1
    return q


def avg_run(N, n_trials=100):
    nums = list(range(1, N + 1))
    results = []
    for _ in range(n_trials):
        tmp = []
        for p in permutations(nums, N):
            tmp.append(bozosort3(list(p)))
        results.extend(tmp)
    return mean(results)

avg_run(4)

avg_run(11)



