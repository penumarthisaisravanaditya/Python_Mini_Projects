import os
from random import randint
import time
password = input("Enter the password to attack: ")
keys=[
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    # '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    # '[', ']', '{', '}', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?',
]
pwg=""
attempts=0
start_time = time.time()
while pwg != password:
    pwg=""
    attempts+=1
    for letter in range(len(password)):
        guessPassword = keys[randint(0, len(keys)-1)]
        pwg = str(pwg) + str(guessPassword)
        print(pwg)
        print("Attacking... please wait")
        os.system("cls")
        
        
end_time = time.time()
total_time = end_time - start_time

print(f"The Password is: {pwg}")
print(f"TotalAttempts: {attempts}")
print(f"Time taken: {total_time:.2f} seconds")