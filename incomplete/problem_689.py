
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


"""

import re
import typing as T
Q = T.TypeVar('Q', str, float, int,)
N = T.TypeVar('N', str, float,)
s_vec = T.List[str]
n_vec = T.List[N]



def to_decimal(n: int) -> int:
    n_str: str = str(n)
    for i, v in enumerate(n_str[::-1]):
        print(f'({v}*(2^{i}))')



tst1 = 0.890625

tmp = [i*2 for i in range(len(str(tst1)))]

def eval_float(float_value: float) -> int:
    if float_value > 1:
        return 1
    return  0


def flost_to_bin(float_value: float, lst: list = None) -> int:
    val = float_value
    max_bits = len(str(float))

    if lst is None:
        lst = list()

    while len(str(val)) > 2:
        tmp = val * 2
        print(tmp)
        lst.append(str(eval_float(tmp)))
        val = tmp % 1
        print(val)

    return (''.join(lst)[::-1])


def make_hexadecimal_dict() -> T.Dict[str, N]:
    abc_list: s_vec = ['a','b','c','d','e','f']
    tmp_dict: T.Dict[int, str] = {i:str(i) for i in range(10)}
    for i, v in enumerate(abc_list, start=10):
        tmp_dict[i] = v
    return {v:k + 0.0 for k,v in tmp_dict.items()}


hex_dict = make_hexadecimal_dict()

"""
General pattern for converting from hex string to float/decimal
May not work for 
float.hex(3740.0) # '0x1.d380000000000p+11'

-> (1 +
    (
     13./16**1 +
     3./16**2 +
     8/16**3
     ) 
    * (2.0 ** 11)

"""



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







