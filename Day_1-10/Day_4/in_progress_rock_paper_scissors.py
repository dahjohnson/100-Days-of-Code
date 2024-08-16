from art import logo, rock, paper, scissors
import random

print(logo)

options = [rock, paper, scissors]


def user_selection(choice):
    if choice == 0:
        print(rock)
        return rock
    elif choice == 1:
        print(paper)
        return paper
    elif choice == 2:
        print(scissors)
        return scissors


def computer_selection():
    computer_option = random.choice(options)
    print(f"Computer chose: ")
    print(computer_option)
    return computer_option


def game_logic(user,computer):
    if user == computer:
        print("It's a Draw")
    elif user == rock and computer == paper:
        print("You lose")
    elif user == rock and computer == scissors:
        print("You win")
    elif user == paper and computer == rock:
        print("You win")
    elif user == paper and computer == scissors:
        print("You lose")
    elif user == scissors and computer == rock:
        print("You lose")
    elif user == scissors and computer == paper:
        print("You win")


keep_playing = True

user_score = 0
computer_score = 0

while keep_playing:

    user_choice = int(input("\nWhat do you choose? Type '0' for Rock, '1' for Paper, or '2' for Scissors: "))

    game_logic(user_selection(user_choice), computer_selection())


