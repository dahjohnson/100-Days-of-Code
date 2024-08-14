from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')


def check_resources(beverage):
    for n in MENU[beverage]["ingredients"]:
        x = resources[n] - MENU[beverage]["ingredients"][n]
        if x < 0:
            return False
    return True


def transaction(beverage):
    payment = 0

    print("Please insert coins.")

    payment += int(input("how many quarters?: ")) * .25
    payment += int(input("how many dimes?: ")) * .10
    payment += int(input("how many nickles?: ")) * .05
    payment += int(input("how many pennies?: ")) * .01

    change = payment - MENU[beverage]['cost']

    if payment > MENU[beverage]['cost']:
        print(f"Here is ${change} in change.")
        print(f"Here is your {beverage}☕. Enjoy!\n")
    else:
        print(f"Sorry that's not enough money. Money refunded.\n")


machine_running = True
print(logo)


while machine_running:

    option = input("What would you like? (espresso/latte/cappuccino): ")

    if option == "report":
        report()
    elif option == "off":
        print("Coffee Machine is Shutting Down")
        print("Good Bye!")
        machine_running = False
    elif option == "espresso" or "latte" or "cappuccino":
        if check_resources(option):
            transaction(option)
            for ingredient in MENU[option]["ingredients"]:
                resources[ingredient] = resources[ingredient] - MENU[option]["ingredients"][ingredient]
        else:
            print("Not enough resources.  Try another option.")
    else:
        print("Invalid option.\n")

