
person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

print(type(person), person[0], len(person))

def get_name(p):
    return f"{p[0]} {p[1]}"

print(get_name(person))

t1 = ()    # empty tuple
t2 = 5,    # one-element tuple
t3 = 1, 2, 3, 4, 5  # five-element, etc

# iterable unpacking  (works with any iterable)
first_name, last_name, product, dob = person

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

print(people[0])
print(people[0][0])
print(people[0][0][0])

for p in people:
    first_name, last_name, product, dob = p
    print(first_name, last_name)
print('-' * 60)

for first_name, last_name, product, dob in people:
    print(first_name, last_name)
print('-' * 60)

places = [('Durham', 'NC'), ('Albany', 'NY'), ('Nashville', 'TN'), ('Richmond', 'Front Royal', 'Roanoke', 'VA', 123)]

for city, state, *junk in places:
    print(city, state, end=' ')
    if junk:
        print(junk, end='')
    print()

values = ['a', 'b', 'c', 'd', 'e', 'f']
x, y, *z = values
print(x, y, z)
x, *y, z = values
print(x, y, z)
*x, y, z = values
print(x, y, z)

colors = ['red', 'blue', 'purple']
for i, color in enumerate(colors):
    print(i, color)
print(list(enumerate(colors)))

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'RDU': 'Raleigh-Durham',
}

for code, name in airports.items():
    print(code, name)
print(list(airports.items()))

print(airports)

print(airports.items())

a = [1, 2, 3,]
b = 5, 6, 7,
c = [
    (1, 2, 3,),
    (4, 5, 6,),
]

d = 5,  # d is tuple
e = 5   # e is int






