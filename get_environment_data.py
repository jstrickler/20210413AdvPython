import os

print(os.environ)
print('-' * 60)

print(os.getenv('USER'))  # os.environ.get(...)
print(os.getenv('PYTHONPATH'))
print(os.getenv('WOMBAT', "UGGGGGHHHH"))

s = "mycommand -u $USER -x blah blahdy blah"
print(os.path.expandvars(s))




