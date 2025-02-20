letter = input("Enter a single letter: ")

if not letter in "ABCDEFGHIJKLMNPPRSTUVWXY":
    print(f"There is no digit on the telephone that corresponds to {letter}.")
else:
    num = 0
    if letter in "ABC":
        num = 2
    elif letter in "DEF":
        num = 3
    elif letter in "GHI":
        num = 4
    elif letter in "JKL":
        num = 5
    elif letter in "MNO":
        num = 6
    elif letter in "PRS":
        num = 7
    elif letter in "TUV":
        num = 8
    elif letter in "WXY":
        num = 9

    print(f"The digit {num} corresponds to the letter {letter} on the telephone.")