
"""
Purpose: Project Euler exercises
Date created: 2021-01-01

Problen Number: 734
Name: A bit of prime
URL: https://projecteuler.net/problem=734
Contributor(s):
    Mark M.
"""


def getbin(N):
    tmp = bin(N).split("b")[1]
    return f"{tmp:0>36}"


def evalbin(n1, n2):
    a = getbin(n1)
    b = getbin(n2)
    tmp = "".join([f"{int(i[0])|int(i[1])}" for i in list(zip(a, b))])
    return int(tmp, 2)

# a = getbin(10)
# b = getbin(6)
evalbin(5, 5)

