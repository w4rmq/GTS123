user_input = input("Input: ").upper()

vowels = "AEIOU"
check_vowels = True
for i in user_input:
    if i not in vowels:
        check_vowels = False
        
if check_vowels == False:
    print('Invalid input, valid characters: ["A", "E", "I", "O", "U"]')
elif len(user_input) != 3:
    print("Only three characters are allowed.")
else:
    for i in user_input:
        output = ""
        output += i
        output1 = ""
        for j in user_input:
            if i != j:
                output1 += j
        print(output + output1)
        print(output + output1[::-1])
        
