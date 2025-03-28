l = []
while True:
    word = input("Input: Enter a word: ")
    if word == "exit":
        break
    if word[-1] == "y":
        word = word[:-1] + "ily"
    l.append(word)
print("Output:", l)
    