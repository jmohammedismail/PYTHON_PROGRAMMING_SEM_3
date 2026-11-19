
import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number (1-100): "))

    if guess == number:
        print("Congratulations! You guessed it correctly.")
        break

    elif guess < number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")
