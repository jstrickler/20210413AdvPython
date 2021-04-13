
value = 56

if value > 75:
    print("alpha")
    print("beta")
elif value > 50:
    print('gamma')
    print('delta')
elif value > 25:
    print('eta')
    print('epsilon')
else:
    print('mu')
    print('nu')

class TrueThing:
    def __bool__(self):
        return True

class FalseThing:
    def __bool__(self):
        return False

t = TrueThing()
f = FalseThing()
print(bool(t), bool(f))

ERROR = False

#   color = ERROR?'RED':'GREEN'      C/C++/Java etc
color = 'RED' if ERROR else 'GREEN'
print(color)

