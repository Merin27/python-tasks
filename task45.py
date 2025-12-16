

def sum_positive_negative(numbers):
    
    positive_sum = sum(filter(lambda x: x > 0, numbers))
    negative_sum = sum(filter(lambda x: x < 0, numbers))
    return positive_sum, negative_sum


numbers = [10, -15, 3, -7, 18, -5, 4, -8]
positive_sum, negative_sum = sum_positive_negative(numbers)

print(f"Sum of positive numbers: {positive_sum}")
print(f"Sum of negative numbers: {negative_sum}")
