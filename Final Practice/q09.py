animal = {}

def summary(animal):
    if len(animal) > 0:
        print("###Summary###")
        for key, value in animal.items():
            print(f"Total Number of {key} : {value}")
    else:
        print("Empty List")
        print("###Summary###")

while True:
    x = input("Input: ")
    if x == "done":
        summary(animal)
        break

    name, amount = x.split()

    if name not in animal:
        animal[name] = int(amount)
    else:
        animal[name] += int(amount)