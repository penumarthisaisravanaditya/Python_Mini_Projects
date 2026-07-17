import time
print("Welcome to the Speed Typing Test!")
sentence = "The quick brown fox jumps over the lazy dog."
print("\nType the following sentence as fast as you can:")
print(sentence)
input("Press Enter when you're ready...")
start=time.time()
typed_sentence = input("\nStart typing.. : ")

end=time.time()
time_taken = round(end - start, 2)
speed = round(len(typed_sentence) / time_taken, 2)
print(f"\nTime taken: {time_taken} seconds")
print(f"Your typing speed: {speed} characters per second")

if typed_sentence == sentence:
    print("Congratulations! You typed the sentence correctly.")
else:
    print("Oops! There were some mistakes in your typing.")