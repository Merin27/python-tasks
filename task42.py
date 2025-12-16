# Write a Python program to square and cube every number in a given list of integers using Lambda.


def square(num):
    return num ** 2

def cube(num):
    return num ** 3

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_lst = list(map(lambda x: square(x), numbers))
cubed_lst = list(map(lambda x: cube(x), numbers))

print("Squared numbers:", squared_lst)
print("Cubed numbers:", cubed_lst)
