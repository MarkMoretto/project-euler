

"""
Purpose: Project Euler problems
Date created: 2019-10-19

Contributor(s):
    Mark M.


ID: 1
URI: https://projecteuler.net/problem=1
Status: Complete
"""



def sum_vals(divisor_list=[3, 5], n = 1000):
    lst = list()
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0 or (i % 3 == 0 and i % 5 == 0):
            lst.append(i)
    return sum([x for x in lst])


if __name__ == '__main__':
    divisors = [3, 5]

    res = sum_vals(divisors, n=1000)
    print('The sum of all the multiples of 3 or 5 below 1000 is: {}'.format(res))
