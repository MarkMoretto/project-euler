
"""
Purpose: Project euler problem
Date created: 2021-04-18

Status: Incomplete

Problen Number: 755
Name: Not Zeckendorf
URL: https://projecteuler.net/problem=755

Contributor(s):
    Mark M.
"""


import itertools as ittr
from functools import reduce

try:
    from functools import cache
except ImportError:
    from functools import lru_cache as cache

import concurrent.futures as ccf



# def fibs(n):
#     fib_list = [0, 1]
#     if n >= 0 and n < 2:
#         return n
#     else:
#         for i in range(2, n + 1):
#             if fib_list[-1] > n:
#                 break
#             else:
#                 fib_list.append(fib_list[i - 1] + fib_list[i - 2])
#         return fib_list


@cache(maxsize=None)
def fibs(n):
    fib_list = [1, 2]
    if n < 0:
        return None
    elif n == 0:
        return [1]
    elif n == 1:
        return [1, 2]
    else:
        for i in range(2, n + 1):
            tmp = fib_list[i - 1] + fib_list[i - 2]
            if tmp > n:
                break
            fib_list.append(tmp)
        return fib_list

# fibs(10)


# @cache(maxsize=3)
# def mod_fib(n):
#     if n >= 0 and n <= 1:
#         return n
#     else:
#         return mod_fib(n - 1) + mod_fib(n - 2)

# mod_fib(10)





# TARGET = 5
# sample = [1,2,3,5,8,13,]
# sample = fibs(TARGET)
# res = [list(ittr.combinations(sample, i)) for i in range(2, len(sample) + 1)]

# r, c = 3, 4
# [[0] * c for _ in range(r)]

# class Matrix:
#     def __init__(self, n, m):
#         self.matrix = [[0] * m for _ in range(n)]

#     def assign(self, n, m, value):
#         self.matrix[n][m] = value

#     def retrieve(self, n, m):
#         return self.matrix[n][m]

# m = Matrix(3, 4)

@cache(maxsize=None)
def f(n):
    if n < 2:
        return 1
    nums = fibs(n)
    rng = range(1, len(nums) + 1)
    COUNT = 0
    for i in rng:
        cnt = sum([1 for c in ittr.combinations(nums, i) if reduce(lambda x, y: x + y, c) == n])
        COUNT += cnt
    return COUNT





def S(N):
    tot = 0
    with ccf.ThreadPoolExecutor() as executor:
        the_futures = {executor.submit(f, i):i for i in range(N + 1)}
        for fut in ccf.as_completed(the_futures):
            data = fut.result()
            if data:
                tot += data
    print(f"The total is: {tot}")

    # return sum((f(i) for i in range(N+1)))

if __name__ == "__main__":
    # S(100)

    S(10000)



