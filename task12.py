# Create a Python program that takes a string as input and checks if all the characters in the string are unique (i.e., no character repeats). Return True if all characters are unique, and False otherwise

def unique_chars(string):
    u_chars = []
    
    for i in string:
        
        if i in u_chars:
            return False
        else:
            u_chars.append(i)
        
    return True

string = "hello python"
print(unique_chars(string))

string = "abcdefgh"
print(unique_chars(string))
