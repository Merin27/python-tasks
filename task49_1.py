# Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

import re

def is_allowed_string(string):
    
    pattern="^[a-zA-Z0-9]*$"
    
    match_str=re.match(pattern,string)
    return match_str

input_string=input('enter the string:')
result=is_allowed_string(input_string)

if result:
    print("The string contains only allowed characters")
    
else:
    print("The string contains characters outside the allowed set")
