
"""
Purpose: Project euler problem
Date created: 2021-08-08

Status: Incomplete

Problen Number: 655
Name: Divisible Palindromes
URL: https://projecteuler.net/problem=655

Contributor(s):
    Mark M.

Description - 

The numbers 545, 5995 and 15151 are the three smallest palindromes
divisible by 109. There are nine palindromes less than 100000 which are divisible
by 109.

How many palindromes less than 10**32 are divisible by 10000019?
"""

from functools import lru_cache as cache

@cache(maxsize=300)
def reverse_n(n: int) -> int:
    reverse = 0
    while n > 0:
        tmp = n % 10
        reverse = reverse * 10 + tmp
        n //= 10
    return reverse

@cache(maxsize=300)
def is_palindrome_n(n: int) -> bool:
    rev = reverse_n(n)
    return rev == n


def srange(start, stop = None, step = 1):
    """Return generator for range of strings."""
    if stop is None:
        stop = start
        start = 0
    if start < stop:
        yield f"{start}"
        yield from srange(start + step, stop, step)



a = [545, 5995, 15151, 64746, 74447, 79897, 84148, 89598, 99299]
lenmap = dict(zip(list(map(str, correct)), list(map(lambda q: len(f"{q}"), correct))))

num_string: str = "59"
numlen = len(num_string)
# lhs = num_string[:numlen - 1]
# rhs = lhs[::-1]



def get_palindrome(num: int):
    if isinstance(num, (int,float)):
        num = str(num)
    numlen = len(num)
    if numlen <= 1:
        return num
    if numlen & 1 == 1:
        lhs = num[:numlen - 1]
        mid = num[numlen - 1]
    else:
        lhs = num
        mid = ""
    rhs = lhs[::-1]
    return int(f"{lhs}{mid}{rhs}")

# get_palindrome("59")
# get_palindrome("151")


for i in srange(10):
    print(i)

def is_palindrome(string):
    return get_palindrome(string) == string

divisor = 109
max_value = int(1e5)
s_max_value = f"{max_value}"
sqrt_max_val = int(max_value ** (1/2))
qtr_max_val = max_value // 4

res = {n:get_palindrome(n) for n in srange(10, max_value>>6) if get_palindrome(n) % divisor == 0}

res = {n:get_palindrome(n) for n in srange(10, 100)}


ddict = {}
for n in srange(10, max_value>>6):
    if n > s_max_value:
        break
    ddict[n] = get_palindrome(n)


res = [n for n in range(divisor, int(max_value ** (1/2)), divisor) if is_palindrome(f"{n}")]

# DIVISOR: int = 10000019
# MAX_N: int = int(1e32)

def run(max_value: int, divisor: int) -> int:
    # n_correct = 0
    # for n in range(DIVISOR, MAX_N + 1, DIVISOR):
    #     if is_palindrome_n(n):
    #         n_correct += 1
    #         if n_correct % 1000 == 0:
    #             print(n_correct)
    _range = range(divisor, max_value, divisor)
    n_correct = [1 for n in _range if is_palindrome_n(n)]
    return sum(n_correct)


if __name__ == "__main__":
    DIVISOR: int = 10000019
    MAX_N: int = int(1e32)

    result = run(MAX_N, DIVISOR)
    print(f"The result is: {result:,}")




