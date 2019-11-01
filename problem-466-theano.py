
"""
Purpose: Project Euler problems
Date created: 2019-10-23

Contributor(s): Mark M.

ID: 466
Title: Distinct terms in a multiplication table
URI: https://projecteuler.net/problem=466
Status: Incomplete

Notes: Using Theano

Desc:
    Let P(m,n) be the number of distinct terms in an m×n multiplication table.

    For example, a 3×4 multiplication table looks like this:
    
    ×	1	2	3	4
    1	1	2	3	4
    2	2	4	6	8
    3	3	6	9	12
    There are 8 distinct terms {1,2,3,4,6,8,9,12}, therefore P(3,4) = 8.
    
    You are given that:
    P(64,64) = 1263,
    P(12,345) = 1998, and
    P(32,10**15) = 13826382602124302.
    
    Find P(64,10**16).
"""


import numpy as np
import theano as th
import theano.tensor as tt

# th.config.device='gpu'

# X = tt.dscalar('X')
# y = tt.dscalar('y')
# z = X + y
# f = th.function([X, y], z)

# f(2,3)
# np.allclose(f(16.3, 12.1), 28.4)


X = tt.zvector('X')
y = tt.zvector('y')




m = tt.dmatrix('m')
n = tt.dmatrix('n')
zout = tt.dot(m, n)

P = th.function([m, n], zout)


s_outputs, s_updates = th.scan(fn=lambda i, j: tt.dot(i, j))
P = th.function(inputs=[m, n], outputs=s_outputs, updates=s_updates)

M = np.array(3, dtype=th.config.floatX)
N = np.array(4, dtype=th.config.floatX)

P(M,N)



z = tt.zscalar('z')

output, updates = th.scan(fn=lambda i, j: tt.dot(i, j), sequences=[X, y])

multiply_f = th.function(inputs=[X, y], outputs=output, updates=update)


P = th.function(inputs=[m, n], z)

def iter_it(n):
    for i in range(1, n + 1):
        yield i


def step(m_row, cumulative_sum):
    return m_row + cumulative_sum



def P(m, n):

    x_iter = iter_it(m)
    y_iter = iter_it(n)

    x = tf.constant([i for i in x_iter])
    y = tf.constant([i for i in y_iter])

    return np.count_nonzero(np.unique(arr))













