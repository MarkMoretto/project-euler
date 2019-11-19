
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
import typing as T
Q = T.TypeVar('Q', str, float, int,)
N = T.TypeVar('N', str, float,)
s_vec = T.List[str]
n_vec = T.List[N]



def eval_float(float_value: float) -> int:
    """
    Function to determine if float value greater than 1.
    """
    if float_value > 1:
        return 1
    return  0



def make_hexadecimal_dict() -> T.Dict[str, N]:
    """
        Hex dict:
            First 10 numbers are the same, then a - f are enumerated.
            In total, there should be 16 values.
    """
    abc_list: s_vec = ['a','b','c','d','e','f']
    tmp_dict: T.Dict[int, str] = {i:str(i) for i in range(10)}
    for i, v in enumerate(abc_list, start=10):
        tmp_dict[i] = v
    return {v:k + 0.0 for k,v in tmp_dict.items()}

#-- Create hexadecimal dictionary
hex_dict = make_hexadecimal_dict()



def enum(it: T.Iterable[Q], start: int = 0) -> T.Iterator[T.Tuple[int, Q]]:
    """
    Enumeration function.
    """
    for element in it:
        yield start, element
        start += 1


#-- Test enum() function.
assert ([[i,v] for i, v in enum(['a','b','c','d',])] == \
         [[0, 'a'], [1, 'b'], [2, 'c'], [3, 'd']]), 'Error with enum() function.'


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
    hex_string: str = eval_input(float_or_hex)

    output: str

    #-- Regular expression to decompose output string.
    hex_pat: str = r"""(-|\+)?0x(\d+)\.(\w*?\d+)p(.\d+)"""
    p = re.compile(hex_pat)
    sign, integer, fraction, exponent = p.findall(hex_string)[0]

    #-- Easier to iterate a list of values
    tokens = tokenizer(fraction)

    #-- Format a list to evaluate binary parts
    eval_list = [f'{hex_dict[v]}/16**{i}' for i, v in enum(tokens, start=1) if v.isdigit() and int(v) > 0 or v.isalpha()]

    ###-- Generate a string to evalute
    ### TODO: Turn this into a separate function with no return value.
    output = f'({str(integer)}'
    if len(eval_list) > 0:
        output += ' + ' + ' + '.join(eval_list)
    output += ') * ' + str(f'(2**{exponent})')

    #-- Return results of call to eval()
    return eval(output) * 1.0


#-- Affirm hex_to_dec output
assert (hex_to_dec('0x1.d380000000000p+11') == 3740.0), 'hex_to_dec error for value 3740.0'
assert (hex_to_dec('0x1.0000000000000p+2') == 4.0), 'hex_to_dec error for value 4.0'





