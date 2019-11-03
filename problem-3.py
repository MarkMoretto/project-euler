
"""
Purpose: Project Euler problems
Date created: 2019-11-02

ID: 3
Title: Largest prime factor
URI: https://projecteuler.net/problem=3
Status: Incomplete

Contributor(s): Mark M.

Desc: 
    The prime factors of 13195 are 5, 7, 13 and 29.
    
    What is the largest prime factor of the number 600851475143?
"""



# Need to figure out a way to break the problem down further
n = 13195

prime_prefilter = lambda iterable: [i for i in iterable if (i==2 or i==3) or (i%2!=0 and i%3!=0)]


base_list = [i for i in range(2, n // 2)]
def prime_prefilter(iterable):
    return set(reduce(list.__add__, ([i, n//i] for i in iterable if (i==2 or i==3) or (i%2!=0 and i%3!=0))))


main_value = 600851475143
main_value_sm = int(main_value // 2)


def f_factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(2, int(n**0.5)) if n % i == 0)))

def p_factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(2, int(n**0.5)) if (i==2 or i==3) or (i%2!=0 and i%3!=0))))






















### First part: Proof of Concept
### SoE recursively finds factors using Sieve of Eratosthenes
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def SoE(n):

    base_list = [i for i in range(2, n + 1)]

    omit_list = list()

    for i in base_list:
        for j in base_list:
            if i != j:
                if i % j == 0:
                    if not i in omit_list:
                        omit_list.append(i)

    return sorted(list(set(base_list).difference(set(omit_list))), reverse=True)


# Checkpoint
assert (SoE(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]), 'Check SoE function!'


test_value = 13195
prime_list = SoE(test_value // 2)

# Lambda function to evaluate prime factors
factorit = lambda n, iterable: [i for i in iterable if n % i == 0]



# Checkpoint
assert (factorit(test_value, prime_list) == [5, 7, 13, 29]), 'FactorIt failed!'

n = 13195

prime_prefilter = lambda iterable: [i for i in iterable if (i==2 or i==3) or (i%2!=0 and i%3!=0)]


base_list = [i for i in range(2, n // 2)]
def prime_prefilter(iterable):
    return set(reduce(list.__add__, ([i, n//i] for i in iterable if (i==2 or i==3) or (i%2!=0 and i%3!=0))))


main_value = 600851475143
main_value_sm = int(main_value // 2)


def f_factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(2, int(n**0.5)) if n % i == 0)))

def p_factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(2, int(n**0.5)) if (i==2 or i==3) or (i%2!=0 and i%3!=0))))


base_factors = p_factors(main_value)

[[i, 100//i] for i in range(4, int(100**0.5)) if (i==2 or i==3) or (i%2!=0 and i%3!=0)]

base_factors = (f_factors(main_value)
for i in base_factors:
    for j in base_factors:
        if i != j:
            if i % j == 0:
                print(f'i: {i}, j: {j}, i%j: {i%j}')
            print(f'i: {i}, j: {j}, i%j: {i%j}, j%i: {j%i}')

max_prime_factor = max(base_factors)



def largest_prime_factor(n):
    base_list = [i for i in range(2, n // 2)]


    # base_list = [i for i in range(2, 100 + 1)]

    base_list = prime_prefilter(base_list)

    ### Remove final values from list
    omit_list = [j for i in base_list for j in base_list if i != j and j % i == 0]

    base_list = sorted(list(set(base_list).difference(set(omit_list))), reverse=True)

    # Print only the largest prime, then stop
    while True:
        for i in base_list:
            if n % i == 0:
                print(i)
                break
        break




main_value = 600851475143
largest_prime_factor(main_value)



main_value_sm = 600851475143 // 2


for i in range(2, 30):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        print(i)
    part1 = [j for j]



import random
a = 5
x = 7
a**(x-1) % x % x



def SoE(n):

    prime = [0] * int(n / 2)

    # Get 2 out first
    i = 2
    if i == 2:
        yield i

    # work on the rest
    i = 3
    while(i ** 2 < n):

        if prime[int(i / 2)] == 0:
            j = i ** 2
            while(j < n):
                prime[int(j / 2)] = 1
                j += i * 2
        i += 2

    i = 3
    while(i < n):
        if prime[int(i / 2)] == 0:
            yield i
        i += 2




ns = normalSieve(30)

[i for i in ns]










