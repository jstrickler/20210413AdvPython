airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(len(airports))
for x in 'EWR', 'RDU', 'ELM', 'GXY', 'ZOMBIE':
    print(airports.get(x, "NOT FOUND!"))
print()

#   non-mut...
#   key   value
for code, name in airports.items():
    print(code, name)
print()

# mutable
# list set dict

# immutable
# everything else (str, int, float, bytes, tuple, bool, ...)

# class Thing:
#     def __setitem__(self, key, value):
#         pass
#
#     def __getitem__(self):
#         pass
#
#     def __hash__(self):  # can be dict key
#         pass

foo = {
    'm': 5,
    'a': 9,
    'z': 4,
    't': 3,
}

for letter, number in foo.items():
    print(letter, number)
print()




