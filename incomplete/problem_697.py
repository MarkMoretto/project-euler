
"""
Purpose: Project Euler problems
Date created: 2020-01-15
Contributor(s): Mark M.

ID: 697
Title: Randomly Decaying Sequence
URI: https://projecteuler.net/problem=697
Difficulty: ?

Status: Incomplete

Problem:
Given a fixed real number c, define a random sequence (Xn)n≥0 by the following
random process:
    X0 = c (with probability 1).
    For n > 0, Xn = Un * X(n-1) where U_n is a real number chosen at random
    between zero and one, uniformly, and independently of all previous
    choices (Um)m < n.

If we desire there to be precisely a 25% probability that X100<1, then this can
be arranged by fixing c such that log10c~=46.27.

Suppose now that c is set to a different value, so that there is precisely a
25% probability that X10000000<1.

Find log10(c) and give your answer rounded to two places after the decimal point.
"""


import numpy as np
from scipy import stats

# from cvxopt import blas, matrix, mul, div




def n_gen(s):
    n, incr = np.int32(1), np.int32(1)
    current = s
    while current >= 1.0:
        rnd = np.random.random()
        last = current
        current = np.multiply(last, rnd)
        n += incr
    yield n



def run_trial(start):
    return n_gen(start).__next__()

def successful_trial_count(results_list):
    tot = np.sum([1 if i < 100 else 0 for i in results_list])
    return np.float64(tot)


c = 1.85e46

N_TRIALS = 10000.0
N_RANGE = np.arange(0., N_TRIALS)

# res = [run_trial(c) for i in N_RANGE]
# n_success = successful_trial_count(res)

# n_success/np.log2(N_TRIALS)

def run_trials():
    res = [run_trial(c) for i in N_RANGE]
    
    n_success = successful_trial_count(res)
    return np.divide(n_success, N_TRIALS)

# run_trials()



res_arr = np.array(res)
print(f"Mean: {}\nVar: {}\nSt Dev: {}")
arr_stat = stats.describe(res)
# min_, max_ = arr_stat.minmax
# mean_ = arr_stat.mean
# stdev_ = res.std()

res_arr.var()


def eval_trial(value_list, n_threshold = 100):
    results_total = np.sum(value_list)
    if results_total < n_threshold:
        return 1
    return 0


class p697:
    def __init__(self, probability = float(0.25)):
        self.probability = probability

    def __trial_gen(self):
        current = self.c
        while current >= 1.0:
            rnd = np.random.random_sample()
            last = current
            current = np.multiply(last, rnd)
            yield 1

    def __iter_gen(start):
        return n_gen(start).__next__()

    def __eval_gen(self, value_list):
        results_total = np.sum(value_list)
        if results_total < n_threshold:
            return 1
        return 0

    def __update_c(self, value):
        self.c = np.float64(value)



### Chebyshev's inequality
# https://www.thoughtco.com/worksheet-for-chebyshevs-inequality-solutions-3126519

def min_deviation(mean, stdev, rng):
    lower, upper = min(rng), max(rng)
    lower_gap = abs(mean - lower)
    upper_gap = abs(mean - upper)
    min_gap = max(lower_gap, upper_gap)
    return min_gap / stdev


def chebyshev_ineq(mean, stdev, expected_range):
    k = min_deviation(mean, stdev, expected_range)
    return 1 - (1 / k ** 2)


# Eample 2
mu2 = 36
std2 = 2
range2 = [31, 41]

chebyshev_ineq(mu2, std2, range2) # 0.84


# Example 3
MINUTES = 60
mu3 = 3 * MINUTES
std3 = 10
range3 = [2 * MINUTES, 4 * MINUTES]

chebyshev_ineq(mu3, std3, range3) # ~0.97




