class library():
    count=0
    d=[]
    def __init__(self,books,catagory):
        self.books=books
       
        
        if self.books in library.d:
            print("Book already exist")
            return
        
        self.catagory=catagory
        library.count+=1
        library.d.append(self.books)        
    def info(self):
        print("the no of books are", library.count,"and the books are",library.d)
    def catagory(self):
        if self.books in library.d:
            print(self.books,f"Catagory : {self.catagory}")
        else:
            print("Book not found")
    def remove(self):
        library.d.remove(self.books)        


a=library("Science","study")
b=library("sst","SOcail")
c=library("Maths","Thinking")

a.info()

