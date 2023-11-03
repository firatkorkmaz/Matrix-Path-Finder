# OPTIONAL: Matrix Data Generator with Random Numbers Between 1 and 9

from random import *

def generate_matrix(row, col, max_value):
    content = ""                # String for the Whole File

    for i in range(0, row):
        line = ""               # String for Each Row

        for j in range(0, col):
            if j != 0:
                line += " "     # Putting Space Between the Numbers
            line += str(randint(1, max_value)).zfill(1)  # zfill(1): 1 >> 1 || 4 >> 4

        content += line + '\n'  # Adding Each Line to the Big Content String

    return content              # Returning the Content of the File


while True:
    row = input("\nRow Number of Matrix: ").strip()
    if not row.isdigit():
        print("Please Enter An Integer!\n")
        continue
    else:
        row = int(row)
        break
        
while True:
    col = input("Column Number of Matrix: ").strip()
    if not col.isdigit():
        print("Please Enter An Integer!\n")
        continue
    else:
        col = int(col)
        break
        
filename = "random_matrix.txt"
max_value = 9                   # Numbers with Up to 1 Digit

with open(filename, 'w') as file:
    content = generate_matrix(row, col, max_value)
    file.write(content)         # Writing the Randomly Generated Matrix to File
    print("\nNew Matrix Data with Random Numbers:")
    print(f"Dim: ({row} x {col}), File: \"random_matrix.txt\"")