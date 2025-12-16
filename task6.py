# Create a Python function that takes a list as input and removes duplicate elements, preserving the order of the elements. Return the new list.

def remove_duplicates(lst):
    
    new_list = []
    
    for item in lst:
        
        if item not in new_list:
            new_list.append(item)       
    
    return new_list

my_list = [2, 4, 3, 4, 2, 1, 3, 3]
new_list = remove_duplicates(my_list)
print(new_list) 
