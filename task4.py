# Write a Python program that takes a list of numbers as input and calculates and prints the sum and average of those numbers

numbers = input("Enter the numbers separated by spaces: ")

numb_list = [float(x) for x in numbers.split()]
print(numb_list)


count = sum(numb_list)

avg = count / len(numb_list)


print("The total sum is:", count)
print("The average is:", avg)

