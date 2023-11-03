# Matrix Path Finder with Maximum Sum
A program written in Python to traverse any given input matrix downwards and rightwards from the first element to the last element and find the path with maximum sum.

## General Information
This program requires any M x N matrix data from an input text file and reads it, then traverses this matrix from the first element (0, 0) to the last element (M, N) only downwards and rightwards and finds the path with maximum sum of the visited values.

## Setup & Run
There are 2 different files to run the program in different ways:
1. **Matrix_Max_Path.ipynb** can be run with Jupyter Notebook:
```
pip install jupyter
```
```
jupyter notebook
```
2. **Matrix_Max_Path.py** can be run with Python and input filenames can be given as either command line arguments or input strings at runtime:
```
python Matrix_Max_Path.py matrix1.txt
```
```
python Matrix_Max_Path.py -> (Filename of the Matrix Data: matrix2.txt_)
```
* There are 3 different input matrix samples given as text files: **matrix1.txt**, **matrix2.txt** and **matrix3.txt**
* There is also a random matrix data generator file **Generate_Matrix.py** which generates a new matrix with the given row and column numbers as inputs at runtime and saves the new matrix in **random_matrix.txt** file to test the program with it.
```
python Matrix_Max_Path.py random_matrix.txt
```