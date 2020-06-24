
"""
Purpose: Modular Exponentiation
Date created: 2020-06-23

Contributor(s):
    Mark M.
"""


# MOD = 999999937
MOD = int(1e9) + 7


def fexp(base, exp, m=MOD):
    res = 1
    if 1 & exp:
        res = base
    while exp:
        exp >>= 1
        base = (base * base) % m
        if exp & 1:
            res = (res * base) % m
    return res

if __name__ == "__main__":


    b = 10
    e = 100

    res = fexp(b, e)
    print(f"The value of {b} ** {e} MOD {MOD} is: {res}")