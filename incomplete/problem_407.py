
"""
Purpose: Project euler problem
Date created: 2021-03-26

Problen Number: 407
Name: Idempotents
URL: https://projecteuler.net/problem=407

Contributor(s):
    Mark M.
"""
import concurrent.futures as ccf
from functools import lru_cache as cache

class Number:
    def __init__(self, number):
        self.__n = number

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, value):
        if isinstance(value, (int, float)):
            self.__n = value
        else:
            raise ValueError("Expected int or float.")

    @property
    def nsq(self):
        return self.__n * self.__n



@cache(maxsize=1000)
def eval_a(A, n):
    return (A * A) % n == A % n


@cache(maxsize=1000)
def M(n):
    largest = -1
    rng = range(n)
    for a in rng:
        if eval_a(a, n):
            largest = a
    return largest


def run(**params):

    rng = range(params["min_"], params["max_"])
    tot = 1
    with ccf.ThreadPoolExecutor() as executor:
        futures_q = (executor.submit(M, N) for N in rng)
        for future in ccf.as_completed(futures_q):
            try:
                tot += future.result()
            except ccf.BrokenExecutor as be:
                print(be.args())
    print(f"The result is: {tot:,}")


if __name__ == "__main__":

    minmax = {"min_": 1, "max_": 100}
    print(r"Running project-euler problem: 407...")
    run(**minmax)
