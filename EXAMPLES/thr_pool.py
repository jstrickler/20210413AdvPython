#!/usr/bin/env python

import random
from multiprocessing.dummy import Pool # <1>
from multiprocessing import Pool # <1>

POOL_SIZE = 32 # <2>

with open('../DATA/words.txt') as words_in:
    WORDS = [w.strip() for w in words_in] # <3>

random.shuffle(WORDS) # <4>

def my_task(arg):  # <5>
    return arg.upper()

tpool = Pool(POOL_SIZE) # <6>

# LIST   = somepool.map(function, iterable of anything)
WORD_LIST = tpool.map(my_task, WORDS) # <7>

# if my_task() takes 2 arguments, pass <pool>.map a list of 2-tuples,
#  [(arg1, arg2), (arg1, arg2), ...]

print(WORDS[:20])
print(WORD_LIST[:20])  # <8>

print("Processed {} words.".format(len(WORD_LIST)))
