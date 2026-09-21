# A lecture script covering Python Booleans, comparison operators, and logic.

# ==========================================
# 0. BOOLEAN BASICS & LITERALS
# ==========================================
print("--- 0. Boolean Basics ---")
is_active = True
is_logged_in = False

print(f"Type of True: {type(is_active)}")
print(f"Type of False: {type(is_logged_in)}")


# ==========================================
# 1. COMPARISON OPERATORS
# ==========================================
print("\n--- 1. Comparison Operators ---")
x = 10
y = 20

print(f"x == y (Equal to): {x == y}")
print(f"x != y (Not equal to): {x != y}")
print(f"x < y (Less than): {x < y}")
print(f"x > y (Greater than): {x > y}")
print(f"10 <= 10 (Less than or equal): {10 <= 10}")
print(f"20 >= 15 (Greater than or equal): {20 >= 15}")

# FAILS: Using assignment (=) instead of equality (==) inside expressions/conditions
# if x = 10:  # SyntaxError: invalid syntax
#     print("Error")


# ==========================================
# 2. LOGICAL OPERATORS (and, or, not)
# ==========================================
print("\n--- 2. Logical Operators ---")
has_id = True
has_ticket = False

# AND: Both must be True
print(f"Can enter (and): {has_id and has_ticket}")

# OR: At least one must be True
print(f"Can enter (or): {has_id or has_ticket}")

# NOT: Inverts the boolean value
print(f"Not has_ticket: {not has_ticket}")


# ==========================================
# 3. TRUTHY AND FALSY VALUES
# ==========================================
print("\n--- 3. Truthiness & Falsiness ---")
# In Python, non-Boolean objects evaluate to True or False in boolean contexts.
# Falsy values: False, None, 0, 0.0, "" (empty string), [] (empty list), {} (empty dict)

username = ""  # Empty string is Falsy
if username:
    print(f"Welcome, {username}!")
else:
    print("Error: Username cannot be blank.")

items_in_cart = 3  # Non-zero integer is Truthy
if items_in_cart:
    print(f"You have {items_in_cart} items in your cart.")


# ==========================================
# 4. IDENTITY VS. EQUALITY (is vs ==)
# ==========================================
print("\n--- 4. Identity (is) vs Equality (==) ---")
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print(f"list_a == list_b (Same values?): {list_a == list_b}")  # True
print(f"list_a is list_b (Same object in memory?): {list_a is list_b}")  # False
print(f"list_a is list_c (Same object in memory?): {list_a is list_c}")  # True


# ==========================================
# 5. SHORT-CIRCUIT EVALUATION
# ==========================================
print("\n--- 5. Short-Circuit Evaluation ---")
# Python stops evaluating logical expressions as soon as the outcome is determined.
x = 0
y = 10

# Safe division because the first condition fails, so the second isn't evaluated (avoids ZeroDivisionError)
if x != 0 and (y / x > 1):
    print("Condition met")
else:
    print("Short-circuited safely without ZeroDivisionError.")
