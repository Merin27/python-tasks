# Create a Python program that takes two sets and returns a new set containing elements that are common in both input sets.

def common_elements(set1, set2):
    
    common_set = set()
    
    for i in set1:
        
        if i in set2:
            common_set.add(i)
    
    return common_set

set1 = {2, 4, 6, 8, 9}
set2 = {4, 6, 7, 9, 10}

common_set = common_elements(set1, set2)
print("Common elements in set1 and set2:", common_set)
