
x = []


def f1():
    x.append(5)

def f2():
    x.append(4)

def f3():
    x.pop()


print(x)
f1()
print(x)
f2()
print(x)
f3()
print(x)
