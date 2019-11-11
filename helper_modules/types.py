
"""
Purpose: Type declaractions for related modules
Date created: 2019-11-09

Contributor(s):
    Mark M.

Ref:
    https://stackoverflow.com/questions/49427944/typehints-for-sized-iterable-in-python
"""


from typing import TypeVar, List as t_List, Iterable as t_Iterable, Dict as t_Dict
from typing_extensions import Protocol

### Various declared types
# Numerics and string
Q_ = TypeVar('Q_', int, float, str)

# Integer and float
N_ = TypeVar('N_', int, float)


### All the vectors

qvector = t_List[Q_]
nvector = t_List[N_]
ivector = t_List[int]
fvector = t_List[float]
svector = t_List[str]


class SizedIterable(Protocol):

    def __len__(self):
        pass

    def __iter__(self):
        pass