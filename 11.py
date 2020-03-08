# In the 20×20 grid below (11-matrix.txt), four numbers along a diagonal line have been marked in red.
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

from typing import List

with open('11-matrix.txt', 'r') as file:
    matrix = [list(map(int, line.split(' '))) for line in file]

maxProduct = 1

for i in range(16):
    for j in range(16):
        horizontal_prod = matrix[i][j] * matrix[i][j+1] * matrix[i][j+2] * matrix[i][j+3]
        vertical_prod = matrix[i][j] * matrix[i+1][j] * matrix[i+2][j] * matrix[i+3][j]
        backslash_prod = matrix[i][j] * matrix[i+1][j+1] * matrix[i+2][j+2] * matrix[i+3][j+3]
        slash_prod = matrix[19-i][j] * matrix[18-i][j+1] * matrix[17-i][j+2] * matrix[16-i][j+3]

        maxProduct = max([maxProduct, vertical_prod, horizontal_prod, backslash_prod, slash_prod])  

print(f"Greatest product of four adjacent matrix numbers: {maxProduct}")
