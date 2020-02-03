
"""
Purpose: Project Euler problems
Date created: 2020-02-03

Contributor(s):
    Mark M.

ID: 700
Title: Eulercoin
URI: https://projecteuler.net/problem=700
Difficulty: ?

Status: Incomplete
"""



def eulercoin(x):
    return (1504170715041707 * x) % 4503599627370517



n = 1
ec_dict = dict()

prev = eulercoin(n)
ec_dict[n] = prev
while True:
    n += 1
    curr = eulercoin(n)
    if curr > 0:
        qual_chk = sum([1 for i in ec_dict.values() if curr < i])
        if qual_chk == 0:
            ec_dict[n] = curr
        prev = curr
    else:
        break


