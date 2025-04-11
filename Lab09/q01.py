import math as m

def CirArea(x):
    area = m.pi * x * x
    return area

def SqArea(x):
    area = x * x
    return area

num = float(input("Input a positive number: "))
if num > 0:
    cir = CirArea(num)
    sq = SqArea(num)

    print(f"The area of the circle is {cir:.2f}")
    print(f"The area of the square is {sq:.2f}")
else:
    print("Wrong Input")