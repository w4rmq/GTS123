namelist = ["Satawat", "Pisit", "Thanaphong", "Pished", "Nut", "Amon"]

for i in range(len(namelist)):
    print(f"Student list: {namelist}")
    name = input("Please enter a student's name that you want to delete (q = exit): ")
    if name == "q":
        break
    print(f"You will remove ' {name} ' from this class.")
    confirm = input("Please type (Confirm 'y', Cancel 'n'): ")
    if confirm == "y":
        namelist.remove(name)