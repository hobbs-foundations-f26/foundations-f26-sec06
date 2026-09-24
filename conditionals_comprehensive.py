# ==========================================
# 0. BASIC IF / ELSE
# ==========================================
print("--- 0. Basic If / Else ---")
student_score = 85
passing_score = 70

# Execution flows into the indented block only if the condition evaluates to True
if student_score >= passing_score:
    print("Result: Pass")
else:
    print("Result: Fail")

# A quick aside about blocks and indentation
if student_score >= passing_score:
    print("Result: Pass")
    print('do this too')
    print('we are still doing things because we\'re in the True block')
else:
    print("Result: Fail")


# # ==========================================
# # 1. THE ELIF LADDER (Multiple Conditions)
# # ==========================================
print("\n--- 1. Elif Ladder ---")
# Python evaluates top-to-bottom and stops at the FIRST True condition.
grade = 88

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
else:
    print("Grade: F")


# ==========================================
# 2. LOGICAL OPERATORS (and, or, not)
# ==========================================
print("\n--- 2. Logical Operators ---")
is_registered = True
has_prerequisites = False

# AND: Both must be true
if is_registered and has_prerequisites:
    print("Status: Enrolled in course.")
else:
    print("Status: Missing registration or prerequisites.")

# OR: At least one must be true
if is_registered or has_prerequisites:
    print("Status: Partial requirements met.")

# NOT: Inverts the boolean value
if not has_prerequisites:
    print("Action Required: Please complete prerequisite courses.")


# ==========================================
# 3. NESTED CONDITIONALS
# ==========================================
print("\n--- 3. Nested Conditionals ---")
user_role = "admin"
is_active_account = True

if is_active_account:
    if user_role == "admin":
        print("Access granted: Full admin panel.")
    else:
        print("Access granted: Standard user dashboard.")
else:
    print("Access denied: Account suspended.")


# ==========================================
# 4. CONDITIONAL EXPRESSIONS (Ternary Operator)
# ==========================================
print("\n--- 4. Conditional Expressions ---")
# A concise way to write simple if/else statements on a single line
# Syntax: [value_if_true] if [condition] else [value_if_false]
inventory_count = 5

if inventory_count > 0:
    status_message = "In Stock"  
else: 
    status_message = "Out of Stock"
status_message = "In Stock" if inventory_count > 0 else "Out of Stock"
print(f"Inventory Status: {status_message}")


# # ==========================================
# # 5. CHAINED COMPARISONS (Pythonic Idiom)
# # ==========================================
# print("\n--- 5. Chained Comparisons ---")
# # Python allows mathematical chaining of operators, cleaner than using 'and'
# exam_score = 85

# # The standard way (common in other languages)
# if exam_score >= 80 and exam_score < 90:
#     print("Standard approach: B Grade")

# # The Pythonic way
# if 80 <= exam_score < 90:
#     print("Chained approach: B Grade")


# # ==========================================
# # 6. IMPLICIT TRUTHINESS
# # ==========================================
# print("\n--- 6. Implicit Truthiness ---")
# # Falsy values: False, None, 0, 0.0, "", [], {}
# enrolled_students = []

# # Anti-pattern (Not Pythonic)
# if len(enrolled_students) == 0:
#     print("Anti-pattern: Class is empty")

# # Pythonic approach: Empty structures evaluate to False implicitly
# if not enrolled_students:
#     print("Pythonic: Class is empty")


# # ==========================================
# # 7. IDENTITY VS EQUALITY (is None)
# # ==========================================
# print("\n--- 7. Identity (is None) ---")
# # Always use 'is' to check for None, never '=='. 'is' checks memory identity.
# active_session = None

# if active_session is None:
#     print("No user is currently logged in.")
# elif active_session is not None:
#     print("User session active.")


# # ==========================================
# # 8. MATCH-CASE (Python 3.10+)
# # ==========================================
# print("\n--- 8. Match-Case ---")
# # A cleaner alternative to long elif ladders for checking specific values
# command = "load"

# match command:
#     case "start":
#         print("Starting system...")
#     case "stop":
#         print("Stopping system...")
#     case "load" | "save":  # The pipe (|) acts as an 'or'
#         print("File operation initiated.")
#     case _:  # The underscore acts as the default catch-all
#         print("Unknown command.")


# # ==========================================
# # 9. THE 'PASS' STATEMENT
# # ==========================================
# print("\n--- 9. The Pass Statement ---")
# # 'pass' acts as a null operation/placeholder for empty code blocks.
# is_maintenance_window = True

# if is_maintenance_window:
#     # TODO: Write the logic to disable the database connection later
#     pass  
# else:
#     print("System operating normally.")


# # ==========================================
# # 10. THE WALRUS OPERATOR (:=) [Python 3.8+]
# # ==========================================
# print("\n--- 10. Assignment Expressions (Walrus) ---")
# # Assigns a value and evaluates it in a single expression.
# data_payload = "Rutgers Business School"

# # Assign and check simultaneously
# if (n := len(data_payload)) > 15:
#     print(f"Walrus: String is long ({n} chars)")


# # ==========================================
# # 11. ALL() AND ANY() WITH ITERABLES
# # ==========================================
# print("\n--- 11. all() and any() ---")
# prereqs = [True, True, False]

# # all() returns True only if EVERY element is Truthy
# if all(prereqs):
#     print("Student has met all prerequisites.")
# else:
#     print("Missing some prerequisites.")

# # any() returns True if AT LEAST ONE element is Truthy
# if any(prereqs):
#     print("Student has met at least one prerequisite.")


# # ==========================================
# # 12. COMMON ERRORS & PITFALLS
# # ==========================================
# print("\n--- 12. Common Errors ---")

# # FAILS: IndentationError (Python relies entirely on whitespace for code blocks)
# # if grade > 50:
# # print("You passed!") # IndentationError: expected an indented block

# # FAILS: Using '=' (assignment) instead of '==' (equality check)
# # if user_role = "admin": # SyntaxError: invalid syntax
# #     print("Admin")

# # FAILS: Using 'else if' instead of 'elif'
# # if grade >= 90:
# #     print("A")
# # else if grade >= 80: # SyntaxError: invalid syntax
# #     print("B")

# # FAILS: Missing the pass statement leaves an empty block
# # if is_maintenance_window:
# #                 # Python expects code here!
# # else:           # IndentationError: expected an indented block
# #     print("System operating normally.")