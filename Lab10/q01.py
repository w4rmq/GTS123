import numpy as np

size = int(input("Input size of matrix: "))
matrix = []
for i in range(size):
    row = []
    for j in range(size):
        element = int(input(f"Input element at row {i + 1} column {j + 1}: "))
        row.append(element)
    matrix.append(row)

matrix = np.array(matrix)
print("Output:")
print("Matrix =\n", matrix)

det = np.linalg.det(matrix)
print("Determinant =", det)
if det != 0:
    inv = np.linalg.inv(matrix)
    print("Inverse matrix =\n", matrix)