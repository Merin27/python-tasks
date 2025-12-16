#Write a Python program to sort a list of tuples using Lambda.

def sort_tuples(result):
    return sorted(result, key= lambda x:x[1])


result = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_result = sort_tuples(result)
print("Sorted list of tuples:", sorted_result)
