alphabet = "abcdefghijklmnopqrstuvwxyz"
# Get user input
char1 = input("Give me a character: ").lower()
char2 = input("Give me another character: ").lower()

if char1 not in alphabet or char2 not in alphabet:
    print("You need to input two characters")
else:
    if char1 > char2:
        char1, char2 = char2, char1

    output = ""
    for char in alphabet:
        if char1 <= char <= char2:  
            output += char
    
    print(output)