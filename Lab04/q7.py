money = float(input("Enter money you have: "))
price = float(input("Enter price of item: "))
tax = price * 0.08
print(f"Tax: {tax}")
total = price + tax
print(f"Total price: {total}")

if money >= total:
    print("yes you have enough money to buy")
else:
    print(f"You have shortfall of {total - money}, you cannot buy.")