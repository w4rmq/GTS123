lines = int(input("enter no. of lines: "))
for i in range(lines+1):
    if i % 2 != 0:
        print("-" * i)
    else:
        print("*" * i)