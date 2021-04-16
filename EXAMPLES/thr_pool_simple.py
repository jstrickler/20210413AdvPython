#!/usr/bin/env python
from multiprocessing.dummy import Pool # <1>

POOL_SIZE = 16 # <2>

def my_task(num):  # <5>
    return num * 10000

tpool = Pool(POOL_SIZE) # <6>

# data
nums = list(range(10))

# pass the data to the pool of threads
results = tpool.map(my_task, nums) # <7>

result_dict = dict(zip(nums, results))

print('results:', results)  # <8>
print('result_dict:', result_dict)
result_tuples = list(zip(nums, results))
print('result_tuples:', result_tuples)
