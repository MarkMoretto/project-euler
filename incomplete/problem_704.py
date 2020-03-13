
"""
Purpose: Project Euler problems
Date created: 2020-03-01

ID: 704
Title: Factors of Two in Binomial Coefficients
URI: https://projecteuler.net/problem=704
Status: Complete
Contributor(s): Mark Moretto

Description:
    Define g(n,m) to be the largest integer k such that 2**k divides (n {over} m).
    For example, (12 {over} 5) = 792 = 2**3⋅3**2⋅11, hence g(12, 5)=3.
    Then define F(n) = max{ g(n, m): 0 ≤ m ≤ n}.
        * F(10) = 3
        * F(100) = 6.

Let S(N) = sum of F(n) for n = 1 to N. You are given that:
    S(100) = 389 and
    S(107) = 203222840

Find S(1016). 
"""



def fact(n):
    """Factorial."""
    if n < 2:
        return 1
    else:
        res_ = 1
        for i in range(2, n + 1): res_ *= i
        return res_

def combos(total_count, sample_size):
    """
    Combinations.
    total_count <-> n
    sample_size <-> r
    """
    return int(fact(total_count) / (fact(sample_size) * fact(total_count - sample_size)))


assert (combos(5, 3) == 10), "Error: combos() test"


def perms(total_count, sample_size):
    """
    Permutations.
    total_count <-> n
    sample_size <-> r
    """
    return int(fact(total_count) / fact(total_count - sample_size))


assert (perms(5, 4) == 120), "Error: perms() test"


def factor_gen(n, start=1):
    i = start
    while i <= n:
        if n % i == 0:
            yield i
        i += 1

def factors(n):
    return [x for x in factor_gen(n, 2)]

target = 792
xyz = factors(target)
output = list()

for idx, i in enumerate(xyz):
    res = []
    res.append(i)
    tot = i
    for j in xyz[idx:]:
        if tot == target:
            res.append(j)
            break
        elif tot > target:
            break
        tot *= j
    output.append(res)








