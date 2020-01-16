
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
Given a fixed real number c, define a random sequence (Xn)n≥0

by the following random process:
    X0=c (with probability 1).
    For n>0, Xn=UnXn−1 where Un is a real number chosen at random between zero 
    and one, uniformly, and independently of all previous choices (Um)m<n.

If we desire there to be precisely a 25% probability that X100<1, then this can
be arranged by fixing c such that log10c≈46.27.

Suppose now that c is set to a different value, so that there is precisely a
25% probability that X10000000<1.

Find log10(c) and give your answer rounded to two places after the decimal point.
"""

import random
import numpy as np
from scipy import stats

# from cvxopt import blas, matrix, mul, div





def n_gen(s):
    n, incr = np.float64(1), np.float64(1)
    current = s
    while current >= 1.0:
        rnd = np.random.random_sample()
        last = current
        current = np.multiply(last, rnd)
        n += incr
    yield n

def run_trial(start):
    return n_gen(c).__next__()




c = np.float64(1e100)

N_TRIALS = 1000000
N_RANGE = np.arange(0, N_TRIALS)

res = [run_trial(c) for i in N_RANGE]
arr_stat = stats.describe(res)
# min_, max_ = arr_stat.minmax
# mean_ = arr_stat.mean
# stdev_ = res.std()

#Dice average
dice_res = [np.random.randint(1, 7) for i in N_RANGE]
dice_stat = stats.describe(dice_res)
#TODO: Probability of convergence



