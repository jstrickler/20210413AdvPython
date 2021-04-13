
file_path = 'DATA/mary.txt'

file_obj = open(file_path)
# ...
file_obj.close()

with open(file_path) as mary_in: # <-- file obj
    for raw_line in mary_in:  # <-- NOT a list of lines
        line = raw_line.rstrip()  # remove trailing \n \r <spc> \t
        print(line)
print('-' * 60)

with open(file_path) as mary_in:
    file_contents = mary_in.read()  # read whole file
    print("normal:")
    print(file_contents)
    print()
    print("raw:")
    print(repr(file_contents))

print('-' * 60)

with open(file_path) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

with open(file_path) as mary_in:
    all_lines_without_nl = mary_in.read().splitlines()
#    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)
