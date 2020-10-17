
"""
Purpose: 
Date created: 2020-09-20

Contributor(s):
    Mark M.
"""



# from math import factorial

x, y = 8, 12


def gcd_(a, b):
    ab_range = range(1, max(a, b) + 1)
    return max([i for i in ab_range if a % i == 0 and b % i == 0])


# def gcd1(*args):
#     print(type(args))
#     if len(args) <= 1:
#         return args[0]

#     ab_range = range(1, max(a, b) + 1)
#     return max([i for i in ab_range if A % i == 0 and B % i == 0])


def lcm_(a, b):
    return (abs(a) / gcd_(a, b)) * abs(b)

lcm_(21, 6) # 42


# def coprimes(n_results=10):
#     # https://en.wikipedia.org/wiki/Coprime_integers
#     counter = 0
#     res = []
#     i, j = 0, 1
#     while counter < n_results:
#         while i < j:
#             if gcd_(i, j) == 1:
#                 res.append([i, j])
#                 counter += 1
#             i += 1
#         i = 0
#         j += 1
#     return res

# coprimes()



# def carmichael(n):  # Robert Daniel Carmichael's Function
#     y = (phi(n) * 1/2) if (n > 4 and ((n & (n - 1)) == 0)) else phi(n)  # phi(n) * 1/2 if 2^x = n, else phi(n) * 1
#     return y

# Leonard Euler's Totient Function
def phi(n):
    y = 0
    # Phi(+n) is the number of integers k in the range (1 <= k >= n)...
    for k in range(1, n + 1):

        # for which gcd(n, k) = 1
        if gcd_(n, k) == 1:
            y += 1
    return y

# def carmichael(n):
#     coprimes = []
#     for i in range(n):
#         if gcd_(i, n) == 1:
#             coprimes.append(i)
#             k = 0
#     while True:
#         for coprime in coprimes:
#             if (coprime ** k) % n != 1:
#                 break
#             else:
#                 return k
#             k += 1

# https://codegolf.stackexchange.com/questions/93739/compute-the-carmichael-function

def carmichael(n):
    coprimes = [x for x in range(1, n) if gcd_(x, n) == 1]
    k = 1
    while not all(pow(x, k, n) == 1 for x in coprimes):
        k += 1
    return k

carmichael(12)
