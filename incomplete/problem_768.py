
"""
Purpose: Project euler problem
Date created: 2021-10-21

Status: Incomplete

Problen Number: 768
Name: Chandelier
URL: https://projecteuler.net/problem=768

Contributor(s):
    Mark M.

Description - 

A certain type of chandelier contains a circular ring of evenly spaced candleholders.
If only one candle is fitted, then the chandelier will be imbalanced. However, if a second
identical candle is placed in the opposite candleholder (assuming n is even) then
perfect balance will be achieved and the chandelier will hang level.

Let f(n,m) be the number of ways of arranging m identical candles in distinct sockets of a
chandelier with n candleholders such that the chandelier is perfectly balanced.

For example,
    f(4,2) == 2
Assuming the chandelier's four candleholders are aligned with the compass points, the two
valid arrangements are "North & South" and "East & West". Note that these are considered
to be different arrangements even though they are related by rotation.

You are given
f(12,4) == 15
f(36,6) == 876

Find f(36,6).
"""
# f(n, m) =>
#   m = number of candles
#   n = number of candleholders
from functools import partial
from itertools import permutations


class ICoord:
    def __call__(self, coord, target) -> bool:
        return abs(coord[0] - coord[1]) == target

coord = ICoord()

# n, m = 4, 2
# n, m = 12, 4
n, m = 36, 6

p_coord = partial(coord, target=n//2)

# [c for c in permutations(range(n), 4) if p_coord(c)]
# sum([1 for c in combinations(range(n), 4) if p_coord(c)])
# res = list(map(lambda c: list(c), permutations(range(n), 4)))




def subsect(iterable):
    if iterable:
        item, iterable = iterable[:2], iterable[2:]
        yield item
        yield from subsect(iterable)
    return

output = []
count = 0
for item in permutations(range(n), m):
    sitem = sorted(item)
    if all([True if p_coord(pair) else False for pair in subsect(sitem)]):
        if not sitem in output:
            count += 1
            output.append(sitem)














def f(n, m):
    p_coord = partial(coord, target=n//2)
    return sum([1 for c in combinations(range(n), 2) if p_coord(c)])

f(4,2)
f(12,4)

