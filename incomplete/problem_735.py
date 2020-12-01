
"""
Purpose: Project euler problem
Date created: 2020-11-29

Problen Number: 735
Name: Divisors of 2n^2
URL: https://projecteuler.net/problem=735

Contributor(s):
    Mark M.

Description:

"""


import gc
gc.enable()

def f(n):
    numer = 2 * (n * n)
    i = 1
    counter = 0
    while i <= n:
        if numer % i == 0:
            counter += 1
        i += 1
    return counter



def F(N):
    i = 1
    tot = 0
    while i <= N:
        tot += f(i)
        i += 1
    return tot

assert (F(15) == 63), "Error: F(15) value assertion."


if __name__ == "__main__":
    number = int(10 ** 12)
    res = F(number)
    print(res)
