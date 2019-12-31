
"""
Purpose: Project Euler problems
Date created: 2019-12-25

ID: 694
Title: Cube-full Divisors
URI: https://projecteuler.net/problem=694
Difficulty: ?

Status: Incomplete

Problem:
A positive integer n is considered cube-full, if for every prime p that divides
n, so does p**3. Note that 1 is considered cube-full.

Let s(n) be the function that counts the number of cube-full divisors of n.
For example, 1, 8 and 16 are the three cube-full divisors of 16. 
Therefore, s(16)=3.

Let S(n) represent the summatory function of s(n), that is S(n)=∑i=1ns(i).

You are given S(16)=19, S(100)=126 and S(10000)=13344.

Find S(10**18). 
"""

from os import chdir
chdir(r'C:\Users\Work1\Desktop\Info\PythonFiles\project-euler')

import tempfile
import numpy as np
from io import BytesIO
import urllib.request as ureq
from zipfile import ZipFile

from utils import m_funcs


### Get prime numbers
prime_n_uri = r"https://www.mathsisfun.com/includes/primes-to-100k.zip"

with ureq.urlopen(prime_n_uri) as resp:
    with ZipFile(BytesIO(resp.read())) as zf:
        # We're lucky happen to know the name of the file here, but adding
        # a section to find a specific file might be necessary.
        with open(zf.extract('primes-to-100k.txt'), 'rb') as f:
            data = f.read().decode('utf-8')

# Need list to start with 1 since it is included
# primes: list = ['1']
# primes.extend([i for i in data.split('\r\n') if len(i) > 0])

primes: list
primes = [i for i in data.split('\r\n') if len(i) > 0]

# We'll need to convert these to integers
primes = list(map(int, primes))



N = 16
count: int # in s()
ppp: int # in s_worker()
lt_n_bool: bool # in s_worker()
temp_range: np.array # in S()
n_list: np.array # in cube_full_gen()
# cube_fulls: list # in s_worker()

# def cube_full_gen(max_n: int):
#     """Generate list of valid cube-full integers."""
#     # Check to see if list will even be complete.
#     if max_n <= max(primes):
#         n_list = np.arange(1, max_n + 1)
#         for n in n_list:
#             if n == 1:
#                 yield n
#             elif n > 1:
#                 for p in primes:
#                     ppp = p ** 3
#                     if n % p == 0 and n % ppp == 0:
#                         yield n


# cfg = cube_full_gen(max(primes))
# cube_fulls = [i for i in cfg]
# list(m_funcs.gen_cube_full(100, primes))



def s_worker(n_value: int):
    lt_n_bool = True
    cube_full_gen = m_funcs.gen_cube_full(n_value, primes)
    for i in cube_full_gen:
        if n_value % i == 0:
            yield 1

    while lt_n_bool:
        for i in cube_full_gen:
            if i <= n_value:
                if n_value % i == 0:
                    yield 1
            else:
                lt_n_bool = False



def s(n):
    cube_full = m_funcs.gen_cube_full(n_value, primes)
    return sum([i for i in s_worker(n)])


assert (s(16) == 3), "s() error"


def S(n):
    temp_range = np.arange(1, n + 1)
    return sum([s(i) for i in temp_range])




# https://docs.python.org/3/library/functions.html?highlight=property#property

class PrimesMixin:

    DEFAULT_ZIP_URI = r"https://www.mathsisfun.com/includes/primes-to-100k.zip"

    def __init__(self, url: str = None):
        self.set_url(url)
        self._primes = self.__get_primes()

    def set_url(self, x: str = None) -> None:
        """Set primes url if different than default."""
        if x is None:
            self.url = self.DEFAULT_ZIP_URI
        else:
            self.url = x

    @property
    def primes(self):
        """Primes getter."""
        return self._primes

    @staticmethod
    def __convert_to_int(value_list: list) -> list:
        """Convert primes list to integers."""
        return list(map(int, value_list))

    def __get_primes(self):
        with ureq.urlopen(self.url) as resp:
            with ZipFile(BytesIO(resp.read())) as zf:
                # We're lucky happen to know the name of the file here, but adding
                # a section to find a specific file might be necessary.
                with open(zf.extract('primes-to-100k.txt'), 'rb') as f:
                    data = f.read().decode('utf-8')

        # Split results into list
        tmp = [i for i in data.split('\r\n') if len(i) > 0]
        return self.__convert_to_int(tmp)




del primes
pm = PrimesMixin()

primes = pm.primes



class S(PrimesMixin):
    def __init__(self):
        super().__init__()
        # Get primes on instantiation
        self.primes_ = self.primes

    def set_n(self, n) -> None:
        self.n = n
        self.__gen_cube_fulls()

    def __gen_cube_fulls(self) -> None:
        self.cube_fulls: list = list(m_funcs.gen_cube_full(self.n, self.primes_))




S = S()
# S.primes_[:5]

S.set_n(16)












