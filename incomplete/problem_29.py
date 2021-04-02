
"""
Purpose: Project euler problem
Date created: 2021-04-02

Problen Number: 29
Name: Distinct powers
URL: https://projecteuler.net/problem=29

Contributor(s):
    Mark M.
"""

MAX: int = 100

rng = range(2, MAX + 1)
values = set([pow(a, b) for a in rng for b in rng])
print(f"The number of distinct terms for the given range is: {len(values):,}")

