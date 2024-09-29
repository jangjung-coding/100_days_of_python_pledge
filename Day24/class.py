# Files

# file = open("Day24\my_file.txt")
# contents = file.read()
# print(contents)
# file.close() # Always close the file after reading or writing

# with open("Day24\my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("Day24\my_file.txt", mode="w") as file:
    file.write("\nNew text.") # Overwrites the file
    