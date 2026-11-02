# modules_packages.py
# Uncomment the designated lines during the lecture to demonstrate errors.

# NOTE: a module in python is a single file (with a .py extension) that contains Python code.
# a package is a collection of modules in a folder 
# that contains a special __init__.py file (which can be empty).

# module/package      a program that is imported
# vs
# script              the main program being run

# ==========================================
# 0. IMPORTING BUILT-IN MODULES
# ==========================================
print("--- 0. Importing Built-in Modules ---")
# Python comes with a "batteries included" standard library.
import math
import random


# Access functions inside a module using dot notation
print(f"Pi is approximately: {math.pi}")
# the square root is not built into the core language, but is available in the math module
# python by itself can only compute: +, -, *, /, **, //, %
print(f"Square root of 144: {math.sqrt(144)}")


# Working with random things
print(f"Random number between 1-10: {random.randint(1, 10)}") # rand integer between [1,10]
print(f"Random float between 0-1: {random.random()}") # random float between (0,1)
print(f"Randomly shuffling a list: {random.shuffle([1,2,3,4,5])}") # shuffles a list **in place**

my_list = [1,2,3,4,5]
random.shuffle(my_list) # shuffles a list **in place** (my_list itself changes in memory)
print(f"Randomly shuffling a list: {my_list}") 
# ==========================================
# 1. IMPORT ALIASING (import X as Y)
# ==========================================
print("\n--- 1. Import Aliasing ---")
# Very common in data science to save typing for long module names.
import datetime as dt

# Now we use 'dt' instead of typing out 'datetime'
current_time = dt.datetime.now()
print(f"Current timestamp: {current_time}")

# NOTE: here are some common standard industry aliases:
import pandas as pd
import numpy as np

# if you fail running the program because of a missing module, you can install it using pip:
# pip install <module_name>

# ==========================================
# 2. SPECIFIC IMPORTS (from X import Y)
# ==========================================
print("\n--- 2. Specific Imports ---")
# Instead of loading the whole module, import only the specific functions you need.
# This allows you to drop the dot notation.

import os # os for operating system, like file paths, directories, etc.

print(f"Current Working Directory: {os.getcwd()}")
print(os.listdir()) # Lists files in the current folder

# vs

from os import getcwd, listdir

print(f"Current Working Directory: {getcwd()}")
print(listdir()) # Lists files in the current folder

# FAILS: The danger of "Star Imports" (from math import *)
# It clutters your namespace and can silently overwrite your own variables.
# For example, if you had a variable named 'pi', 'from math import *' would overwrite it.
# ALWAYS avoid star imports in production code.
# from os import * # DO NOT DO THIS IN REAL CODE
# # vs
# import os  # Just take the whole thing like this if you need to


# # ==========================================
# # 3. CREATING CUSTOM MODULES
# # ==========================================
# print("\n--- 3. Custom Modules ---")
# # Any Python file (.py) is automatically a module. 
# # If you have a file named 'analytics_tools.py' in the same folder:

# # import analytics_tools
# # clean_data = analytics_tools.remove_outliers(my_dataset)

# # FAILS: Trying to import a file that doesn't exist or is in the wrong folder
# try:
#     import nonexistent_module
# except ModuleNotFoundError as e:
#     print(f"Caught Import Error: {e}")


# # ==========================================
# # 4. PACKAGES & DIRECTORY STRUCTURES
# # ==========================================
# print("\n--- 4. Packages ---")
# # A package is simply a folder containing multiple Python modules.
# # Historically, a folder needed an empty file named '__init__.py' to be recognized 
# # as a package, though Python 3.3+ made this optional (Namespace packages).

# # If you have a folder structure like:
# # /my_project
# #   /database
# #       connections.py
# #       queries.py

# # You would import it using dot notation for the path:
# # from database.connections import connect_to_mysql


# # ==========================================
# # 5. THE DUNDER MAIN BLOCK (Crucial Pattern)
# # ==========================================
# print("\n--- 5. The __name__ == '__main__' Block ---")
# # When you import a module, Python executes ALL the code in that file immediately.
# # If 'analytics_tools.py' has print statements or function calls at the bottom, 
# # they will run the moment you import it. 

# # To prevent this, we use the Dunder (Double Underscore) Main block.
# # Code inside this block ONLY runs if the file is executed directly, 
# # NOT if it is imported by another script.

# if __name__ == "__main__":
#     print("This file is being run directly as the main program!")
#     print("If another script imported this file, this text would NOT print.")
    
#     # NOTE: Best practice is to put all your script execution logic 
#     # (like argparse and main function calls) inside this block.
