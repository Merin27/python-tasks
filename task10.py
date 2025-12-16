# Write a Python program that takes a list of person tuples (name, age) and calculates and prints the average age of the group

people = [("Liya", 23), ("Anish", 25), ("Gibz", 30), ("Sherin", 35)]

ages = [person[1] for person in people]

average_age = sum(ages) / len(ages)

print("Average age:", average_age)
