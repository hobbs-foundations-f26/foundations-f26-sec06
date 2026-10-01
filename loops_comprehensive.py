# loops_comprehensive.py
# A complete lecture script covering Python loops, iteration tools, and loop control.
# Uncomment the designated lines during the lecture to demonstrate errors.

# ==========================================
# 0. THE RANGE() FUNCTION
# ==========================================
print("--- 0. The range() Function ---")
# range() *generates* a sequence of numbers. Highly used in for-loops.
# Syntax: range(start, stop, step) - 'stop' is exclusive!

print("range(5):", list(range(5)))          # 0, 1, 2, 3, 4 (default start is 0)
print("range(2, 6):", list(range(2, 6)))    # 2, 3, 4, 5
print("range(10, 0, -2):", list(range(10, 0, -2))) # 10, 8, 6, 4, 2 (stepping backward)

# The range() object is a brief/short description of a sequence.
# A sequence can be veeeeeery long.  A list needs to *store* the sequence in memory.
# the range object *generates* the sequence.  It doens't have to rememeber the past
# or have knowledge of the far future. It only needs to know 
# 1) where it is now (start)
# 2) where to go next (step)
# 3) when to stop (stop)
print("range(10, 0, -2): without a cast shows that it's a new type",range(10, 0, -2))
range_object = range(0, 1000000, 1) # this stores in memory 3 numbers
list_object = list(range(0, 1000000, 1)) # this stores in memory 1000000 numbers

# ==========================================
# 1. BASIC FOR LOOPS (Lists)
# ==========================================
print("\n--- 1. Basic For Loops (Lists) ---")
# 'for' loops in Python are "for-each" loops. They iterate over items in a collection directly.
departments = ["Accounting", "Finance", "MSIS"]

# this is a *really* nice feature in python, the ability to iterate through the
# *values* of something, not just numbers (e.g. having to use range)
for dept in departments:
    print(f"Rutgers Business Department: {dept}")

# Using range() when you need the index, though enumerate() is usually better (see section 8)
for i in range(len(departments)):
    print(f"Index {i}: {departments[i]}")

# ==========================================
# 2. ITERATING OVER STRINGS & TUPLES
# ==========================================
print("\n--- 2. Iterating Over Strings & Tuples ---")
course_code = "MIS330"

# Strings are iterable sequence of characters
# notice that this is the same as iterating through the *values* of a list
# here, char stores the value of character in that step of the sequence.
print("Characters in course code:")
for char in course_code:
    print(f"- {char}")

print("\nTuple unpacking in a loop (if dealing with a list of tuples):")
roster = [("Ptolemy", 3.8), ("Emily", 3.9)]
for name, gpa in roster:
    print(f"Student: {name}, GPA: {gpa}")


# ==========================================
# 3. ITERATING OVER DICTIONARIES
# ==========================================
print("\n--- 3. Iterating Over Dictionaries ---")
enrollment = {"Python": 45, "Databases": 120, "Security": 35}

# Default iteration is over keys
for course in enrollment:
    print(f"Course: {course}")

# Iterating over both keys and values using .items() - VERY COMMON
for course, students in enrollment.items():
    print(f"{course} has {students} students enrolled.")


# ==========================================
# 4. WHILE LOOPS
# ==========================================
print("\n--- 4. While Loops ---")
# 'while' loops continue executing as long as a condition remains True.
# Great for when you don't know exactly how many times you need to loop.

inventory = 3
while inventory > 0:
    print(f"Selling item... {inventory} remaining.")
    inventory -= 1  # CRITICAL: Must modify the condition variable to avoid an infinite loop
print("Out of stock!")


# # ==========================================
# # 5. LOOP CONTROL (break, continue)
# # ==========================================
# print("\n--- 5. Loop Control (break, continue) ---")

# # break: Exits the loop completely, skipping any remaining iterations
# print("Demonstrating 'break':")
# for num in range(1, 10):
#     if num == 4:
#         print("Hit 4, breaking out of loop!")
#         break
#     print(num)

# # continue: Skips the rest of the CURRENT iteration and moves to the next one
# print("\nDemonstrating 'continue':")
# for num in range(1, 6):
#     if num == 3:
#         print("Skipping 3!")
#         continue
#     print(num)


# # ==========================================
# # 6. THE LOOP 'ELSE' CLAUSE (Python Specific)
# # ==========================================
# print("\n--- 6. The Loop 'else' Clause ---")
# # The 'else' block runs ONLY if the loop finishes completely without hitting a 'break'.
# # Think of it as the "no-break" clause. Excellent for search operations.

# target_id = 99
# student_ids = [10, 20, 30, 40]

# for sid in student_ids:
#     if sid == target_id:
#         print(f"Found student ID {target_id}!")
#         break
# else:
#     # This runs because the loop finished without breaking
#     print(f"Student ID {target_id} was not found in the roster.")


# # ==========================================
# # 7. NESTED LOOPS
# # ==========================================
# print("\n--- 7. Nested Loops ---")
# # Loops inside of loops. The inner loop finishes all its iterations for EVERY single outer loop iteration.
# terms = ["Fall", "Spring"]
# classes = ["Python", "Stats"]

# for term in terms:
#     print(f"--- {term} Term ---")
#     for cls in classes:
#         print(f"Teaching: {cls}")


# # ==========================================
# # 8. PYTHONIC ITERATION: enumerate() & zip()
# # ==========================================
# print("\n--- 8. Pythonic Iteration (enumerate & zip) ---")

# # enumerate(): Gets both the index and the value at the same time.
# # Much cleaner than doing: for i in range(len(list))
# top_companies = ["Apple", "Microsoft", "Nvidia"]
# for rank, company in enumerate(top_companies, start=1):
#     print(f"Rank {rank}: {company}")

# # zip(): Iterates through multiple lists in parallel, stopping at the shortest one.
# names = ["Ptolemy", "Emily", "Victor"]
# grades = ["A", "A", "B"]
# for name, grade in zip(names, grades):
#     print(f"{name} earned an {grade}")


# # ==========================================
# # 9. COMMON ERRORS & PITFALLS
# # ==========================================
# print("\n--- 9. Common Errors ---")

# # FAILS: Modifying a list while iterating over it can cause skipped elements or logic errors
# # active_users = ["Alice", "Bob", "Charlie"]
# # for user in active_users:
# #     if user == "Bob":
# #         active_users.remove(user) # Danger! Iterating shifts elements, causing skips.
# # print(active_users) 
# # LECTURE FIX: Iterate over a copy instead: for user in active_users.copy():

# # FAILS: The Infinite Loop (Interrupt with Ctrl+C in terminal)
# # x = 10
# # while x > 5:
# #     print("This will run forever because x never decreases!")
# #     # Missing: x -= 1