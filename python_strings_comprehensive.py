# This is a comment in python.
# The hash symbol (#) at the front tells the python
# interpreter to ignore it.

'''
Triple quotes can make a multi-line 
comment.

Sometime's that's what people want.
'''





# python_strings_comprehensive.py
# A complete lecture script covering Python string operations and built-in methods.

# ==========================================
# 0. BASIC & MULTILINE STRINGS
# ==========================================
# print("--- 0. Basic & Multiline Strings ---")

# # single quote strings allow for easy inclusion of "" in the string
# course = 'python "programming"' # avoid's "python \"programming\""

# # double quote strings allow for easy inclusion of ' in the string
# course = "Python Programming's awesome" # avoids 'Python Programming\'s awesome'

# # Multiline strings (docstrings) preserve exact formatting and line breaks
# # as well as avoiding escape characters for ' and "
# syllabus = """Week 1: Intro
# Week 2: Data Types
# Week 3: Strings's are "great" """
# print(syllabus)


# ==========================================
# 1. F-STRINGS & FORMATTING
# F-Strings are useful when you want a variable's value to be part of the string.
# ==========================================
# print("\n--- 1. F-Strings & Formatting ---")
# instructor = "Nathaniel"
# students = 45

# # this is called "hard coding" and is to be avoided when you want to *re-use* code in different ways
# print("Professor Nathaniel is teaching 45 students.")
# # without an f-string
# print("Professor " + instructor + ' is teaching ' + str(students) + ' students.')
# # Standard f-string
# print(f"Professor {instructor} is teaching {students} students.")

# # F-strings can handle inline math and specific formatting (e.g., decimal places, percentages)
# pass_rate = 0.9567
# print(f"Expected pass rate: {pass_rate:.2}")  # Keeps 2 decimal points
# print(f"Expected pass rate: {pass_rate:.1%}")  # Keeps 1 decimal point and formats as % (*100)
# print(f"Double the students: {students * 2}")

# # This prints the value of the variable only:
# print(f'{students}')

# # This will print the name of the variable AND the value (note the =)
# print(f'{students=}')

# # ==========================================
# WARNING about mixing types that support + operator
# # ==========================================

# integers can be added
# print(55 + 10)

# # strings can be concatenated
# print('55' + '10')

# but you can not mix types with the + operator
# print(55 + '10') # one kind of error
# print('55' + 10) # another kind of error


# ==========================================
# 2. ESCAPE CHARACTERS
# ==========================================
# print("\n--- 2. Escape Characters ---")
# print("These start with a backslash \\")
# # \n for newline, \t for tab, \' or \" to bypass quote termination, \\ for backslash itself
# escaped_str = "First line.\n\tIndented second line.\nhere's a backslash \\ .\nShe said, \"Python is fun!\""
# print(escaped_str)

# # # Raw strings (prefix 'r') ignore escape characters - excellent for regex or file paths
# raw_str = r"C:\new_folder\test.txt"
# print(f"Raw string: {raw_str}")


# ==========================================
# 3. INDEXING & IMMUTABILITY
# ==========================================
# print("\n--- 3. Indexing & Immutability ---")
# word = "Rutgers"
# # R  u  t  g  e  r  s
# # 0  1  2  3  4  5  6
# #-7 -6 -5 -4 -3 -2 -1

# print(f"First letter: {word[0]}")
# print(f"Last letter (negative indexing): {word[-1]}")

# # # some examples without the f string
# # # THE len() FUNCTION
# print('the length of a string can be found with the len function, e.g. ' + str(len(word)))

# # # why the negative indexing is useful (it's annoying to work with the end otherwise)
# print("Last Letter (positive indexing): " + word[len(word)-1])

# FAILS: Accessing an index that doesn't exist
# print("Last Letter (positive indexing): " + word[len(word)]) # IndexError: string index out of range

# FAILS: Strings are IMMUTABLE. You cannot change a string in place.
# word[0] = "r"  # TypeError: 'str' object does not support item assignment




# ==========================================
# 4. SLICING [start:stop:step]
# NOTE: start has default 0, stop has default len(...)-1, step has default 1
# NOTE: start is INCLUSIVE, stop is EXCLUSIVE
# ==========================================
# print("\n--- 4. Slicing ---")
# alphabet = "abcdefg"

# print(f"First three letters: {alphabet[0:3]}")  # include 0, and everything up to, but NOT including index 3
# print(f"Starting from index 3 and all the way to the end: {alphabet[3:]}") # len(alphabet) is the default, you can omit it
# print(f"Every second letter (step): {alphabet[::2]}")
# # NOTE: below is the same as above (which is the usual way to write it), but making things explicit
# print(f"Every second letter (step): {alphabet[0:len(alphabet):2]}")
# print(f"Reversed string: {alphabet[::-1]}")     # Classic interview trick


# # ==========================================
# # 5. OPERATORS & MEMBERSHIP
# # ==========================================
# print("\n--- 5. Operators & Membership ---")
# str1 = "Business"
# str2 = "Analytics"

# # Concatenation (+) and Repetition (*)
# print(f"Concatenated: {str1 + ' ' + str2}")
# print(f"Repetition: {'Echo! ' * 3}") # concatenate the string to itself 3 times

# # Membership operator (in / not in) - returns a boolean
# NOTE: you can ignore this for a few weeks but I'll leave here for later review
# print(f"Is 'Bus' in str1?: {'Bus' in str1}")
# print(f"Is 'Math' not in str2?: {'Math' not in str2}")

# # FAILS: Subtracting strings or adding to integers
# # print(str1 - str2)  # TypeError: unsupported operand type(s) for -
# # print(str1 + 5)     # TypeError: can only concatenate str (not "int") to str


# # ==========================================
# # 6. BUILT-IN METHODS: CASE & SPACING
# # ==========================================
# print("\n--- 6. Methods: Case & Spacing ---")
# dirty_string = "   data analytics   "

# # Stripping whitespace
# print(f"Original: '{dirty_string}'")
# print(f"Strip: '{dirty_string.strip()}'")     # Removes leading/trailing spaces
# print(f"RStrip: '{dirty_string.rstrip()}'")   # Removes trailing only

# # Case formatting (returns a NEW string)
# clean_string = dirty_string.strip()
# print(f"Upper: {clean_string.upper()}")
# print(f"Title: {clean_string.title()}")
# print(f"Capitalize: {clean_string.capitalize()}") # Only first letter of string

# NOTE: Methods don't change the original variable unless reassigned
# clean_string.upper()
# print(clean_string) # Still lowercase! Must do: clean_string = clean_string.upper()


# # ==========================================
# # 7. BUILT-IN METHODS: SEARCH & REPLACE
# # ==========================================
# print("\n--- 7. Methods: Search & Replace ---")
# sentence = "Python is hard, but Python is powerful."

# # Replace (replaces ALL occurrences by default)
# print(f"Replace: {sentence.replace('hard', 'fun')}")

# # Count
# print(f"Count of 'Python': {sentence.count('Python')}")

# # Find (returns the starting index of the first match, or -1 if not found)
# print(f"Find 'powerful': {sentence.find('powerful')}")
# print(f"Find 'Java': {sentence.find('Java')}") # Returns -1, no error

# # FAILS: .index() is like .find(), but it throws an error if missing
# # print(sentence.index('Java')) # ValueError: substring not found


# # ==========================================
# # 8. BUILT-IN METHODS: BOOLEAN EVALUATION
# # ==========================================
# print("\n--- 8. Methods: Boolean Evaluation ---")
# # Checking prefixes and suffixes
# print(f"Starts with 'Python': {sentence.startswith('Python')}")
# print(f"Ends with 'weak.': {sentence.endswith('weak.')}")

# # Checking character composition
# print(f"Is '12345' all digits?: {'12345'.isdigit()}")
# print(f"Is 'Python3' all letters?: {'Python3'.isalpha()}") # False because of '3'


# ==========================================
# 9. STRINGS <--> LISTS
# ==========================================
print("\n--- 9. Strings to Lists & Lists to Strings ---")
csv_data = "apple,banana,cherry"

# .split() divides a string based on a delimiter into a list
fruit_list = csv_data.split(",")
print(f"Split by comma: {fruit_list}")



# # list() casts a string into a list of individual characters
print(f"Characters list: {list('apple')}")

# # .join() combines a list of strings using a string as the "glue"
sentence_words = ["Python", "is", "great"]
print(f"Joined with spaces: {' '.join(sentence_words)}")
print(f"Joined with dashes: {'-----'.join(sentence_words)}")


# # FAILS: .join() expects ONLY strings in the list
# # mixed_list = ["Number", 1]
# # "".join(mixed_list)  # TypeError: sequence item 1: expected str instance, int found


# # a look ahead: conditionals and loops
# # ==========================================
# # 10. ITERATING THROUGH STRINGS
# # ==========================================
# print("\n--- 10. Iteration ---")
# # Since strings are sequences, we can loop through them like lists
# vowel_count = 0
# for char in "education":
#     if char.lower() in "aeiou":
#         vowel_count += 1
# print(f"Found {vowel_count} vowels in 'education'.")
