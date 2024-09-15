print("Welcome to the Guess the Answer Game!")
print("I'm thinking of a number between 1 and 100.")


# Generate a random number between 1 and 100
import random
random_number = random.randint(1, 100)

# Set the number of attempts based on the difficulty
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    opportunity = 0
    if difficulty == "easy":
        opportunity = 10
    else:
        opportunity = 5
    return opportunity
    
# Get a number from user
def game(opportunity):
    still_wrong = True
    while still_wrong:
        print(f"You have {opportunity} attempts remaining to guess the number")
        guess_number = int(input("Make a guess: "))

        if guess_number > random_number:
            print("Too high")
        elif guess_number < random_number:
            print("Too low")
        else:
            print(f"You got it!. The number is {random_number}")
            still_wrong = False
        
        opportunity -= 1
        if opportunity == 0:
            still_wrong = False
            print("You are running out of life.. Game Over")
            
game(set_difficulty())

