# TODO-1: Ask the user for

# TODO-2: Save data into dictionary {name: price}

# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
bids = {}

continue_bidding = True

while continue_bidding:
    name = input("What is your name? ")
    bid = int(input("What is your bid: $"))

    bids[name] = bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")

    if more_bidders == "yes":
        print("\n" * 20)
    else:
        continue_bidding = False


def findhighestbidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


findhighestbidder(bids)