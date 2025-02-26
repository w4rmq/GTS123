print("Multiplication table:")
num = int(input("Please enter a number between 1 to 25: "))
if 1 <= num <= 25:
    print("Multiplication table of {num}")
    for i in range(12):
        print(f"{num} x {i+1} = {num * (i+1)}")
else:
    print("You entered invalid number")