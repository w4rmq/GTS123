price = float(input("Enter the price of the product: "))
items = int(input("Enter the number of items: "))
have_code = input("Do you have a promotion code (y/n)? ").lower()
discount = 0
if have_code == "y":
    code = input("Enter your promotion code: ").lower()
    if code == "supersale1010":
        discount = 30
    elif code == "mega1010":
        discount = 20
    elif code == "loveshopping":
        discount = 10
    else:
        print("----------------------------")
        print("Your promotion code is invalid.")
    
print("----------------------------")
total = price*items
print(f"Total amount: {total:.2f} baht")

if discount:
    print(f"Amount after Discount: {total*(1-discount/100):.2f} baht")