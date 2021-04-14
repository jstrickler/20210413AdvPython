import re

s = "WomBat"


print(re.search("bat", s, re.I | re.S))

print([int(x) for x in (re.I, re.S, re.M, re.X)])

