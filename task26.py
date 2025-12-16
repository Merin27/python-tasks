# Write a Python program that uses a list comprehension to create a new list that contains only the uppercase letters in an existing list of strings.

strings_list = ["HTML", "Python", "React", "JavaScript", "SQL"]

uppercase_letters = []

for string in strings_list:
    for char in string:
        if char.isupper():
            uppercase_letters.append(char)

print("Uppercase letters:", uppercase_letters)
