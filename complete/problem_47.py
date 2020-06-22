
"""
Purpose: Project Euler exercises
Date created: 2020-06-19

Problen Number: 47
Name: Unpredictable Permutations
URL: https://projecteuler.net/problem=47

Contributor(s):
    Mark M.
"""

from functools import lru_cache



def unique_prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors


def test_upf():
    '''Test unique_prime_factors function against known results.'''
    unique_prime_factors(14) == set([2, 7])
    unique_prime_factors(15) == set([3, 5])
    unique_prime_factors(644) == set([2, 7, 23])
    unique_prime_factors(645) == set([3, 5, 43])
    unique_prime_factors(646) == set([2, 17, 19])



@lru_cache(maxsize=5)
def upf_len(num):
    """Helper function to memoize upf() length results for a given value."""
    return len(unique_prime_factors(num))



# ####### Method 1 #######

def run(n, results):
    """Run function to find first"""
    i = 2
    success = 0
    while success < 1:
        a, b, c, d = i, i + 1, i + 2, i + 3
        resA = upf_len(a)
        resB = upf_len(b)
        resC = upf_len(c)
        resD = upf_len(d)
        if resA == resB == resC == resD == n:
            success += 1
            results.extend([a, b, c, d])
        i += 1



# ####### Method 2 #######

def equality(iterable):
    """Check equality of all elements in interable."""
    return iterable[1:] == iterable[:-1]


def run2(n):
    """Run function to find first. This may be a little quicker than run()."""
    i = 2
    success = 0
    out = []
    while success < 1:
        # Increment each value of a generated range
        group = list(map(lambda x, y=i: y + x, [i for i in range(n)]))

        # Run elements through out unique_prime_factors function
        # Append our target number to the end.
        checker = list(map(upf_len, group))
        checker.append(n)

        # If all numbers in the list are euqal, increment our success variable
        # to exit the while loop and return the current group of numbers.
        if equality(checker):
            success += 1
            return group
        i += 1



if __name__ == "__main__":

    N = 3

    # results = []
    # run(N, results)

    results = run2(N)

    print(f"The results for N = {N}: {results}")












