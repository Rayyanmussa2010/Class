# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 15:10:32 2021

@author: DELL
"""

class Book:
    def __init__(self, book, author, price, year, reg, yearpub):
        self.book_name=book
        self.book_author=author
        self.book_price=price
        self.book_year=year
        self.book_add=reg
        self.book_yearpub=yearpub
    def add_Book(self):
        print("Book Name:"+self.book_name)
        print("Author:"+(self.book_author))
        print("Price:"+self.book_price)
        print("Year Published:"+self.book_year)
        print(self.book_add)
        print("Book was published"+self.book_yearpub)

book1=Book(" Harry Potter and the Philosopher's Stone", " J.K Rowling", " 1928", " 1997", "Book Added", "23 years ago")
book1.add_Book()

book2=Book(" Diary of a Wimpy Kid", " Jeff Kinney", " 700", " 2017", "Book Added", "3 years ago")
book2.add_Book()
