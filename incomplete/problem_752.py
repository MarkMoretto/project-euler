
"""
Purpose: Project euler problem
Date created: 2021-03-21

Problen Number: 752
Name: Powers of 1  sqrt(7)
URL: https://projecteuler.net/problem=752

Contributor(s):
    Mark M.
"""

from math import sqrt

sqrt7 = sqrt(7)

q = lambda n: (1 + sqrt7) ** n


q(2)