# Print the Fibonacci series for first 12 numbers.

a = 0
b = 1

n = 12

for count in range(n):
    print(a, end=" ")
    
    temp = a + b
    a = b
    b = temp
