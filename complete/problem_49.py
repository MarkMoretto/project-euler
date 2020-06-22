
"""
Purpose: Project Euler exercises
Date created: 2020-06-19

Problen Number: 49
Name: Prime permutations
URL: https://projecteuler.net/problem=49

Contributor(s):
    Mark M.
"""

import itertools as ittr


def sieve(n):
    """generates primes up to n."""
    s = [True] * (n + 1)
    for p in range(2, n):
        if s[p]:
            yield p
            for i in range(p * p, n, p):
                s[i] = False



def get_permutations(n):
    """generates tuples of 3 permutations each within range n."""
    permut_primes = dict()
    for p in sieve(n):
        permut_primes.setdefault(''.join(sorted(str(p))), []).append(p)
    for perms in permut_primes.values():
        for a, b, c in ittr.combinations(perms, 3):
            assert c > b > a
            yield a, b, c


def run(n):
    """checks permutations within range n for subtraction rules.
    returns valid permutations."""
    permutations = get_permutations(n)
    for x, y, z in permutations:
        if abs(x - y) == abs(y - z) and x != 1487:
            return x, y, z

if __name__ == "__main__":
    x, y, z = run(10000)
    print(f"The values are x: {x}, y: {y}, z: {z}")
    print(f"The combined result is: {x}{y}{z}")

