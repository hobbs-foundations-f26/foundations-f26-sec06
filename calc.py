# NOTE: a module in python is a single file (with a .py extension) that contains Python code.
# a package is a collection of modules in a folder 
# that contains a special __init__.py file (which can be empty).

# module/package      a program that is imported
# vs
# script              the main program being run

author = "Alice"

def sum(a,b,*args):
    return_val = a+b
    for arg in args:
        return_val += arg
    
    return return_val

def product(a,b,*args):
    return_val = a*b
    for arg in args:
        return_val *= arg
    
    return return_val

# NOTE: The below lines run no matter whether the file is run as a script or imported as a module.
print(f'{sum(3,4,56)=}')

# NOTE: The if __name__ == '__main__': block runs only when the file is run as a script, not when it is imported as a module.
if __name__ == '__main__':
    print(f'{sum(3,4)=}')
    print(f'{sum(3,4,5,6,7,8)=}')
    print(f'{product(3,4)=}')
    print(f'{product(3,4,5,6,7,8)=}')
