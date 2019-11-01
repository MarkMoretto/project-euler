
"""
Purpose: Project Euler problem 686
Date created: 2019-10-30

Contributor(s):
    Mark M.

ID: 686
URI: https://projecteuler.net/problem=686
Title: Powers of Two

Desc:
    2**7 = 128 is the first power of two whose leading digits are "12".
    The next power of two whose leading digits are "12" is 2**80.
    
    Define p(L,n) to be the nth-smallest value of j such that the base 10
    representation of 2j begins with the digits of L.
    So p(12,1)=7 and p(12,2)=80.
    
    You are also given that p(123, 45) = 12710.
    
    Find p(123, 678910).
"""




def log(x, base=2):
    n=0
    while True:
        n += 1
        if base ** n == x:
            return n
            break

def log_eval(x):
    n = 0
    while EXP2(n) != x:
        n += 1
    return n

# [exp2(i).__next__() for i in range(1, 10)]
# [[print(x) for x in exp(i)] for i in range(1, 10)]

def SUM(obj):
    tot = 0
    if obj.__iter__():
        for i in obj:
            tot += i
    return tot




LEN = lambda x: SUM([1 for i in str(x)])

EXP2 = lambda n: 2 ** n

def str_exp(n):
    return '{}'.format(EXP2(n))


def p_worker(target, nth_val):
    match_count = 0
    N = 10**(len(str(target)) - 1)
    idx = len(target)
    while match_count < nth_val:
        N += 1
        if str_exp(N, 2)[:idx] == str(target):
            match_count += 1
            yield N


def p(L, n):
    match_list = [i for i in p_worker(L, n)]:
    return match_list[-1]








p(12, 2)

res = p(123, 678910)








import unittest
class PrelimCase(unittest.TestCase):
    def test_12_1(self):
        L = 12
        n = 1
        expected = 7
        test_str = f'p({L}, {n})'
        self.assertEqual(eval(test_str), expected, 'Test for {} failed.'.format(test_str))

    def test_12_2(self):
        L = 12
        n = 2
        expected = 80
        test_str = f'p({L}, {n})'
        self.assertEqual(eval(test_str), expected, 'Test for {} failed.'.format(test_str))


    def test_123_45(self):
        L = 123
        n = 45
        expected = 12710
        test_str = f'p({L}, {n})'
        self.assertEqual(eval(test_str), expected, 'Test for {} failed.'.format(test_str))


if __name__ == 'TEST':
    unittest.main()
