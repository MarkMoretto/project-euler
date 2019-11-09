
"""
Purpose: Project Euler problems
Date created: 2019-11-08
Contributor(s): Mark M.

ID: 76
Title: Counting summations
URI: https://projecteuler.net/problem=76
Difficulty: 10%

Status: Incomplete



Problem:
    It is possible to write five as a sum in exactly six different ways:
    
    4 + 1
    3 + 2
    3 + 1 + 1
    2 + 2 + 1
    2 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1
    
    How many different ways can one hundred be written as a sum of at
    least two positive integers?
"""


import typing as T


Q = T.TypeVar('Q', int, float, str)
NUM = T.TypeVar('NUM', int, float)
xvector = T.List[NUM]
ivector = T.List[int]
fvector = T.List[float]
svector = T.List[str]
qvector = T.List[Q]




def xSUM(it: T.Iterable[NUM], tot: NUM = 0) -> NUM:
    for i in it:
        tot += i
    return tot


def xLEN(it: T.Iterable[Q]) -> NUM:
    return xSUM([1 for i in str(it)])

def xEXP(n: NUM) -> NUM:
    return 2 ** n

def xRANGE(start: int, stop: int = None, increment: int = 1) -> T.Iterable[int]:

    if increment == 0:
        increment = 1

    if increment > 0:
        if stop is None:
            stop = start
            start = 0

        while start < stop:
            yield start
            start += increment

    elif increment < 0:
        if stop is None:
            stop = 0

        elif start < stop:
            stop = start
            start = stop

        while start > stop:
            yield start
            start += increment


#-- Generate a list of integers
def range_gen(start: int, stop: int = None, increment: int = 1) -> ivector:
    return [i for i in vrange(start, stop, increment)]


def factorial(n: int):
    x: int = 1
    for i in range_gen(1, n + 1):
        x *= i
    return x



#-- Absolute value (mypy)
def xABS(n: NUM) -> NUM:
    return n * -1 if ((n ^ 1) < 0) else n


def HCF(x: NUM, y: NUM) -> T.Iterable[int]:
    x, y = xABS(x), xABS(y)
    if x == 0:
        return y
    while y != 0:
        if x > y:
            x -= y
        else:
            y -= x
    return x


def vDIVIDE(x: NUM, y: NUM) -> float:
    return x / y


def permutation_eq(n: int, r: int) -> int:
    return int(factorial(n) / factorial(n - r))

def combination_eq(n: int, r: int) -> int:
    return int(factorial(n) / factorial(n - r) * factorial(r))


def lte_target(tot: int, trgt: int) -> bool:
    """ Is the sum less than or equal to the target?"""
    return True if tot <= trgt else False

def gen_ones(n: int) -> ivector:
    """Return vector of 1s"""
    return [1] * n


#-- Integers must be positive
#-- Max number of items on a list is the target number (repeating 1s)
N: int = 5
index_range = range_gen(0, N)
incr_range = range_gen(1, N - 1)

count = 0
while N > 1:
    #-- Generate vector of length N filled with 1s
    ones = gen_ones(N)

    #-- If the sum of the largest vector equals the target, increment
    #-- counter by 1.
    if xSUM(gen_ones(N)) == N:
        count += 1

    else:
        for i in index_range:
            for j in incr_range:
                ones[i] += 1
                print(ones)
                if lte_target(ones, N):
                    counter += 1
                else:


        N -= 1


###-- Matrix action
# def gen_matrix(rows: int, cols: int) -> T.Iterable[int]:
#     return [[1 for c in xRANGE(cols)] for r in xRANGE(rows)]
# matrix = gen_matrix(N, N)


def gen_lower_matrix(rows: int, cols: int) -> T.Iterable[int]:
    return [[1 if c <= r else 0 for c in xRANGE(cols)] for r in xRANGE(rows)]

def min_threshold_matrix(it: T.Iterable[NUM], threshold: NUM = 1) -> T.Iterable[int]:
    return [row for row in it if xSUM(row) > 1]

lmatrix = min_threshold_matrix(gen_lower_matrix(N, N), 2)

counter = 0
for row in lmatrix:
    if xSUM(row) == N:
        counter += 1
    else:
        base = row
        for i in xRANGE(xLEN(base)):
            base[i] += 1
            if lte_target(xSUM(base), N):
                counter += 1
            else:
                base[i] =- 1


        while lte_target(xSUM(row), N):
            for c in row:
                lmatrix[row][c] += 1

        tmp = lmatrix[r]
        for c in xRANGE(xLEN(r) - ):


for row in lmatrix:
    for c in row:
        print(row, c)





