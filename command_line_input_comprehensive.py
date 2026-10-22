# cli_arguments.py
# A script covering command line inputs using sys.argv and argparse.
# NOTE: Run this script from the terminal to demonstrate properly:
# e.g., python command_line_input_comprehensive.py input.csv --rows 50 --verbose

import sys
import argparse

# ==========================================
# 0. SYS.ARGV (The Quick & Dirty Way)
# ==========================================
print("--- 0. Using sys.argv ---")
# sys.argv is just a simple list of strings passed to the script.
# Index 0 is ALWAYS the name of the script itself.

print(f"All arguments: {sys.argv}")
print(f"Script name: {sys.argv[0]}")

# FAILS: If the user doesn't provide enough arguments, accessing index 1 crashes.
# Try running just `python command_line_input_comprehensive.py` in the terminal to see this fail.
input_file = sys.argv[1] # IndexError: list index out of range

# FAILS: sys.argv ALWAYS imports everything as a string. You must manually cast.
# limit = sys.argv[2] 
# print(limit + 5) # TypeError: can only concatenate str (not "int") to str


# ==========================================
# 1. ARGPARSE: THE BASICS & POSITIONAL ARGS
# ==========================================
# print("\n--- 1. argparse: Positional Arguments ---")
# # argparse is the Pythonic standard for building robust command-line interfaces.
# # It automatically generates help messages and handles type casting.

# # Step 1: Create the parser object
# parser = argparse.ArgumentParser(description="A script to process business data.")

# # Step 2: Add a positional argument (Mandatory, order matters)
# # If the user doesn't provide this, argparse automatically halts and shows an error.
# parser.add_argument("filename", help="The CSV file you want to process.")

# # (We will parse the arguments below in Section 4)


# # ==========================================
# # 2. ARGPARSE: OPTIONAL ARGUMENTS (FLAGS)
# # ==========================================
# print("\n--- 2. argparse: Optional Arguments ---")
# # Optional arguments start with '--' (long form) or '-' (short form).
# # They are not strictly required unless you specify required=True.

# # A standard optional argument requiring a value (e.g., --rows 100)
# parser.add_argument("-r", "--rows", help="Number of rows to process.")

# # A boolean flag: store_true means if the flag is present, it's True. If absent, False.
# # (e.g., running `python script.py --verbose` sets it to True)
# parser.add_argument("-v", "--verbose", action="store_true", 
#                     help="Enable detailed logging output.")


# # ==========================================
# # 3. ARGPARSE: TYPE CASTING, DEFAULTS & CHOICES
# # ==========================================
# print("\n--- 3. argparse: Types and Defaults ---")

# # Type casting: argparse can automatically convert inputs (e.g., to integers or floats)
# # Default: If the user doesn't provide the flag, use this value.
# parser.add_argument("--timeout", type=int, default=30, 
#                     help="Timeout in seconds (default: 30)")

# # Choices: Restrict the user to a specific list of valid inputs
# parser.add_argument("--mode", choices=["fast", "safe"], default="safe",
#                     help="Execution mode (fast or safe)")


# # ==========================================
# # 4. EXECUTING THE PARSER
# # ==========================================
# print("\n--- 4. Executing & Using the Arguments ---")
# # LECTURE NOTE: In a real script, this usually goes inside your main block.
# # We parse the arguments into an object (usually called 'args').

# # WARNING FOR IDEs: If you run this file directly in an IDE without setting up 
# # run configurations, argparse will crash here because it expects terminal arguments.
# # For lecture purposes, you might want to mock the arguments like this:
# # args = parser.parse_args(["data.csv", "--rows", "50", "--verbose"])

# try:
#     args = parser.parse_args()
    
#     # Access arguments using dot notation matching the argument names
#     print(f"Target File: {args.filename}")
#     print(f"Rows requested: {args.rows}")
#     print(f"Verbose mode: {args.verbose}")
#     print(f"Timeout (int): {args.timeout}")
#     print(f"Mode selected: {args.mode}")

# except SystemExit:
#     print("\n[Argparse caught an error or a help request (--help) and exited safely.]")

# # DEMO: run: `python cli_arguments.py -h` or `--help`
# # See how argparse automatically builds a beautiful instruction manual!