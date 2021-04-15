

class Dog:

    def __init__(self, name):
        self.nickname = name

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, name):
        if isinstance(name, str):
            self._nickname = name
        else:
            raise TypeError("Nickname must be a string")

    def bark(self):
        print("woof woof")

if __name__ == '__main__':

    d1 = Dog('Andy')
    d2 = Dog('Nellie')

    print(d1.nickname)
    d2.bark()

    print(dir(d1))

    print(d1.nickname)
    print(d1._nickname)  # naughty!!
    print(d1.bark)

    attr_name = "nickname"
    print(getattr(d1, attr_name))
    b = getattr(d1, 'bark')
    b()
    print("\U0001F92F")
    print('-' * 60)

    for attr_name in dir(d1):
        if not attr_name.startswith('__'):
            attr_value = getattr(d1, attr_name)
            print(f"{attr_name:10s} {str(attr_value)[:40]}")


    x = 'bark'
    if hasattr(d1, x):
        getattr(d1, x)()

    f = lambda self: print("pant pant!")

    setattr(Dog, 'pant', f)

    d1.pant()


