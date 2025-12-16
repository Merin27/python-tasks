# Write a program to check palindrome number

def is_palindrome_number(num):
    
    str_num = str(num)
    
    return str_num == str_num[::-1]

number = int(input("Enter the number:"))

if is_palindrome_number(number):
    print(number, "is a palindrome number.")
else:
    print(number, "is not a palindrome number.")

