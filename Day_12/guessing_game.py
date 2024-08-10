from random import randint
from art import logo


def guessing_game(mode):
    chosen_num = randint(1, 100)
    num_of_attempts = -1
    incorrect_answer = True
    if mode == 'easy':
        num_of_attempts = 10
    elif mode == 'hard':
        num_of_attempts = 5
    while incorrect_answer:
        guess = int((input("Make a guess: ")))
        if guess == chosen_num:
            print(f"You got it🎊🥳! The answer was {chosen_num}")
            incorrect_answer = False
        elif num_of_attempts == 0:
            print("You've run out of guesses. you lose.😓")
            incorrect_answer = False
        elif guess > chosen_num:
            num_of_attempts -= 1
            print("Too high.")
            print("Guess again.")
            print(f"You have {num_of_attempts} attempts remaining to guess the number.")
        elif guess < chosen_num:
            num_of_attempts -= 1
            print("Too low.")
            print("Guess again.")
            print(f"You have {num_of_attempts} attempts remaining to guess the number.")


play_game = True

while play_game:
    print(logo)
    print("Welcome to the Number guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    guessing_game(input("Choose a difficulty. Type 'easy' or 'hard': ").lower())
    should_continue = input("Do you wish to play again? 'Y' for Yes or 'N' for No: ").upper()
    if should_continue == "Y":
        print("\n" * 25)
    else:
        play_game = False
        print("\n")
        print("Good Bye!!!👋🏽")
        print("\n")

