seq = input("Input: ").split()
l = {}

for i in seq:
    if i.isnumeric():
        if i not in l: 
            l[i] = 1
        else:
            l[i] += 1

good = True
for integer, num in l.items():
    if int(integer) != num:
        good = False

if good:
    print(f"Output: good sequence")
else:
    print(f"Output: not good sequence")