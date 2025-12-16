# Write a program to create an iterator to print English alphabets from A to Z.

class Alphabets:

   def __iter__(self):
       self.unicode = 65
       return self
   def __next__(self):
       if self.unicode > 90:
           raise StopIteration
       temp = self.unicode
       self.unicode += 1
       return chr(temp)

alphabets = Alphabets()
iter_obj = iter(alphabets)

for letter in iter_obj:
   print(letter, end=" ")