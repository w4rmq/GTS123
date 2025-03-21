l = []
for i in range(5):
    num = int(input(f"Input#{i+1} : "))
    l.append(num)

opt = input("Select the option: 1) Summary, 2) average, 3) min, 4) max ....")
if opt == "1":
    result = sum(l)
elif opt == "2":
    result = sum(l) / len(l)
elif opt == "3":
    result = min(l)
elif opt == "4":
    result = max(l)

print(f"Your result is {result}")