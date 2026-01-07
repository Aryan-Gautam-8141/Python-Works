def encrypt(text,shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt (text, shift):
    return encrypt(text, -shift)

plain_text = input("Enter text to encrypt: ")
shift_value = int(input("Enter value: "))

encrypted_text = encrypt(plain_text, shift_value)
decrypted_text = decrypt(encrypted_text, shift_value)

print("\n ---RESULT---")
print("Plain Text: ", plain_text)
print("Shift Value: ",shift_value)
print("Encrypted Text: ",encrypted_text)
print("Decrypted Text: ",decrypted_text)