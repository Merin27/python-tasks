# Write a Python program to remove duplicates from a list while preserving the order of elements

list = [20, 40, 12, 42, 30, 45, 10, 80, 16, 10, 12, 30]

new_list = []

for item in list:
    if item not in new_list:
        new_list.append(item)

print("List without duplicates:", new_list)
