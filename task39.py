# Write a program to create a custom iterator that iterates from 1 to 10 in 0.5 intervals.

class numbers:

   def __iter__(self):
       self.num = 1
       return self

   def __next__(self):
       if self.num > 10:
           raise StopIteration
       temp = self.num
       self.num += 0.5
       return temp

obj = numbers()
iter_obj = iter(obj)
for num in iter_obj:
   print(num, end=" , ")