# Write a Python function that takes a list and returns a new list with the elements reversed. Do this without using the built-in reverse method.

def reverse_list(lst):
    
    reversed_list = []
    
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    
    return reversed_list
my_list = [9, 5, 4, 8, 6]
reversed_my_list = reverse_list(my_list)
print(reversed_my_list) 

