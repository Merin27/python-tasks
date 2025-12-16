# To write a program in python find the second smallest and third largest number in a list
list1 = [50, 48, 3, 45, 31, 10, 24, 16, 8]

largest = list1[0]
smallest = list1[0]
largest2 = None
largest3 = None
smallest2 = None

for item in list1[1:]:
    if item > largest:
        largest3 = largest2
        largest2 = largest
        largest = item
    elif largest2 is None or item > largest2:
        largest3 = largest2
        largest2 = item
    elif largest3 is None or item > largest3:
        largest3 = item
    if item < smallest:
        smallest2 = smallest
        smallest = item
    elif smallest2 is None or item < smallest2:
        smallest2 = item

print("Third Largest number is:", largest3)
print("Second Smallest number is:", smallest2)
