
"""
Purpose: Project Euler exercise
Date created: 2020-06-08

Problen Number: 25
Name: 1000-digit Fibonacci number
URL: https://projecteuler.net/problem=25


Contributor(s):
    Mark M.

Description:

    The Fibonacci sequence is defined by the recurrence relation:
    
        Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
    
    Hence the first 12 terms will be:
    
        F1 = 1
        F2 = 1
        F3 = 2
        F4 = 3
        F5 = 5
        F6 = 8
        F7 = 13
        F8 = 21
        F9 = 34
        F10 = 55
        F11 = 89
        F12 = 144
    
    The 12th term, F12, is the first term to contain three digits.
    
    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

import gc
from functools import lru_cache
gc.enable()


@lru_cache(None)
def cfib(n):
    """
    Using cache method to expedite calculation.
    """
    if n < 2:
        return n
    return cfib(n-1) + cfib(n-2)


if __name__ == "__main__":
    target_length = 1000
    i = 400
    while True:
        i += 1
        res = len(f"{cfib(i)}")
        if res == target_length:
            print(i)
            break
        if i % 500 == 0:
            print(f"i = {i}")

