"""Simple number guessing game."""


import random


def guess_number():
    """Generate a number and let user guess it."""
    secret = random.randint(1, 10)
    attempts = 0

    print("Guess a number between 1 and 10")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret:
                print("Too low!")
            elif guess > secret:
                print("Too high!")
            else:
                print(f"Correct! You guessed in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    guess_number()
    