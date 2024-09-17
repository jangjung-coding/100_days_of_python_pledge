print("Welcome to the coffee machine")

Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

# 1. Prompt user by asking "What would you like?" (espresso/latte/cappuccino)
while True:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order in Menu.keys():
        break
    else:
        print("Invalid order. Please try again.")
    
# 2. Turn off the Coffee Machine by entering "off" to the prompt.

# 3. Print report.

# 4. Check resources suufficient?

# 5. Process coins.

# 6. Check transaction successful?

# 7. Make Coffee.
