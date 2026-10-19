# ==========================================
# 0. LIST COMPREHENSIONS (Review & Deep Dive)
# ==========================================
print("--- 0. List Comprehensions ---")
# Syntax: [expression for item in iterable]
# A highly optimized way to map and filter data in a single line.

raw_prices = [10, 22, 35, 40, 55]

# without a comprehension, to create an populate a list takes a few lines
taxed_prices = []
for price in raw_prices:
    taxed_prices.append(price * 1.0)

# Mapping: Apply an operation to every item (e.g., add 7% sales tax)
taxed_prices = [price * 1.07 for price in raw_prices]
print(f"Taxed prices: {taxed_prices}")

for tax in taxed_prices:
    print(f'{tax=:.2f}' for tax in taxed_prices)

# Filtering: Keep only items that meet a condition (e.g., even numbers)
# Syntax: [expression for item in iterable if condition]
raw_prices = [10, 22, 35, 40, 55]
even_prices = [price for price in raw_prices if price % 2 == 0]
print(f"Even prices only: {even_prices}")


# ==========================================
# 1. DICTIONARY COMPREHENSIONS
# ==========================================
print("\n--- 1. Dictionary Comprehensions ---")
# Syntax: {key_expression: value_expression for item in iterable}
# Excellent for transforming data or flipping dictionaries.

students = ["Ptolemy", "Emily", "Victor"]

# Creating a dictionary from a list (e.g., name as key, length of name as value)
name_lengths = {student: len(student) for student in students}
print(f"Name lengths: {name_lengths}")

# Flipping a dictionary (Swapping keys and values)
course_codes = {"Python": "MIS330", "Databases": "MIS331"}
flipped_courses = {code: name for name, code in course_codes.items()}
print(f"Flipped dict: {flipped_courses}")

# FAILS: Forgetting .items() when iterating over a dictionary in a comprehension
# bad_flip = {course_codes[k]: k for k in course_codes} # Works, but is un-Pythonic
# syntax_fail = {v: k for k, v in course_codes} # ValueError: not enough values to unpack


# ==========================================
# 2. SET COMPREHENSIONS
# ==========================================
print("\n--- 2. Set Comprehensions ---")
# Syntax: {expression for item in iterable}
# Similar to list comprehensions, but uses curly braces and automatically deduplicates!

messy_data = [10, 20, 10, 30, 20, 40, 50, 40]

# Automatically filters out duplicates while applying logic
list_tens = [num // 10 for num in messy_data] # list []
unique_tens = {num // 10 for num in messy_data} # set {}
print(f"{list_tens=} {unique_tens=}")

# Extracting unique characters (ignoring spaces)
quote = "data analytics"
unique_chars = {char for char in quote if char != " "}
print(f"Unique characters in string: {unique_chars}")


# ==========================================
# 3. THE IF/ELSE TRAP (Ternary vs Filter)
# ==========================================
print("\n--- 3. The If/Else Trap ---")
# Placement of the 'if' changes everything. 
# IF ONLY: Goes at the END (acts as a filter).
# IF/ELSE: Goes at the BEGINNING (acts as a ternary mapping operation).

grades = [95, 65, 82, 50, 88]

# If only (Filtering out failing grades)
passing_only = [g for g in grades if g >= 70]
print(f"Passing only (Filter): {passing_only}")

# If/Else (Mapping to Pass/Fail labels)
# Notice the 'for' loop is pushed to the very end!
labels = ["Pass" if g >= 70 else "Fail" for g in grades]
print(f"Pass/Fail Labels (Ternary): {labels}")

# FAILS: Putting if/else at the end is a SyntaxError
# bad_syntax = [g for g in grades if g >= 70 else "Fail"] # SyntaxError: expected ']'


# ==========================================
# 4. NESTED COMPREHENSIONS (Flattening)
# ==========================================
print("\n--- 4. Nested Comprehensions (Flattening) ---")
# You can put multiple 'for' loops inside a single comprehension.
# Rule of thumb: Read them from left to right, just like standard nested loops.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Goal: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Outer loop comes first, inner loop comes second!
flat_list = [num for row in matrix for num in row]
print(f"Flattened matrix: {flat_list}")


# ==========================================
# 5. NESTED COMPREHENSIONS (Matrix Transposition)
# ==========================================
print("\n--- 5. Matrix Transposition ---")
# Sometimes the comprehension itself contains another comprehension.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# This builds a new matrix where rows become columns.
transposed = [[row[i] for row in matrix] for i in range(3)]
print("Transposed Matrix:")
for row in transposed:
    print(row)

# ==========================================
# 6. THE PROBLEM: MEMORY EXHAUSTION
# ==========================================
print("--- 0. The Memory Problem ---")
# List comprehensions generate the ENTIRE list in memory at once.
# If you create a list of 10 million items, your computer might crash.

import sys
standard_list = [x ** 2 for x in range(1000000)]
print(f"List memory size: {sys.getsizeof(standard_list)} bytes")


# ==========================================
# 6.1 GENERATOR EXPRESSIONS to the rescue!
# ==========================================
print("\n--- 1. Generator Expressions ---")
# Replace brackets [] with parentheses (). 
# This creates a generator object that yields one item at a time, saving massive amounts of RAM.

gen_expr = (x ** 2 for x in range(1000000))
print(f"Generator type: {type(gen_expr)}")
print(f"Generator memory size: {sys.getsizeof(gen_expr)} bytes") # Radically smaller!

# # You can iterate through it just like a list
print("First three values from generator:")
for _ in range(3):
    print(next(gen_expr))

print(next(gen_expr)) # always continues where it left off

# # NOTE: Memory Warning
# # List comprehensions load the entire list into RAM at once. 
# # If processing 10 million rows, use a Generator Expression instead!
# # Generator Expression (uses parentheses instead of brackets):
# # memory_safe = (x * 2 for x in massive_dataset)

# # ==========================================
# # 7. COMMON ERRORS & PITFALLS
# # ==========================================
# print("\n--- 6. Common Errors ---")

# # FAILS: Trying to put an unhashable type (like a list) into a set comprehension
# # nested_lists = [[1, 2], [3, 4], [1, 2]]
# # unique_lists = {lst for lst in nested_lists} # TypeError: unhashable type: 'list'
# # FIX: Convert the inner lists to tuples first: {tuple(lst) for lst in nested_lists}
