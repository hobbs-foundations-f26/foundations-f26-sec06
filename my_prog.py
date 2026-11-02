# NOTE: importing a calc.py does not use the .py extension, just the name of the file (without the .py)
# import calc.py # DO NOT DO THIS
import calc  # THIS IS CORRECT


print(calc.author)
print(calc.sum(8,8))
print(calc.product(8,8))


















# NOTE: The below behaves the same as the above
# but renames calc as c, so you can use c instead of calc 
# to access the functions and variables in the module.

# import calc as c

# print(c.author)
# print(c.sum(8,8))
# print(c.product(8,8))

# NOTE: The below behaves the same as the above
# but imports only the functions and variables you want to use

# from calc import sum, product
# from calc import author as calc_author

# author = "Bob"

# print(author)
# print(calc_author)
# print(sum(8,8))
# print(product(8,8))



