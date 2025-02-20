print("========Welcome to Hi!! Car Wash========")
service = input("Choose your services: W=Wash C=Wash+Vacuum ")
price = 0
if service != "W" and service != "C":
    print("Please Choose Your Services")
else:
    size = input('Enter your car size: "S", "M", "L": ')
    
    if size != "S" and size != "M" and size != "L":
        print("You Enter the wrong car size")
    else:
        if service == "W":
            if size == "S":
                price = 100
            elif size == "M":
                price = 120
            else:
                price = 140
        else:
            if size =="S":
                price = 120
            elif size == "M":
                price = 140
            else:
                price = 160
        print(f"Price = {price}")

