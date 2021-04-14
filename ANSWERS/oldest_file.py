#!/usr/bin/python
import sys
import os
from datetime import datetime

if len(sys.argv) > 1:
    directory = sys.argv[1]
else:
    print("Syntax: %s directory" % sys.argv[0])
    sys.exit(1)

# get files in specified directory and prepend the full path
entries = [os.path.join(directory, file) for file in os.listdir(directory)]

# filter out non-files
files = [f for f in entries if os.path.isfile(f)]

# transform list of filenames into list of (filename,unixtimestamp) tuples
files = [[f, os.path.getmtime(f)] for f in files]

# sort files by timestamp
sorted_files = sorted(files, key=lambda e: e[1])

# convert from Unix timestamp to python datetime object
filetime = datetime.fromtimestamp(sorted_files[0][1])

# print as human-readable date (which it defaults to)
print(filetime, sorted_files[0][0])

# slightly less Pythonic:

raw_files = []
for entry in os.listdir(directory):
    file_path = os.path.join(directory, entry)
    if os.path.isfile(file_path):
        raw_files.append((file_path, os.path.getmtime(file_path)))

def sort_by_time(t):
    return t[1]

sorted_files = sorted(raw_files, key=sort_by_time)

file_name, file_timestamp = sorted_files[0]
oldest_date = datetime.fromtimestamp(file_timestamp)
print(file_name, oldest_date)



