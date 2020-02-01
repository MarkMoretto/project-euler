"""
Purpose: Project Euler problems
Date created: 2020-02-01

ID: 16
Title: Power digit sum
URI: https://projecteuler.net/problem=16
Status: Complete
Contributor(s): Mark Moretto

Description:
  2*15 = 32768 and the sum of its
  digits is 3 + 2 + 7 + 6 + 8 = 26.

  What is the sum of the digits of the number 2^1000?
"""

base = 2
expon = 1000
core = base ** expon
res = sum([int(i) for i in str(core)])
# Output: 1366
