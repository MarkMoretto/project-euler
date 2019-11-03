
"""
Purpose: Project Euler problems
Date created: 2019-11-03
Contributor(s): Mark M.

ID: 11
Title: Largest product in a grid
URI: https://projecteuler.net/problem=11

Status: Complete!

Desc: 
    In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
    
    [Removed for brevity, but reproduced in the `raw_matrix` variable below.]
    
    The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
    
    What is the greatest product of four adjacent numbers in the same
    direction (up, down, left, right, or diagonally) in the 20×20 grid?
"""


def enum(iterable, start=0):
    n = start
    for i in iterable:
        yield n, i
        n += 1



raw_matrix = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
"""
#-- Split string into tokens
tokenizer = lambda x, split_on='\n': [i for i in x.split(split_on) if len(i) > 0]

#-- Sum function
def xsum(iterable):
    n = 0
    for i in iterable:
        if isinstance(i, (int, float)):
            n+=i
    return n


#-- Length lamda func
xlen = lambda iterable: xsum([1 for i in iterable])


def convert_type(iterable, dtype='int', inplace=True):
    """Convert matrix iterable into a given data type"""
    for r, row in enum(iterable):
        for c, ele in enum(row):
            if inplace:
                iterable[r][c] = eval(f'{dtype}(\'{ele}\')')
            else:
                return eval(f'{dtype}(\'{ele}\')')


#-- Create columns
cols = tokenizer(raw_matrix)


#-- Iterate columns and append to main matrix
matrix = list()
for i, v in enum(cols):
    matrix.append(v.split(' '))


#-- Convert matrix values to integers
convert_type(matrix, 'int')



def gen_product(x):
    """Generator for product of an iterable"""
    n = x[0]
    for i in x[1:]:
        n *= i
        yield n


def xproduct(iterable):
    """
    Generates product of an iterable (cumulative)
    Returns the max value.
    """
    return max(i for i in gen_product(iterable))


def chunker(iterable, n_values=4, step=1):
    """
    Generator to return a section of an iterable.
    The output increments by the step amount given.
    """
    start = 0
    end = start + n_values
    while end <= len(iterable):
        yield iterable[start:end]
        start += step
        end = start + n_values




if __name__ == '__main__':
    #-- Run all sections (row, column, and diagonal
    #-- Print the result to console

    while True:
        max_value = 0
        #-- Row-wise products
        for r, row in enum(matrix):
            xrow = chunker(row)
            max_product = max([xproduct(chunk) for c_idx, chunk in enum(xrow) if not 0 in chunk])
            if max_product > max_value:
                max_value = max_product
        
        
        
        #-- Column-wise products
        for r, _ in enum(matrix):
            col = [row[r] for row in matrix]
            xcol = chunker(col)
            max_product = max([xproduct(chunk) for c_idx, chunk in enum(xcol) if not 0 in chunk])
            if max_product > max_value:
                max_value = max_product
        
        
        
        #-- Diagonal products
        #-- (top-left to bottom-right and top-right to bottom-left)
        diags = list()
        for r, row in enum(matrix):
            for c in range(xlen(matrix[r]) - r):
                #-- Top-left to bottom-right
                d_norm = [row[r + (c - 1)] for r, row in enum(matrix) if 0 <= r + (c - 1) < xlen(row)]
                if not d_norm in diags and len(d_norm) > 3:
                    diags.append(d_norm)
        
                #-- Top-right to bottom-left
                d_opp = [row[xlen(row) - 1 - (r + (c - 1))] for r, row in enum(matrix) if 0 <= r + (c - 1) < xlen(row)]
                if not d_opp in diags and len(d_opp) > 3:
                    diags.append(d_opp)
        
        #-- Once diagonals are collected, find max value.
        for idx, diag in enum(diags):
            xdiag = chunker(diag)
            max_product = max([xproduct(chunk) for c_idx, chunk in enum(xdiag) if not 0 in chunk])
            if max_product > max_value:
                max_value = max_product
        break
    if max_value:
        print(f'The maximum product found in the matrix was: {max_value}')



