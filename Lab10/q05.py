import numpy as np
import math

def d(i, j):
    distance = math.sqrt((i[0]-j[0])**2 + (i[1]-j[1])**2 + (i[2]-j[2])**2)
    return distance

p1 = input("Input coordinate fo P1: ").split()
p2 = input("Input coordinate fo P2: ").split()
p3 = input("Input coordinate fo P3: ").split()

p1 = np.array([int(i) for i in p1])
p2 = np.array([int(i) for i in p2])
p3 = np.array([int(i) for i in p3])

d12 = d(p1, p2)
d13 = d(p1, p3)
d23 = d(p2, p3)

longest_distance = max(d12, d13, d23)
print("Output:")
print(f"the longest distance = {longest_distance:.2f}")