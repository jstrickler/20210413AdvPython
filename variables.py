x = 5
#  1. determine type of argument
#  2. create object of type int
#  3. assign value 5 to int
#  4. "bind" nickname "x" to that object

# every object has
# -- type
# -- value
# -- unique ID

t = type(x)
print(t)

y = x
# bind "y" to same object to which "x" is bound
print(x, type(x), id(x))
print(y, type(y), id(y))
print()

x = 10  # create new object, assign 'x'
print(x, type(x), id(x))
print(y, type(y), id(y))
print()

things = [1, 2, 3]
stuff = things # stuff and things are same object
stuff.append('wombat')
print("things: {}\n".format(things))
print("stuff: {}\n".format(stuff))

items = list(stuff)  # create new list
items.append("muffin")
print("items: {}\n".format(items))
print("things: {}\n".format(things))
print("stuff: {}\n".format(stuff))
items = stuff[::]  # create new list
print(id(things), id(stuff), id(items))
print()

a1 = [
    ['a', 'b', 'c'],
    [10, 20, 30],
]
a2 = list(a1)
print(id(a1), id(a2))
a1.append(['do', 're', 'mi'])
print("a1: {}\n".format(a1))
print("a2: {}\n".format(a2))

a1[0].append('d')
print("a1: {}\n".format(a1))
print("a2: {}\n".format(a2))

from copy import deepcopy
a3 = deepcopy(a1)
a1[0].append('e')
print("a1: {}\n".format(a1))
print("a2: {}\n".format(a2))
print("a3: {}\n".format(a3))

a4 = a1  # alias -- a1 and a4 are same object

x = 5
print(x * '*')

animal = None  # similar to Null, null, nil, etc
print(animal)

# A-Z a-z 0-9 _
# part_number  cheese_flavor  funny_hat
foo_bar = 22

_ = 100
print(_)






