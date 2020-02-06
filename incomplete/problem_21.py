
"""
Purpose: Project Euler problems
Date created: 2020-02-05

Problem #: 21
URI: https://projecteuler.net/problem=21

Contributor(s):
    Mark M.
"""




def divisor_gen(n):
    for i in range(1, n):
        if n % i == 0:
            yield i


def divisors(n):
    q = divisor_gen(n)
    return [i for i in q]


def d(n):
    return sum(divisors(n))



max_n = 10000
rng = [i for i in range(1, max_n)]
ddict = {i:d(i) for i in rng}

amics = []
amicss = set()
for k1, v1 in ddict.items():
    for k2, v2 in ddict.items():
        if k1 != k2:
            if k2 == v1:
                amics.append(k2)
                amicss.add(k2)
            if k1 == v2:
                amics.append(k1)
                amicss.add(k1)

# len(amics)
# len(amicss)
amics = sorted(amics)
amicss = sorted(amicss)
res1 = sum([i for i in amics])
res2 = sum([i for i in amicss])
print(f"\nResult all: {res1}\nResult set: {res2}")

# # Test proc for n = 100
# t_amics = []
# for x in rng:
#     for y in rng:
#         if x != y:
#             if d(x) == y or d(y) == x:
#                 t_amics.append([x, y]) # 180

