
"""
Purpose: Project Euler exercises
Date created: 2020-10-18

Problen Number: 730
Name: Shifted Pythagorean Triples
URL: https://projecteuler.net/problem=730

Contributor(s):
    Mark M.
"""


from math import gcd

def assert_pqr(p, q, r):
    if p < 1:
        return False
    elif q < r:
        return False
    elif r < q:
        return False
    else:
        return True


assert assert_pqr(-1, 2, 3) == False
assert assert_pqr(2, 1, 3) == False
assert assert_pqr(1, 1, 1) == True


def shift(p, q, r, k):
    if assert_pqr(p, q, r):
        return (p**2 + q**2 + k) == r ** 2


N= 10
P, Q, R = 1, 1, 1

while True:
    if (P + Q + R) <= N:
        while Q <= R:


            while P <= Q:

                P += 1



