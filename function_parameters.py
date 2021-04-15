
def double(x):
    return x * 2

a1 = double(5)
a2 = double("mint")
a3 = double(True)

print(a1, a2, a3)

def make_line(char, size):
    return char * size

print(make_line('*', 10))
print(make_line('-', 50))

def spam(a, b, *c):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("---")

spam(1, 2)
spam(1, 2, 3)
spam(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def ham(*x, a, b):
    print("optional:", x)
    print("named:", a, b)
    print()

ham(a=1, b=2)
ham(1, 2, 3, a=500, b=600)

def toast(*, a, b):
    pass

def bacon(p1, p2, *, p3, p4):
    pass

bacon('a', 'b', p3='c', p4='d')

def process_file(file_name, *, output_format='pdf'):
    pass

process_file('foo.txt')
process_file('foo.txt', output_format='png')

def config(**values):
    print(values, '\n')

config(country='Australia', animal='wombat', food='beer')

def wacky(p1, p2, *p3, p4=12, p5="smersh", **p6):
    pass







