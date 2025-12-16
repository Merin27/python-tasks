# Write a Python function that takes a list and an element as input and counts how many times that element appears in the list

def count_element(list, element):

    count = 0 
    
    for i in list:  
        if i == element: 
            count += 1  
    return count


my_list = [10, 2, 9, 9, 4, 10, 9]
element=int(input('Enter the Number:'))
count = count_element(my_list, element)
print("count:",count)
