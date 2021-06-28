
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

import concurrent.futures as ccf

MOD: int = 1000000007
total: int = 0

def g(m: int, n: int) -> int:
    return (m^n) + (m|n) + (m&n)

def sub_g(num):
    num += 1
    return sum((g(k, num-k) % MOD) for k in range(num))

# print("\n".join([f"{i}: {sub_g(i+1) - sub_g(i)}" for i in range(10)]))


def G(N):
    total: int = 0
    rngN = range(N+1)
    for n in rngN:
        subtot: int = 0
        for k in range(n+1):
            total = total + (g(k, n-k) % MOD)
    return total


G(10)
G(100)

if __name__ == "__main__":
    with ccf.ProcessPoolExecutor() as executor:
        fut = executor.submit(G)