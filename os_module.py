import os   # os.path

print(os.getcwd())
print(os.getenv('USER'))
print(os.getuid(), os.getgid())
print(os.getpid(), os.getppid())

# kill(pid, sig)

print(os.listdir('DATA'))
print('-' * 60)

os.makedirs('fee/fi/fo/fum', exist_ok=True)
os.makedirs('ANSWERS', exist_ok=True)

file_name = 'delete_me.txt'
if os.path.exists(file_name):
    os.remove(file_name)  # or os.unlink(...) same thing

s = os.stat('DATA/mary.txt')
print(s)
print()

os.rmdir('fee/fi/fo/fum')




