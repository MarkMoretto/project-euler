
"""
Purpose: Project Euler exercises
Date created: 2020-05-28

Problen Number: 167
Name: Investigating Ulam sequences
URL: https://projecteuler.net/problem=167

Contributor(s):
    Mark M.

Desc:
    For two positive integers a and b, the Ulam sequence U(a,b) is defined by
        U(a,b)1 = a,
        U(a,b)2 = b
    and for k > 2, U(a,b)k is the smallest integer greater than U(a,b)(k-1) which can
    be written in exactly one way as the sum of two distinct previous members of U(a,b).
    
    For example, the sequence U(1,2) begins with
    1,
    2,
    3 = 1 + 2,
    4 = 1 + 3,
    6 = 2 + 4,
    8 = 2 + 6,
    11 = 3 + 8;

    5 does not belong to it because 5 = 1 + 4 = 2 + 3 has two representations as the
    sum of two previous members.
    likewise 7 = 1 + 6 = 3 + 4.
    
    Find ∑ U(2,2n+1)k for 2 ≤ n ≤ 10, where k = 10**11.    
"""

# https://github.com/lucamollica/umap_test/tree/df8ed203336b88cdfaf18494790a81f07af89a18/umap

# from __future__ import print_function

# import numba
import numpy as np


# K = 20
# A = 2
# B = 5

# @numba.njit(['void(int32, int32, int32[:])', 'void(int64, int64, int64[:])'], nogil=True)
# def create_array(a1, b1, out):
#     return out[:] = [a1, b1]


def ulam(A_, B_, K_):

    arr = [A_, B_]

    current = B_

    i = 2
    n = 2
    ulen = 0

    while i < K_:
        current += 1
        count = np.int32(0)
        ulen = len(arr) + 1
        for x in range(ulen):
            for y in range(ulen):
                if x < y:
                    if sum([arr[x], arr[y]]) == current:
                        count += 1

        # Evaluate count; append current to ulam if count equal to 1.
        if count == 1:
            arr.append(current)
            i += 1
        n += 1
    return arr




def main(a, b, k):

    res = ulam(a, b, k)

    print(res)




if __name__ == "__main__":

    K = 60
    A = 2
    B = 5

    main(A, B, K)

# inline='always'
# @numba.guvectorize
# @numba.njit(["i8(i4, i4, i4)"])


# @numba.njit(['uint32[:](uint32[:], uint32)','float32[:](float32[:], float32)'])
# @numba.guvectorize(['(uint32[:], uint32, uint32[:])','(uint64[:], uint64, uint64[:])'],
#                     locals={
#                         "current": numba.types.uint32,
#                         "i": numba.types.uint32,
#                         "n": numba.types.uint32,
#                         "count": numba.types.uint32,
#                     },
#                     signature="(m),(),(n)->(m)",
#                     nopython=True)
# @numba.njit
# @numba.generated_jit(nopython=True)
# def ulam(u, k, out):

#     current = np.uint32(u[-1])
#     i = np.uint32(2)
#     n = np.uint32(2)

#     while i < k:
#         current = current + 1
#         count = 0
#         for x in u:
#             for y in u:
#                 if x < y:
#                     workarr = np.array([x, y])
#                     if workarr.sum() == current:
#                         count = count + 1

#         # Evaluate count; append current to ulam if count equal to 1.
#         if count == 1:
#             # out[i] = current
#             out = np.append(out, current)
#             i += 1
#         n += 1


    # print(ulam_arr)
    # ulam_tot = ulam_arr.sum()
    # return ulam_tot
# u = np.append(u, current)

# @numba.njit(**{'parallel': False, 'cache': False})
# @numba.njit
# def main(a, b, k):

#     inarr = np.array([a, b], dtype=np.uint32).reshape((-1, 1))
#     out_arr = np.copy(inarr)


#     ulam(inarr, k, out_arr)

#     print(out_arr)




# if __name__ == "__main__":

#     K = 60
#     A = 2
#     B = 5

#     main(A, B, K)
    # res = main(A, B, K)
    # print("The sum of U({A}, {B}) for k = {K} is: {res}")


# a, b = 2, 5
# xx = np.array(a, dtype=np.uint32).reshape((1, -1))
# yy = np.array(b, dtype=np.uint32).reshape((1, -1))

# @numba.generated_jit(nopython=True)
# @numba.njit
# def ulam_eval(current, iterable):

#     sum_count = np.array(0, dtype=np.uint64).reshape((-1,1))

#     for i in iterable:
#         for j in iterable:
#             if i < j:
#                 currpair = np.array([j, i], dtype=np.uint32)
#                 if currpair.sum(axis=0) == current:
#                     sum_count[0:1] += 1

#     return np.asscalar(sum_count)



# @numba.njit("(i8[:], i4)")
# def ulam_sequence(ulist, k_value):

#     ct = 2

#     n = ulist.max()
#     idx = 0

#     yield ulist[0].item()
#     yield ulist[1].item()

#     # While count is less than numeric limit k.
#     while ct < k_value:
#         n += 1

#         # ulan_eval returns the count of values, which should equal 1.
#         res = ulam_eval(n, ulist)

#         if res == 1:
#             ulist.append(n)
#             ct += 1
#             return ulist[-1]


# @numba.njit(fastmath=True)
# def calc_b(num):
#     return 2 * num + 1




# def run_ulam(n):
#     tot = 0
#     k = 100
#     b = calc_b(n)
#     ab_list = [2, b]

#     zz = np.zeros((k, 1), dtype=np.float32)
#     zz[0] = 1.
#     zz[1] = 2.
#     np.trim_zeros(zz)

#     ugen = ulam_sequence(ab_list, k)

#     for q in ugen:
#         tot += q
#     return tot


"""
Via: https://voodooguru23.blogspot.com/2018/10/ulam-numbers.html?m=0

ulam=[i for i in range(1,200)]
ulam[0], ulam[1]=2,3
k=2
while k<len(ulam):
    count=0
    for x in range(k):
        for y in range(k):
            if ulam[x] > ulam[y]:
                if ulam[x] + ulam[y] == ulam[k]:
                    count+=1
    if count!=1:
        ulam.remove(ulam[k])
        k-=1
    k+=1
print ulam
"""


# @numba.njit(["int32(int32, int32)", "float32(float32, float32)"])

# k = 50
# a = 2
# b = 5

# ulam = np.array([a, b], dtype=np.uint32)

# # Seed initial values
# current = ulam.max()
# i = ulam.size

# while i < k:
#     current += 1
#     count = 0
#     n = ulam.size
#     for x in range(n):
#         for y in range(n):
#             if x < y:
#                 if sum([x, y]) == current:
#                     count += 1
#     if count == 1:
#         ulam = np.insert(ulam, ulam.size, current, axis=0)
#         i += 1






# for n in numba.prange(2, 11): # 2 ≤ n ≤ 10
#     b = calc_b(n)
#     print(b)




# if __name__ == "__main__":

#     k = 50
#     a = 2
#     b = 5
    
#     ulam = np.array([a, b], dtype=np.uint32)
    
#     # Seed initial values
#     current = ulam.max()
#     i = ulam.size
#     n = ulam.size

#     while i < k:
#         n += 1
#         current += 1
#         count = 0

#         for x in range(n):
#             for y in range(n):
#                 if x < y:
#                     if sum([x, y]) == current:
#                         count += 1
#         if count == 1:
#             # ulam = np.insert(ulam, i, current, axis=0)
#             ulam[i:i+1] = current
#             i += 1
#     print(ulam)
























