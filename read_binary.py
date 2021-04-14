with open('DATA/apple.png', 'rb') as apple_in:
    data = apple_in.read(100)

    print(len(data))
    print(type(data))
    print(data)
    print(list(data))
    more_data = apple_in.read(100)
    apple_in.seek(1000)
    even_more_data = apple_in.read(25)
    print(apple_in.tell())



