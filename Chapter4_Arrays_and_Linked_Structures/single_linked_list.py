# coding=utf-8
class LinkedList(object):
    class Node(object):
        def __init__(self, data, next_=None):
            super(LinkedList.Node, self).__init__()
            self._data = data
            self._next = next_

        def __str__(self):
            super(LinkedList.Node, self).__init__()
            return str(self._data)

    def __init__(self, *args):
        super(LinkedList, self).__init__()
        self._length = 0
        self._head = None
        for i in args:
            self.prepend(i)

    def prepend(self, value):
        self._head = self.Node(value, self._head)
        self._length += 1
        return value

    def append(self, value):
        if self._head is None:
            self._head = self.Node(value, self._head)
        else:
            temp = self._head
            while temp._next is not None:
                temp = temp._next
            temp._next = self.Node(value, None)
        self._length += 1

    def __len__(self):
        return self._length

    def pre_delete(self):
        if self._length == 0:
            raise print("The length is less than 1")
        value = self._head._data
        self._head = self._head._next
        self._length -= 1
        return value

    def behind_delete(self):
        if self._length == 0:
            raise print("The length is less than 1")
        temp = self._head
        self._length -= 1
        if temp._next is None:
            value = self._head._data
            self._head = None
            return value
        while temp._next._next is not None:
            temp = temp._next
        value = temp._next._data
        temp._next = temp._next._next
        return value

    def __str__(self):
        super(LinkedList, self).__init__()
        link_ = []
        temp = self._head
        while temp is not None:
            link_.append(temp._data)
            temp = temp._next
        return str(link_)

    def delete(self, index):
        if index <= 0:
            self.pre_delete()
        elif index >= self._length:
            self.behind_delete()
        else:
            temp = self._head
            while index > 1 and temp._next._next is not None:
                temp = temp._next
                index -= 1
            value = temp._next._data
            temp._next = temp._next._next
            self._length -= 1
            return value

    def insert(self, index, value):
        if self._length == 0 or index <= 0:
            self.prepend(value)
        elif index >= self._length:
            self.append(value)
        else:
            temp = self._head
            while index > 1:
                temp = temp._next
                index -= 1
            temp._next = self.Node(value, temp._next)
            self._length += 1
            return value

    def search(self, value):
        temp = self._head
        while temp is not None and value != temp._data:
            temp = temp._next
        if temp is None:
            return False
        else:
            return True


class LinkedListNil(object):
    """带哨兵的单链表"""
    class Node(object):
        def __init__(self, data, next_=None):
            super(LinkedListNil.Node, self).__init__()
            self._data = data
            self._next = next_

        def __str__(self):
            super(LinkedListNil.Node, self).__init__()
            return str(self._data)

    def __init__(self, *arg):
        super(LinkedListNil, self).__init__()
        self.nil = self.Node(None, None)
        self.nil._next = self.nil
        self._length = 0
        for i in arg:
            self.append(i)

    def prepend(self, value):
        temp_node = self.nil
        node = self.Node(value, temp_node._next)
        temp_node._next = node
        self._length += 1
        return value

    def append(self, value):
        temp_node = self.nil
        node = self.Node(value, temp_node)
        while temp_node._next is not self.nil:
            temp_node = temp_node._next
        temp_node._next = node
        self._length += 1
        return value

    def insert(self, index, value):
        if self._length == 0 or index <= 0:
            self.prepend(value)
        elif index >= self._length:
            self.append(value)
        else:
            temp_node = self.nil
            while index > 0:
                temp_node = temp_node._next
                index -= 1
            node = self.Node(value, temp_node._next)
            temp_node._next = node
            self._length += 1
            return value

    def pre_delete(self):
        if self._length == 0:
            raise print("The length is less than 1")
        value = self.nil._next._data
        self.nil._next = self.nil._next._next
        self._length -= 1
        return value

    def behind_delete(self):
        if self._length == 0:
            raise print("The length is less than 1")
        temp_node = self.nil
        self._length -= 1
        while temp_node._next._next is not self.nil:
            temp_node = temp_node._next
        value = temp_node._next._data
        temp_node._next = temp_node._next._next
        return value

    def delete(self, index):
        if index <= 0:
            self.pre_delete()
        elif index >= self._length:
            self.behind_delete()
        else:
            temp_node = self.nil
            while index > 0:
                temp_node = temp_node._next
                index -= 1
            value = temp_node._next._data
            temp_node._next = temp_node._next._next
            self._length -= 1
            return value

    def search(self, value):
        temp_node = self.nil._next
        while temp_node is not self.nil and value != temp_node._data:
            temp_node = temp_node._next
        if temp_node is self.nil:
            return False
        else:
            return True

    def __len__(self):
        return self._length

    def __str__(self):
        super(LinkedListNil, self).__init__()
        link_ = []
        temp = self.nil._next
        while temp is not self.nil:
            link_.append(temp._data)
            temp = temp._next
        return str(link_)


def main():
    li = LinkedList(1, 2, 3)
    print("The length of li is {}".format(len(li)))
    print("The value in li is", str(li))
    li.append(4)
    print("After append, the value in li is", str(li))
    li.pre_delete()
    print("After pre delete, the value in li is", str(li))
    li.prepend(0)
    print("After pre append, the value in li is", str(li))
    li.behind_delete()
    print("After behind delete, the value in li is", str(li))
    li.delete(1)
    print("After delete, the value in li is", str(li))
    li.insert(1, 8)
    print("After insert, the value in li is", str(li))
    print("8 in list?", li.search(8))
    li = LinkedListNil(1, 2)
    print("The length of li is {}".format(len(li)))
    print("The value in li is", str(li))
    li.append(4)
    print("After append, the value in li is", str(li))
    li.pre_delete()
    print("After pre delete, the value in li is", str(li))
    li.prepend(0)
    print("After pre append, the value in li is", str(li))
    li.behind_delete()
    print("After behind delete, the value in li is", str(li))
    li.delete(1)
    print("After delete, the value in li is", str(li))
    li.insert(1, 8)
    print("After insert, the value in li is", str(li))
    print("8 in list?", li.search(8))


if __name__ == '__main__':
    main()

