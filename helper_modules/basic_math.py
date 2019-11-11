
"""
Purpose: Slightly optimized math and stats functions
Date created: 2019-11-09

Contributor(s):
    Mark M.
"""

__all__ = [
        'mADD','mSUBTRACT','vDIVIDE','mMULTIPLY',
        'mABS','mEXP', 'mEXP2', 'HCF',
        'permutations','combinations'
        ]


from .types import *
from .utilities import *


#-----------------------------------------------
#-------------------------------------------------------
### basic math functions

def mADD(x: N_, y: N_) -> N_:
    """Add one number to another number."""
    return x + y


def mSUBTRACT(x: N_, y: N_) -> N_:
    """Subtract one number from another number."""
    return x - y


def vDIVIDE(x: N_, y: N_) -> float:
    """ Divide one number by another number. Should return float type."""
    return x / y


def mMULTIPLY(x: N_, y: N_) -> N_:
    """ Multiply one number by another number."""
    return x * y


def mABS(n: N_) -> N_:
    return n * -1 if ((n ^ 1) < 0) else n


def mEXP2(n: N_) -> N_:
    """ Returns 2 ^ n """
    return 2 ** n


def mEXP(x: N_, y: N_) -> N_:
    """ Returns x ^ y """
    return x ** y


def HCF(x: N_, y: N_) -> t_Iterable[int]:
    x, y = mABS(x), mABS(y)
    if x == 0:
        return y
    while y != 0:
        if x > y:
            x -= y
        else:
            y -= x
    return x


def factorial(n: int) -> int:
    """ Simple factorial function """
    x: int = 1
    for i in mRANGE_GEN(1, n + 1):
        x *= i
    return x


#-----------------------------------------------
#-------------------------------------------------------
# Some stats functions
def permutations(n: int, r: int) -> int:
    return int(factorial(n) / factorial(n - r))


def combinations(n: int, r: int) -> int:
    return int(factorial(n) / factorial(n - r) * factorial(r))

