print("Fever Symptoms Advisor Program")

temp = float(input("Check your body temperature in F = "))

if temp < 100.4:
    print("You are fine")
else:
    print("You got a fever.")

    treatment = input("Choose your treatment: 1 = medication 2 = no medication ")
    if treatment == "1":
        print("Take Tylenol every 4 hours as needed")
    elif treatment == "2":
        print("Taking bath in lukewarm water or get cool packs")
    else:
        print("You choose the wrong choice")
