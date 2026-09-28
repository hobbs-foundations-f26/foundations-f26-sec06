# ==========================================
# 0. DICTIONARIES: CREATION & STRUCTURE
# ==========================================
# here's a picture to reference: https://hughewilliams.com/wp-content/uploads/2012/09/450px-hash_table_5_0_1_1_1_1_1_ll-svg.png
print("--- 0. Creation & Structure ---")
# Dictionaries store data in key-value pairs. Keys must be unique and immutable.
student = {
    "name": "Ptolemy",  # syntax is key:value  (each entry is seperated with a ,)
    "major": "Business Analytics",
    "gpa": 3.8
} 

# doing the above with a list is not reliable. It would be built on promises, e.g.
# [name, major, gpa] , i.e. pretty please, the below values mean this, okay? please?
student = ["Ptolemy", "Business Analytics", 3.8]


print(f"Dictionary type: {type(student)}")
print(f"Full dictionary: {student}")

# Keys must be unique
student = {
    "name": "Ptolemy",  # syntax is key:value  (each entry is seperated with a ,)
    "name": "Business Analytics",
    "gpa": 3.8
}

print(f"Dictionary type: {type(student)}")
print(f"Full dictionary: {student}")


# # ==========================================
# # 1. ACCESSING, MODIFYING, & ADDING
# # ==========================================
# print("\n--- 1. Accessing & Modifying ---")
# # Accessing values using bracket notation
# print(f"Student Name: {student['name']}")

# # Modifying an existing value
# student["gpa"] = 3.95
# print(f"Updated GPA: {student['gpa']}")

# # Adding a new key-value pair dynamically
# student["graduation_year"] = 2028
# print(f"After adding graduation_year: {student}")


# # ==========================================
# # 2. SAFE ACCESS: THE .get() METHOD
# # ==========================================
# print("\n--- 2. Safe Access (.get) ---")
# # FAILS: Bracket notation throws an error if the key doesn't exist
# # print(student["minor"])  # KeyError: 'minor'

# # SUCCESS: .get() returns None (or a default value) if the key is missing
# minor = student.get("minor")
# print(f"Using .get('minor'): {minor}")

# minor_with_default = student.get("minor", "No minor declared")
# print(f"Using .get() with default: {minor_with_default}")


# # ==========================================
# # 3. DICTIONARY METHODS (Views)
# # ==========================================
# print("\n--- 3. Dictionary Views ---")
# # These methods return dynamic view objects, which are iterable
# print(f"Keys: {student.keys()}")
# print(f"Values: {student.values()}")
# print(f"Items (Tuples of key-value pairs): {student.items()}")

# # Converting views to lists if indexing is needed
# keys_list = list(student.keys())
# print(f"Keys as a list: {keys_list}")


# # ==========================================
# # 4. REMOVING ITEMS
# # ==========================================
# print("\n--- 4. Removing Items ---")
# # .pop() removes the key and returns its value
# grad_year = student.pop("graduation_year")
# print(f"Popped value: {grad_year}")
# print(f"Dictionary after pop: {student}")

# # 'del' keyword removes the key-value pair but returns nothing
# del student["major"]
# print(f"Dictionary after del: {student}")


# # ==========================================
# # 5. ITERATING THROUGH DICTIONARIES
# # ==========================================
# print("\n--- 5. Iterating ---")
# course_enrollment = {
#     "Foundations of Programming": 45,
#     "Operations Management": 120,
#     "Information System Security": 35
# }

# # Looping defaults to iterating over KEYS
# print("Looping (default):")
# for course in course_enrollment:
#     print(f"- {course}")

# # Looping over ITEMS (unpacking the key and value simultaneously)
# print("\nLooping over items:")
# for course, count in course_enrollment.items():
#     print(f"- {course} has {count} students.")


# # ==========================================
# # 6. NESTED DICTIONARIES
# # ==========================================
# print("\n--- 6. Nested Dictionaries ---")
# faculty = {
#     "prof_hobbs": {
#         "department": "MSIS",
#         "courses": ["Python", "MIS"],
#         "office": "Room 101"
#     }
# }

# # Chaining brackets to drill down into nested data
# prof_courses = faculty["prof_hobbs"]["courses"]
# print(f"Professor Hobbs' courses: {prof_courses}")


# # ==========================================
# # 7. COMMON ERRORS & PITFALLS
# # ==========================================
# print("\n--- 7. Common Errors ---")

# FAILS: Keys MUST be immutable (strings, integers, tuples). Lists/Dicts are invalid keys.
# invalid_dict = {
#     ["my", "list"]: "Value"  # TypeError: unhashable type: 'list'
# }

# # NOTE: While dictionary keys must be immutable, 
# # the VALUES can be absolutely anything (lists, other dicts, functions, objects).