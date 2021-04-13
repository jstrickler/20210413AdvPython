
actor = 'Chris Hemsworth'
animals = ['wombat', 'platypus', 'kookaburra', 'wallaby']
person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

for thing in actor, animals, person:
    print(type(thing), len(thing), thing[0], thing[-1])
print()

# for k, v in some_dict.items():
#     pass
#
# for i, thing in enumerate(things):
#     pass

# a, b, c = some_variable_with_three_values
print(animals[0:2])
print(animals[1:3])
print(actor[0:4])  # usually actor[:4]
print(actor[:4])
print(actor[6:9])
print()

for animal in animals:
    print(animal.upper())
print()

s = 'abc'
for char in s:
    print(char)
print()

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

for code in airports:
    print(code)
print()

print("animals: {}\n".format(animals))

more_animals = ['kangaroo', 'koala']
animals.extend(more_animals)
print("animals: {}\n".format(animals))

animals.insert(3, 'quokka')
print("animals: {}\n".format(animals))
animals.append(more_animals)
print("animals: {}\n".format(animals))

even_more_animals = ['crocodile', 'shark']

animals[2:2] = even_more_animals
print("animals: {}\n".format(animals))

x = animals.pop(2)
print("animals: {}\n".format(animals))
print("x: {}\n".format(x))

list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']
list3 = ['g', 'h', 'i']

new_list = list1 + list2 + list3  # should BENCHMARK this!

new_list = []
for folder in folders:
    temp_list = ['what', 'ever']
    new_list.extend(temp_list)

colors = ['red', 'blue']
c1 = ['green', 'orange']
c2 = ['purple', 'mauve', 'taupe', 'black']
# colors.extend(c1 + c2)
for c in c1, c2:
    colors.extend(c)




