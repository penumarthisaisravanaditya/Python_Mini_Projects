import random
import string

length = int(input("Enter password length: "))
characters = string.ascii_letters + string.digits + string.punctuation 
# character = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+={}[]|;:',.<>?/"
password = ""
for i in range(length):
    password += random.choice(characters)
print("Generated Password:", password)