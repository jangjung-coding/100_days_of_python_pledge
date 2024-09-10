print("Welcome to Hangman!")

import random

lives = 6
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

for _ in range(len(chosen_word)):
    print("_", end=" ")
            
game_over = False
correct_letters = []
        
while not game_over:
    guess = input("\nGuess a letter: ").lower()
    
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"         
    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess. You have {lives} lives left.")
        if lives == 0:
            game_over = True
            print("You lose!")

    if "_" not in display:
        gmame_over = True
        print("You win!")
        
    print(lives)