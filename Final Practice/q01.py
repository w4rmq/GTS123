balance = int(input("Enter the initial balance: "))
def invalid():
    print("Invalid transaction!")

def transaction(tran_type,amount):
    global balance

    if tran_type == "D":
        balance += amount
        print(f"Deposit = {amount} THB, current balance = {balance} THB.")
    elif tran_type == "W":
        if amount > balance:
            invalid()
        else:
            balance -= amount
            print(f"Withdrawal = {amount} THB, current balance = {balance} THB.")
        

while True:
    x = input('Transaction type and amount ("done 0" to exit): ')

    if x == "done 0":
        print(f"Current balance = {balance}")
        break

    tran_type, amount = x.split()

    if tran_type not in "DW":
        invalid()
    elif int(amount) < 0:
        invalid()
    else:
        transaction(tran_type,int(amount))