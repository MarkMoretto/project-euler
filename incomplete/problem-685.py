
"""
Purpose: Project Euler problems
Date created: 2019-10-19

Contributor(s):
    Mark M.


ID: 685
URI: https://projecteuler.net/problem=685
Status: Incomplete
"""



sum_nums = lambda x: sum([int(i) for i in str(x)])

def f(n, m):
    idx = 1
    for i in range(n, 1000000000000):
        if sum_nums(i) == n:
            if idx == m:
                yield i
            idx += 1


def inv_mod(a, c):
    if c == 0:
        return 0
    else:
        for q in range(1, c-1):
            if (a * q) % c == 1:
                return q



inv_mod(S(3), 0)


# S = lambda k: sum([f(j**3, j**4) for j in range(1, k+1)])
S = lambda k: sum([f(n**3, n**4).__next__() for n in range(1, k+1)])
k = 3

inv_mod(S(k), 0)



f = lambda n, m: {}

1, 1 # 1
8, 16 # 161
27, 81 # 6996