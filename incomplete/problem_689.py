
"""
Purpose: Project Euler problems
Date created: 2019-11-17
Contributor(s): Mark M.

ID: 689
Title: Binary Series
URI: https://projecteuler.net/problem=689
Difficulty: ?

Status: Incomplete

Ref(s):
    https://blog.penjee.com/binary-numbers-floating-point-conversion/

Problem:



Notes:
General pattern for converting from hex string to float/decimal - 

    float.hex(3740.0)
    -> '0x1.d380000000000p+11'
    
    ---> (1 +
              (
                 13. / 16 ** 1 +
                 3. / 16 ** 2 +
                 8 / 16 ** 3
            ) 
            * (2.0 ** +11)

"""

import re
from decimal import Decimal, getcontext
import typing as T
Q = T.TypeVar('Q', str, float, int,)
N = T.TypeVar('N', str, float,)
s_vec = T.List[str]
n_vec = T.List[N]
f_vec = T.List[float]

getcontext().prec = 8

def flexRANGE(start: float, stop: float = None, increment: float = 1.0) -> T.Iterable[float]:

    if increment == 0:
        increment = Decimal('1')

    if increment > 0.0:
        if stop is None:
            stop = start
            start = 0.0

        while start < stop:
            yield float.fromhex(start.hex())
            start += increment

    elif increment < 0.0:
        if stop is None:
            stop = 0.0

        elif start < stop:
            stop = start
            start = stop

        while start > stop:
            yield float.fromhex(start.hex())
            start += increment


#-- Generate a list of values
def genRANGE(start: float, stop: float = None, increment: float = 1.0) -> f_vec:
    return [i for i in flexRANGE(start, stop, increment)]



def eval_float(float_value: float) -> int:
    if float_value >= 1.0:
        return 1
    return  0



def make_hexadecimal_dict() -> T.Dict[str, N]:
    abc_list: s_vec = ['a','b','c','d','e','f']
    tmp_dict: T.Dict[int, str] = {i:str(i) for i in range(10)}
    for i, v in enumerate(abc_list, start=10):
        tmp_dict[i] = v
    return {v:k + 0.0 for k,v in tmp_dict.items()}


hex_dict = make_hexadecimal_dict()






def enum(it: T.Iterable[Q], start: int = 0) -> T.Generator[int, Q]:
    for element in it:
        yield start, element
        start += 1



def tokenizer(it: T.Iterable[str]) -> T.Iterable[str]:
    return [it[i] for i in range(len(it))]


def eval_input(x: str) -> str:
    if isinstance(x, (int, float)):
        return float.hex(x * 1.0)
    return x


#-- Test eval_input function
assert (eval_input(4)  == '0x1.0000000000000p+2'),'Error: eval_input using integer'
assert (eval_input('0x1.0000000000000p+2') == '0x1.0000000000000p+2'),'Error: eval_input using string'


def hex_to_dec(float_or_hex: str) -> float:
    if isinstance(float_or_hex, (int, float)):
        hex_string = float.hex(float_or_hex * 1.0)
    output: str = ''

    hex_pat: str = r"""(-|\+)?0x(\d+)\.(\w*?\d+)p(.\d+)"""
    p = re.compile(hex_pat)
    sign, integer, fraction, exponent = p.findall(hex_string)[0] # Need to unpack list

    tokens = tokenizer(fraction)

    eval_list = [f'{hex_dict[v]}/16**{i}' for i, v in enum(tokens, start=1) if v.isdigit() and int(v) > 0 or v.isalpha()]
    
    output = f'({str(integer)}' + ' + '
    output += ' + '.join(eval_list)
    output += ') * ' + str(f'(2**{exponent})')

    eval(output)


tst1 = 0.890625


def float_to_binary(n: float):
    res = n * 2
    tmp = res % 1
    for i in range(23):
        # print(f'res: {res}, tmp: {tmp}')
        yield eval_float(res)
        res = tmp * 2
        tmp = res % 1

[i for i in float_to_binary(tst1)]


def d(x, nth_spot: int = 2):
    """Return nth value of floating point binary value."""
    #-- Instantiate generator
    xyz = float_to_binary(x)

    #-- Run through range, offset by 1
    for i in range(1, nth_spot + 1):
        while True:
            val = xyz.__next__()
            #-- if nth_spot met, return value
            if i == nth_spot:
                return val
            break

assert (d(0.25, 2) == 1), 'd() return value error!'




def f(x):
    n













