num_customers = int(input("Enter the number of customers: "))

for i in range(num_customers):
    cus_name = input(f"Enter the name of customer {i+1}: ")
    spend = int(input(f"Enter the spending amount for {cus_name}: "))
    discount = 0
    if spend < 500:
        discount = 0
    elif spend < 1000:
        discount = 5
    elif spend < 2000:
        discount = 10
    else:
        discount = 15

    paid = spend * ((100-discount)/100)
    print(f"{cus_name} paid {paid:.2f} Baht")