
"""
Purpose: Project Euler exercises
Date created: 2020-06-25

Problen Number: 358
Name: Cyclic numbers
URL: https://projecteuler.net/problem=358

Contributor(s):
    Mark M.

Description:
    A cyclic number with n digits has a very interesting property:
    When it is mmultiplied by 1, 2, 3, 4, ... n, all the products have exactly the same
    digits, in the same order, but rotated in a circular fashion!
    
    The smallest cyclic number is the 6-digit number 142857 :
    142857 × 1 = 142857
    142857 × 2 = 285714
    142857 × 3 = 428571
    142857 × 4 = 571428
    142857 × 5 = 714285
    142857 × 6 = 857142
    
    The next cyclic number is 0588235294117647 with 16 digits:
    0588235294117647 × 1 = 0588235294117647
    0588235294117647 × 2 = 1176470588235294
    0588235294117647 × 3 = 1764705882352941
    ...
    
    0588235294117647 × 16 = 9411764705882352
    
    Note that for cyclic numbers, leading zeros are important.
    
    There is only one cyclic number for which, the eleven leftmost digits are
    00000000137 and the five rightmost digits are 56789 (i.e., it has the form
    00000000137...56789 with an unknown number of digits in the middle).

    Find the sum of all its digits.
"""

from itertools import product as ittr_product
# from functools import lru_cache
import concurrent.futures as ccf


class Formatter:
    def __init__(self, length):
        self.length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if not isinstance(value, int):
            print("Error! Integer type expected.")
        else:
            self.__length = value

    def zeropad(self, numeric_string):
        return f"{numeric_string:>0{self.__length}}"




# @lru_cache(maxsize=None)
def rotator(num_str: str):
    """
    Rotate a string of numbers indefinitely.

    >>> next(rotator('012345'))
    '012345'
    >>> r = rotator(012345)
    Traceback (most recent call last):
        ...
    SyntaxError: invalid token
    """
    # Check if argument is string type; Raise exception if not.
    if not isinstance(num_str, str):
        raise SyntaxError("Integer string required")

    ns = num_str

    zp = Formatter(len(num_str))

    while True:
        yield zp.zeropad(ns)
        ns = f"{ns[-1]}{ns[:-1]}"


def producter(length: int):
    """
    Generator for the product of a collection of numbers.  Numbers range from 0 to 9.
    Output is string since we want to keep any leading zeroes.

    Parameters:
        length - length of product collections to output.

    >>> p = producter(5)
    >>> next(p)
    '00001'
    """
    # x = list(range(0, 10))
    rng = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    p = ittr_product(rng, repeat=length)

    # Advance iterable by 1 to avoid all zeroes tuple.
    p.__next__()

    while True:
        tmp = next(p)
        yield "".join([f"{n}" for n in tmp])


def evaluator(ns: str):
    """
    Function to evaluate each numeric collection.
    :param: ns - number string
    """
    n = int(ns)

    equal_ct = 0

    zp = Formatter(len(ns))

    r = rotator(ns)
    cycles = [next(r) for _ in range(n_len)]
    
    for i in range(1, n_len + 1):
        if zp.zeropad(f"{n * i}") in cycles:
            equal_ct += 1

    if equal_ct == n_len:
        print("cyclic number found!")
        return ns


def run(target_length: int = 6):
    p = producter(target_length)
    result = None
    while result is None:
        current_p = next(p)
        result = evaluator(current_p)
    print(result)



# __name__ = "__test__"

# if __name__ == "__test__":
#     import doctest
#     doctest.testmod()



if __name__ == "__main__":
    LENGTH = 6
    run(LENGTH)












# def permutationer(length: int):
#     """
#     Generator for numeric permutations.  Numbers range from 0 to 9.
#     Output is string since we want to keep any leading zeroes.

#     Parameters:
#         length - length of permutation collections to output.
#     """
#     p = ittr.permutations(range(0, 10), length)
#     while True:
#         tmp = next(p)
#         yield "".join([f"{n}" for n in tmp])