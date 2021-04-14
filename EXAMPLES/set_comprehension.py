#!/usr/bin/env python
import re

# \W   [^a-zA-Z0-9_]
# \w   [a-zA-Z0-9_]
# \w+
# \W+ one or more non-letter/digit/_ in a row
with open("../DATA/alice.txt") as mary_in:
    contents = mary_in.read()
    s = {w.lower() for w in re.findall(r'\w+', contents) if w} #<1>
print(s)
print(len(s))

