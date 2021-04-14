import os

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

# non-Pythonic:
f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0: {}\n".format(f0))

f1 = [f.upper() for f in fruits]   #similar to apply() and map()

print("f1: {}\n".format(f1))

# [EXPR for VAR ... in ITERABLE if CONDITION ...]

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2: {}\n".format(f2))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
big_nums = [n for n in nums if n > 300]
print("big_nums: {}\n".format(big_nums))

f3 = [f for f in fruits if f.startswith('p')]
print("f3: {}\n".format(f3))

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
companies = [p[2] for p in people]
print("companies: {}\n".format(companies))

FOLDER = 'DATA'
file_paths = [os.path.join(FOLDER, f) for f in os.listdir(FOLDER) if f.endswith('.txt')]
print("file_paths: {}\n".format(file_paths))




