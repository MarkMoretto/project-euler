
"""
Purpose: Project Euler questions
Date created: 2019-10-22
Main URI: https://projecteuler.net

Problem ID: 678
URI: https://projecteuler.net/problem=678
Title: Fermat-like equations

Description 
    If a triple of positive integers (a,b,c) satisfies a**2 + b**2 = c**2, it is called
    a Pythagorean triple.  No triple (a,b,c) satisfies a**e + b**e = c**e
    when e ≥ 3 (Fermat's Last Theorem).

    However, if the exponents of the left-hand side and right-hand side differ,
    this is not true. For example, 3 ** 3 + 6 ** 3 = 3 ** 5.
    
    Let a, b, c, e, f be all positive integers:
        0 < a < b,
        e ≥ 2,
        f ≥ 3 and
        c**f ≤ N.

    Let F(N) be the number of (a,b,c,e,f) such that a**e + b**e = c**f.

    You are given:
        F(10**3) = 7;
        F(10**5) = 53; and
        F(10**7) = 287
    
    Find F(10**18).

Contributor(s): Mark M.
"""

import math
import numpy as np

n = 10
n_exp = 3

N = n ** n_exp

min_e = 2
min_f = 3

a, b, c = 1, 2, 0
e, f = min_e, min_f

lhs = lambda a, b, e: a ** e + b ** e
rhs = lambda c, f: c ** f
gt_check = lambda x, y: True if x > y else False
eq_check = lambda x, y: True if x == y else False

lhs(a, b, e)
rhs(c ,f)












