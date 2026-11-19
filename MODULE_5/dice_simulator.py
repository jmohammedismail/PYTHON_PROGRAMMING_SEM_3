"""Dice simulator using Python's random module."""
import random


def roll_dice():
    return random.randint(1, 6)


def main():
    print("===== DICE SIMULATOR =====")
    while True:
        choice = input("Press Enter to roll the dice or type q to quit: ").strip().lower()
        if choice == "q":
            print("Thanks for playing!")
            break
        print(f"You rolled: {roll_dice()}")


if __name__ == "__main__":
    main()
