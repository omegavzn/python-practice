from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

private_key = rsa.generate_private_key(public_exponent=65537,
                                       key_size=4096,
                                       backend=default_backend())

public_key = private_key.public_key()

message = b'All of your secrets go here'

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
    
encrypted = public_key.encrypt(message,
                               padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                            algorithm=hashes.SHA256(),
                                            label=None))

decrypted = private_key.decrypt(encrypted,
                                padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                             algorithm=hashes.SHA256(),
                                             label=None))
print(decrypted)

