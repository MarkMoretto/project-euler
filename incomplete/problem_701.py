
"""
Purpose: Projec-Euler
Date created: 2020-02-10

Problem: 701
Title:Random connected area
URI: https://projecteuler.net/problem=701

Contributor(s):
    Mark M.
"""

import random

sample_res = [0,1,1,1,1,1,1,2,2,2,2,3,3,3,3,4,]
sample_tot_area = sum(sample_res)
sample_tot_conn_area = sum([i for i in sample_res if i > 1])

# w = 2
# h = 2
# area_ = w * h
# rng = [i for i in range(area_)]

def prob_check(width=2, height=2, p_black = 0.5, n_iters = 1000, value_list = None):
    rng_ = [i for i in range(width*height)]
    denom = sum([1 for r in rng_ for c in rng_])
    if value_list is None:
        avg_list = list()
    iters = n_iters
    while iters > 0:
        tot_blk = 0
        for r in rng_:
            for c in rng_:
                randn = random.random()
                if randn >= p_black:
                    tot_blk += 1
        avg_list.append(round(tot_blk/denom, 8))
        iters -= 1
    
    avg_check = sum(avg_list) / 1000
    frmt_avg = avg_check * 100
    print(f"Probability of black area after {n_iters} iterations ~{frmt_avg:0<.2f}%")

def permutes(n):
    for i in range(1 << n):
        s = bin(i)[2:]
        s ='0' * (n - len(s)) + s
        yield list(map(int, list(s)))


w, h = 3, 3
perms = [i for i in permutes(w * h)]


matrix = [[0. for c in range(w)] for r in range(h)]

for r in range(h):
    cols = [i for i in range(w)]
    print(f"{r}, {cols}")
        for j in range(h):
            for k in range(w):
                tot = sum([r1, c1, r2, c2])
                print(f"[[{r1}, {c1}],\n[{r2}, {c2}]] = {tot}\n")



# for i in [0, 1,]:
#     for j in [0, 1,]:
#         for k in [0, 1,]:
#             for l in [0, 1,]:
#                 print(f"({i}, {j}, {k}, {l})")

# class Matrix:
#     def __init__(self, row, column, default_value = 0.):
#         self.row, self.column = row, column
#         self.array = [[default_value for c in range(column)] for r in range(row)]





