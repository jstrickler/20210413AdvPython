
animal = 'wombat'

def spam():
    print("I am a can of fatty meat")


var_name = "animal"
function_name = "spam"

g = globals()
print(g[var_name])

s = g[function_name]
s()

print(globals()['animal'])

g['color'] = 'blue'

print(color)

print("\U0001F92F")

g['bark'] = lambda : print("woof woof")

bark()
print("\U0001F92F")


def splat(char):
    x = char * 5
    print(x)
    print(locals())

splat('*')

m = dict(g)
for thing, thing_value in m.items():
    print(thing, str(thing_value)[:30])


