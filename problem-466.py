
"""
Purpose: Project Euler problems
Date created: 2019-10-22

Contributor(s): Mark M.

ID: 466
Title: Distinct terms in a multiplication table
URI: https://projecteuler.net/problem=466
Status: Testing

Desc:
    Let P(m,n) be the number of distinct terms in an m×n multiplication table.

    For example, a 3×4 multiplication table looks like this:
    
    ×	1	2	3	4
    1	1	2	3	4
    2	2	4	6	8
    3	3	6	9	12
    There are 8 distinct terms {1,2,3,4,6,8,9,12}, therefore P(3,4) = 8.
    
    You are given that:
    P(64,64) = 1263,
    P(12,345) = 1998, and
    P(32,10**15) = 13826382602124302.
    
    Find P(64,10**16).
"""

import numpy as np



def P(m, n):

    x = np.zeros((n,),)
    y = np.zeros((m,),)

    x[:] = [i for i in range(1, n + 1)]
    y[:] = [i for i in range(1, m + 1)]

    x = x.reshape((-1,1))
    y = y.reshape((-1,1))

    arr = np.linalg.multi_dot([x, y.T])

    return np.count_nonzero(np.unique(arr))



P(3, 4)
P(64, 64)
P(12, 345)

P(32, 10**15)








# timesall = lambda a, b: [np.prod([i, j]) for i in a for j in b]
# unique_count = lambda x: [1 for i in list(set(x))]
# sum_count = lambda x: sum(x)