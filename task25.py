# Write a Python program that uses a "for" loop to iterate over a string and prints out each character along with its count

string =input("Enter the string : ")
string=string.lower()

char_count = {}

for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Character along with its count: ", char_count)
