
"""
Purpose: Project euler problem
Date created: 2021-06-27

Status: Incomplete

Problen Number: 760
Name: Sum over Bitwise Operators
URL: https://projecteuler.net/problem=760


Contributor(s):
    Mark M.
"""
# from os import cpu_count
from functools import lru_cache as cache
import concurrent.futures as ccf

MOD: int = 1000000007
total: int = 0


@cache(maxsize=1000)
def g(m: int, n: int) -> int:
    return (m^n) + (m|n) + (m&n)


@cache(maxsize=1000)
def sub_g(n):
    return sum(g(k, n-k) for k in range(n+1))

# print("\n".join([f"{i}: {sub_g(i+1) - sub_g(i)}" for i in range(10)]))


def G(N):
    total: int = 0
    rngN = range(N+1)
    with ccf.ProcessPoolExecutor(max_workers = 40) as executor:
        futures = [executor.submit(sub_g, num) for num in rngN]
        for fut in ccf.as_completed(futures):
            total = total + (fut.result() % MOD)
    # for n in rngN:
    #     total = total + sub_g(n)
        # for k in range(n+1):
        #     total = total + (g(k, n-k) % MOD)
    return total


# G(10)
# G(100)

if __name__ == "__main__":
    NUMBER: int = 10**18
    res = G(NUMBER)
    print(f"The result for G({NUMBER}) is {res}")

