
"""
Purpose: Project euler problem
Date created: 2021-04-03

Problen Number: 39
Name: Integer right triangles
URL: https://projecteuler.net/problem=39

Contributor(s):
    Mark M.
"""

try:
    from functools import cache
except ImportError:
    from functools import lru_cache as cache


# p = 120
# s = p // 2


@cache(maxsize=100)
def isqrt(n: int) -> int:
    """Quick square root function which returns an integer value."""
    return int(n ** 0.5)

@cache(maxsize=100)
def calc_c(a, b):
    return isqrt((a * a) + (b * b))


def is_valid(a, b, c, p, s):
    cond1 = a <= b and b < c
    cond2 = sum([a, b, c]) == p
    cond3 = (s - a) * (s - b) == s * (s - c)
    return cond1 and cond2 and cond3


def count_solutions(perimeter: int):
    semiperimeter = perimeter // 2

    results = []

    for a in range(1, semiperimeter + 1):
        for b in range(1, semiperimeter + 1):
            if a <= b:
                c = calc_c(a, b)
                if is_valid(a, b, c, perimeter, semiperimeter):
                    tmp_tup = (a, b, c)
                    if not tuple(sorted(tmp_tup)) in results:
                        results.append(tmp_tup)

    return len(results)


def main():
    max_count = -1
    max_value = 0

    for i in range(3, 1001):
        tmp = count_solutions(i)
        if tmp > max_count:
            max_count = tmp
            max_value = i
    print(f"The maximum number of solutions is {max_count} for p = {max_value}")

main()

