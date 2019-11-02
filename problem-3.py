
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

    return [i for i in base_list if not i in omit_list]


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


# base_list = [i for i in range(2, 100 + 1)]

base_list = prime_prefilter(base_list)

### Remove final values from list
omit_list = [j for i in base_list for j in base_list if i != j and j % i == 0]

base_list = sorted(list(set(base_list).difference(set(omit_list))), reverse=True)

[i for i in base_list if n % i == 0]

count = 0
while True:
    for i in base_list:
        if n % i == 0:
            print(i)
            break
    break




main_value = 600851475143
prime_list = SoE(main_value // 2)

final = factorit(main_value, prime_list)




















