import math
print(math.sqrt(16))

import random 
print(random.randint(1,10))

from random import choices
print(choices(["Apple","Banana","Cherry"]))

import random as r
print(r.randint(1,10))

#Random Password Generator
import random, string

#Step 1: Define Password Generation Function
def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be atleast 4 characters")

    #Characterset for the password
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*()_=+[]{}<>/;'?"

    #Ensure atleast one of each character
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    print("password:", password)
    #Fill the remaining length with random choices from all sets
    all_chars = uppercase + lowercase + digits + special_chars

    password += random.choices(all_chars, k = length - 4)
    print("password:", password)

    #Shuffle the password to make it more random
    random.shuffle(password)
    str(password)
    #Convert the list to a string and return
    return ''.join(password)

try:
    length = int(input("Enter the desired password length (minimum 4): "))
    password = generate_password(length)
    print("Generated password:", password)
except ValueError as e:
    print(e)






