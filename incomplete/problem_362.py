
"""
Purpose: Project Euler exercises
Date created: 2020-06-25

Problen Number: 362
Name: Squarefree factors
URL: https://projecteuler.net/problem=362

Contributor(s):
    Mark M.

Description:
    Consider the number 54.

    54 can be factored in 7 distinct ways into one or more factors larger than 1:
        54,
        2×27,
        3×18,
        6×9,
        3×3×6,
        2×3×9 and
        2×3×3×3.

    If we require that the factors are all squarefree only two ways remain: 3×3×6 and 2×3×3×3.
    
    Let's call Fsf(n) the number of ways n can be factored into one or more squarefree factors larger than 1, so Fsf(54)=2.
    
    Let S(n) be ∑ Fsf(k) for k=2 to n.
    
    S(100)=193.
    
    Find S(10 000 000 000).
"""

import math
PI = math.pi

sf_nums = [1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30, 31,
           33, 34, 35, 37, 38, 39, 41, 42, 43, 46, 47, 51, 53, 55, 57, 58, 59, 61, 62,
           65, 66, 67]


def prime_factor_gen(n):
    i = 2
    while pow(i, 2) <= n:
        if n % i:
            i += 1
        else:
            n //= i
            yield i
    if n > 1:
        yield n


def pfactors(n):
    return [i for i in prime_factor_gen(n)]



def is_square_free(prime_factors: list) -> bool:
    """
    # doctest: +NORMALIZE_WHITESPACE
    This functions takes a list of prime factors as input.
    returns True if the factors are square free.
    >>> is_square_free([1, 1, 2, 3, 4])
    False
    
    These are wrong but should return some value
    it simply checks for repition in the numbers.
    >>> is_square_free([1, 3, 4, 'sd', 0.0])
    True
    
    >>> is_square_free([2, 5]) # Prime factors of 10
    True
    >>> is_square_free([2, 2, 3]) # Prime factors of 12
    False
    >>> is_square_free('asd')
    True
    >>> is_square_free(24)
    Traceback (most recent call last):
        ...
    TypeError: 'int' object is not iterable
    """
    return len(set(prime_factors)) == len(prime_factors)




# https://github.com/TheAlgorithms/Python/blob/ad2db80f8aeba7fe407eccd69327cfb3bdfaacd2/maths/factors.py
def factors_of_a_number(num: int) -> list:
    """
    >>> factors_of_a_number(54)
    [2, 3, 6, 9, 18, 27, 54]
    >>> factors_of_a_number(24)
    [2, 3, 4, 6, 8, 12, 24]
    >>> factors_of_a_number(-24)
    []
    """
    return [i for i in range(2, num) if num % i == 0]


N = 54
facts = factors_of_a_number(N)
pfacts = pfactors(N)
sq_facts = {f: f**2 for f in facts}




for i in sq_facts.keys():
    for fsq in sq_facts.values():
        if i % fsq == 0:
            print(i, ": ", fsq)



def is_square_free(factors: list) -> bool:
    if isinstance(all(facts), int):

        square_factors = {f: f**2 for f in factors}

        result: bool = True

        for factor in square_factors.keys():
            if factor > 1:
                for f_squared in square_factors.values():
                    if not factor is f_squared:
                        if factor % f_squared == 0:
                            result = False
                            break
        return result

is_square_free([1, 2, 3,])


def is_square_free(factors: List[int]) -> bool:
    """
    # doctest: +NORMALIZE_WHITESPACE
    This functions takes a list of prime factors as input.
    returns True if the factors are square free.
    >>> is_square_free([1, 1, 2, 3, 4])
    False
    
    These are wrong but should return some value
    it simply checks for repition in the numbers.
    >>> is_square_free([1, 3, 4, 'sd', 0.0])
    True
    
    >>> is_square_free([1, 0.5, 2, 0.0])
    True
    >>> is_square_free([1, 2, 2, 5])
    False
    >>> is_square_free('asd')
    True
    >>> is_square_free(24)
    Traceback (most recent call last):
        ...
    TypeError: 'int' object is not iterable
    """
    return len(set(factors)) == len(factors)


if __name__ == "__main__":
    import doctest

    doctest.testmod()




def factor_combos(n):
    out = []

    prod = 1
    prev_n = 2

    while prod != n:

        arr = []

        for i in range(prev_n, n):
            if (i * prod) > n:
                break
            if n % i == 0:
                arr.append(i)
                prev_n = i
                prod *= i

        out.append(arr)
    return out


factor_combos(10)


# factors_of_a_number(10)
# [2, 5, 10]











