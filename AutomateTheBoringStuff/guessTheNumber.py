# This is a guess the number game

import random

secretNumber = random.randint(1,20)

print("I'm thinking of a number betweent 1 and 20")

for guesses in range(1,7):
    print("Take a guess.")
    guess=int(input())

    if guess < secretNumber:
        print("Too Low!")
    elif guess > secretNumber:
        print("Too High!")
    else:
        break

if guess == secretNumber:
    print("Congratulations, you guessed my number! You took " + str(guesses) + " attempts to crack it!")
else:
    print("Sorry, you didn't guess right - my number was " + str(secretNumber) + "!")