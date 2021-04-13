import os

start_dir = '.'
# start_dir = os.path.abspath(start_dir)

for folder, folders, files in os.walk(start_dir):
    if '.git' in folders:
        folders.remove('.git')  # how to skip a folder on search
    print(folder)
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(folder, file_name)
            file_size = os.path.getsize(file_path)
            stat_info = os.stat(file_path)
            mode = stat_info.st_mode
            user_read = 256
            readable = 'Y' if bool(mode & user_read) else 'N'
            group_write = 16
            writable = 'Y' if bool(mode & group_write) else 'N'

            if file_size > 1000:
                print("    {:8d} {:16b} {} {} {}".format(file_size, mode, readable, writable, file_name))


