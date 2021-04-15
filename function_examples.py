
def get_message():
    return "Hello, Python world"

def show_message():
    message = get_message()
    print(message)

show_message()

m1 = get_message()  # calls the function
m2 = get_message    # IS the function

print(m1, m2)
print(m2())

class Foo:
    def spam(self):  # method
        pass

    @classmethod
    def ham(cls):
        pass

    @staticmethod
    def toast():
        pass



def wombat(name):
    print("My name is", name)
    return 42

wfun = wombat


print(wfun, wombat)
x =  wombat
print(x)
print(wombat("Willie"))
x("Wanda")
print(x("Wanda"))

wfun("Willard")

a = wombat("Walter") # a set to return value
b = wombat   # b set to function ITSELF





















