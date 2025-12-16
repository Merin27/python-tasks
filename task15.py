# Write a program to check Armstrong number.

numb = int(input("Enter a number: "))

order = len(str(numb))
sum = 0
temp = numb

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if numb == sum:
    print(numb,"is an Armstrong number")

else:
    print(numb,"is not an Armstrong number")
