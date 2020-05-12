
"""
Purpose: Projec Euler 713
Date created: 2020-04-26

Problen Number: 713
Name: Turán's water heating system
URL: https://projecteuler.net/problem=713

Contributor(s):
    Mark M.

More info:
    https://math.stackexchange.com/questions/1822342/minimum-number-of-flips-to-guarantee-heads

Description:
    Turan has the electrical water heating system outside his house in a shed. The
    electrical system uses two fuses in series, one in the house and one in the shed.
    (Nowadays old fashioned fuses are often replaced with reusable mini circuit breakers,
    but Turan's system still uses old fashioned fuses.) For the heating system to work,
    both fuses must work.
    
    Turan has N fuses. He knows that m of them are working and the rest are blown. 
    However, he doesn't know which ones are blown. So he tries different combinations
    until the heating system turns on.
    
    We denote by T(N,m) the smallest number of tries required to ensure the heating
    system turns on.
    
    T(3,2) = 3 and T(8,4)=7.
    
    Let L(N) be the sum of all T(N,m) for 2≤ m ≤ N.
    
    L(10^3) = 3281346
    
    Find L(10^7). 
"""

# import scipy.stats as ss
# import scipy.special as ssp
import numpy as np
import cupy as cp
import numba

# Ntest = 3
# mtest = 2

# Binomial probability; Either yes or no, on or off.
p = cp.float64(0.5)
q = cp.float64(1 - p)

# H/T https://gist.github.com/rougier/ebe734dcc6f4ff450abf

@numba.njit
def min_(a, b):
    if a < b:
        return a
    return b

@numba.njit(fastmath=True)
def binom(n, k):
    if not 0 <= k <= n: return 0
    b = 1
    mink = min_(k, n-k)
    for t in range(mink):
        b *= n
        b /= t + 1
        n -= 1
    return b

@numba.njit(fastmath=True)
def T(N, m):
    # Number of required successes.
    x = N - m
    tot = 0
    n = 1

    while tot <= p:
        n += 1
        res = binom(n, n-x) * (p**x) * (q ** (n - x))
        tot += res
    return n


@numba.njit(fastmath=True, parallel=True)
def L(N):
    res = 0
    N += 1
    # rng = np.arange(2, N)
    for n in numba.prange(2, N):
        for m in numba.prange(2, N):
            if m < n:
                res += T(n, m)
    return res


if __name__ == "__main__":
    res = L(1000)
    print(res)



# def T(N, M=0, p = 0.5):
#     return ss.binom.ppf(0.995, N, p)

# def L(N):
#     N += 1
#     rng = np.arange(2, N)
#     return sum([T(j, i) for i in rng for j in rng if i < j])




N = 8
m = 4
x = N - m # Number of required successes.
p = 0.5
q = 1 - p


tot = 0
n = 0
while tot <= p:
    n += 1
    res = ssp.binom(n, n-x) * (p**x) * (q ** (n - x))
    tot += res



"""
rng = np.arange(2, N)
for n in rng:
    for m in rng:
        res += T(n, m)

dists = {}
tot = 0
for n in range(2, N+1):
    # res = ssp.binom(n, i) * (p**i) * (q ** (n - i))
    res = ssp.binom(n, n-x) * (p**x) * (q ** (n - x))
    #res = ssp.binom(n-1, n-x) * (p**x) * (q ** (n - x))
    # res = ((1 - p)**(n - 1))*p
    # res = ssp.binom(n, n-i) * (p**i) * (q ** (n - i))
    dists[n] = round(res, 12)
    tot += res
tot = round(tot, 4)

sum([v for k, v in dists.items()])
sum([v for k, v in dists.items() if k <= 4])
sum([v for k, v in dists.items() if k <= 5])
sum([v for k, v in dists.items() if k <= 6])
sum([v for k, v in dists.items() if k <= 7])

# The Negative Binomial Distribution


x = np.arange(ss.geom.ppf(0.01, p), ss.geom.ppf(0.99, p))
ss.geom.pmf(x, p)


mu = N * p
var = N * p * p
z_statistic = ss.norm.ppf(.99)
def calc_n(N, p, conf=0.99):
    z_statistic = ss.norm.ppf(.99)
    z_statistic * np.sqrt(var) + (mu - p)

# ssp.binom(N - 1, m - 1) * (p ** m) * ((1 - p) ** (N - 2))
N = 40
mu = N * p
var = N * p * p
z_statistic = ss.norm.ppf(.90)
z_statistic * np.sqrt(var) + (mu - p)



n = 20
r = 4
p = 0.02
q = 1 - p

dists = {}
tot = 0
for i in range(n+1):
    res = ssp.binom(n, i) * (p**i) * (q ** (n - i))
    # res = ssp.binom(n, n-i) * (p**i) * (q ** (n - i))
    dists[i] = round(res, 12)
    tot += res
tot = round(tot, 4)


dist_mean = sum(map(lambda x: x[0] * x[1], dists.items()))
dist_mean_2 = n * p
dist_stdev = (n * p * q) ** (1/2)
print(f"The distribution mean is: {dist_mean:.4f}")




# N = 1000
# rng_m = np.arange(2, N)
# # rng_n = np.arange(2, N + 1)
# # matrix = [T(n,m) for n in rng_n for m in rng_m if m <= n]
# # tot = sum(matrix)
# matrix = [T(n,m) for n in rng_n]
# tot = sum(matrix)








# Possible outcomes
N = 3
m = 2
p = 1/2
k = N - m

"""
"""
Bag has 11 chips:
    6 red
    4 blue
    7 white
What is probability of drawing a red chip at least three out of five times?
"""
"""
n = 5
r = 3
p = 6/17

tot = 0
for i in range(r, n+1):
    tot += ssp.binom(n, i) * (p**i) * ((1-p) ** (n - i))
tot = round(tot, 3)


# https://saylordotorg.github.io/text_introductory-statistics/s08-03-the-binomial-distribution.html
n = 5
r = 4
p = 0.17
q = 1 - p

dists = {}
tot = 0
for i in range(0, n+1):
    res = ssp.binom(n, n-i) * (p**i) * (q ** (n - i))
    dists[i] = round(res, 4)
    tot += res
tot = round(tot, 4)


dist_mean = sum(map(lambda x: x[0] * x[1], dists.items()))
dist_mean_2 = n * p
dist_stdev = (n * p * q) ** (1/2)
print(f"The distribution mean is: {dist_mean:.4f}")



"""
"""
ssp.binom(3,1)

ssp.binom(8,4)*((7+1) * (0.5**7))

mean, var, skew, kurt = ss.binom.stats(N, p, moments='mvsk')

ss.binom.ppf(0.99, N, p)
ss.binom.ppf(0.99, N, p)
"""
"""

# https://www.real-statistics.com/binomial-and-related-distributions/binomial-distribution/
N = 10
m = 4
p = 1/6 # Probability of unbiased die landing on a face.

ssp.binom(N, m) * ((p**m)*((1-p)**(N-m)))


# https://www.real-statistics.com/binomial-and-related-distributions/binomial-distribution/
n = 20
p = 0.25
x = np.arange(ss.binom.ppf(0.01, n, p), ss.binom.ppf(0.99, n, p))

ss.binom.pmf(x, n, p)
"""


