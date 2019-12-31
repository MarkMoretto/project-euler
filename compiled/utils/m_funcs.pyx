"""
Purpose: Utility functions
Date created: 2019-12-21

Contributor(s):
    Mark M.
"""


# -- Produce a range of numbers
def m_range(start, stop=None, increment=None):
    """Range function with start, stop, and increment."""
    if increment is None:
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


def m_range_gen(start, stop=None, increment=1):
    """Generator for above range function."""
    tmp_rng = m_range(start, stop, increment)
    return [i for i in tmp_rng]


def m_quotient(n, d) -> int:
    return n // d


def m_mod(n, d) -> int:
    return n % d


def m_divmod(numer, denom) -> tuple:
    """Returns tuple of quotient and modulo from a numerator and denominator."""
    return (m_quotient(numer, denom), m_mod(numer, denom))


def m_sum(*args):
    """ Returns total value of elements in interable object."""
    tot_ = 0
    for i in args:
        tot_ += i
    return tot_


def m_add(a, b):
    """Add one number to another number."""
    return m_sum(a, b)


def m_subtract(x, y):
    """Subtract one number from another number."""
    return x - y


def m_divide(x, y):
    """ Divide one number by another number. Should return float type."""
    return (x * 1.0) / y


def m_multiply(x, y):
    """ Multiply one number by another number."""
    return x * y


def m_abs(n):
    return n * -1 if ((n ^ 1) < 0) else n


def m_exp(x, y):
    """ Returns x ** y """
    return x ** y


def m_exp2(n):
    """ Returns 2 ** n """
    return 2 ** n


def m_len(iterable):
    """ Returns character count of iterable."""
    return m_sum([1 for i in str(iterable)])


def enum(iterable, start=0):
    """Enumerate an iterable object."""
    for i in iterable:
        yield start, i
        start += 1


def enum_dict(iterable, start=0):
    """Return an enumerated dictionary."""
    return {k: v for k, v in enum(iterable, start)}


def m_hcf(x, y):
    """Highest common factor."""
    x, y = m_abs(x), m_abs(y)
    if x == 0:
        return y
    while y != 0:
        if x > y:
            x -= y
        else:
            y -= x
    return x


def gen_cube_full(n_max: int, prime_numbers: list):
    """
    Generate list of valid cube-full integers.
    Params:
        n_max - maximum integer value to evaluate
        prime_numbers - a list of prime numbers
    """
    ppp: int
    n_list: list
    # Check to see if list will even be complete.
    if n_max <= max(prime_numbers):
        n_list = [i for i in m_range(1, n_max + 1)]
        for n in n_list:
            if n == 1:
                yield n
            elif n > 1:
                for p in prime_numbers:
                    ppp = p ** 3
                    if n % p == 0 and n % ppp == 0:
                        yield n


# cfg = cube_full_gen(max(primes))
# cube_fulls = [i for i in cfg]
