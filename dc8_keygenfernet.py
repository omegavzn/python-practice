# Encrpytion Practice: Symmetric Key Encryption
# Generating a key using AES algorythm Fernet

# Import cryptography & fernet
from cryptography.fernet import Fernet

key = Fernet.generate_key() # Generate key usuing fernet
# print(key)

# Store the key securely - needed to dcrypt
# Encrypt key using Fernet
f = Fernet(key)
message = b"These are all of my secrets"
encrypted = f.encrypt(message)
# print(encrypted)

# I can now decrypt the data using key
dcrpyt = f.decrypt(encrypted)
print(dcrpyt)
 