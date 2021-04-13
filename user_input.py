
while True:
    x = input("Best Marvel Character (q to quit): ")
    if x == 'q':
        break
    if x == '':
        continue
    print("Nope: you are wrong about", x)

while True:
    raw_num = input("How many times have you watched WandaVision? ")
    if raw_num == 'q':
        break

    # num = input(...)
    # num = int(num)
    try:
        num = int(raw_num)
    except Exception as err:
        print(err)
    else:
        print(num * '*')

