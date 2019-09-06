import random
import string

def generatePassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

choice = 1
while(choice):
    choice = input("Enter 0 to exit. Any other key to generate a new password")
    if(not choice):
        break
    length = int(input("Enter length"))
    print("Your password is", generatePassword(length))
