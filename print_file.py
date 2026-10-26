import sys

if len(sys.argv) == 1:
    print('Too few arguments, please give the name of a file to read')
else:
    file_name = sys.argv[1]
    with open(file_name) as f:
        print(f.read())

