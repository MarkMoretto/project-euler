
"""
Purpose: Project euler problem
Date created: 2021-03-09

Problen Number: 749
Name: Near Power Sums
URL: https://projecteuler.net/problem=749

Contributor(s):
    Mark M.

Description:
    A positive integer, n, is a <i>near power sum</i> if there exists a positive
    integer, k, such that the sum of the k-th powers of the digits in its decimal
    representation is equal to either n+1 or n-1.

    For example 35 is a near power sum number because 3^2+5^2 = 34.
    Define S(d) to be the sum of all near power sum numbers of digits or less.

    Then S(2) = 110 and S(6) = 2562701. 

    Find S(16).
"""


# from math import sqrt
from multiprocessing import cpu_count
from concurrent.futures import as_completed, ThreadPoolExecutor
from functools import lru_cache as cache


# pow_ = lambda base, exponent: base ** exponent

# def split_n(a, n):
#     k, m = divmod(len(a), n)
#     return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))

@cache
def validate(iterable):
    return any(map(lambda q: q > 1, iterable))


def split_n(n):
    return list(map(int, str(n)))


def add_parts(iterable, exponent):
    return sum(map(lambda n, p = exponent: pow(n, p), iterable))
        # return sum(map(lambda n, p = exponent: pow_(n, p), map(int, str(integer))))

def eval_near_power(n, target):
    return (n == target - 1) or (n == target + 1)

# eval_near_power(34, 35)

def s_worker(N):

    print(f"Processing N = {N}\n")

    min_N = int(eval(f"1e{N-1}"))
    max_N = int(eval(f"1e{N}"))
    
    output = []
    for i in range(min_N, max_N):
        tmp = split_n(i)
        expon = 0
        if validate(tmp):
            while True:
                sum_parts = add_parts(tmp, expon)
                if sum_parts > (i + 1):
                    break
                elif eval_near_power(i, sum_parts):
                    # print(f"match: {i}, exponent: {expon}")
                    output.append(i)
                    break
                expon += 1

    return sum(output)


def S(d):
    tot = 0
    # d += 1
    n_workers = d * 2
    rng = range(2, d + 1)
    with ThreadPoolExecutor(max_workers = n_workers, thread_name_prefix="hello_") as executor:
        mapped_futures = {executor.submit(s_worker, i):str(i) for i in rng}
        for fut in as_completed(mapped_futures):
            completed = mapped_futures[fut]
            print(f"N {completed} completed.")
            tot += fut.result()
    return tot

if __name__ == "__main__":
    res = S(8)
    print(res)




# t1 = 999999
# ttmp1 = split_n(t1)
# s_parts1 = add_parts(ttmp1, 1)
# s_parts1 > (t1 + 1)

# t2 = 100001
# ttmp2 = split_n(t2)
# s_parts2 = add_parts(ttmp2, 1)
# s_parts2 > (t2 + 1)