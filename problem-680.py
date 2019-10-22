
"""
Purpose: Project Euler questions
Date created: 2019-10-22
Main URI: https://projecteuler.net

Problem ID: 680
URI: https://projecteuler.net/problem=680
Title: Yarra Gnisrever

Description 
    Let N and K be two positive integers.
    
    Fn is the n-th Fibonacci number:
        F1 = F2 = 1,
        Fn = Fn − 1 + Fn − 2 for all n >= 3.
    Let s{sub}n = F{sub}2n − 1 mod N and let tn = F{sub}2n mod N.
    
    Start with an array of integers A = (A[0],..., A[N−1]) where initially
    every A[i] is equal to i. Now perform K successive operations on A,
    where the j-th operation consists of reversing the order of those elements
    in A with indices between sj and tj (both ends inclusive).
    
    Define R(N, K) to be sum of i * A[i] for i=0 to N-1 after K operations.
    
    For example, R(5, 4) = 27, as can be seen from the following procedure:
    
    Initial position: (0,1,2,3,4)
    Step 1 - Reverse A[1] to A[1]: (0,1,2,3,4)
    Step 2 - Reverse A[2] to A[3]: (0,1,3,2,4)
    Step 3 - Reverse A[0] to A[3]: (2,3,1,0,4)
    Step 4 - Reverse A[3] to A[1]: (2,0,1,3,4)
    R(5,4) = 0 x 2 + 1 x 0 + 2 x 1 + 3 x 3 + 4 x 4 = 27
    Also, R(10**2,10**2)=246597 and R(10**4,10**4)=249275481640.
    
    Find R(10**18,10**6) giving your answer modulo 109.

Contributor(s): Mark M.
"""

import re
import numpy as np
import unittest

def fib(n):
    n = int(n)
    counter = 0
    a, b = 0, 1
    while counter < n:
        # print(b)
        yield b
        a, b = b, a + b
        counter += 1

# bigfib = [i for i in fib(1e6)]
nth_fib = lambda n: max([i for i in fib(n)])





N = 5
K = 4

a = [i for i in range(0, N)]
s = [i for i in range(1, K + 1)]

istart, iend = 1, 1

for i in s:
    nnorm = a[istart:iend]
    nrev = nnorm = a[istart:iend][::-1]
    indexss = f'a[{istart}] and a[{iend}]'
    print(f'Index subsection range: {indexss}')
    print(f'Norm: {nnorm}, Reverse: {nrev}')

    istart = i
    iend += istart



def R(N, K):
    rng = [nth_fib(i)%N if i > 2 else 1%N for i in range(1,N+1)]
    A = [i for i in range(0, N)]
    s = [i for i in range(1, K + 1)]


    a[2:4][::-1]


def reformat_str_part():
    tst1 = 'R(5,4)=0x2+1x0+2x1+3x3+4x4=27'
    return re.sub(r'(x|\+|\=)', r' \1 ', tst1)




class FibTestCase(unittest.TestCase):
    def test_nth_fib_10(self):
        """
            Test that nth_fib(10) == 55
        """
        test_n = 10
        expected_result = 55
        self.assertEqual(nth_fib(test_n, expected_result)



__name__ = 'TEST'

if __name__ == 'TEST':
    unittest.main()













