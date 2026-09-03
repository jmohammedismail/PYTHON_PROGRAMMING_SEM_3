import random

number = random.randint(1, 100)

guess = int(input("Guess the number (1-100): "))

if guess == number:
    print("Congratulations! You guessed it correctly.")
elif guess < number:
    print("Too low! The number was", number)
else:
    print("Too high! The number was", number)
