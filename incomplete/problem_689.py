
"""
Purpose: Project Euler problems
Date created: 2019-11-17
Contributor(s): Mark M.

ID: 689
Title: Binary Series
URI: https://projecteuler.net/problem=689
Difficulty: ?

Status: Incomplete

Ref(s):
    https://blog.penjee.com/binary-numbers-floating-point-conversion/

Problem:


"""


BinaryNumber = 1001111
Decimal value = (1*(2^6)) + (0*(2^5)) + (0*(2^4)) + (1*(2^3)) + (1*(2^2)) + (1*(2^1)) + (1*(2^0))

def to_decimal(n: int) -> int:
    n_str: str = str(n)
    for i, v in enumerate(n_str[::-1]):
        print(f'({v}*(2^{i}))')


# def flost_to_bin():
