

import random


def main():
    number = random.randint(1,10)
    guess = None
    attempts = 0
    print('============**********==================')
    print("Welcome to the Guessing Game casino!")
    print("Guess a number between 1 and 10.")

    while guess != number:
       
        guess = int(input("Enter your guess: "))
        attempts += 1
        try:
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()