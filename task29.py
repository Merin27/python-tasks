# Create a simple calculator operations using function.
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error Division by zero."
    else:
        return n1 / n2
print("Simple Calculator")
print("Select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
select = int(input("Enter (1/2/3/4) :"))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if select == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif select == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))
elif select == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))
elif select == 4:
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")