def clean_text(text):
    lower_text = text.lower()
    clean = ""
    for char in lower_text:
        if char.isalnum():
            clean += char
    return clean

def is_palindrome(text):
    clean = clean_text(text)
    return clean == clean[::-1]

sentence = input("Enter a sentence: ")
print(f"Clean text = {clean_text(sentence)}")
print(f"That is{' ' if is_palindrome(sentence) else ' not '}a palindrome.")