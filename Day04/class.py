states_of_america = ["Delaware", "Pennsylvania"]
print(states_of_america)
# List can store multiple data types with order
print(states_of_america[0])
print(states_of_america[-1])

states_of_america[1] = "Washington"
print(states_of_america[1])
print(states_of_america)
# We can change the calue of the list by using index

states_of_america.append("New York")
print(states_of_america)
# We can add new value to the list by using append method

states_of_america.extend(["New Jersey", "New Mexico"])
print(states_of_america)
# We can add multiple values to the list by using extend method

# Error) Index out of range
