
"""
Purpose: Project Euler problems
Date created: 2019-10-26

Contributor(s): Mark M.

ID: 31
Title: Coin sums
URI: https://projecteuler.net/problem=31
Status: Incomplete

Desc:
    In England the currency is made up of pound, £, and pence, p, and there 
    are eight coins in general circulation:
    
        1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
    
    It is possible to make £2 in the following way:
    
        1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
    
    How many different ways can £2 be made using any number of coins?
"""

from itertools import (
        combinations_with_replacement, permutations, combinations
        )

multipleof = lambda numer, denom: int(numer / denom) if numer % denom == 0 else int(round(numer / denom, 0))

# All possible pence
p_vals = [1, 2, 5, 10, 20, 50, 100, 200]

# Goal count
target = 200

# Dictionary of max values for a given amount
pdict = {i:multipleof(target, i) for i in p_vals}




