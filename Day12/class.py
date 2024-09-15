# Scope

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
    
# increase_enemies()
# print(f"enemies outside function: {enemies}") # This will give an error because enemies is not defined outside the function

# Local Scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength) # NameError: name 'potion_strength' is not defined

# Global Scope
# player_health = 10

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
    
#     drink_potion()
    
# game()
# print(player_health)

# There is no Block Scope in Python
# game_level = 10
# enemies = ["Skeleton", "Zombie", "Alien"]

# def create_enemy():
#     new_enemy = ""
#     if game_level < 5:
#         new_enemy = enemies[0]
    
#     print(new_enemy)
    
# # Prime Number Checker
# def is_prime(num):
    
#     for _ in range(2, num):
#         if num % _ == 0:
#             return False
#         else:
#             pass
#     return True
        
# is_prime(75)
