
"""
Purpose: 
Date created: 2020-02-05

Contributor(s):
    Mark M.
Desc:

    Using names.txt (right click and 'Save Link/Target As...'), a 46K text
    file containing over five-thousand first names, begin by sorting it into
    alphabetical order. Then working out the alphabetical value for each name,
    multiply this value by its alphabetical position in the list to obtain a
    name score.

    For example, when the list is sorted into alphabetical order, COLIN, which
    is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
    So, COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?
"""


import string

file_path = r"C:\Users\MMorett1\Desktop\Projects Main\project-euler\names.txt"

with open(file_path) as f:
    data = f.read()

name_tokens = sorted([i.replace('"','').lower() for i in data.split(",") if len(i) > 0])
name_dict = {k:v for k, v in enumerate(name_tokens, 1)}

abc_123 = {v:k for k, v in enumerate(string.ascii_lowercase, 1)}

def name_sum(name_string):
    tot = 0
    for ltr in name_string:
        tot += abc_123[ltr]
    return tot


name_tot = 0
for k, name in name_dict.items():
    name_tot += (k * name_sum(name))





