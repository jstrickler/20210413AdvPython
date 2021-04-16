#!/usr/bin/env python

from threading import Thread
import random
import time


class SimpleThread(Thread):
    def __init__(self, num, other):
        super().__init__()  # <1>
        self._threadnum = num

    def run(self):  # <2>
        self._wombat = self._threadnum * 10000
        time.sleep(random.randint(1, 3))
        print("Hello from thread {}".format(self._threadnum))

    @property
    def wombat(self):
        return self._wombat

pool = []
for i in range(10):
    x = i * 10
    t = SimpleThread(i, x)  # <3>
    t.start()  # <4>
    pool.append(t)

print("Threads launched")

results = []
for t in pool:
    t.join()
    results.append(t.result)

print("results:", results)

print("Done.")
