#!/usr/bin/env python

from threading import Thread, Lock
import random
import time

all_links_lock = Lock()

all_links = []

# the work you want to do
def doit(num):  # <1>
    # fetch page using URL
    # find links
    # add links to some global list
    time.sleep(random.randint(1,3))
    with all_links_lock:
       all_links.append(num * 100)
    print("Hello from thread {}".format(num), flush=True)

all_threads = []

for i in range(10):
    t = Thread(target=doit, args=(i,))  # <2>
    t.start() # <3>
    all_threads.append(t)

print("Threads launched.")  # <4>

for t in all_threads:
    t.join()

print("Done.")  # <4>


print("All links:", all_links)
