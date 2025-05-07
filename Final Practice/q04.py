player = {}

def summarize(player):
    if len(player) > 0:
        total = 0
        for i in player.values():
            total += i
        average = total/len(player)
        for key,value in sorted(player.items(),key = lambda x:x[1], reverse = True ):
            if value == max(player.values()):
                print(f"{key}\t{value}\tGold")
            elif value > average:
                print(f"{key}\t{value}\tSilver")
            else:
                print(f"{key}\t{value}")
    else:
        print("No players")

while True:
    x = input("Input: ")
    if x == "done":
        summarize(player)
        break

    name, score = x.split()
    
    if name in player:
        print("Duplicated player")
    else:
        if not score.isnumeric():
            print("Invalid input")
        elif int(score) < 0:
            print("Invalid input")
        else:
            player[name] = int(score)