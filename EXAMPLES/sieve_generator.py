#!/usr/bin/env python

def next_prime(limit):
    flags = set()  # <1>

    for i in range(2, limit):
        if i in flags:
            continue
        for j in range(2 * i, limit + 1, i):
            flags.add(j)  # <2>
        yield i  # <3>  # get next value


np = next_prime(200)  # <4>
# for i in range(5):
#     print(next(np))
# print(next(np))

for prime in np:  # <5>   # next(np) -> np.__next__()
    print(prime, end=' ')
print()
