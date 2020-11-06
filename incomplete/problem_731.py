
"""
Purpose: Project Euler exercises
Date created: 2020-10-25

Problen Number: 731
Name: A Stoneham Number
URL: https://projecteuler.net/problem=731

Contributor(s):
    Mark M.
"""

# from math import gcd
from decimal import Decimal # format(d, ".50f")
from fractions import Fraction
# from functools import lru_cache


# def coprime_check(a, b):
#     return gcd(a, b) == 1

# assert coprime_check(14, 15) == True
# assert coprime_check(14, 28) == False


# @lru_cache(maxsize=128)
def worker(I):
    return Fraction( 1, 3**I * 10**(3**I) )


N = 100
i = 1
r = Fraction(1, i)

while i <= N:
    r += worker(i)
    i += 1

Decimal(r.numerator)/Decimal(r.denominator)[100:111]

print(Decimal(r.numerator)/Decimal(r.denominator))


# for n in range(repetitions):
#     r += Fraction(1, d) - Fraction(1, d + 2)
#     d += 4