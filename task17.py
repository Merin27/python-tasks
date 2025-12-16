# Write a program to print sum of digits

def sum_digits(num):
    total_sum = 0
    
    while num > 0:
        digit = num % 10
        total_sum += digit
        num = num // 10
    return total_sum

number = int(input("Enter the number:"))
print("Sum of digits:", sum_digits(number))
