print('''Welcome to Income Tax Computation Program
''')
income = float(input("Please enter your income (THB): "))
if income < 0:
    print("You are in debt!")
else:
    tax = 0
    if income <= 15000:
        tax = income * 0
    elif income <= 50000:
        tax = 15000 * 0 + (income - 15000) * 0.05
    elif income <= 100000:
        tax = 15000 * 0 + 35000 * 0.05 + (income - 50000) * 0.075
    else:
        tax = 15000 * 0 + 35000 * 0.05 + 50000 * 0.075 + (income - 100000) * 0.1
    
    print(f"Tax expense = {tax}")

    net = income - tax
    print(f"Your net income after tax = {net}")
