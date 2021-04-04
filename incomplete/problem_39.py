
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

import concurrent.futures as ccf

# p = 120
# s = p // 2


@cache(maxsize=1000)
def isqrt(n: int) -> int:
    """Quick square root function which returns an integer value."""
    return int(n ** 0.5)

@cache(maxsize=1000)
def calc_c(a, b) -> int:
    return isqrt((a * a) + (b * b))


def is_valid(a, b, c, p, s) -> bool:
    cond1 = a <= b and b < c
    cond2 = sum([a, b, c]) == p
    cond3 = (s - a) * (s - b) == s * (s - c)
    return cond1 and cond2 and cond3


def count_solutions(perimeter: int) -> int:
    semiperimeter = perimeter // 2
    sp = semiperimeter + 1

    results = []
    checked = set()
    for a in range(1, sp):
        for b in range(1, sp):
            if not b in checked:
                c = calc_c(a, b)
                if is_valid(a, b, c, perimeter, semiperimeter):
                    checked.add(a)
                    results.append((a, b, c))
                    # tmp_tup = (a, b, c)
                    # if not tuple(sorted(tmp_tup)) in results:
                    #     results.append(tmp_tup)

    return len(results)


def main(limit: int) -> None:
    max_count = -1
    max_value = 0
    max_range = limit + 1
    with ccf.ThreadPoolExecutor() as executor:
        count_futures = {executor.submit(count_solutions, i):i for i in range(3, max_range)}
        for fut in ccf.as_completed(count_futures):
            val = count_futures[fut]
            data = fut.result()
            if data > max_count:
                max_count = data
                max_value = val
    print(f"The maximum number of solutions is {max_count} for p = {max_value}")

if __name__ == "__main__":
    max_range: int = 1000
    main(max_range)

