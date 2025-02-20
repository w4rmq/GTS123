print("""Welcome to pizza online ordering.
please input 'y' if you want to order, otherwise input 'n'
""")

pizza = input("pizza? (price_359): ")
chicken = input("chicken? (price_3 pieces for 199): ")
pasta = input("pasta? (price_99): ")
salad = input("salad? (price_99): ")
coke = input("coke? (price_550 ml for 25): ")

price = 0
if pizza == "y":
    price += 359
if chicken == "y":
    price += 199
if pasta == "y":
    price += 99
if salad == "y":
    price += 99
if coke == "y":
    price += 25

print(f"""total price is {price}
thanks""")