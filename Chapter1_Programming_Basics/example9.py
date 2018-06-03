# coding=utf-8
"""
针对图书馆的一个简单的软件系统，会将图书馆建模为图书和读者的一个集合。读
者在任何给定的时间内，最多只能够借3本图书。每本图书有一个等待借阅的读者的
列表。每本图书有一个标题、一个作者、已经借阅了它的一名读者，以及等待这本图
书还回后再继续借阅读者的列表。编写Book和Patron类来建模这些对象。首先考虑每
个类的接口或方法，然后为对象的状态选择适当的数据结构。此外，还要编写一个简短
的脚本来测试这些类。
"""


class Book(object):
    def __init__(self, title='', author=''):
        self.title = title
        self.author = author
        self.browse = ''
        self.waiters = []

    def reader(self, browse='', waiters=list()):
        self.browse = browse
        for i in waiters:
            self.waiters.append(i)

    def info(self):
        return self.title, self.author


class Patron(object):
    def __init__(self, name='', sex='', ID='', books=list()):
        self.name = name
        self.sex = sex
        self.id = ID
        self.book = []
        for i in books:
            self.book.append(i)

    def info(self):
        return self.name, self.sex, self.id, self.book

    # flag=0 表示借书， flag=1 表示还书
    def read_book(self, book, flag=0):
        if flag == 0:
            if len(self.book) < 3:
                self.book.append(book)
                book.browse = self.name
            else:
                book.waiters.append(self.name)
                raise IndexError("out range")
        else:
            self.book.remove(book)
            book.browse = ''


def main():
    book1 = Book("book1", "author1")
    print(book1.reader())
    book2 = Book("book2", "author2")
    book2.reader("cansy", ["bob", "david"])
    book3 = Book("book3", "author3")
    book3.reader("bob", ["andy", "cansy", "david", "enki"])
    book4 = Book("book4", "author4")
    book4.reader("cansy", ["bob", "david"])
    book5 = Book("book5", "author5")
    book5.reader("bob", ["andy", "cansy", "david", "enki"])
    book6 = Book("book6", "author6")
    book6.reader("cansy", ["bob", "david"])
    print(book6.info())
    print(book6.browse)
    print(book6.waiters)
    patron1 = Patron("bob", "man", "123", [book1, book3, book5])
    print(patron1.info())
    for i in patron1.info()[3]:
        print(i.info(), end=" ")
    print("")
    patron1.read_book(book1, 1)
    for i in patron1.info()[3]:
        print(i.info(), end=" ")
    print("")
    patron1.read_book(book1, 0)
    for i in patron1.info()[3]:
        print(i.info(), end=" ")


if __name__ == '__main__':
    main()

