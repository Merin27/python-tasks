# Write a Python function that takes a tuple and an element as input and counts how many times that element appears in the tuple

def count_element(tuple, element):
    
    count = 0 
    for i in tuple:
        if i == element:
            count+= 1 
    return count 


my_tuple = (5, 2, 3, 4, 2, 2, 5)
element = int(input('Enter the Number:'))
count = count_element(my_tuple, element)
print("count:", count)
