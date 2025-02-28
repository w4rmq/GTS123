user_input = input("Input: ")
check = True
for i in user_input:
    if not i.isnumeric():
        check = False
    
if check:
    for i in user_input:
        for j in range(1, int(i)+1):
            if j % 2 == 0:
                print("*",end="")
            else:
                print("#",end="")
        print()
else:
    print("Error")