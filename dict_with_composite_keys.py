from pprint import pprint

data = {}

# possible dict keys:
# int, float, bool, str, bytes, tuple (of immutables)

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        key = name, title
        data[key] = color, quest, comment

pprint(data)
print('-' * 60)

print(data['Arthur', 'King'])
print(data['Arthur', 'Sir'])
