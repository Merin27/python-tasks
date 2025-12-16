# Create a Python function that takes a string as input and counts the number of vowels and consonants in the string

def count(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in input_string:
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1 
    
    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)

string = input("Enter a string: ")
count(string)
