# Asymetric Key Encryption Project
# Create a public key to encrypt and private key to decrypt 
# Using Cryptography Library's RSA Algorithm

from email import message
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

# Generate private key
private_key = rsa.generate_private_key(public_exponent=65537,
                                       key_size=4096,
                                       backend=default_backend())
# print(private_key)

# Generate public key
public_key = private_key.public_key()
# print(public_key)

# Now you can use the public key to encrypt 
message = b'All of your secrets go here'

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
    
encrypted = public_key.encrypt(message,
                               padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                            algorithm=hashes.SHA256(),
                                            label=None))
print(encrypted)

