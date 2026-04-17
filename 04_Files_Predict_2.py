# filename: 04_Files_Predict_2.py
"""
Activity: Predict the Output

1.  Imagine a file named `shopping.txt` with the following content:
    Milk
    Bread
    Eggs

2.  Read the Python code below.
3.  Without running the code, predict what the `print(lines)` statement will output.
    Pay close attention to the details, including special characters!
"""

prediction = "" # ["Milk", "Bread", "Eggs"]

# This code assumes "shopping.txt" exists with the content described above.
file = open("shopping.txt", "r")

lines = file.readlines()

file.close()

print(lines)
