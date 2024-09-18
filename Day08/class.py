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
# def greet_with(name, location):
#     print(f"Hello, {name}")
#     print(f"What is it like in {location}?")

# greet_with("JJ", "San Francisco") #Positional Arguments
# greet_with(location="San Francisco", name="JJ") #Keyword Arguments

# Love calculator
def calculate_love_score(name1, name2):
    fullName = (name1 + name2).lower()
    true_list = ["t", "r", "u", "e"]
    love_list = ["l", "o", "v", "e"]
    
    true_num = 0
    love_num = 0
    
    for i in true_list:
        true_num += fullName.count(i)
    for j in love_list:
        love_num += fullName.count(j)
    
    print(true_num*10 + love_num)

calculate_love_score(name1 = "Jack", name2= "Angela")