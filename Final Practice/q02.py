info = {}

def summarize(info):
    print("List:")
    if len(info) > 0:
        for key,value in sorted(info.items(),key = lambda x:x[1], reverse = True ):
            print(f"{key}\t{value}")
    else:
        print("empty list!")



while True:
    x = input("Enter student name and score: ")

    if x == "end 0" or x == "end":
        summarize(info)
        break

    name,score = x.split()

    if name not in info:
        if 0 <= int(score) <=100:
            info[name] = int(score)
        else:
            print("Invalid score!")
    elif name in info:
        print("Duplicate name!")