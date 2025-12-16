# Write a Python program that uses list comprehension to create a new list containing the squares of the numbers from 1 to 10

squares = []

for x in range(1, 11):
    squares.append(x ** 2)

print("Squares of numbers from 1 to 10:", squares)
