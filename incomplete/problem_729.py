
"""
Purpose: Project Euler exercises
Date created: 2020-10-11

Problen Number: 729
Name: Range of periodic sequence
URL: https://projecteuler.net/problem=729

Contributor(s):
    Mark M.

Description:

"""

import math

func = lambda num: num - (1 / num)

a_memo = {}
def inner():
    while not n in a_memo:
        a_memo[n] = func(n)
        return a_memo[n]


def a(n):

    seq_memo = {}
    def inner(num):
        i = 0
        res = func(num)
        while not res in seq_memo.values():
            seq_memo[i] = res
            return inner(res)

    inner(n)
    return max(seq_memo.values()) - min(seq_memo.values())





a0 = math.sqrt(1/2)
a(a0)
