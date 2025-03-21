num = int(input("how many persons in a group? : "))

a = []
print("please enter grade from group A")
for i in range(num):
    grade = float(input("enter grade: "))
    a.append(grade)
print()

b = []
print("please enter grade from group B")
for i in range(num):
    grade = float(input("enter grade: "))
    b.append(grade)
print()

c = []
print("please enter grade from group C")
for i in range(num):
    grade = float(input("enter grade: "))
    c.append(grade)
print()

tmp = ["A", "B", "C"]
l = [a, b, c]
for i, group in enumerate(l):
    print(f"the highest grade of group {tmp[i]} is {max(group)}")