sentence = input("Input: ").split()
count = {}
for word in sentence:
    word = word.lower()
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print("Output: ")
for word in count:
    if count[word] == max(count.values()):
        print(f"{word} = {count[word]}")