height = int(input("Height: "))
if height < 1:
    print("Error")
else:
    count = 1
    for i in range(height,0,-1):
        print(f"{"#" * (i-1)}{"." * count}{"#" * (i-1)}")
        count += 2
