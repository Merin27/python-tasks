# Book

class Book:
    def __init__(self,title,author,year):
        
        self.title=title
        self.author=author
        self.year=year
        
    def getBookInfo(self):
        
        return f"Title: {self.title} , Author: {self.author} , Year: {self.year}"
    
bk= Book("Wings of Fire", "APJ Abdul Kalam", 1999)    
print(bk.getBookInfo())
