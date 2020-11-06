
"""
Purpose: Project Euler exercises
Date created: 2020-11-01

Problen Number: 732
Name: Standing on the shoulders of trolls
URL: https://projecteuler.net/problem=732

Contributor(s):
    Mark M.
"""




class Troll:
    MOD = 1000000007
    def __init__(self, nth):
        self.n = nth
        self.nnn = self.n * 3
        self.nnn1 = self.nnn + 1
        self.nnn2 = self.nnn + 2


    def __r(self, N):
        return (((5 ** N) % self.MOD) % 101) + 50


    @property
    def h(self):
        return self.__r(self.nnn)


    @property
    def l(self):
        return self.__r(self.nnn1)

    @property
    def q(self):
        return self.__r(self.nnn2)

    @property
    def attrs(self):
        return (self.h, self.l, self.q)


t = Troll(0)
t.attrs

r = lambda n: (((5**n) % MOD) % 101) + 50
h = lambda n: r(3 * n)
l = lambda n: r((3 * n) + 1)
q = lambda n: r((3 * n) + 2)


def D(N):
    i = 0
    factor = 1 / (2**(1/2))
    ht = 0
    while i < N-1:
        t = Troll(i)
        ht += t.h
        i += 1
    return ht * factor


N = 5
hole_depth = D(N)
f2s = 0 # feet to shoulder
iqs = 0 # IQ sum
prev_f2s = 0
prev_iqs = 0

t = Troll(0)
f2s += t.h
iqs += t.q
i = 1
while True:
    if (hole_depth - (f2s + t.l)) <= 0:
        break
    while i < N:
        if (hole_depth - (f2s + t.l)) <= 0:
            break
        t = Troll(i)
        f2s += t.h
        iqs += t.q


for i in range(1, N):
    t = Troll(i)
    f2s += t.h
    iqs += t.q
    print(t.attrs, f2s, iqs, hole_depth - f2s, hole_depth - (f2s + t.l))
    prev_f2s += t.h
    prev_iqs += t.q
    print(prev_f2s, prev_iqs)


def Q(N):
    height = D(N)






