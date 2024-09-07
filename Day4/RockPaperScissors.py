print("Welcome to Rock, Paper, Scissors!")
# Get rock, paper, or scissors ascii art
rock_ascii = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper_ascii = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors_ascii = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# Make a list of the 3 possible choices
rps_list = ["rock", "paper", "scissors"]
rps_ascii_list = [rock_ascii, paper_ascii, scissors_ascii]
# Get the user's choice
user_choice = input("What do you choose (rock, paper, scissors)? ")
# Get the computer's choice
import random
computer_choice = str(random.choice(rps_list))
# Compare the two choices
result = ""
if user_choice == "rock":
  if computer_choice == "rock":
    result = "It's a draw!"
  elif computer_choice == "paper":
    result = "You lose!"
  else:
    result = "You win!"
elif user_choice == "paper":
  if computer_choice == "rock":
    result = "You win!"
  elif computer_choice == "paper":
    result = "It's a draw!"
  else:
    result = "You lose!"
else:
  if computer_choice == "rock":
    result = "You lose!"
  elif computer_choice == "paper":
    result = "You win!"
  else:
    result = "It's a draw!"
    
# Print the results
print(f"You chose: {user_choice}")
print(rps_ascii_list[rps_list.index(user_choice)])
print(f"Computer chose: {computer_choice}")
print(rps_ascii_list[rps_list.index(computer_choice)])
print(result)