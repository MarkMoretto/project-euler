
"""
Purpose: Project euler problem
Date created: 2021-06-13

Status: Incomplete

Problen Number: 759
Name: A squared recurrence relation
URL: https://projecteuler.net/problem=759

Contributor(s):
    Mark M.
"""

from typing import Union
Number = Union[int, float]

MOD: int = 1_000_000_007

def is_even(N: Number) -> bool:
    return N&1 == 0


def f(n):
    if n == 1:
        return 1
    if is_even(n):
        return 2 * f(n // 2)
    else:
        return ()
