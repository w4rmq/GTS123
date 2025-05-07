def triangle(x):
    for i in range(1, x+1):
        print(f"{' '*(x-i)}" + f"{(str(x)+' ')*i}")

while True:
    x = input("Enter an integer number (0 to exit): ")
    if x == "0":
        print("Exit program. Bye!")
        break

    try:
        x = int(x)
        if 0 <= x <= 9:
            triangle(x)
        else:
            print("Valid value is between 0 and 9!")
            break
    except ValueError:
        print("Invalid input!")
        break