num = int(input("Enter an integer number (n>0): "))
if num <= 0:
    print("N/A Operations")
else:
    print("(1) Factorial of n (n!)")
    print("(2) Summation of n integers")
    op = input("Select operation: ")
    if op == "1":
        fac = 1
        for i in range(num):
            fac *= (i + 1)

        print(f"Factorial of n (n!) = {fac}")
    elif op == "2":
        sum = 0
        for i in range(num):
            sum += i + 1
        print(f"Summation of n intergers = {sum}")
    else:
        print("N/A Operation!")