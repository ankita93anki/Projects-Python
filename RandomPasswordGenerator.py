import math 
print(math.sqrt(16))

import random
print(random.randint(1,10))

from random import choices
print(choices([1,2,3,4,5], k=3))

from random import choices
print(choices(["Apple","Banana","Cherry"]))

import random as r
print(r.randint(1,10))

import random
password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789',k=8))
print(password)

import greetings
print(greetings.say_hello("John"))

#Random Password Generator
import random, string

#Step 1: Define Password Generation Function
def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be atleast 4 characters")
    
    #Character set for the password
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits 
    special_chars = "!@#$%^&*()_+=[]{}|;:',.<>?/"

    #Ensure at least one of each character type 
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    #Fill the remaining length with random choices from all sets
    all_chars = uppercase + lowercase + digits + special_chars 
    password += random.choices(all_chars, k=length-4)

    #Shuffle the password to make it more random
    random.shuffle(password)

    #Convert the list to a string and return
    return ''.join(password)

    #Step 2: User Interact

try:
    length = int(input("Enter the desired password length (minimum 4):"))
    password = generate_password(length)
    print("Generated Password:", password)
except ValueError as e:
    print(e)
