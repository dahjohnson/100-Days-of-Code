import art
print(art.logo)


def highest_bid():
    high_bid = 0
    bids[name] = bid
    if bids[name] > high_bid:
        high_bid = bids[name]


bids = {}

anymore_bidders = True


while anymore_bidders:

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    highest_bid()

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.").lower()

    if should_continue == "no":
        anymore_bidders = False
        print(f"The winner is {name} with a bid of ${bid}.")
    elif should_continue == "yes":
        print("\n" * 20)
