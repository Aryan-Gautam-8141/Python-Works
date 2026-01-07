key="qwertyuiopasdfghjklzxcvbnm"
letters="abcdefghijklmnopqrstuvwxyz"

text=input("Enter Text : ").lower()
result=""

for char in text:
    if char in letters:
        index=letters.index(char)
        result+=key[index]
    else:
        result+=char

print("Encrypted Text : ",result)

decrypted=""
for char in result:
    if char in key:
        index=key.index(char)
        decrypted+=letters[index]
    else:
        decrypted+=char

print("Decrypted Text : ",decrypted)