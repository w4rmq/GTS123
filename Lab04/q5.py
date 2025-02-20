amount = input("Please specify amount of money you would like to withdraw: ")
if not amount.isnumeric():
    print("Please enter a number")
else:
    amount = int(amount)
    if amount / 500 >= 1:
        bill = amount // 500
        amount %= 500
        print(f"{bill} bill (s) of 500 baht")
    if amount / 100 >= 1:
        bill = amount // 100
        amount %= 100
        print(f"{bill} bill (s) of 100 baht")
    if amount / 50 >= 1:
        bill = amount // 50
        amount %= 50
        print(f"{bill} bill (s) of 50 baht")
    if amount / 2 >= 1:
        coin = amount // 2
        amount %= 2
        print(f"{coin} coin (s) of 2 baht")
    if amount:
        print(f"{amount} amount (s) of 1 baht")


    
    # b500, rmd1 = amount//500, amount%500
    # b100, rmd2 = rmd1//100,rmd1%100
    # b50, rmd3 = rmd2//50,rmd2%50
    # c2,c1 = rmd3//2, rmd3%2

