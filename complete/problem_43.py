
"""
Purpose: Project Euler exercises
Date created: 2020-06-08

Problen Number: 43
Name: Number Sub-string divisibility
URL: https://projecteuler.net/problem=43

Contributor(s):
    Mark M.

Description:


    The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each
    of the digits 0 to 9 in some order, but it also has a rather interesting sub-string
    divisibility property.
    
    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the
    following:

        d2d3d4=406 is divisible by 2
        d3d4d5=063 is divisible by 3
        d4d5d6=635 is divisible by 5
        d5d6d7=357 is divisible by 7
        d6d7d8=572 is divisible by 11
        d7d8d9=728 is divisible by 13
        d8d9d10=289 is divisible by 17
    
    Find the sum of all 0 to 9 pandigital numbers with this property.
"""

import itertools as ittr

# nums = list(range(10))
# primes = [2,3,5,7,11,13,17,]
# nums = 1406357289

def nlist(num, base = 10):
    """Convert integer to list of digits for a given base."""
    out=[]
    while num:
        num, rem = divmod(num, base)
        out.append(rem)
    return out[::-1]


def njoin(iterable):
    """
    Function to join digits of list into single integer.
    Note: This function will only work for chunk sizes of 3.
    """
    return (iterable[0]*100)+(iterable[1]*10)+(iterable[2])

def divisor_kv(gen, primes = [2,3,5,7,11,13,17,]):
    """Function to map range keys to prime number list."""
    return {k:v for k, v in zip(gen, primes)}

def to_int(iterable):
    """Convert tuple or list of digits to single integer."""
    return int("".join(map(str, iterable)))


# Set variables used in process.

START = 1 # Starting value for range.
CHUNKSIZE = 3 # What step size to use for each subgroup
N_DIGITS = 10 # Number of digits (0 - 9)
END = N_DIGITS - CHUNKSIZE + 1 # Max value in range()
PDICT = divisor_kv(range(START, END)) # Primes dictionary

def evaluate(n_iter):
    """Function to evaluate """
    tot = 0
    rng = range(START, END)
    for i in rng:
        tot += njoin(n_iter[i:i+CHUNKSIZE]) % PDICT[i]
    return tot


# Affirm evaluate() function on test case.
assert (evaluate([1, 4, 0, 6, 3, 5, 7, 2, 8, 9]) == 0), "Error: evaluate() test case."


if __name__ == "__main__":

    # Variable to hold final result.
    TOTAL = 0

    # Generated list of digits 1 - 9.
    NUMS = list(range(10))

    # Permutation generator.
    perms = ittr.permutations(NUMS, 10)

    # Iterate permutations; Evaluate
    # If valid, increment TOTAL by resulting integer value.
    for p in perms:
        if evaluate(p) == 0:
            TOTAL += to_int(p)
    print(f"The result is: {TOTAL}")















