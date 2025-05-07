def command(command_type, amount):
    global points

    if command_type == "P":
        earn = amount//50
        points += earn
        print(f"You earned {earn} points")
        print(f"Your accumulated points = {points} points")
    else:
        if amount > points:
            print("Not enough points")
        else:
            points -= amount
            print(f"You redeemed {amount} points")
            print(f"Your accumulated points = {points} points")
        

points = 100

while True:
    x = input("Command: ")
    if x == "done 0":
        break

    command_type, amount = x.split()

    if command_type not in "PR" or not amount.isnumeric():
        print("Invalid command")
    elif int(amount) < 0:
        print("Invalid command")
    else:
        command(command_type, int(amount))