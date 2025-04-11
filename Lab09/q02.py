def LeftRotate(x: list, num):
    l = x[num:] + x[:num]
    return l

def RightRotate(x: list, num):
    l = x[-num:] + x[:-num]
    return l

l = input("Enter 5 inputs: ").split()
num = input("Enter an integer number of rotations (0-4): ")
if num.isnumeric() and 0 <= int(num) <= 4:
    num = int(num)
    left_rotate = LeftRotate(l, num)
    right_rotate = RightRotate(l, num)
    print(f"The left-rotated list: {left_rotate}")
    print(f"The right-rotated list: {right_rotate}")
else:
    print("Error!")
