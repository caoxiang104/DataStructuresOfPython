# coding=utf-8
"""
编写一个Library类，它能够管理“编辑项目9”中的图书和读者。这个类应该
包含添加、删除和查找图书和读者的方法，还应该有借阅和归还图书的办法。
编写一段脚本来测试所有这些方法。
"""
from Chapter1_Programming_Basics.example9 import Book, Patron


class Library(object):
    def __init__(self, book=list(), reader=list()):
        self.book = []
        self.reader = []
        self.book_length = 0
        self.reader_length = 0
        for i in book:
            self.book.append(i)
            self.book_length += 1
        for i in reader:
            self.reader.append(i)
            self.reader_length += 1

    def __str__(self):
        return str(self.book), str(self.reader)

    def add_book(self, book=Book()):
        self.book.append(book)
        self.book_length += 1
        return book.title, book.author

    def delete_book(self, book=Book()):
        if self.book_length <= 0:
            raise IndexError("library is empty, can't delete!")
        else:
            self.book.remove(book)
            self.book_length -= 1
        return book.title, book.author

    def find_book(self, book=Book()):
        for i in self.book:
            if i.title == book.title and i.author == book.author:
                return True
        return False

    def add_reader(self, patron=Patron()):
        self.reader.append(patron)
        self.reader_length += 1
        return patron.name, patron.id

    def delete_reader(self, patron=Patron()):
        if self.reader_length <= 0:
            raise IndexError("library is empty, can't delete!")
        else:
            self.reader.remove(patron)
            self.reader_length -= 1
        return patron.name, patron.id

    def find_reader(self, patron=Patron()):
        for i in self.reader:
            if i.name == patron.name and i.id == patron.id:
                return True
        return False

    def borrow_book(self, book=Book(), patron=Patron()):
        if self.find_book(book) and self.find_reader(patron):
            patron.read_book(book, 0)
            self.delete_book(book)
        else:
            raise IndexError("Can't find book or reader")
        return book.title, book.author

    def return_book(self, book=Book(), patron=Patron()):
        if self.find_reader(patron):
            self.add_book(book)
            patron.read_book(book, 1)
        else:
            raise IndexError("Can't find reader")
        return book.title, book.author


def main():
    lib = Library()
    book1 = Book("Gone with the Wind", "Margaret Mitchell")
    book2 = Book("Pride and Prejudice", "Jane Austen")
    book3 = Book("Oliver Twist", "Charles Dickens")
    book4 = Book("The Little Prince", "Antoine de Saint-Exupéry")
    lib.add_book(book1)
    lib.add_book(book2)
    lib.add_book(book3)
    lib.add_book(book4)
    print("The total number of books in library is:{}".format(lib.book_length))
    print("The title of books in library is:")
    for i in lib.book:
        print(i.title, end="  ")
    print("")
    print("Can we find the book of {} in library?".format(book1.title), lib.find_book(book1))
    lib.delete_book(book1)
    print("After delete book of {} Can we find it in library?".format(book1.title), lib.find_book(book1))
    patron1 = Patron("Jack", "man", "121")
    patron2 = Patron("Bob", "man", "122")
    patron3 = Patron("Tim", "man", "123")
    patron4 = Patron("Ann", "woman", "124")
    patron5 = Patron("Jane", "woman", "125")
    lib.add_reader(patron1)
    lib.add_reader(patron2)
    lib.add_reader(patron3)
    lib.add_reader(patron4)
    lib.add_reader(patron5)
    print("The total number of readers in library is:{}".format(lib.reader_length))
    print("The name and id of readers in library is:")
    for i in lib.reader:
        print(i.name, i.id, end=",")
    print("")
    print("Can we find {} in library?".format(patron1.name), lib.find_reader(patron1))
    lib.delete_reader(patron5)
    print("After delete {} Can we find it in library?".format(patron5.name), lib.find_reader(patron5))
    lib.borrow_book(book2, patron1)
    print("{} has borrow book {}?".format(patron1.name, book2.title), not lib.find_book(book2))
    print("The book is in {}'s hand and he/she has {} book/books".format(book2.browse, len(patron1.book)))
    lib.return_book(book2, patron1)
    print("{} has return book {}?".format(patron1.name, book2.title), lib.find_book(book2))
    # print(book2.browse, len(patron1.book))


if __name__ == '__main__':
    main()






