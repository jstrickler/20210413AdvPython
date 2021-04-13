
set1 = {'apple', 'banana', 'orange', 'kumquat', 'peach', 'lemon'}
set2 = {'lemon', 'lemon', 'lemon', 'lime', 'strawberry', 'apple',
        'jackfruit', 'lemon', 'lemon'}

print("set1: {}\n".format(set1))
print("set2: {}\n".format(set2))

print("Both:", set1 & set2)  # intersection
print("Not both:", set1 ^ set2)  # Xor
print("Either:", set1 | set2)  # union
print("set 1 only:", set1 - set2)
print("set 2 only:", set2 - set1)


