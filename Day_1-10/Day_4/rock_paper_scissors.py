rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

game_images = [rock, paper, scissors]

print("Welcome to the Rock, Paper, Scissors Game!!!")

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

print()

if choice == 0:
    print("You Chose Rock!")
    print(rock)
elif choice == 1:
    print("You Chose Paper!")
    print(paper)
elif choice == 2:
    print("You Chose Scissors!")
    print(scissors)
else:
    print("You must type 0 for Rock, 1 for Paper, or 2 for Scissors.")
    exit()

computer_choice = random.randint(0,2)
if computer_choice == 0:
    print("The Computer Chose Rock!")
    print(rock)
elif computer_choice == 1:
    print("The Computer Chose Paper!")
    print(paper)
elif computer_choice == 2:
    print("The Computer Chose Scissors!")
    print(scissors)

if choice == 0 and computer_choice == 1:
    print("The Computer Wins!")
elif choice == 1 and computer_choice == 0:
    print("You Won!!!")
elif choice == 0 and computer_choice == 2:
    print("You Won!!!")
elif choice == 2 and computer_choice == 0:
    print("The Computer Wins!")
elif choice == 1 and computer_choice == 2:
    print("The Computer Wins!")
elif choice == 2 and computer_choice == 1:
    print("You Won!!!")
else:
    print("Its a Draw.")
