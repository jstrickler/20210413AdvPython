from glob import glob

files = glob('DATA/*.txt')

print(files)

print(glob('DATA/*.xmz'))

print(glob('schmoo'))

