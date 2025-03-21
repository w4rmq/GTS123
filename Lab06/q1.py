l = input("Enter a comma-separated list: ").split(",")
for i in l:
    for j in l:
        for k in l:
            if i != j and i != k and j != k:

                print(f"{i} {j} {k}")
    