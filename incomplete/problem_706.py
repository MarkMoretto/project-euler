
"""
Purpose: Project Euler problems
Date created: 2020-03-15

ID: 706
Title: 3-Like Numbers
URI: https://projecteuler.net/problem=706
Status: Complete
Contributor(s): Mark Moretto

Description:
    For a positive integer n, define f(n) to be the number of non-empty substrings of n
    that are divisible by 3. For example, the string "2573" has 10 non-empty substrings,
    three of which represent numbers that are divisible by 3, namely 57, 573 and 3.
    So f(2573) = 3.
    
    If f(n) is divisible by 3 then we say that n is 3-like.

    Define F(d) to be how many d digit numbers are 3-like.
    For example, F(2)=30 and F(6)=290898.
    
    Find F(105). Give your answer modulo 1000000007.
"""
import gc
import numpy as np
from array import array
gc.enable()

def f_gen(num):
    iterable = str(num)
    rng = array("Q", [i for i in range(len(iterable) + 1)])
    for i in rng:
        for j in rng:
            v = iterable[i:j]
            if v:
                if int(v) % 3 == 0:
                    yield 1



def f(n):
    return sum([i for i in f_gen(n)])



[iterable[i:j] for i in ]

assert (f("2573") == 3), f"Error: f() for {test1} failed."


def F(d):
    """
    Find how many f(n) values are evenly divisible by 3. 
    Param:
        d = number of digits.
    """

    start_ = int(f"{1:0<{d}}")
    end_ = int(f"{1:0<{d + 1}}")

    rng = array("Q", [i for i in range(start_, end_)])

    counter = [1 for i in rng if f(i) % 3 == 0]

    return sum(counter) % 1000000007



def test_F():
    assert (F(2) == 30), f"Error: F(2) test failed."
    assert (F(6) == 290898), f"Error: F(6) test failed."


target = int(1e5)
result = F(target)





import os
os.environ["THEANO_FLAGS"] = 'device=cpu,floatX=float32'

from theano import function, config, shared, tensor
import numpy as np
import time










