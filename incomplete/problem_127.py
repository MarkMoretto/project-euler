
"""
Purpose: Project Euler exercises
Date created: 2020-06-09

Problen Number: 127
Name: abc-hits
URL: https://projecteuler.net/problem=127

Contributor(s):
    Mark M.
"""

import gc
# import numba
import numpy as np

gc.enable()

# @numba.jit
def iter_prime_factors(n):
    i = 2
    while pow(i, 2) <= n:
        if n % i:
            i += 1
        else:
            n //= i
            yield i
    if n > 1:
        yield n

# @numba.jit
def distinct_ipf(n):
    res = set()
    ipf = iter_prime_factors(n)
    for f in ipf:
        res.add(f)
    return res

# @numba.jit
def rad(num):
    r=1
    dipf = distinct_ipf(num)
    for i in dipf:
        r *= i
    return r


# assert (rad(504) == 42), "Assertion error: rad(504)"
# assert (rad(4320) == 30), "Assertion error: rad(4320)"


# @numba.jit
# @numba.vectorize(["boolean(int32, int32, int32), boolean(int64, int64, int64)"])
def gcd_tf(A, B, C):
    return np.gcd(A, B) == np.gcd(A, C) == np.gcd(B, C) == 1


# assert (gcd_tf(5, 27, 32) == True), "Assertion error: eval_gcd(5, 27, 32)"
# assert (gcd_tf(5, 27, 33) == False), "Assertion error: eval_gcd(5, 27, 33)"


# @numba.vectorize(["boolean(int32, int32, int32), boolean(int64, int64, int64)"])
def ab_eq_c(A, B, C):
    """Function to evaluate a + b == c."""

    tmp = A + B
    return tmp == C

# def ab_eq_c(*args):
#     """Function to evaluate a + b == c."""
#     A, B, C = args[0], args[1], args[2]
#     tmp = np.sum([A, B])
#     return tmp == C

# assert (ab_eq_c(5, 27, 32) == True), "Assertion error: ab_eq_c(5, 27, 32)"
# assert (ab_eq_c(5, 27, 33) == False), "Assertion error: ab_eq_c(5, 27, 33)"


# @numba.njit(parallel=True)
def run(n):
    tmp = []
    C_START = n - 1
    for c in range(C_START, 0, -1):
        for a in range(n):
            for b in range(a+1, n):
                if ab_eq_c(a, b, c):
                    if gcd_tf(a, b, c):
                        abc_product = np.multiply.reduce([a, b, c])
                        if rad(abc_product) < c:
                            tmp.append(c)
    return tmp



if __name__ == "__main__":
    # N = int(1000)
    N = int(12*1e4)
    # C_START = np.int32(N - 1)
    # clist = list()
    clist = run(N)
    # for c in range(C_START, 0, -1):
    #     for a in range(N):
    #         for b in range(a+1, N):
    #             if ab_eq_c(a, b, c):
    #                 if gcd_tf(a, b, c):
    #                     abc_product = np.multiply.reduce([a, b, c])
    #                     if rad(abc_product) < c:
    #                         print(f"C-value: {c}")
    #                         clist.append(c)

    list_len = len(clist)
    c_sum = sum(clist)
    print("Done!")
    print(f"The number of c values is: {list_len}\nThe sum of the c values is: {c_sum}")



''' Working version

N = 1000
C_START = N - 1
c_rng = range(C_START, 0, -1)
clist = list()
for c in range(C_START, 0, -1):
    for a in range(N):
        for b in range(a+1, N):
            if ab_eq_c(a, b, c):
                if gcd_tf(a, b, c):
                    abc_product = np.multiply.reduce([a, b, c])
                    if rad(abc_product) < c:
                        clist.append(c)

list_len = len(clist)
c_sum = sum(clist)
print("Done!")
print(f"The number of c values is: {list_len}\nThe sum of the c values is: {c_sum}")
'''


















