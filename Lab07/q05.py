l = []
a = 1
while True:
    num = int(input("Enter an integer number: "))
    if 1 <= num <= 10:
        row = 1
        while row <= (num*2)-1:
            if row <= num:
                l.append(str(a))
                print(" ".join(l))
                a += 1
            else:
                l.pop(-1)
                print(" ".join(l))
            row += 1
        break
    else:
        print("1 - 10 !!!!")
