
"""
Purpose: Project Euler problems
Date created: 2019-11-03
Contributor(s): Mark Moretto

ID: 7
Title: 10001st Prime
URI: https://projecteuler.net/problem=7

Status: Complete!

Desc: 
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
    see that the 6th prime is 13.
    
    What is the 10 001st prime number?
"""


### SoE recursively finds factors using Sieve of Eratosthenes
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def SoE(nth_prime):

    n = 2
    value_list = [n]

    while len(value_list) < nth_prime:
        n += 1
        if sum([1 for i in value_list if n % i == 0]) == 0:
            value_list.append(n)


    return value_list[-1]

# Test
assert (SoE(10) == 29), 'SoE error!'


if __name__ == '__main__':
    target = 10001
    res = SoE(target)
    print('The 10001st prime number is: {}'.format(res))



