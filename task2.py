# Write Program to given string is a palindrome (reads the same forwards and backwards).

string = input("Enter a string: ")

string=string.lower()

if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
