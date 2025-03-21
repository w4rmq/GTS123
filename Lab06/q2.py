l = input("Enter a comma-separated list: ").split(",")
if len(l) >= 3:
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            for k in range(j+1, len(l)):
                    
                print(f"{l[i]} {l[j]} {l[k]}")