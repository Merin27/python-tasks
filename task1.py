#Write a program that counts the number of vowels and consonants in a string.

strings=input('Enter the string:')
vowels = "aeiouAEIOU"

vowel_count = 0
consonant_count = 0

for i in strings:
    if i in vowels:
        vowel_count += 1
    else:
        consonant_count += 1

print(vowel_count)
print(consonant_count)
