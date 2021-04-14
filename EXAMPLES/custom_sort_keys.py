#!/usr/bin/env python

fruit = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon",
         "Kiwi", "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG",
         "pear", "banana", "Tamarind", "persimmon", "elderberry", "peach",
         "BLUEberry", "lychee", "grape"]

def ignore_case(item):  # <1>
    return item.lower()  # <2>

fs1 = sorted(fruit, key=ignore_case)  # <3>
print("Ignoring case:")
print(" ".join(fs1), end="\n\n")

fs2x = sorted(fruit, key=str.lower)
print("fs2x: {}\n".format(fs2x))

flen = sorted(fruit, key=len)
print("flen: {}\n".format(flen))

def by_last(x):  # x is ONE FRUIT, not entire array
    return list(reversed(x.lower()))

# key function arg must be a function that accepts one object (which is one element of sequence to be sorted)
flast = sorted(fruit, key=by_last)
print("flast: {}\n".format(flast))

nums = [65, 8.2, -10, 14.5, -3, -70.6, 28, 19]
n1 = sorted(nums)
print("n1: {}\n".format(n1))
n2 = sorted(nums, key=abs)
print("n2: {}\n".format(n2))
n3 = sorted(nums, key=str)
print("n3: {}\n".format(n3))

# stuff = ['wombat', 27, 8.6, None, ['foo', 'bar']]
# s1 = sorted(stuff)

"""
@results = sort { lc($a) cmp lc($b) } @original_array;   # perl
"""

def by_length_then_name(item):
    return len(item), item.lower() # <4>

fs2 = sorted(fruit, key=by_length_then_name)
print("By length, then name:")
print(" ".join(fs2))
print()

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = sorted(nums)  # <5>
print("Numbers sorted numerically:")
for n in n1:
    print(n, end=' ')
print("\n")

n2 = sorted(nums, key=str)  # <6>
print("Numbers sorted as strings:")
for n in n2:
    print(n, end=' ')
print('\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print('-' * 60)

def by_last_name(p):
    return p[1], p[0], p[2]

for person in sorted(people, key=by_last_name):
    print(person)
print('-' * 60)




