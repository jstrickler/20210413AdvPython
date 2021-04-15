from wombat.misc import johnlib
# find wombat/misc folders using PYTHONPATH
# then load johnlib.py from misc folder
import sys

johnlib.spam()
johnlib.ham()

johnlib._toast() # naughty programmer


for path in sys.path:
    print(path)
