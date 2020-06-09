
"""
Purpose: Fibonacci for N
Date created: 2020-06-08

URL: https://en.wikipedia.org/wiki/Fibonacci_number

Contributor(s):
    Mark M.
"""

import unittest
from math import floor, sqrt


def count_digits(N, base=10):
    """Count the number of digits in a number, n, with a given base."""
    count = 0
    while N:
        count += 1
        N //= base
    return count



def F(n):
    """
    Function to calculate the Fibonacci number for a given input n, where n in [0, inf).
    """
    if n >= 0:
        rho = (1 + sqrt(5)) / 2 # p-shaped symbol, for some reason
        psi = 1 - rho # Trident shape
        return floor((pow(rho, n) - pow(psi, n)) / sqrt(5))


def F_len(n):
    """Function to find the digit count for a given Fibonacci result."""
    return len(f"{F(n)}")




class FibCase(unittest.TestCase):
    def test_F_name(self):
        """Test F function name."""
        self.assertEqual(F.__name__, "F")

    def test_F12_calc(self):
        """Test F(12) result."""
        self.assertEqual(F(12), 144)

    def test_F0_calc(self):
        """Test F(0) result."""
        self.assertEqual(F(0), 0)

    def test_F400_digit_length(self):
        """Test F_len(400) result."""
        self.assertEqual(F_len(400), 84)


if __name__ == "__main__":
    unittest.main()