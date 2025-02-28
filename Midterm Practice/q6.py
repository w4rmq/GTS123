cleartext = input("cleartext=")
k = int(input("k="))

ciphertext = ""
for i in cleartext:
    ciphertext += chr((ord(i)+k)%256)
print(f"ciphertext= {ciphertext}") 