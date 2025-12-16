#Write a Python program that matches a string that has an a followed by zero or one 'b'

import re

def match_string(input_string):
    
    pattern = "^ab?$"
    
    if re.match(pattern, input_string):
        return "Match found"
    else:
        return "No match found"

input_string = input("Enter a string: ")
print(match_string(input_string))


