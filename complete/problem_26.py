
"""
Purpose: Project euler problem
Date created: 2021-04-02

Problen Number: 26
Name: Reciprocal cycles
URL: https://projecteuler.net/problem=26

Contributor(s):
    Mark M.
"""


from heapq import heappush, heappop


def gen_terminators():
    q = [1]
    visited = set(q)
    while True:
        v = heappop(q)
        yield v
        visited.remove(v)
        for i in 2 * v, 5 * v:
            if not i in visited:
                heappush(q, i)
                visited.add(i)

# Generate first 1000 terminating values.
f1k_terms = []
terminator = gen_terminators()
v = next(terminator)
while True:
    v = next(terminator)
    if v > 1000:
        break
    f1k_terms.append(v)



def is_terminating(n):
    return n in f1k_terms

def decimal_period(N):
    if is_terminating(N):
        return 0
    lpow = 1
    while True:
        for i in range(lpow - 1, -1, -1):
            if (10 ** lpow - 10 ** i) % N == 0:
                return lpow - i
        lpow += 1

if __name__ == "__main__":
    # Limit range
    rng = [i for i in range(1, 1000) if not is_terminating(i)]
    resdict = {i:decimal_period(i) for i in rng}
    
    for k, v in resdict.items():
        if v == max(resdict.values()):
            res = k
            break
    
    print(f"The value of d with the greatest decimal period for d < 1000 is: {res}")


