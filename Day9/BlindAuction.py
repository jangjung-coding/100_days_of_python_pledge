print("Welcome to the secret auction program.")

bidder = {}
# Ask the user for input
while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    # Save the user's name and bid in a dictionary
    bidder[name] = bid

    # Ask the user if there is another bidder
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    # If there is another bidder, clear the screen and ask for input again
    if should_continue == "yes":
        print("\033c")
    else:
        break

# If there are no more bidders, find the highest bidder
highest_bid = 0
highest_bidder = ""

for key in bidder:
    if bidder[key] > highest_bid:
        highest_bid = bidder[key]
        highest_bidder = key

# Print the highest bidder's name and bid
print(f"The winner is {highest_bidder} with a bid of $ {highest_bid}.")