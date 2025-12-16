# Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda


def divisible_numbers(numbers):
    return list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))

numbers = [10, 13, 19, 25, 26, 38, 47, 51, 56, 65, 76, 85, 104, 113, 119]

result = divisible_numbers(numbers)

print("Numbers divisible by 19 or 13:", result)
