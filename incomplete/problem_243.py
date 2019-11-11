
"""
Purpose: Project Euler problems
Date created: 2019-11-08
Contributor(s): Mark M.

ID: 243
Title: Resilience
URI: https://projecteuler.net/problem=243
Difficulty: ?

Status: Incomplete

Problem:
    A positive fraction whose numerator is less than its denominator is called a 
    proper fraction.
    
    For any denominator, d, there will be d−1 proper fractions; for example, with d = 12:
        1/12, 2/12, 3/12, 4/12, 5/12, 6/12, 7/12, 8/12, 9/12, 10/12, 11/12.
    
    We shall call a fraction that cannot be cancelled down a resilient fraction.
    
    Furthermore we shall define the resilience of a denominator, R(d), to be the
    ratio of its proper fractions that are resilient; for example, R(12) = 4/11.
    
    In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10.
    
    Find the smallest denominator d, having a resilience R(d) < 15499/94744.
"""
from time import sleep
from os import getcwd
from os.path import join as pjoin
import typing as T
Q = T.TypeVar('Q', int, str, float)
N = T.TypeVar('N', int, float)
q_vec = T.List[Q]
n_vec = T.List[N]
s_vec = T.List[str]
StrFileOutput = T.NewType('StrFileOutput', str)

sample: s_vec = [
        '1/12',
        '2/12',
        '3/12',
        '4/12',
        '5/12',
        '6/12',
        '7/12',
        '8/12',
        '9/12',
        '10/12',
        '11/12',
        ]


def mABS(n: N) -> N:
    return n * -1 if n < 0 else n

def HCF(x: N, y: N) -> N:
    x, y = mABS(x), mABS(y)
    if x == 0:
        return y
    while y != 0:
        if x > y:
            x -= y
        else:
            y -= x
    return x

def print_frac(n: int, d: int) -> None:
    print(f'{n}/{d}')


def format_frac(n: int, d: int) -> str:
    return f'{n}/{d}'


def split_em(x: str, split_by: str) -> T.Iterator[str]:
    """Split a string and yield results."""
    for i in x.split(split_by):
        yield i


def fraction_generator(n: int) -> T.Iterable[str]:
    """Generate n - 1 fractions in string format."""
    for numer in range(1, n):
        yield f'{numer}/{n}'

#-- Affirm fraction_generator output
assert ([i for i in fraction_generator(12)] == sample), 'Fraction generator error!'


def split_n_check(itr: T.Collection[str], split_on: str = '/') -> T.Tuple[int, float]:
    n: int # Numerator
    d: int # Denominator
    ct: int = 0 # Running count
    t_ct: int = len(itr) # Total count
    for i in itr:
        vals = list(split_em(i, split_on))
        n, d = int(vals[0]), int(vals[1])
        if HCF(n, d) == 1:
            ct += 1
    return ct, t_ct



def R(n: int) -> str:
    count, tot_count = split_n_check([i for i in fraction_generator(n)])
    return format_frac(count, int(tot_count))


def eval_R(target_resilience: str, start: int = 10) -> T.Tuple[int, str]:
    max_resilience: float = eval(target_resilience)
    n: int = start
    current_frac: str = R(n) # Seed first calc
    while eval(current_frac) >= max_resilience:
        n += 1
        current_frac = R(n)
        # print(n, current_frac)
    return n, current_frac


# res, frac = eval_R('4/10')
# res, frac = eval_R('15499/94744')
def print_to_file(result: int, fraction: str, fn: str) -> None:
    print(f'Results of problem 243:\n\nN value: {result}\n\nFraction: {fraction}', file = fn)

def print_msg(msg: str) -> None:
    print(msg)

if __name__ == '__main__':
    start_level = 94744
    target = '15499/94744'
    filepath: str = pjoin(getcwd(), r'incomplete\problem_243_results.txt')
    print(f'Script running...\nFinding largest fraction below {target}')
    while True:
        res, frac = eval_R(target, start_level)
        print_msg('Processing complete!')
        break
    print_to_file(res, frac, filepath)
    print_msg('Goodbye!')
    sleep(2)

