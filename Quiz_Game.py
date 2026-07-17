print("Welcome to the Quiz Game!")
print("-" * 30)

questions = ["What is the capital of India?", 
             "what is the answer of 20 + 5?", 
             "how many days in a year?"]
answers = ["New Delhi",
           "25", 
           "365"]

score = 0
for i in range(len(questions)):
    print("\nQ",i+1)
    print(questions[i])
    user_answer = input("Your Answer: ")
    if user_answer.lower() == answers[i].lower():
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer! The correct answer is:", answers[i])

print("\nYour final score is:", score, "out of", len(questions))