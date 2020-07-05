
"""
Purpose: Project Euler exercises
Date created: 2020-07-03

Problen Number: 122
Name: Efficient exponentiation
URL: https://projecteuler.net/problem=122

Contributor(s):
    Mark M.

Description:
    The most naive way of computing n^15 requires fourteen multiplications:
    
    n × n × ... × n = n^15
    
    But using a "binary" method you can compute it in six multiplications:
    
    n × n = n^2
    n^2 × n^2 = n^4
    n^4 × n^4 = n^8
    n^8 × n^4 = n^12
    n^12 × n^2 = n^14
    n^14 × n = n^15
    
    However it is yet possible to compute it in only five multiplications:
    
    n × n = n^2
    n^2 × n = n^3
    n^3 × n^3 = n^6
    n^6 × n^6 = n^12
    n^12 × n^3 = n^15
    
    We shall define m(k) to be the minimum number of multiplications to compute nk; for
    example m(15) = 5.
    
    For 1 ≤ k ≤ 200, find ∑ m(k).
    
Additional references:
    https://en.wikipedia.org/wiki/Addition-chain_exponentiation
"""

import numpy as np
import itertools as ittr

N = 15
NUMS = np.arange(1, N + 1, dtype=np.int32)

plist = list(ittr.product(NUMS, repeat=2))
psums = {i:sum(i) for i in plist if sum(i) <= N}


# THe naive number of computations for an exponent.
min_count = N - 1
idx = 0
results = {}
for k1, v1 in psums.items():
    prev = v1
    count = 1
    tot = v1
    tmp = [k1]
    for k2, v2 in psums.items():
        if prev == k2[0]:
            count += 1
            tot += v2
            prev = v2
            tmp.append(k2)
    results[idx] = tmp
    idx += 1
    if count < min_count:
        min_count = count

            print(k1, v1, k2)




xv, yv = np.meshgrid(NUMS, NUMS, sparse=False, indexing='ij')
z = np.sum([xv, yv], axis=0)
zz = np.where(z<=15, z, -1)


q= np.stack(np.meshgrid(NUMS, NUMS), -1).reshape(-1, 2)
qq = q.sum(axis=1).reshape((-1, 1))
qqq = np.append(q, qq, axis=1)

np.where(qqq<=15, qqq)














