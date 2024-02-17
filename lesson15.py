# CLASSES 
# Class definition
# class Car:
#     # Attributes
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model

#     # Methods
#     def start_engine(self):
#         return(f"The {self.color} {self.model} is starting the engine.")

#     def drive(self):
#         return(f"The {self.color} {self.model} is now driving.")
 
#    # Creating objects (instances)
# my_car = Car(color="blue", model="Sedan")
# your_car = Car(color="red", model="SUV")

# # Using methods
# print(my_car.start_engine())
# print(your_car.drive())

'''
Car is a class.
my_car and your_car are objects (instances) of the Car class.
color and model are attributes of the Car class.
start_engine and drive are methods of the Car class.
'''

'''
Create a Python program that simulates a simple book inventory system using classes. 
Define two classes: Book and Inventory.

Book Class:

The Book class should have the following attributes:
title: Title of the book (string).
author: Author of the book (string).
isbn: ISBN (International Standard Book Number) of the book (string).
price: Price of the book (float).


The Inventory class should manage a collection of books.
It should have the following methods:
add_book(book): Adds a book to the inventory.
remove_book(isbn): Removes a book from the inventory based on its ISBN.
display_inventory(): Displays the details of all books in the inventory.
'''


class Book:

    def __init__(self,title, author, isbn, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price

    def __str__(self):
        return self.title
    
    # def info(self):
    #     return (f"The book is {self.title}, by {self.author}, ISBN: {self.isbn} Price: {self.price}")
    
class Inventory:
    def __init__(self):
        self.total_books = []
    # def __init__(self,title, author, isbn, price):
    #     Book.__init__(self,title, author, isbn, price)


    def add_book(self,list_of_books):
        self.total_books.extend(list_of_books)
        print(self.total_books)
    
    def remove_book(self,isbn):
        print(len(self.total_books))
        for book in self.total_books:
            if book.isbn == isbn:
                self.total_books.remove(book)
        print(len(self.total_books))

    def price_remove(self,price):
        print(len(self.total_books))
        for book in range(self.total_books):
            print(self.total_books[book].price)
            if book.price == price:
                self.total_books.remove(book)
        print(len(self.total_books))


    def display_inventory(self):
        for book in self.total_books:
            print(f"Book: {book.title} Author: {book.author}, ISBN: {book.isbn} Price: {book.price}")
        print(len(self.total_books))
            #return book 
    

# book1 = Book("A series of unfortunate events","Lemony Snickett","002374075348",13.78)
# book2 = Book("bastard","Tyler The Creator","00237493748",20)
# book3 = Book("wolf","Pharell Williams","0977653348",13.75)
# book4 = Book("cherry bomb","Syd The Kid","9084750848",70.00)
# book5 = Book("mad villainy","MF DOOM and Quasimoto","00439743947",21.00)
# total_books = []
# for i in range(1,6):
#     book = Book("A series of unfortunate events","Lemony Snickett","002374075348",13.78)
#     total_books.append(book.title)
# print(total_books)

library_of_books = [Book("A series of unfortunate events", "Lemony Snickett", "002374075348", 13.78) for _ in range(1, 6)]
#print(total_books)
inventory = Inventory()

inventory.add_book(library_of_books)

inventory.price_remove(13.78)
# inventory.remove_book("002374075348")
inventory.display_inventory()



'''

class Inventory:
    def __init__(self, list_of_books):
        self.total_books = list_of_books

    def add_book(self, book):
        self.total_books.append(book)

    def remove_book(self, isbn):
        for book in self.total_books:
            if book.isbn == isbn:
                self.total_books.remove(book)
                break

    def display_inventory(self):
        for book in self.total_books:
            print(f"Book: {book.title} Author: {book.author}, ISBN: {book.isbn} Price: {book.price}")


book1 = Book("A series of unfortunate events", "Lemony Snickett", "002374075348", 13.78)
book2 = Book("Bastard", "Tyler The Creator", "00237493748", 20)
book3 = Book("Wolf", "Pharell Williams", "0977653348", 13.75)
book4 = Book("Cherry Bomb", "Syd The Kid", "9084750848", 70.00)
book5 = Book("Mad Villainy", "MF DOOM and Quasimoto", "00439743947", 21.00)

total_books = [book1, book2, book3, book4, book5]

inventory = Inventory(total_books)
inventory.display_inventory()

# Adding a new book
new_book = Book("New Book", "New Author", "1234567890", 30.00)
inventory.add_book(new_book)

print("\nAfter adding new book:")
inventory.display_inventory()

# Removing a book
inventory.remove_book("9084750848")

print("\nAfter removing a book:")
inventory.display_inventory()

'''


# def sum(a,b):
#     c = a + b
#     print(f"the sum of {a} and {b} is {c}")

# sum(1,2)

# list1 = [123,4,567,7,8]
# def list_output(*list1):
#     print(list1) 

# list_output(list1)

