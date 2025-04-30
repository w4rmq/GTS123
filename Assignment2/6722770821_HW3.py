words = {}

while True:
    line = input("Enter a line (or 'END' to finish): ").lower().split()
    if len(line) == 1 and line[0] == "end":
        break
    l = [word.rstrip(".,") for word in line]
    for word in l:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

count1 = 0
count2 = 0
count3 = 0
for num in words.values():
    if num <= 2:
        count1 += 1
    elif num <= 4:
        count2 += 1
    else:
        count3 += 1

print("1. Number of words that appear once or twice:", count1)
print("2. Number of words that appear three and four times:", count2)
print("3. Number of words that appear more than four times:", count3)