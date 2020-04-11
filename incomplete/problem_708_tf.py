
"""
Purpose: 
Date created: 2020-04-10

Contributor(s):
    Mark M.
"""


import tensorflow as tf
import tensorflow_core as tfc

# tf.compat.v1.disable_eager_execution()
# tf.compat.v1.InteractiveSession()



# def count_gpus(verbose=False):
#     gpu_ct = len(tf.config.experimental.list_physical_devices("GPU"))
#     if verbose:
#         print(f"Number of GPUs available: {gpu_ct}")
#     return gpu_ct > 0

# def gpu_available():
#     if not count_gpus():
#         print(f"No GPU(s) detected.")
#     else:
#         print(f"GPU(s) found!")


# v = tf.Variable(1.0)
# v.assign_add(1)
# v.read_value()
# v.value().numpy()

# a = tf.Variable(1.0)
# b = tf.Variable(2.0)
# a.read_value()
# a.assign(2.0 * b)
# b.assign_add(1.0 * a) # Like addition.  2.0 + 4.0 -> 6.0

"""

two_ = tf.Variable(2.0, dtype=tf.float16)
ttwo_ = tf.constant([two_.numpy()], dtype=tf.float32)
ttwo = tf.concat([ttwo_, ttwo_], 0)
ttwo = tf.concat([ttwo, ttwo_], 0)
tf.math.reduce_prod(ttwo,0)
"""


# While loop
# n_ = tf.constant(90.0, dtype=tf.float64)
# n_div = n_.assign(n_ / 2)

# res_ = tf.constant(1, dtype=tf.uint64)
# res_incr = result.assign(tf.math.multiply(res_ , 2))

# c = lambda n: tf.math.mod(n, 2) == 0
# b = lambda n: (result.assign(result * 2), n.assign(n / 2))
# r = tf.while_loop(c, b, [i])



# tarr = tf.TensorArray(dtype=tf.uint64, size=0, dynamic_size=True)


# @tf.function
# def w(q):
#     return tf.cast(q ** (1/2) + 1, dtype=tf.uint64)


tarr = tf.TensorArray(dtype=tf.uint64, size=0, dynamic_size=True)

@tf.function
def f(n):
    """Prime decomposition function."""

    result = 1

    while n % 2 == 0:
        result *= 2
        n /= 2

    n_max = int(n ** (1/2)) + 1
    for i in range(3, n_max, 2):
        while n % i == 0:
            result *= 2
            n /= 2

    if n > 2:
        result *= 2

    return tf.cast(result, dtype=tf.uint64)

# print(tf.autograph.to_code(f.python_function)) # print graph

total = tf.Variable(0)

@tf.function
def S(N):
    N += 1
    rng = tf.range(1, 10, dtype=tf.float64)
    for i in rng:
        n = tf.cast(i, dtype=tf.float64)

        total.assign_add(f(n))





if __name__ == "__main__":
    tot = tf.Variable(0)

    N = 1000
    S(N)
    print(tot)








# @tf.function
# def f(n):
#     """Prime decomposition function."""

#     result = tf.cast(1, dtype=tf.uint64)
#     two = tf.constant(2, dtype=tf.uint64)

#     while tf.equal(tf.math.mod(n, 2), 0):
#         result.assign_add(result * two) # result *= 2
#         n /= 2

#     n_max = tf.cast(n ** (1/2) + 1, dtype=tf.uint64)
#     for i in tf.range(3, n_max, 2):
#         while tf.equal(tf.math.mod(n, i), 0):
#             result.assign_add(result * two) # result *= 2
#             n /= 2

#     if tf.greater(n, 2): # n > 2
#         result.assign_add(result * two) # result *= 2

#     return tf.cast(result, dtype=tf.uint64)
