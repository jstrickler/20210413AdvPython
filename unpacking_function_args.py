
def spam(a, b, c):
    print(a)
    print(b)
    print(c)

spam(1, 2, 3)
spam('fee', 'fi', 'fo')

values = 100, 200, 300, 400, 500
print(type(values))

spam(values[0], values[1], values[2])
spam(*values[:3])  # unpacks iterable to individual arguments


