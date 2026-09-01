#python -m pip install pyjokes

import pyjokes

jokee = pyjokes.get_joke()

print("Joke of the moment:", jokee, "\n")

print("Here are some more jokes for you:\n")

count = 1

while count <= 5:
    joke = pyjokes.get_joke()
    print(str(count) + ". " + joke)
    count += 1

print("\nBonus Joke:")

print(pyjokes.get_joke(category="chuck"))