number = {}
def summary(number):
    print("----SUMMARY----")
    if len(number) > 0:
        for key, value in sorted(number.items(), key=lambda x: int(x[0])):
            print(f"{key}  {value}")
    else:
        print("The list is empty")

while True:
    x = input("Input: ")
    if x == "done":
        summary(number)
        break

    if not x.isnumeric():
        print("ERROR")
    elif 1 <= int(x) <= 1000:
        if x not in number:
            number[x] = 1
        else:
            number[x] += 1
    else:
        print("ERROR")