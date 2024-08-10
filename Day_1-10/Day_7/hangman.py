import random
import hangman_art
from hangman_words import word_list

#Hangman Game Title
print(hangman_art.logo)

#Word selected for Hangman
chosen_word = random.choice(word_list)

placeholder = ""

lives = 6


for position in range(len(chosen_word)):
    placeholder += "_"

#print(chosen_word)
print(placeholder)

correct_letters = []
game_over = False

while not game_over:

    print(f"****************************{lives} LIVES LEFT!!!****************************")
    guess = input("Guess a letter: ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter

        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"the letter \"{guess}\" was not in the word!!")
        print("You lose a life!!!")

        if lives == 0:
            game_over = True
            print("*****************YOU LOSE*****************")
            print(f"The word was {chosen_word}")

    if "_" not in display:
        game_over = True
        print("*****************YOU WIN*****************")

    print(hangman_art.stages[lives])
