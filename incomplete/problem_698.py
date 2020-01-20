
"""
Purpose: Project Euler problems
Date created: 2020-01-19
Contributor(s): Mark M.

ID: 698
Title: 123 NUmbers
URI: https://projecteuler.net/problem=698
Difficulty: ?

Status: Incomplete

Problem:
 We define 123-numbers as follows:

    * 1 is the smallest 123-number.
    * When written in base 10 the only digits that can be present are "1", "2"
    and "3" and if present the number of times they each occur is also a
    123-number.

So 2 is a 123-number, since it consists of one digit "2" and 1 is a 123-number.
Therefore, 33 is a 123-number as well since it consists of two digits "3" and
2 is a 123-number.
On the other hand, 1111 is not a 123-number, since it contains 4 digits "1" and
4 is not a 123-number.

In ascending order, the first 123-numbers are:
1,2,3,11,12,13,21,22,23,31,32,33,111,112,113,121,122,123,131,…

Let F(n)
be the n-th 123-number. For example
F(4)=11
F(10)=31,
F(40)=1112,
F(1000)=1223321
and F(6000)=2333333333323.

Find F(111111111111222333). Give your answer modulo 123123123. 
"""


import os
import gc
import numpy as np
gc.enable()

# from threading import Thread
import threading
import concurrent.futures
# from multiprocessing import Queue
# from queue import Queue
# from multiprocessing.pool import ThreadPool


TARGET_N = str("123")


def tight_split(numeric_string):
    return np.array([f"{i}" for i in numeric_string])


TARGET_SET = set(tight_split(TARGET_N))


first_19 = np.array([1,2,3,11,12,13,21,22,23,31,32,33,111,112,113,121,122,123,131,])
first_19s = np.array([str(i) for i in first_19])
f19_dict = {k:v for k, v in enumerate(first_19s, start=int(1))}

# output_folder = r'C:\Users\Work1\Desktop\Info\PythonFiles\project-euler\results_output'
# output_name = str("problem_698.txt")
# output_path = f"{output_folder}\{output_name}"
# os.chdir(output_folder)

# Known results
f4 = str("11")
f10 = str("31")
f40 = str("1112")
f1000 = str("1223321")
f6000 = str("2333333333323")



def count_dict(iterable):
    tmp_dict = dict()
    incr = np.int64(1)
    for i in iterable:
        if not i in tmp_dict.keys():
            tmp_dict[i] = incr
        else:
            tmp_dict[i] += incr
    return tmp_dict



def keys_check(dictionary):
    if len(set(dictionary.keys()).difference(TARGET_SET)) == 0:
        return True
    return False



def values_check(dictionary):
    val_set  = set(tight_split(''.join([f"{i}" for i in dictionary.values()])))
    if len(val_set.difference(TARGET_SET)) == 0:
        return True
    return False



def full_check(dictionary):
    return keys_check(dictionary), values_check(dictionary)



def is_123(number_string):
    ddict  = count_dict(number_string)
    keys_bool, values_bool = full_check(ddict)
    if keys_bool and values_bool:
        return True
    return False



def F_worker(target_val, i = np.int64(0), incr = np.int64(1), count=float(0)):
    while True:
        i += incr
        if is_123(f"{i}"):
            count += incr
        if count == target_val:
            gc.collect(2)
            yield i

# F_runner(1000.).__next__()
# F_runner(6000.).__next__()


def F(n):
    return F_worker(float(n)).__next__()


"""
F(4)
F(10)
F(40)
F(1000)
F(6000)
"""


if __name__ == '__main__':
    f_target = 60000
    res = F(f_target)
    print(f"Result for F({f_target}): {res}")
















