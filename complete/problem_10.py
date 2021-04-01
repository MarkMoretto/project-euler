
"""
Purpose: Project euler problem
Date created: 2021-03-31

Problen Number: 10
Name: Summation of primes
URL: https://projecteuler.net/problem=10

Contributor(s):
    Mark M.
"""


def gen_primes():
    """Prime generator.
    """
    D = {}
    q = 2

    while True:
        if q not in D:

            yield q

            D[q * q] = [q]

        else:
            for p in D[q]:

                D.setdefault(p + q, []).append(p)

            del D[q]
        
        q += 1


def prime_sum_to_n(n):
    tot = 0
    for gp in gen_primes():
        prime = gp
        if prime >= n:
            break
        tot += prime
    return tot

res = prime_sum_to_n(2000000)
print(f"The sum of prime numbers below 2 million is: {res:,}")

