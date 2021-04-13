import os

for folder, folders, file_names in os.walk('.'):
    if '.git' in folders:
        folders.remove('.git')
    for file_name in file_names:
        file_path = os.path.join(folder, file_name)
        stat_info = os.stat(file_path)
        print(stat_info.st_ino, file_path)

