# Traversing Matrices Downwards and Rightwards to Find the Maximum Sum of Visited Values #

import sys

def MaxPathSum(matrix):
    n = len(matrix)         # Number of Rows
    m = len(matrix[0])      # Number of Columns

    summary = [[[] for i in range(m + 1)] for j in range(n + 1)]    # (n+1) x (m+1) Empty-List Matrix

    # Finding the Path of Maximum Sum
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if sum(summary[i - 1][j]) >= sum(summary[i][j - 1]):
                summary[i][j] = summary[i - 1][j].copy()
            else:
                summary[i][j] = summary[i][j - 1].copy()
            summary[i][j].append(matrix[i - 1][j - 1])
            
    '''
    Example Matrix: m, (2 x 2) -> Zero Matrix: sum, (3 x 3)
    m:|1  2| sum:|0  0  0| sum:|0       0       0  |
      |3  1|     |0  0  0|     |0       1      1+2 | -> sum[1][1]=max(0,0)+m[0][0]; sum[1][2]=max(0,1)+m[0][1]
                 |0  0  0|     |0      1+3    1+3+1| -> sum[2][1]=max(1,0)+m[1][0]; sum[2][2]=max(1+2,1+3)+m[1][1]
    
    maxSum = sum[-1][-1] = sum[2][2] = 1+3+1 = 5
    ''';
    return summary[n][m]


def main(filename=None):
    if filename == None:
        filename = input("\nFilename of the Matrix Data: ").strip()

    try:
        f_lines = open(filename, "r")
    except:
        print(f"\n{filename} File does Not Exist!")
        return

    matrix = []
    temp = []

    # Getting Matrix Values to Print
    for line in f_lines:
        num_line = line.replace("\n", "").split(" ")
        for num in num_line:
            if num != "":
                temp.append(int(num))
        matrix.append(temp.copy())
        temp.clear()

    # Printing Matrix Values
    print("\nMatrix:")
    for numbers in matrix:
        for num in numbers:
            print(num, end="  ")
        print()
    print()

    # Calculating and Printing the Maximum Sum of Visited Values
    max_sum = MaxPathSum(matrix)
    print(f"The Path of Maximum Sum from (0,0) to ({len(matrix) - 1},{len(matrix[0]) - 1})")
    print(f"by Only Traversing Downwards & Rightwards:\n")
    print(f"{max_sum} -> {sum(max_sum)}")


if __name__ == '__main__':
    # filename="matrix1.txt"
    # main(filename)
    if len(sys.argv) == 1:
        main()
    else:
        main(sys.argv[1])