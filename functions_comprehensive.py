# ==========================================
# 0. DEFINING & CALLING (The Basics)
# ==========================================
print("--- 0. Defining & Calling ---")
# 'def' creates the function. It doesn't run until explicitly called.
def greetStudent(name):
    # Docstrings (triple quotes) explain what the function does
    """Prints a welcome message for a student."""
    print(f"Welcome to Business Programming, {name}!")

# this is called "calling"/"invoking"/"executing" the function.
greetStudent("Emily")
greetStudent("Ptolemy")


# ==========================================
# 1. RETURN VALUES
# ==========================================
print("\n--- 1. Return Values ---")
# Functions evaluate to whatever they 'return'. If no return is specified, they return None.

def calculate_roi(revenue, cost):
    roi = (revenue - cost) / cost
    return roi # the word "return" is used to specify a function's output

# Capturing the returned value into a variable
project_roi = calculate_roi(15000, 10000)
print(f"Project ROI: {project_roi:.1%}")

# Multiple returns (returns a packed tuple)
def summarize_grades(scores):
    return min(scores), max(scores), sum(scores)/len(scores)

# you can capture multiple outputs with tuple unpacking
low, high, avg = summarize_grades([85, 92, 78, 100])
print(f"Low: {low}, High: {high}, Avg: {avg}")

result = summarize_grades([85, 92, 78, 100])
print(f"{type(result)}, {result} Low: {result[0]}, High: {result[1]}, Avg: {result[2]}")

# Note, in python functions *always* return something. 
# By default this is the value None
def greetStudent(name):
    # Docstrings (triple quotes) explain what the function does
    """Prints a welcome message for a student."""
    print(f"Welcome to Business Programming, {name}!")
    # return None  # without writing this, the behavior is the same

# this is called "calling"/"invoking"/"executing" the function.
print(greetStudent("Emily")) # this will print the value None

# ==========================================
# 2. DEFAULT PARAMETERS
# ==========================================
print("\n--- 2. Default Parameters ---")
# You can assign default values to parameters. They must come AFTER non-default parameters.

# here, price is called a positional argument, and discount_rate is called a named argument
def calculate_discount(price, discount_rate=0.10):
    return price * (1 - discount_rate)

# # Uses the default 10% discount
print(f"Standard discount: ${calculate_discount(100):.2f}")

# Overrides the default with a 25% discount
print(f"Special discount: ${calculate_discount(100, 0.25):.2f}")

# FAILS: Non-default arguments cannot follow default arguments in the definition
# def invalid_func(discount_rate=0.10, price): # SyntaxError: non-default argument follows default argument
#     pass


# ==========================================
# 3. KEYWORD VS POSITIONAL ARGUMENTS
# ==========================================
print("\n--- 3. Keyword vs Positional ---")
def create_profile(first, last, major):
    print(f"Profile: {first} {last}, Major: {major}")

# Positional (Order matters entirely)
create_profile("Ptolemy", "Hobbs", "BAIT")

# Keyword (Order doesn't matter, clarity improves)
create_profile(major="Finance", last="Smith", first="Victor")

# FAILS: Positional arguments cannot follow keyword arguments in the function call
# create_profile(major="Accounting", "John", "Doe") # SyntaxError: positional argument follows keyword argument
# create_profile("John", "Doe", major="Accounting") # SyntaxError: positional argument follows keyword argument


# ==========================================
# 4. VARIABLE ARGUMENTS (*args, **kwargs)
# ==========================================
print("\n--- 4. *args and **kwargs ---")
# The * character "upgrades" an input (only one!!)
# to catch an unlimited number of **positional** arguments into a TUPLE.
def calculate_average(*args):
    if not args:
        return 0
    return sum(args) / len(args)

print(f"Average of 0 grades: {calculate_average()}")
print(f"Average of 2 grades: {calculate_average(80,90)}")
print(f"Average of 5 grades: {calculate_average(90, 85, 100, 75, 88)}")

# **kwargs catches an unlimited number of keyword arguments into a DICTIONARY.
def build_server_config(**kwargs):
    for key, value in kwargs.items():
        print(f"Setting {key} -> {value}")

build_server_config(os="Ubuntu Server", ram="32GB", storage="1TB NVMe")


# ==========================================
# 5. VARIABLE SCOPE (Local vs Global)
# ==========================================
print("\n--- 5. Variable Scope ---")
# Variables created inside a function are LOCAL and disappear when the function ends.
university_name = "Rutgers"  # Global scope

def update_records():
    term = "Fall 2026"       # Local scope
    print(f"Accessing global: {university_name}")
    print(f"Accessing local: {term}")

update_records()

# FAILS: Cannot access a local variable from the global scope
# print(term)  # NameError: name 'term' is not defined

# The 'global' keyword (Generally avoid this in good software design)
def change_university():
    global university_name
    university_name = "Rutgers Business School"

change_university()
print(f"Modified global: {university_name}")


# ==========================================
# 6. THE MUTABLE DEFAULT ARGUMENT PITFALL
# ==========================================
print("\n--- 6. The Mutable Default Gotcha ---")
# This is the most common bug in intermediate Python. 
# Default arguments are evaluated ONLY ONCE when the function is defined, not every time it's called.

# Anti-pattern:
def add_student_bad(name, roster=[]):
    roster.append(name)
    return roster

print("Bad Roster 1:", add_student_bad("Alice"))
print("Bad Roster 2:", add_student_bad("Bob"))   # Wait, Alice is still here! The list persists.

# Pythonic Fix: Use None as the default
def add_student_good(name, roster=None):
    if roster is None:
        roster = []  # Creates a fresh list every time
    roster.append(name)
    return roster

print("Good Roster 1:", add_student_good("Alice"))
print("Good Roster 2:", add_student_good("Bob"))


# ==========================================
# 7. TYPE HINTING (Python 3.5+)
# ==========================================
print("\n--- 7. Type Hinting ---")
# Type hints don't enforce types at runtime, but they help IDEs (like VS Code) 
# and developers catch errors before running the code.

def calculate_tax(revenue: float, tax_bracket: str = "standard") -> float:
    if tax_bracket == "standard":
        return revenue * 0.21
    return revenue * 0.15

print(f"Corporate tax: ${calculate_tax(100000.0):.2f}")


# ==========================================
# 8. LAMBDA FUNCTIONS (Anonymous Functions)
# ==========================================
print("\n--- 8. Lambda Functions ---")
# One-line functions without a name. Used heavily in data science (Pandas) for quick operations.
# Syntax: lambda arguments: expression

square = lambda x: x ** 2
print(f"Lambda squared: {square(5)}")

# Often used with sorting dictionaries or complex lists
students = [("Ptolemy", 3.8), ("Victor", 3.2), ("Emily", 3.9)]
# Sort by GPA (the second element in each tuple)
students.sort(key=lambda student: student[1], reverse=True)
print(f"Sorted by GPA: {students}")
