#!/usr/bin/env python

fruits = ['watermelon', 'Apple', 'Mango', 'KIWI', 'apricot', 'LEMON', 'guava']

def spam(e):
    return e.lower()


sfruits = sorted(fruits, key=lambda e: e.lower())  # <1>

print(" ".join(sfruits))
