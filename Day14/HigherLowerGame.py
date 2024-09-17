print("Welcom to the Higher Lower Game!")

data = [
    {
        "name": "Instagram",
        "follower_count": 346,
        "description": "Social media platform",
        "country": "United States"
    },
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 215,
        "description": "Footballer",
        "country": "Portugal"
    },
    {
        "name": "Ariana Grande",
        "follower_count": 183,
        "description": "Musician and actress",
        "country": "United States"
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 181,
        "description": "Actor and professional wrestler",
        "country": "United States"
    },
    {
        "name": "Selena Gomez",
        "follower_count": 174,
        "description": "Musician and actress",
        "country": "United States"
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 172,
        "description": "Reality TV personality and businesswoman",
        "country": "United States"
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 167,
        "description": "Reality TV personality and businesswoman",
        "country": "United States"
    }
]

import random

score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    
    if account_a == account_b:
        account_b = random.choice(data)

    # Fomat the account data into printabel format
    def format_data(account):
        account_name = account["name"]
        account_description = account["description"]
        account_country = account["country"]
        return f"{account_name}, a {account_description}, from {account_country}"

    def check_answer(guess, a_follower_count, b_follower_count):
        if a_follower_count > b_follower_count:
            return guess == "a"
        else:
            return guess == "b"

    print(format_data(account_a))
    print("-------------vs-------------")
    print(format_data(account_b))

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n"*20)
    
    # Check if user is correct
    ## Get follower count of each account
    ## Use if statement to check if user is correct
    a_follwer_count = account_a["follower_count"]
    b_follwer_count = account_b["follower_count"]
    is_corrcet = check_answer(guess, a_follwer_count, b_follwer_count)
    print()
    # Give user feedback on their guess
    # Score keepping
    if is_corrcet:
        score += 1
        print("You're right! Current score: ", score)
    else:
        print("You're wrong! Final score: ", score)
        game_should_continue = False

# Make the game repeatable
# Making account at position B become the next account at position A
