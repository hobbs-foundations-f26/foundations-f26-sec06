# ==========================================
# 0. LISTS: CREATION & MUTABILITY
# ==========================================
print("--- 0. Lists: Creation & Mutability ---")
courses = ["Python", "MIS", "Business Analytics"]

# Lists are mutable: elements can be modified in place
courses[1] = "Information System Security"
print(f"Modified courses list: {courses}")


# ==========================================
# 1. LIST METHODS: ADDING & REMOVING
# ==========================================
print("\n--- 1. List Methods (Add/Remove) ---")
# .append() adds an item to the end
courses.append("Database Management")
print(f"After append: {courses}")

# .insert() adds an item at a specific index
courses.insert(0, "Foundations")
print(f"After insert: {courses}")

# .remove() deletes the first matching value
courses.remove("MIS") if "MIS" in courses else None
print(f"After remove: {courses}")

# .pop() removes and returns an item by index (default is the last item)
popped_course = courses.pop()
print(f"Popped item: '{popped_course}', Remaining: {courses}")


# ==========================================
# 2. LIST METHODS: ORDERING & UTILITIES
# ==========================================
print("\n--- 2. List Ordering & Utilities ---")
scores = [88, 92, 75, 100, 64]

# Sorting in place vs sorted() builtin
scores.sort()  # Modifies original list
print(f"Sorted ascending: {scores}")

scores.sort(reverse=True)
print(f"Sorted descending: {scores}")

print(f"Count of 100s: {scores.count(100)}")
print(f"Index of score 92: {scores.index(92)}")

# FAILS: Trying to sort a list containing mixed, incompatible data types
# mixed_list = [42, "Python", True]
# mixed_list.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'


# ==========================================
# 3. INDEXING & SLICING (Same mechanics as strings)
# ==========================================
print("\n--- 3. List Indexing & Slicing ---")
data = [10, 20, 30, 40, 50, 60]
print(f"First element: {data[0]}")
print(f"Slice index 1 to 4: {data[1:4]}")
print(f"Reversed list via slicing: {data[::-1]}")


# ==========================================
# 4. TUPLES: IMMUTABLE SEQUENCES
# ==========================================
print("\n--- 4. Tuples ---")
# Defined using parentheses (). Immutable: cannot be altered, appended, or sorted.
professor = ("Nathaniel", "Hobbs", "Rutgers")
print(f"Professor tuple: {professor}")
print(f"First name: {professor[0]}")

# FAILS: Tuples do not support item assignment (Immutability)
# professor[0] = "Nat"  # TypeError: 'tuple' object does not support item assignment


# ==========================================
# 5. TUPLE UNPACKING
# ==========================================
print("\n--- 5. Tuple Unpacking ---")
first, last, institution = professor
print(f"Unpacked variables -> First: {first}, Last: {last}, School: {institution}")

# Variable swapping is clean via tuple packaging/unpacking
a = 5
b = 10
a, b = b, a
print(f"Swapped values -> a: {a}, b: {b}")


# ==========================================
# 6. REFERENCES, ALIASING, & COPYING
# ==========================================
print("\n--- 6. References & Aliasing Pitfall ---")
original_list = [1, 2, 3]
alias_list = original_list  # Points to the exact same object in memory!
alias_list.append(4)

print(f"Original list modified via alias: {original_list}")  # [1, 2, 3, 4]!

# Proper way to clone/copy a list
true_copy = original_list.copy()
true_copy.append(5)
print(f"Original list safe: {original_list}")
print(f"True copy modified: {true_copy}")
