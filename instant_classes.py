

class_name = 'Cat'

def meow(self):
    print("Meowwwwwww")

Cat = type(class_name, (), {'meow': meow})

c1 = Cat()
c2 = Cat()
for cat in c1, c2:
    cat.meow()
