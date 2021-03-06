#!/usr/bin/env python
from timeit import Timer

setup_code = """
data = list(range(100000000))
list1 = list(data)
list2 = list(data)
list3 = list(data)
"""

codes = [
    '''new_list = list1 + list2 + list3''',

    '''
new_list = []
for x in list1, list2, list3:
    new_list.extend(x)
    ''',
]

for code in codes:
    t = Timer(code, setup_code)
    print(code, '\n')
    print(t.timeit(10))
    print()
