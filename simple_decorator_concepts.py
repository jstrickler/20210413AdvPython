from datetime import datetime
from functools import wraps

log = []

def wrapper(func):

    @wraps(func)
    def replacement(*args, **kwargs):
        log.append((func.__name__, datetime.now().ctime()))
        return func(*args, **kwargs)

    return replacement

@wrapper
def spam(a, b):
    print("hello from spam()")

#  spam = wrapper(spam)

@wrapper
def ham(x):
    print("hello from ham()")

@wrapper
def toast():
    print("toasty!!")

spam(1, 2)
ham('wombat')
ham('aardvark')
spam(9, 18.6)
toast()
toast()
toast()


print(log)

for f in spam, ham, toast:
    print(f.__name__)
