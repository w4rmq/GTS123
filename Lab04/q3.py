days = input("Input number of days: ")
hours = input("Input number of hours: ")
if not days.isnumeric() or not hours.isnumeric():
    print("Please enter a number")
else:
    days = int(days)
    hours = int(hours)
    print('''Please select a choice:
1-to calculate the total number of seconds or
2-to calculate the total number of minutes: ''')
    choice = input("Enter your selected choice: ")
    print("------------------------------------------------")
    if choice == "1":
        second = days * 24 * 60 * 60 + hours * 60 * 60
        print(f"The total number of seconds are {second}.")
    elif choice == "2":
        minute = days * 24 * 60 + hours * 60
        print(f"The total number of minutes are {minute}.")
    else:
        print("Choose 1 or 2")