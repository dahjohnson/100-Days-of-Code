from random import choice, shuffle
from art import logo

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def random_letters(num_of_letters):
    """Takes user input for number of letters chosen and returns a list of
     randomly chosen letters"""
    letters_list = []
    for _ in range(num_of_letters):
        letters_list += choice(letters)
    return letters_list


def random_symbols(num_of_symbols):
    """Takes user input for number of symbols chosen and returns a list of
     randomly chosen symbols"""
    symbols_list = []
    for _ in range(num_of_symbols):
        symbols_list += choice(symbols)
    return symbols_list


def random_numbers(num_of_numbers):
    """Takes user input for number of numbers chosen and returns a list of
     randomly chosen numbers"""
    numbers_list = []
    for _ in range(num_of_numbers):
        numbers_list += choice(numbers)
    return numbers_list


def generated_password():
    """Randomizes and returns the generated lists of letters, symbols, and
    numbers as a string"""
    password_list = []
    password_list += random_letters(nr_letters)
    password_list += random_symbols(nr_symbols)
    password_list += random_numbers(nr_numbers)

    shuffle(password_list)

    return "".join(password_list)


print(logo)

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


print(f"Your password is: {generated_password()}")

