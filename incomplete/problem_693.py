
"""
Purpose: Project Euler problems
Date created: 2019-12-21
Contributor(s): Mark M.

ID: 693
Title: Finite Sequence Generator
URI: https://projecteuler.net/problem=693
Difficulty: ?

Status: Incomplete

Problem:
Two positive integers x and y (x>y) can generate a sequence in the following manner:
1. ax = y is the first term,
2. az + 1 = az**2 mod z for z=x, x+1, x+2, …
3. the generation stops when a term becomes 0 or 1.

The number of terms in this sequence is denoted l(x,y).

For example, with x = 5 and y = 3, we get:
    a5 = 3,
    a6 = 3**2 mod 5 = 4,
    a7 = 4**2 mod 6 = 4,
    etc.

Giving the sequence of 29 terms: 3,4,4,2,4,7,9,4,4,3,9,6,4,16,4,16,16,4,16,3,9,6,10,19,25,16,16,8,0

Hence l(5,3) = 29

g(x) is defined to be the maximum value of l(x,y) for y<x.
    For example, g(5)=29

Further, define f(n) to be the maximum value of g(x) for x≤n.
    For example, f(100)=145 and f(10000)=8824

Find f(3000000)
"""

import os
os.chdir(r"C:\Users\Work1\Desktop\Info\PythonFiles\project-euler")

from utils.m_funcs import *

def gen_matrix(x, y):
    y_rng = m_range_gen(1, y+1)
    X_rng = m_range_gen(1, x+1)
    return [[i,j] for j in y_rng for i in X_rng if j < i]


def l(x, y):
    if y:
        yield y
    z = x
    ax = y
    while ax > 1:
        res = m_mod(ax**2, z)
        ax = res
        z += 1
        yield res




def g(x):
    rng = m_range_gen(1, x + 1)
    for y_ in rng: # y
        for x_ in rng: # X
            if y_ < x_:
                yield len([i for i in l(x_, y_)])


def g_gen(x):
    return set(list(g(x)))

def g_max(x):
    return max(g_gen(x))


def f(n):
    frng = m_range_gen(2, n + 1)
    max_val = 1
    for q in frng:
        # current_val = max([i for i in g(q)])
        current_val = g_max(q)
        if current_val > max_val:
            max_val = current_val
    return max_val


F = 1000
frng = m_range_gen(2, F + 1)
max([g_max(q) for q in frng])



















