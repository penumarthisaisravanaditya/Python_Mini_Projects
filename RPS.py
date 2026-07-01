import random
choices = ["rock","paper","scissors"]
user = input("Enter rock, paper or scissors: ").lower()
computer =random.choice(choices)
print("You chose:", user)
print("Computer chose:", computer)
if user == computer:
    print("It's a Tie!")
elif (user == "rock" and computer == "scissors") or \
    (user == "scissors" and computer == "paper") or \
    (user == "paper" and computer == "rock" ):
    print("You Win!")
else:
    print("Computer Wins!")