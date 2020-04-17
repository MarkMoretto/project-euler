
"""
Purpose: 
Date created: 2020-04-11

Contributor(s):
    Mark M.
"""
# os.environ["NUMBA_DUMP_CFG"] = "1"
# os.environ["NUMBA_NUM_THREADS"] = "2"
# os.environ["NUMBA_THREADING_LAYER"] = "tbb"
# os.environ["NUMBA_ENABLE_AVX"] = "1"
# x_gpu = cuda.device_array(shape=(1,), dtype=np.float64)

import os
# os.environ["NUMBA_ENABLE_CUDASIM"] = "0"


import cupy as cp
import numpy as np
from numba import cuda, vectorize, guvectorize

"""
x_gpu = cp.array([0], dtype = cp.float64)
fin_gpu = cp.array([0], dtype = cp.float64)

tpb = 1 # threads per block
bpg = (x_gpu.size + (tpb - 1)) // tpb # blocks per grid

@cuda.jit("(float64[:])")
def incr_kernel(arr):
    ix = cuda.grid(1)
    arr[ix] += 1


incr_kernel[bpg, tpb](x_gpu)
out_arr = x_gpu.get()
print(out_arr)
"""

@cuda.jit(device=True)
# @vectorize(['float64(int64)'], target='cuda')
def f_cuda(n):
    result = np.float64(1)
    while n % 2 == 0:
        result *= 2.0
        n /= 2

    max_n = np.int64(n ** 0.5 + 1)
    for i in range(3, max_n, 2):
        while n % i == 0:
            result *= 2.0
            n /= i

    if n > 2:
        result *= 2.0
    return np.float64(result)


#@guvectorize("(u8[:], f8[:])", '(n) -> (n)', target='cuda', nopython=True)
@cuda.jit
def S_cuda(N, tot_arr):
    pos = cuda.grid(1)

    max_n = N.item() + 1
    #N += 1
    for i in range(1, max_n):
        tot_arr[pos] += f_cuda(i)
    cuda.syncthreads()





if __name__ == "__main__":

    #x_gpu = cp.array([0], dtype = cp.float64)
    out_gpu = cp.array([0], dtype=cp.float64)

    tpb = 16
    bpg = (out_gpu.size + (tpb - 1)) // tpb

    # # Expected test results for a given integer
    # expected = {
    #         "1e7": np.uint64(746246327),
    #         "1e8": np.uint64(9613563919),
    #         }

    # test_str = "1e7"
    # test_value = np.array(eval(f"{test_str}"), dtype=np.int64)

    # test_arr = cp.array([1e6], dtype=cp.int64)
    test_val = cp.uint64([1e6])
    #test_arr = cp.array([1e6], dtype=cp.uint64)
    #out_gpu = cp.empty(shape=(1,), dtype=cp.float64)

    S_cuda[bpg, tpb](test_val, out_gpu)
    # S_cuda(test_arr, out_gpu)
    res = out_gpu.get()
    print(f"{res}")

    # if expected[test_str] == res:
    #     print("Result matches expected!")