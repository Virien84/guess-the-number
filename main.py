from art import logo
import random

EASY = 10
HARD = 5

attempts = EASY
num_to_guess = random.randint(1, 100)
continue_guessing = True


def guess_again():
    global guess
    print("Guess again")
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))


def guessing_game():
    global attempts
    global num_to_guess
    global continue_guessing
    global guess

    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"Tss the number is {num_to_guess}")

    difficulty = (input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()

    if difficulty == "hard":
        attempts = HARD

    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    while continue_guessing:
        if guess == num_to_guess:
            continue_guessing = False
            print(f"You got it! The answer was {num_to_guess}")
        elif guess > num_to_guess:
            print("Too high")
            attempts -= 1

        elif guess < num_to_guess:
            print("Too low")
            attempts -= 1

        if attempts > 0:
            if continue_guessing:
                guess_again()
        else:
            continue_guessing = False
            print("You've run out of guesses, you lose.")


guessing_game()
