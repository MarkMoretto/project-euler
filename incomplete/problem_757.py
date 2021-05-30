
"""
Purpose: Project euler problem
Date created: 2021-05-16

Status: Incomplete

Problen Number: 757
Name: Not Zeckendorf
URL: https://projecteuler.net/problem=757

Contributor(s):
    Mark M.
"""

import itertools as ittr
from functools import reduce




def two_prod(a, b) -> int:
    return int(a * b)


def check_len(*args, target = 4) -> bool:
    return len([*args]) == target



def check_sum(*args) -> bool:
    lhs: int = (args[0] + args[1])
    rhs: int = (args[2] + args[3] + 1)
    return lhs == rhs


def check_prod(*args) -> bool:
    lhs: int = two_prod(args[0], args[1])
    rhs: int = two_prod(args[2], args[3])
    return lhs == rhs == args[4]




def checker(*args, n) -> bool:
    if check_len(*args):
        if check_sum(*args):
            if check_prod(*[args, n]):
                return True
    return False

checker(4,9,6,6, n = 36)

test_limit = 10**6



# check_prod(*[4,9,6,6],36)





def functests():
    # check_len()
    assert (check_len(1,2,3,4) == True), "Error: check_len() validity."
    assert (check_len(1,2,3,4, target = 4) == True), "Error: check_len() validity."
    assert (check_len(1,2,3,4, target = 5) == False), "Error: check_len() invalidity."
    assert (check_len(1,2,3,4,5) == False), "Error: check_len() invalidity."
    assert (check_len(1,2,3,4,5, target = 5) == True), "Error: check_len() validity."

    # check_sum()
    assert (check_sum(4,9,6,6) == True), "Error: check_sum() validity."

    # check_prod()
    assert (check_prod(4,9,6,6, N = 36) == True), "Error: check_prod() validity."
    assert (check_prod(4,9,6,6, N = 37) == False), "Error: check_prod() validity."
    assert (check_prod(4,9,6,6, N = 36) == False), "Error: check_prod() invalidity."
    assert (check_prod(4,9,6,6, N = 37) == True), "Error: check_prod() invalidity."