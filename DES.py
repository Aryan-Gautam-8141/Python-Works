from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
# install pycryptodome
# DES requires 8-byte key
key = get_random_bytes(8)
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b"ABCDEFGH"  # must be multiple of 8 bytes

print("Plain text is :",plaintext)

ciphertext = cipher.encrypt(plaintext)
print("DES Encrypted:", ciphertext)

decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("DES Decrypted:", decrypted)
