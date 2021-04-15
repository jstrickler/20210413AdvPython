
a = 100  # global variable

def alpha():  # global function
    print("in alpha(): a is", a)
    b = 200   # local variable

alpha()

print(a)

def beta():
    name = 'Louise'

    def gamma():
        # warning warning Will Robinson!!!
        # global a  # DON'T DO THIS!
        a = 'Alice'
        print("in gamma(): a is", a)
        print("in gamma(): nickname is", name)

    return gamma

f = beta()
f()

santa = beta()
santa()
print("in main: a is", a)





