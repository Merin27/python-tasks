#Write a function in Python to count and display the total number of words in a text file.

def count_words():
    file = open("story.txt","r")
    count = 0
    data = file.read()
    words = data.split()
    for word in words:
        count += 1
    print("Total number of words:",count)
    file.close()

count_words()