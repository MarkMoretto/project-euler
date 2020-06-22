
"""
Purpose: Project Euler exercises
Date created: 2020-06-19

Problen Number: 50
Name: Consecutive prime sum
URL: https://projecteuler.net/problem=50

Contributor(s):
    Mark M.
"""

import itertools as ittr


class Worker:
    def __init__(self, current_list):
        self.current = current_list
        self.current_sum = sum(self.current)
        self.current_len = len(self.current)


def sieve(n):
    """generates primes up to n."""
    s = [True] * (n + 1)
    for p in range(2, n):
        if s[p]:
            yield p
            for i in range(p * p, n, p):
                s[i] = False



if __name__ == "__main__":

    N = int(1e6)
    
    primes = list(sieve(N))
    qprimes = list(sieve(N//4))
    max_rng = len(qprimes)
    max_len = 0
    
    for i in range(max_rng):
        for j in range(i+2, max_rng + 1):
    
            w = Worker(qprimes[i:j])
    
            if w.current_sum in primes:
                if w.current_len > max_len:
                    max_len = w.current_len
                    top_result = dict(
                            values=w.current,
                            prime_value=w.current_sum,
                            list_length=w.current_len
                            )
                    print(top_result["prime_value"], top_result["list_length"])









