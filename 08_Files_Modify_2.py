# filename: 08_Files_Modify_2.py
"""
Activity: Modify the Code

This program asks for a filename and tries to read it. If you type a filename
that doesn't exist (e.g., "nonexistent_file.txt"), the program will crash.

Your goal:
1.  Wrap the file operations in a `try...except` block.
2.  Specifically, you should catch the `FileNotFoundError`.
3.  If the file is not found, print a friendly error message like
    "Error: That file could not be found." instead of crashing.
"""

filename = input("Enter the filename to read: ")

# --- MODIFY THE CODE BELOW ---
# Add a try...except block to handle a FileNotFoundError
try:
    file = open(filename, "r")
    content = file.read()
    file.close()
except:
    print("Error: that file couldn't be found")
print("\n--- File Content ---")
print(content) #python also gives a traceback for this
print("--------------------")

# --- END MODIFICATION ---
