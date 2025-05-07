l = []
def display(l):
    print("-------")
    for i in range(3):
        print(f"|{l[i*3]}|{l[(i*3)+1]}|{l[(i*3)+2]}|")
        print("-------")

while True:
    user_input = input("Input: ")
    if user_input not in ["x", "o"]:
        print("Wrong input")
        break
    l.append(user_input)

    if len(l) == 9:
        display(l)
        break




