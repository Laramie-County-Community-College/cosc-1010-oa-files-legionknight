# filename: 09_Files_Make_Assignment.py
"""
Assignment: Simple Journal

In this assignment, you will create a program that lets a user write journal
entries. Each new entry should be added to the end of a file called `journal.txt`.

Instructions:
1.  Ask the user for their journal entry for the day using `input()`.
2.  Open the file `journal.txt` in **append mode**. This is very important, as
    you don't want to erase previous entries.
3.  Write the user's entry to the file.
4.  Make sure to add a newline character `\n` after the entry so that the next
    entry will start on a new line.
5.  Close the file.
6.  Print a confirmation message to the user, like "Journal entry saved."

Run the program multiple times and enter different entries. Then, open the
`journal.txt` file in a text editor to see if all your entries were saved correctly.
"""

# --- YOUR CODE GOES BELOW ---

# 1. Ask the user for a journal entry
entry = str(input("Please write what you want to add to the journal\n--->   "))
# 2. Open journal.txt in append mode
file = open("journal.txt","a")
# 3. Write the entry to the file (don't forget the newline character!)
file.write(entry)
file.write("\n")
# 5. Close the file
file.close()
# 6. Print a confirmation message
print("Your entry has been added!")
# --- END YOUR CODE ---
