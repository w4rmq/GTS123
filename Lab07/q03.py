num = int(input("Enter an inter number: "))
row = 1
while row <= num:
    col = 1
    while col <= num:
        if row == 1 or row == num or col == 1 or col == num:
            print("o", end=" ")
        elif col >= row:
            print("x", end=" ")
        else:
            print(" ", end=" ")
        col += 1
    print()
    row += 1
