# ==========================================
# 0. THE 'WITH' STATEMENT (Best Practice)
# ==========================================
print("--- 0. The 'with' Statement ---")
# Always use the 'with' block (Context Manager) for file operations.
# It automatically closes the file when the block ends, even if the program crashes.
# Syntax: 
# with open(filename, mode) as variable:
# this replaces:
# variable = open(filename,mode)
# variable.close()

# We will use this syntax for all the following examples.


# ==========================================
# 1. WRITING TO FILES ('w' mode)
# ==========================================
print("\n--- 1. Writing to Files ('w' mode) ---")
# DANGER: 'w' mode will completely OVERWRITE an existing file. 
# If the file doesn't exist, it creates a new one.

# Writing a single string
with open("roster.txt", "w") as f:
    f.write("Line one:\n")
    f.write("Line two\n")
    # f.read() # this would FAIL b/c no read permission
print("Created and wrote to roster.txt")

# Writing multiple lines from a list using .writelines()
new_students = ["2. Emily\n", "3. Victor\n"]
with open("roster.txt", "w") as f:
    # Notice this completely erased Ptolemy from the file!
    f.writelines(new_students)
print("Overwrote roster.txt using .writelines()")


# ==========================================
# 2. APPENDING TO FILES ('a' mode)
# ==========================================
print("\n--- 2. Appending to Files ('a' mode) ---")
# SAFE: 'a' mode adds new data to the very end of the file without erasing it.
# Excellent for logging systems or adding new records.

with open("roster.txt", "a") as f:
    f.write("4. Nathaniel\n")
    # NOTE: You must manually add newline characters (\n)! 
    # Python does not add them automatically.
    f.write("5. Sarah\n")
print("Appended new students to roster.txt")


# ==========================================
# 3. READING FILES ('r' mode)
# ==========================================
print("\n--- 3. Reading Files ('r' mode) ---")
# 'r' is the default mode. If you omit the mode, Python assumes 'r'.

print("Method A: .read() (Loads entire file into one string)")
with open("roster.txt", "r") as f:
    entire_file = f.read()
    print(entire_file)

print("Method B: .readlines() (Loads every line into a List)")
with open("roster.txt", "r") as f:
    lines_list = f.readlines()
    print(f"List format: {lines_list}")

    # make ['2. Emily', '3. Victor', '4. Nathaniel', '5. Sarah']
    clean_lines_list = [line.strip() for line in lines_list]
    print(f"List format: {clean_lines_list}")



# ==========================================
# 4. MEMORY-EFFICIENT READING (For Massive Files)
# ==========================================
print("\n--- 4. Memory-Efficient Reading ---")
# If you have a 5GB CSV file, .read() or .readlines() will crash your computer's RAM.
# Instead, iterate directly over the file object. It yields one line at a time.

print("Iterating directly over the file object:")
with open("roster.txt", "r") as f:
    for line in f:
        # .strip() removes the invisible newline character (\n) from the print output
        print(f"Processing: {line.strip()}")


# ==========================================
# 5. COMMON ERRORS
# ==========================================
# print("\n--- 5. Common Errors ---")

# # FAILS: Trying to write to a file opened in read mode
# with open("roster.txt", "r") as f:
#     f.write("6. John\n") # io.UnsupportedOperation: not writable

# FAILS: Trying to read a file that doesn't exist
# with open("missing_grades.csv", "r") as f:
#     data = f.read()  # FileNotFoundError: [Errno 2] No such file or directory
import io
# PROPER EXCEPTION HANDLING:
# try:
#     with open("roster.txt", "r") as f:
#         f.write("6. John\n") # io.UnsupportedOperation: not writable

#     # with open("missing_grades.csv", "r") as f: # FileNotFoundError
#     #     data = f.read()
# except FileNotFoundError:
#     print("Caught FileNotFoundError: Please verify the file path!")
# except io.UnsupportedOperation:
#     print('Check your permissions!')
# except: # this catches all other kinds of errors
#     print('something went wrong, but the file was found and permissions were okay')