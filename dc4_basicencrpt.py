# Encrpytion Practice 1: Ceasar Cypher
# Create a string to store all letters of the alphabet
alphabet = 'abcdefghijklmnopqrstuvqxyz'

# Create a key value; used to generate new text
key = 5

# Create a message to prompt input & define "encrypt" as empty string
message = input('Enter the message: ')
encrypt = ''

# Create for loop to check for each character in message
# for its position inside the alphabet. The for loop will
# then add the key value to that position and the new value
# will be stored in a new variable as the encrypted message.
for i in message:
    position = alphabet.find (i) # Storing values  within variable
    new_position = (position + key) % 26 # Adding key value to indexed value % 26
    encrypt += alphabet[new_position] # Slicing alphabet with new variable

print(encrypt)



