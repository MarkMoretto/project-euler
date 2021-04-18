
"""
Purpose: Project euler problem
Date created: 2021-04-04

Status: Incomplete

Problen Number: 66
Name: Diophantine equation
URL: https://projecteuler.net/problem=66

Contributor(s):
    Mark M.
"""

import math

try:
    from functools import cache
except ImportError:
    from functools import lru_cache as cache


# @cache(maxsize=500)
def is_prime(n):

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True



def diophantine(x, y, D):
    return (x * x) - (D * (y * y))

x_list = []
for d in range(2, 8):
    x, y = 1, 1
    running = True
    while running:
        if diophantine(x, y, d) == 1:
            x_list.append(x)
            running = False

