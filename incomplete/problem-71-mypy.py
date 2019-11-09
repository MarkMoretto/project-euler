
"""
Purpose: Project Euler problems
Date created: 2019-11-05
Contributor(s): Mark M.

ID: 71
Title: Ordered fractions
URI: https://projecteuler.net/problem=71
Difficulty: 10%

Status: Incomplete

Additional notes:
    Uses mypy (https://mypy.readthedocs.io/en/latest/)

Desc: 
    Consider the fraction, n/d, where n and d are positive integers. If n<d
    and HCF(n,d)=1, it is called a reduced proper fraction.
    
    If we list the set of reduced proper fractions for d ≤ 8 in ascending order
    of size, we get:
    
    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
    5/7, 3/4, 4/5, 5/6, 6/7, 7/8
    
    It can be seen that 2/5 is the fraction immediately to the left of 3/7.
    
    By listing the set of reduced proper fractions for d ≤ 1,000,000 in
    ascending order of size, find the numerator of the fraction immediately to
    the left of 3/7.

"""
# https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html
# https://docs.python.org/3/library/typing.html


import typing as T

NUM = T.TypeVar('NUM', int, float)
xvector = T.List[NUM]
fvector = T.List[float]
ivector = T.List[int]
svector = T.List[str]




def vrange(start: int, stop: int = None, increment: int = 1) -> T.Iterable[int]:

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

# vHCF = np.vectorize(HCF, cache=False)


# def frac_gen(x, y):


#-- Set variables
#-- d = max_value, target = fraction to find, support = minimum fraction

d: int = int(1e3)
target: float = 3/7
support: float = 2/5


#-- Create two lists for numerators and denominators
numer = range_gen(1, d + 1)
denom = range_gen(1, d + 1)


#-- Create vector of fraction strings
target_str: str = '3/7'
support_str: str = '2/5'

def gen_frac_str_matrix(numer: T.Iterable[int], denom: T.Iterable[int]) -> svector:
    return [f'{n}/{d}' for n in numer for d in denom if n != d and n < d and HCF(n, d) == 1]

# frac_str_grid = [f'{n}/{d}' for n in numer for d in denom if n != d and n < d]
frac_str_grid = gen_frac_str_matrix(numer, denom)


#--Generator
frac_str_grid[frac_str_grid.index(target_str)]
frac_str_grid[frac_str_grid.index(target_str) - 1]


#-- Create fractions vector
#-- Conditions:
#--     1. n / d < 1
#--     2. n / d < target
#--     3. n / d > support

# frac_vec = np.array([np.divide(n, d) for n in numer for d in denom \
#                       if np.divide(n, d) < 1 \
#                       and np.divide(n, d) < target \
#                       and np.divide(n, d) > support])



def gen_frac_grid(numer: T.Iterable[int], denom: T.Iterable[int]) -> fvector:
    return [vDIVIDE(n, d) for n in numer for d in denom if n != d and n < d and HCF(n, d) == 1]

frac_grid = gen_frac_grid(numer, denom)



#-- Merge the string and float vectors
def dictionize(x: T.Iterable[str], y: T.Iterable[float]) -> T.Dict[str, float]:
    return {k:v for k, v in zip(x, y)}

def enum_num_dict(x: T.Iterable[NUM]) -> T.Dict[int, NUM]:
    return {k:v for k, v in enumerate(x)}

def enum_str_dict(x: T.Iterable[str]) -> T.Dict[int, str]:
    return {k:v for k, v in enumerate(x)}

fdict = dictionize(frac_str_grid, frac_grid)
fdict = dict(sorted(fdict.items(), key = lambda x: x[1]))
fdict.get(target_str)

enum_frac_grid = enum_num_dict(frac_grid)
enum_frac_str_grid = enum_str_dict(frac_str_grid)

#--TODO: Use index from composite dictionary to find index in enumerated dictionaries
#-- and eventually find a solution.




#-- Reduce values to between support and target
max_val = max(qrs)
target_rc = frac_str_grid[np.where(qrs == max_val)]

















