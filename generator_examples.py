colors = ['red', 'purple', 'pink', 'magenta']

ecolors = enumerate(colors)
print(ecolors)

# print(list(ecolors))

print("ROUND 1")
for i, color in ecolors:
    print(i, color)
    if i == 2:
        break
print()

print("ROUND 2")
for i, color in ecolors:
    print(i, color)
print()

r = reversed(colors)
print(r)
for color in r:
    print(color)

c1 = [c.upper() for c in colors]
print("c1: {}\n".format(c1))

colors.append('mauve')

cgen = (c.upper() for c in colors)
print("cgen: {}\n".format(cgen))
for color in cgen:
    print(color)
print()


