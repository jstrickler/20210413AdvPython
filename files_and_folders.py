import os

FOLDER = 'DATA'
FILE_NAME = 'alice.txt'

file_path = os.path.join(FOLDER, FILE_NAME)
print("file_path: {}\n".format(file_path))

file_size = os.path.getsize(file_path)
print("file_size: {}\n".format(file_size))

file_base = os.path.basename(file_path)
file_dir = os.path.dirname(file_path)
file_abs = os.path.abspath(file_path)
print("paths:", file_base, file_dir, file_abs)

