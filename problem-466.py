
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

### Note: Will need a bunch of tensorflow and GPU stuff installed to run.

from __future__ import absolute_import, division, print_function, unicode_literals

import theano
import numpy as np



m=3
n=4


@tf.function
def iter_it(n):
    for i in range(1, n + 1):
        yield i


x_iter = iter_it(m)
y_iter = iter_it(n)



def P(m, n):

    x_iter = iter_it(m)
    y_iter = iter_it(n)




prev = 0
for i in range(1, 11):
    res = P(i, i)
    growth = res - prev
    print(f'P({i},{i}) # {res}, diff: {growth}')
    prev = res


prev = 0
for i in range(0, 11):
    res = P(32, 10**i)
    growth = res - prev
    print(f'P({i},{i}) # {res}, diff: {growth}')
    prev = res

P(3, 4)
P(1,1) # 1
P(2,2) # 3
P(3,3) # 6
P(4,4) # 9
P(5,5) # 14
P(6,6) # 18
P(7,7) # 25
P(8,8) # 30
P(9,9) # 36
P(10,10) # 42
P(11,11) # 53
P(12,12) # 59
P(13,13) # 72
P(14,14) # 80
P(15,15) # 89
P(16,16) # 97
P(17,17) # 114
P(18,18) # 123
P(19,19) # 142
P(20,20) # 152
P(21,21) # 164
P(22,22) # 176
P(23,23) # 199
P(24,24) # 209
P(25,25) # 225
P(26,26) # 239
P(27,27) # 254
P(28,28) # 267
P(29,29) # 296
P(30,30) # 308

P(64, 64)
P(12, 345)

P(32, 10**15)


P(32,10)
P(32,10**2)%32
P(32,10**3)%32
P(32,10**4)%32
P(32,10**5)%32

P(64, 4**2)


### Works
# def P(m, n):

#     x = np.ndarray((n,),)
#     y = np.ndarray((m,),)

#     x_iter = iter_it(m)
#     y_iter = iter_it(n)

#     x = np.array([i for i in range(1, n + 1)])
#     y = np.array([i for i in range(1, m + 1)])

#     x = x.reshape((-1,1))
#     y = y.reshape((-1,1))

#     arr = np.linalg.multi_dot([x, y.T])

#     return np.count_nonzero(np.unique(arr))


# timesall = lambda a, b: [np.prod([i, j]) for i in a for j in b]
# unique_count = lambda x: [1 for i in list(set(x))]
# sum_count = lambda x: sum(x)