#!/usr/bin/env python
import os
from pprint import pprint

animals = ['OWL', 'Badger', 'bushbaby', 'Tiger', 'Wombat', 'GORILLA', 'AARDVARK']

# {KEY: VALUE for VAR ... in ITERABLE if CONDITION}
d = {a.lower(): len(a) for a in animals}  # <1>

print(d, '\n')

FOLDER = '../DATA'
file_paths = [os.path.join(FOLDER, f) for f in os.listdir(FOLDER) if f.endswith('.txt')]
file_sizes = {fp: os.path.getsize(fp) for fp in file_paths}
print(file_sizes, '\n')


words = ['unicorn', 'stigmata', 'barley', 'bookkeeper']

d = {w:{c:w.count(c) for c in sorted(w)} for w in words} # <2>

# for word, word_signature in d.items():
#     print(word, word_signature)
pprint(d)
