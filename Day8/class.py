# Fuction with Inputs
# def greet_with_name(name): #Parameter : Value that we define to the function
#     print("Hello, " + name)
#     print("How do you do?")
#     print("Isn't the weather nice today?")
    
# greet_with_name("JJ") #Argument : Value that we pass to the function

# def life_in_weeks(x):
#     y = (90 - x) * 52
#     print(f"You have {y} weeks left.")
        
# age = int(input("How old are you?"))
# life_in_weeks(age)

# Function with more than 1 input
def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}?")

greet_with("JJ", "San Francisco") #Positional Arguments