

"""
Purpose: Project Euler problems
Date created: 2019-10-24

Contributor(s): Mark M.

ID: 675
Title: 2**w(n)
URI: https://projecteuler.net/problem=675
Status: Incomplete

Desc:
	Let ω(n) denote the number of distinct prime divisors of a positive integer n.

	So ω(1)=0 and ω(360) = ω(2**3 × 3**2 × 5) = 3.

	Let S(n) be sum(d|n) 2**ω(d). 

	E.g. S(6)=2**ω(1)+2**ω(2)+2**ω(3)+2**ω(6)=2**0+2**1+2**1+2**2=9.

	Let F(n) = sum(ni) = 2S(i!).
    Then,
        F(10)=4821.

	Find F(10000000). Give your answer modulo 1000000087.
"""

import ctypes as C
import numpy as np

import msvcrt

counter = 0
while counter < 10:
    tmplist = list()
    if msvcrt.kbhit():
        tmplist.append(msvcrt.getch())
        counter += 1

n = C.c_ulonglong(5)
n_Ptr = C.pointer(n)



def w(n, outlist=None):
    if outlist is None:
        outlist = list()
    for i in range(2, n + 1):
        if n % 2 == 0:
            outlist.append(2)
        for i in range(2, n/2):
            if i*i <=n:
                if n % i == 0:
                    outlist.append(i)
    print(outlist)





w(1)


# Function to find the smallest divisor 
def smallestDivisor(n): 
  
    # if divisible by 2 
    if (n % 2 == 0): 
        return 2

    # iterate from 3 to sqrt(n) 
    i = 3;  
    while(i * i <= n): 
        if (n % i == 0): 
            return i
        i += 2
  
    return n

