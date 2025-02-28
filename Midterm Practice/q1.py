import math

pace_min, pace_sec = input("Enter your running pace (minutes per kilometer): ").split(":")
pace_min, pace_sec = float(pace_min), float(pace_sec)
distance = input("Enter your distance (a) Mini-marathon, (b) Half-marathon, (c) Full-marathon: ").lower()

pace_time_min = pace_min + pace_sec/60
check = True

dis = 0
cutoff = 0
if distance == "a":
    dis = 10
    cutoff = 2.5
elif distance == "b":
    dis = 21.0975
    cutoff = 4.0
elif distance == "c":
    dis = 42.195
    cutoff = 6.0
else:
    print("Invalid distance selection")
    check = False

if check == True:
    finish_time = pace_time_min * dis
    finish = "can" if finish_time <= (cutoff * 60) else "cannot"
    print(f"Your estimated finish time is {(finish_time//60):.0f} hours {math.floor(finish_time%60)} minutes")
    print(f"You {finish} finish in cutoff time (Your cutoff time is {cutoff:.2f} hours).")