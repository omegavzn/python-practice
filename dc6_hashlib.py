# Hashing a password using hashlib
# Import hashlib
import hashlib

# Create your secret message
secret = "This is the password or document text"

# Use 'encode' method to turn string into binary. Assign to variabe bsecret.
bsecret = secret.encode()

# Hash using MD5 algorithm 
m = hashlib.md5()

m.update(bsecret)

m.digest()