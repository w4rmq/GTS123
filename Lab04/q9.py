time = int(input("Input parking time (in minutes): "))

hour = time // 60
if time % 60 > 15:
    hour += 1
charge = hour * 20

print(f"The charge is {charge} baht.")

