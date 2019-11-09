
"""
Purpose: Project Euler problems
Date created: 2019-10-26

Contributor(s): Mark M.

ID: 4
Title: Largest palindrome product
URI: https://projecteuler.net/problem=4
Status: Incomplete

Desc:
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.
    
    Find the largest palindrome made from the product of two 3-digit numbers.
"""

def RANGE(start, stop, increment=1):
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

# 2-digit
max_val = 0
max_i = 0
max_j = 0
for i in RANGE(99, 10, -1):
    for j in RANGE(99, 10, 1):
        current_val = i*j
        current_i = i
        current_j = j
        if str(current_val) == str(current_val)[::-1]:
            if current_val > max_val:
                max_val = current_val
                max_i = i
                max_j = j


# 3-digit
max_val = 0
max_i = 0
max_j = 0
for i in RANGE(100, 999, -1):
    for j in RANGE(100, 1000, 1):
        current_val = i*j
        current_i = i
        current_j = j
        if str(current_val) == str(current_val)[::-1]:
            if current_val > max_val:
                max_val = current_val
                max_i = i
                max_j = j
