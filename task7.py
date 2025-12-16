# Create a Python program that takes two lists and returns a new list containing elements that are common in both input lists.

list1 = [4, 2, 3, 7, 5]
list2 = [4, 5, 6, 7, 8]

common_list = []

for item in list1:
    
    if item in list2:
        
        if item not in common_list:
            common_list.append(item)

print("Common elements:", common_list)
