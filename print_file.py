import sys

file_name = sys.argv[1]
with open(file_name) as f:
    print(f.read())

