# Convert two lists into a dictionary in Python without using a built-in method

def lists_to_dict(keys, values):
    
    new_dict = {}
    
    for i in range(len(keys)):
        new_dict[keys[i]] = values[i]
    return new_dict


keys = ['Apple', 'Banana', 'Orange']
values = [85.50, 55.50, 90.50]

dict = lists_to_dict(keys, values)
print(dict)
