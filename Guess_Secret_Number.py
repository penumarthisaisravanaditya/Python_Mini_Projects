import random
secret_number = random.randint(1,100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == secret_number:
        print("Congratulations! You guess is correct")
        break
    elif guess <secret_number:
        print("Too Low! Try Again.")
    else:
        print("Too High! Try Again.")