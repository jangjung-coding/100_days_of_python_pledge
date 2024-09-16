# Debugging

# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")
            
# my_function() # Output: None
# # The output is None because the condition in the if statement is not met.
# # Change the range to 21 to get the output "You got it"

# from random import randint
# dice_images = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(1, 6) # Index out of range error
# print(dice_images[dice_num]) # Change the range to 0, 5 to fix the error

# year = int(input("Which year do you want to check? "))

# if year > 1980 and year < 1994:
#     print("You are a millenial")
# elif year > 1994:
#     print("You are a Gen Z") # Change the condition to year >= 1994 to fix the error

# try:
#     age = int(input("What is your age? "))
# except ValueError:
#     print("Please enter a valid number")
#     age = int(input("What is your age? "))

# if age > 18:
#     print("You can drive")