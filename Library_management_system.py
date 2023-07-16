#The first class,Book
class Book:
    def __init__(self,title,author,publication_year,borrowed): #The attributes in the constant,function
        self.title=title
        self.author=author
        self.publication_year=publication_year
        self.borrowed=True,False

    def Borrow_book(self):    #The function that returns True if a book is borrowed
        borrowed_book=True
        return True
        
    def Return_book(self):     #The function that returns False if a book is returned or nor borrowed
        borrowed_book=False
        return False
    
    def Display_info(self ):  #The function will display the information concerning the book(s)
        print("Title for the books:"+str( list(["Python Programming","Multimedia Systems","Computer Science","Software Engineering"  ])))
        print("Author:E.N MAINA")
        print("Year of Publication:2020")
        print("Borrowed status:None")
        
class LibraryMember(Book):
    def __init__(self,title,author,publication_year,borrowed,member_ID,Name,borrowed_books):
        self.member_ID=member_ID
        self.Name=Name
        self.borrowed_books=borrowed_books
        super().__init__(title,author,publication_year,borrowed)
        
    def Borrowed_books(self,book):   #The function that returns the book borrowed 
       borrowed_book=self.borrowed_book 
       return (list(borrowed_book))
        
    def Return_books(self,book):   #The function that returns the book is returned
       returned_book=returned_book.remove[x,y,z]
       return returned_book 
       
    def display_info(self):   #The function  returns the basic details concerning the library member
       print("Member ID:12345")
       print("Name:MAINA ERIC")
       print("Borrowed books:"+str (borrowed_book))
       print("Borrowing Status : True")

#The objects of  the class
print("~A sample of a Library Management System containing books; \n")
obj=Book(["Python Ptogramming","Multimedia Systems","Computer Science","Software Engineering"],"E.N MAINA",2023,None)
print(obj.Display_info())

borrowed_book=input("Enter the title of the book from the list given above to borrow: ")

obj_1=LibraryMember(["Python Ptogramming","Networking"],"E.N MAINA",2023, True,12345,"MAINA ERIC",borrowed_book)
print(obj_1.display_info())
 
