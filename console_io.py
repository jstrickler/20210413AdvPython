import sys

x = 5.9
y = "weasel"
z = 14
m = ['Mary', 'Martha', 'Mimsy']

print(x, y, z, m)
# default sep is ' '
# default end is '\n'

print(x, y, z, m, sep="=")
print(x, y, z, m, sep=" - ")
print(x, y, z, m, sep=", ")
print(x, y, z, m, sep="")
print(x, y, z, m, sep="\n")

print(x, y, sep='/', end=' ')
print(z, m, sep='+')

print("Look out!", file=sys.stderr)

print("Look out!", file=sys.stdout, sep=' ', end='\n', flush=False)




