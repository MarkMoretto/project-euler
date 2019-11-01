
"""
Purpose: Project Euler problems
Date created: 2019-11-01

Contributor(s): Mark M.

ID: 489
Title: Common factors between two sequences
URI: https://projecteuler.net/problem=489
Status: Incomplete

Desc:
    Let G(a, b) be the smallest non-negative integer n 
    for which gcd(n**3 + b, (n + a)**3 + b) is maximized.

    For example, G(1, 1) = 5 because gcd(n**3 + 1, (n + 1)**3 + 1) reaches its
    maximum value of 7 for n = 5, and is smaller for 0 ≤ n < 5.

    Let H(m, n) = ∑ G(a, b) for 1 ≤ a ≤ m, 1 ≤ b ≤ n.

    You are given H(5, 5) = 128878 and H(10, 10) = 32936544.
    
    Find H(18, 1900).
"""


ABS = lambda n: n * -1 if ((n ^ 1) < 0) else n


def HCF(x, y):
    x, y = ABS(x), ABS(y)
    if x == 0:
        return y
    while y != 0:
        if x > y:
            x -= y
        else:
            y -= x
    return x


LCM = lambda i, j: (i*j) / HCF(i, j)



def lhs(n, b):
    return n ** 3 + b


def rhs(n, a, b):
    return (n + a) ** 3 + b



def G(a, b):

    n = 0
    n_prev = 0
    prev_vals = []
    curr_max = [0]
    tot_max = [0]

    while True:
        # Calculate highest ccommon factor from two algorithms
        res = HCF(lhs(n, b), rhs(n, a, b))

        # If prev_vals is empty, append the first result
        # Set curr_max and tot_max to the result
        if len(prev_vals) == 0:
            prev_vals.append(res)
            curr_max[0] = res
            tot_max[0] = res

        else:
            # If the result is larger than all values in the list
            if all([res > i for i in prev_vals]):
                # Set current max to result value
                curr_max[0] = res

                # If current max is larger than the total max
                if curr_max > tot_max:
                    tot_max[0] = curr_max[0]
                else:
                    return n
            else:
                prev_vals.append(res)


        n += 1

    print(HCF(lft, rght))




m = 5
n = 5










