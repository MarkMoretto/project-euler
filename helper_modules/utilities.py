
"""
Purpose: Slightly optimized utilities for problem solving
Date created: 2019-11-09

Contributor(s):
    Mark M.
"""

__all__ = ['mRANGE','mRANGE_GEN','mSUM', 'mLEN','enum',]

from .types import *


#-- Produce a range of numbers
def mRANGE(start: int, stop: int = None, increment: int = 1) -> t_Iterable[int]:

    if increment == 0:
        increment = 1

    if increment > 0:
        if stop is None:
            stop = start
            start = 0

        while start < stop:
            yield start
            start += increment

    elif increment < 0:
        if stop is None:
            stop = 0

        elif start < stop:
            stop = start
            start = stop

        while start > stop:
            yield start
            start += increment


#-- Generate a list of numbers (integers or floats)
def mRANGE_GEN(start: N_, stop: N_ = None, increment: N_ = 1) -> nvector:
    """Auto-iterate the mRANGE function"""
    return [i for i in mRANGE(start, stop, increment)]



def mSUM(it: t_Iterable[N_], tot: N_ = 0) -> N_:
    """ Returns total value of elements in interable object."""
    for i in it:
        tot += i
    return tot


def mLEN(it: t_Iterable[Q_]) -> N_:
    """ Returns character count of iterable."""
    return mSUM([1 for i in str(it)])


def enum(it: t_Iterable[Q_], start: int = 0) -> t_Dict[int, Q_]:
    for i in it:
        yield start, i
        start += 1

