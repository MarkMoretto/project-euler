"""
Purpose: Ancillary math functions
Date created: 2019-12-21

Contributor(s):
    Mark M.
"""


def m_quotient(n, d) -> int:
    return n // d


def m_mod(n, d) -> int:
    return n % d


def m_divmod(numer, denom) -> tuple:
    """Mimics divmod() in standard library, but hopefully a bit faster."""
    return (m_quotient(numer, denom), m_mod(numer, denom))

