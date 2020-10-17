
"""
Purpose: Project Euler exercises
Date created: 2020-09-13

Problen Number: 725
Name: Digit sum numbers
URL: https://projecteuler.net/problem=725

Contributor(s):
    Mark M.

Description:
    A number where one digit is the sum of the other digits is called a digit sum numbe
    or DS-number for short. For example, 352, 3003 and 32812 are DS-numbers.
    
    We define S(n) to be the sum of all DS-numbers of n digits or less.
    
    You are given S(3) = 63270 and S(7) = 85499991450.
    
    Find S(2020). Give your answer modulo 10^16.    
"""



MOD = 10**16

N = 3
range_min, range_max = 10**(N-1), 10**N
srng = [f"{i}" for i in range(range_min, range_max)]


def zero_count(snumber):
    return sum([1 for i in snumber if i == '0'])

def S(n):
    tot = 0
    for x in range(2, n + 1):
        range_min, range_max = 10**(x-1), 10**x

        # Range generator
        rng = range(range_min, range_max)

        for i in rng:
            str_num = f"{i}"
            len_str_num = len(str_num) # Length of full number
            max_num = max(list(str_num)) # Max value of full number.

            small_num = str_num.replace(max_num, "")

            max_num_ct = len(str_num) - len(small_num)

            zc = zero_count(str_num)

            if len_str_num == 2 and max_num_ct == 2:
                tot += int(str_num)
            elif max_num_ct == 1 or zc == (len(str_num) - 2):
                if f"{sum(map(int, small_num))}" == max_num:
                    tot += int(str_num)

    return tot

S(3)



tot = 0
sample = 32812
ssample = str(sample)
max_val = max(list(ssample))
sm_sample = ssample.replace(max_val, "")
n_max_val = len(ssample) - len(sm_sample)
if n_max_val == 1:
    if f"{sum(map(int, sm_sample))}" == max_val:
        tot += int(max_val)
