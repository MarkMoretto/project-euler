
"""
Purpose: Project Euler problems
Date created: 2019-10-26

Contributor(s): Mark M.

ID: 26
Title: Reciprocal cycles
URI: https://projecteuler.net/problem=26
Status: Incomplete

Desc:
    A unit fraction contains 1 in the numerator. The decimal representation of
    the unit fractions with denominators 2 to 10 are given:
    
        1/2	 = 	0.5
        1/3	 = 	0.(3)
        1/4	 = 	0.25
        1/5	 = 	0.2
        1/6	 = 	0.1(6)
        1/7	 = 	0.(142857)
        1/8	 = 	0.125
        1/9	 = 	0.(1)
        1/10 = 	0.1 
    
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
    be seen that 1/7 has a 6-digit recurring cycle.
    
    Find the value of d < 1000 for which 1/d contains the longest recurring
    cycle in its decimal fraction part.

"""


def RANGE(start, stop=None, increment=1):
    if stop is None:
        stop = start
        start = 1
    value_list = sorted([start, stop])

    if increment == 0:
        print('Error! Please enter nonzero increment value!')
    else:
        value_list = sorted([start, stop])
        if increment < 0:
            start = value_list[1]
            stop = value_list[0]
            while start >= stop:
                worker = start
                start += increment
                yield worker
        else:
            start = value_list[0]
            stop = value_list[1]
            while start < stop:
                worker = start
                start += increment
                yield worker


def SUM(iterable):
    """Pass matrix to iter_vals function; increment and return total"""
    tot = 0.0
    for v in iterable:
        tot += v
    return tot


def LEN(x):
    x = str(x)
    return int(SUM([1 for i in x]))

REPEAT = lambda obj, n: ''.join([obj for i in RANGE(n+1)])


from decimal import Decimal as D # For accuracy sake


max_len = 0
max_val = 0
for i in RANGE(999, 1):
    x = D.from_float(1 / i)
    for j in RANGE(2, 20):
        y = (x * 10 ** j)
        denom = int(REPEAT('9', j))
        y_eval = (y / denom)
        if round((y % y_eval), j) == round(x, j):
            if j > max_len:
                max_len = j
                max_val = i

























