# Create a random password generator
# Import random variable generator
import random

# Specify characters being used to create passwords
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"

# Create main loop
while 1:  # "While true..."
    password_len = int(input("What length would you like your password to be: "))
    password_count = int(input("How many passwords would you like: "))
    for x in range(0,password_count): #Run loop for as many times as passwords wanted
        password = "" #Assign password to blank string
        for x in range(0,password_len): #Run loop until password length is met
            password_char = random.choice(chars) #Select random character from list
            password = password + password_char #Add character to password
        
        print("Here is your password: ", password)