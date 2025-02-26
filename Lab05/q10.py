user_input = input("Input: ")

cnt=0
for i in user_input:
    if i in "X.O":
        cnt += 1
        
if cnt == 9:
    print("-------")
    for i in range(len(user_input)//3):
        print(f"|{user_input[i * 3]}|{user_input[(i * 3)+1]}|{user_input[(i * 3)+2]}|")
        print("-------")
else:
    print("Error")

    