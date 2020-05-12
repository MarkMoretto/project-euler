
"""
Purpose: 
Date created: 2020-04-19

Contributor(s):
    Mark M.
"""

from __future__ import print_function

from pyspark import SparkContext

# from pyspark.sql import SparkSession
# spark = SparkSession.builder.appName("test1").getOrCreate()

sc = SparkContext(appName="matrices1")

rdd = sc.parallelize([1, 2,])
sorted(rdd.cartesian(rdd).collect())

n = 10
rng = sc.range(1, n + 1)
sum_ = rng.sum()
print(f"The sum of the numbers from 1 to 10 is: {sum_}")

sc.stop()