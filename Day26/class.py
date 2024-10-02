# List Comprehension

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = []
for n in number:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

new_list_2 = [n+1 for n in number]
print(new_list_2)

print([n*2 for n in range(1,5) if n % 2 == 0])