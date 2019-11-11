
"""
Purpose: Project Euler problem 686
Date created: 2019-10-30

Contributor(s):
    Mark M.

ID: 686
URI: https://projecteuler.net/problem=686
Title: Powers of Two

Status: Incomplete

Desc:
    2**7 = 128 is the first power of two whose leading digits are "12".
    The next power of two whose leading digits are "12" is 2**80.
    
    Define p(L,n) to be the nth-smallest value of j such that the base 10
    representation of 2j begins with the digits of L.
    So p(12,1)=7 and p(12,2)=80.
    
    You are also given that p(123, 45) = 12710.
    
    Find p(123, 678910).
"""

import typing as T
from typing_extensions import Protocol

Q = T.TypeVar('Q', int, float, str)
NUM = T.TypeVar('NUM', int, float)
iscalar = T.List[int]
fscalar = T.List[float]
xscalar = T.List[NUM]
qscalar = T.List[Q]


class SizedIterable(Protocol):
    def __len__(self):
        pass

    def __iter__(self):
        pass



def xSUM(it: T.Iterable[NUM], tot: NUM = 0) -> NUM:
    for i in it:
        tot += i
    return tot


def xLEN(it: T.Iterable[Q]) -> NUM:
    return xSUM([1 for i in str(it)])

def xEXP(n: NUM) -> NUM:
    return 2 ** n





def log(x: NUM, base: NUM = 2) -> NUM:
    n: NUM = 0
    while True:
        n += 1
        if base ** n == x:
            return n
            break


def log_eval(x: NUM) -> NUM:
    n: NUM = 0
    while xEXP(n) != x:
        n += 1
    return n

# [exp2(i).__next__() for i in range(1, 10)]
# [[print(x) for x in exp(i)] for i in range(1, 10)]


def str_exp(n: NUM) -> str:
    return '{}'.format(xEXP(n))


def p_worker(target: int, nth_val: NUM) -> T.Iterable[int]:
    match_count: int = 0

    N: int = 10 ** (len(target) - 2)

    idx: int = len(target)

    while match_count < nth_val:
        N += 1
        if str_exp(N)[:idx] == str(target):
            match_count += 1
            yield N


def p(L: T.Collection[int], n: int) -> NUM:
    match_list = [i for i in p_worker(L, n)]
    return match_list[-1]








# p(12, 2)

# p(123, 45) = 12710

# res = p(123, 678910)








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


if __name__ == '__main__':
    print('Calculating  p(123, 678910)...')
    L: int = 123
    n: int = 678910
    res = p(L, n)
    try:
        print('The answer is: {res}', file=open('p-686-ans.txt', 'w'))
        input('press any key to continue')
    except KeyboardInterrupt:
        pass