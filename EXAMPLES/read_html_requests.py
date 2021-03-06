#!/usr/bin/env python

import requests

response = requests.get("https://www.python.org")  # <1>

for header, value in sorted(response.headers.items()): # <2>
    print(header, value)
print()

# response.content raw content (bytes)
# response.text    (str)

print(response.text[:200])   # <3>
print('...')
print(response.text[-200:])   # <4>
