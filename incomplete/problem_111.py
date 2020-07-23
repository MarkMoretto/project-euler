
"""
Purpose: Project Euler exercises
Date created: 2020-07-21

Problen Number: 111
Name: Primes with runs
URL: https://projecteuler.net/problem=111

Contributor(s):
    Mark M.
"""


import os

PROJECT_FOLDER = r"C:\Users\Work1\Desktop\Info\PythonFiles\project-euler\incomplete"

def memoize(func):
    cache = []
    def memoizer(n):
        nonlocal cache
        if n > len(cache):
            cache = func(n)
        return cache
    return memoizer

@memoize


def is_prime(n):
    if n <= 1:
      return False

    elif n == 2:
      return True
    elif n > 2 and n % 2 == 0:
      return False
    else:
      for i in range(3, int(n**0.5) + 1, 2):
          if n % i == 0:
            return False
      return True


def primes(n):
    outlist = []
    return [i for i in range(n+1) if is_prime(i)]




def sqrt_(n):
    return n ** 0.5

def primes_up_to(n):
    """Generates all primes less than n."""
    if n <= 2: return
    yield 2
    F = [True] * n
    seq1 = range(3, int(sqrt_(n)) + 1, 2)
    seq2 = range(seq1[-1] + 2, n, 2)
    for p in filter(F.__getitem__, seq1):
        yield p
        for q in range(p * p, n, 2 * p):
            F[q] = False
    for p in filter(F.__getitem__, seq2):
        yield p

p_list = list(primes_up_to(100))



'1117'.count("1")

def M(n, d):
    max_repeats = -1
    min_, max_ = eval(f"int(1e{n-1})"), eval(f"int(1e{n})")
    p = primes_up_to(max_)
    c_dict = {}
    for prime in p:
        if prime >= min_:
            n_count = f"{prime}".count(f"{d}")
            if n_count > max_repeats:
                max_repeats = n_count
                c_dict[prime] = n_count
            elif n_count == max_repeats:
                c_dict[prime] = n_count
    return max_repeats, c_dict

def N(n, d):
    repeats, ddict = M(n, d)
    outlist = []
    for k, v in ddict.items():
        if v == repeats:
            outlist.append(k)
    return len(outlist), outlist


def S(n, d):
    _, p_list = N(n, d)
    return sum(p_list)

# M(4, 1)
# N(4, 1)
# S(4, 1)



tot = -1
for D in range(10):
    tmp = S(10, D)
    tot += tmp







