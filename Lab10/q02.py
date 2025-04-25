import numpy as np

A = []
b = []
count = 1
for i in range(3):
    row = []
    for j in range(3):
        element = int(input(f"Input C{count}: "))
        row.append(element)
        count += 1
    A.append(row)
    element = int(input(f"Input C{count}: "))
    b.append(element)
    count += 1
A = np.array(A)
b = np.array(b)

try:
    A_inv = np.linalg.inv(A)
    v = np.matmul(A_inv, b)
    print(f"Solution: \nx = {v[0]:.2f} \ny = {v[1]:.2f} \nz = {v[2]:.2f}")
except np.linalg.LinAlgError:
    print("Unable to find a solution")