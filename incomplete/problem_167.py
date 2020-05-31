
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

import concurrent.futures as ccf
from functools import lru_cache
# from multiprocessing import Pool, cpu_count
import multiprocessing as mp
from multiprocessing.pool import ThreadPool


@lru_cache(maxsize=500)
def sorter(x, y):
    if x >= y: return (x, y)
    return (y, x)


@lru_cache(maxsize=500)
def sumcache(iterable):
    return sum(iterable)


def ulam_eval(current, iterable):
    sum_count = 0
    for i in iterable:
        for j in iterable:
            if i < j:
                current_pair = sorter(j, i)
                if sumcache(current_pair) == current:
                    sum_count += 1
    return sum_count



def ulam_sequence(ulist):

    ct = 2

    n = max(*ulist)

    yield ulist[0]
    yield ulist[1]


    # Limit of number sequence values. Can land on or before it.
    K = pow(10,11)
    # K = 100
    # While count is less than numeric limit k.
    while ct < K:
        n += 1

        # ulan_eval returns the count of values, which should equal 1.
        res = ulam_eval(n, ulist)

        if res == 1:
            ulist.append(n)
            ct += 1
            yield ulist[-1]


# useq = ulam_sequence(2,5)
def test_ulan_sequence(start=[1, 2]):
    def run(x):
        res = []
        useq = ulam_sequence(x)
        count = 2
        for q in useq:
            res.append(q)
        return res
    return run(start)


def run_ulam(n):
    tot = 0

    b = (2 * n) + 1
    ab_list = [2, b]

    ugen = ulam_sequence(ab_list)

    for q in ugen:
        tot += q
    return tot



def main():
    rng = list(range(2, 11))
    # k = pow(10,11)
    # k = 100
    tot_list = []

    with ccf.ThreadPoolExecutor(max_workers=10) as executor:
        future_dict = {executor.submit(run_ulam, i):f"{i}" for i in rng}
        for future in ccf.as_completed(future_dict):
            current = future_dict[future]
            try:
                res = future.result()
                tot_list.append(res)
            except Exception as exc:
                print(f'Thread {current} generated an exception: {exc}')
            else:
                print(f'Thread {current} compete with value of: {res}')
    return tot_list



def main_proc():

    rng = list(range(2, 11))

    # k = 100
    tot_list = []

    with ccf.ProcessPoolExecutor() as executor:
        future_dict = {executor.submit(run_ulam, i):f"{i}" for i in rng}
        for future in ccf.as_completed(future_dict):
            current = future_dict[future]
            try:
                res = future.result()
                tot_list.append(res)
            except Exception as exc:
                print(f'Thread {current} generated an exception: {exc}')
            else:
                print(f'Thread {current} compete with value of: {res}')
    return tot_list






if __name__ == "__main__":
    # total = main() # concurrent.futures.ThreadPoolExecutor
    # total = main_proc() # concurrent.futures.ProcessPoolExecutor


    # Multiprocessing
    # import multiprocessing as mp
    # from multiprocessing.pool import ThreadPool
    try:
        # Set worker count based on # of CPUs, but don't go nuts.
        workers = mp.cpu_count() - 1
    except NotImplementedError:
        workers = 1


    rng = list(range(2, 11))

    # k = 100
    total = []


    # with mp.Pool(processes=workers) as pool:
    with ThreadPool(processes = workers) as pool:
        # total = pool.map(run_ulam, range(2, 11))

        multiple_results = [pool.apply_async(run_ulam, (i,)) for i in range(2, 11)]
        # print([res.get() for res in multiple_results])
        for res in multiple_results:
            total.append(res.get())

        print(f"The final sum is: {sum(total)}")



