# coding=utf-8
class LinkedList(object):
    class Node(object):
        def __init__(self, value, prev_node, next_node):
            super(LinkedList.Node, self).__init__()
            self.value = value
            self.prev_node = prev_node
            self.next_node = next_node

        def __str__(self):
            super(LinkedList.Node, self).__str__()
            return str(self.value)

    def __init__(self, *arg):
        self.head = None
        self.tail = None
        self.length = 0
        for i in arg:
            self.append(i)

    def __str__(self):
        list_ = []
        temp_node = self.head
        while temp_node is not None:
            list_.append(temp_node.value)
            temp_node = temp_node.next_node
        return str(list_)

    def prepend(self, value):
        if self.length == 0:
            self.head = self.Node(value, self.head, self.tail)
            self.tail = self.head
        else:
            temp_node = self.head
            self.head = self.Node(value, None, temp_node)
            temp_node.prev_node = self.head
        self.length += 1
        return value

    def append(self, value):
        if self.length == 0:
            self.tail = self.Node(value, self.head, self.tail)
            self.head = self.tail
        else:
            temp_node = self.tail
            self.tail = self.Node(value, temp_node, None)
            temp_node.next_node = self.tail
        self.length += 1
        return value

    def insert(self, index, value):
        if index <= 0:
            self.prepend(value)
        elif index >= self.length:
            self.append(value)
        else:
            temp_node = self.head
            while index > 1:
                temp_node = temp_node.next_node
                index -= 1
            node = self.Node(value, temp_node, temp_node.next_node)
            temp_node.next_node.prev_node = node
            temp_node.next_node = node
            self.length += 1
        return value

    def pre_delete(self):
        if self.length == 0:
            raise print("The length is less than 1")
        else:
            value = self.head.value
            self.head = self.head.next_node
            if self.head is not None:
                self.head.prev_node = None
            self.length -= 1
            return value

    def behind_delete(self):
        if self.length == 0:
            raise print("The length is less than 1")
        else:
            value = self.tail.value
            self.tail = self.tail.prev_node
            if self.tail is not None:
                self.tail.next_node = None
            self.length -= 1
            return value

    def delete(self, index):
        if index <= 0:
            self.pre_delete()
        elif index >= self.length:
            self.behind_delete()
        else:
            temp_node = self.head
            while index > 0:
                temp_node = temp_node.next_node
                index -= 1
            value = temp_node.value
            if temp_node.next_node is not None:
                temp_node.prev_node.next_node = temp_node.next_node
                temp_node.next_node.prev_node = temp_node.prev_node
            else:
                temp_node.prev_node.next_node = None
            self.length -= 1
            return value

    def search(self, value):
        temp_node = self.head
        while temp_node is not None and temp_node.value != value:
            temp_node = temp_node.next_node
        if temp_node is None:
            return False
        else:
            return True


class LinkedListNil(object):
    """带哨兵的双链表"""
    class Node(object):
        def __init__(self, value, prev_node, next_node):
            super(LinkedListNil.Node, self).__init__()
            self.value = value
            self.prev_node = prev_node
            self.next_node = next_node

        def __str__(self):
            super(LinkedListNil.Node, self).__str__()
            return str(self.value)

    def __init__(self, *arg):
        self.nil = self.Node(None, None, None)
        self.nil.prev_node = self.nil
        self.nil.next_node = self.nil
        self.length = 0
        for i in arg:
            self.append(i)

    def __str__(self):
        list_ = []
        temp_node = self.nil.next_node
        while temp_node is not self.nil:
            list_.append(temp_node.value)
            temp_node = temp_node.next_node
        return str(list_)

    def prepend(self, value):
        temp_node = self.nil.next_node
        node = self.Node(value, self.nil, temp_node)
        temp_node.prev_node = node
        self.nil.next_node = node
        self.length += 1
        return value

    def append(self, value):
        temp_node = self.nil.prev_node
        node = self.Node(value, temp_node, self.nil)
        temp_node.next_node = node
        self.nil.prev_node = node
        self.length += 1
        return value

    def insert(self, index, value):
        if index <= 0:
            self.prepend(value)
        elif index >= self.length:
            self.append(value)
        else:
            temp_node = self.nil
            while index > 0:
                temp_node = temp_node.next_node
                index -= 1
            node = self.Node(value, temp_node, temp_node.next_node)
            temp_node.next_node.prev_node = node
            temp_node.next_node = node
            self.length += 1
        return value

    def pre_delete(self):
        if self.length == 0:
            raise print("The length is less than 1")
        else:
            temp_node = self.nil.next_node
            value = temp_node.value
            temp_node.next_node.prev_node = self.nil
            self.nil.next_node = temp_node.next_node
            self.length -= 1
            return value

    def behind_delete(self):
        if self.length == 0:
            raise print("The length is less than 1")
        else:
            temp_node = self.nil.prev_node
            value = temp_node.value
            self.nil.prev_node = temp_node.prev_node
            temp_node.prev_node.next_node = self.nil
            self.length -= 1
            return value

    def delete(self, index):
        if index <= 0:
            self.pre_delete()
        elif index >= self.length:
            self.behind_delete()
        else:
            temp_node = self.nil.next_node
            while index > 0:
                temp_node = temp_node.next_node
                index -= 1
            value = temp_node.value
            temp_node.prev_node.next_node = temp_node.next_node
            temp_node.next_node.prev_node = temp_node.prev_node
            self.length -= 1
            return value

    def search(self, value):
        temp_node = self.nil.next_node
        while temp_node is not self.nil and temp_node.value != value:
            temp_node = temp_node.next_node
        if temp_node is self.nil:
            return False
        else:
            return True


def main():
    li = LinkedList(1, 2, 3)
    print("The value in li is:", str(li))
    li.prepend(4)
    print("After prepend, the value in li is:", str(li))
    li.append(5)
    print("After append, the value in li is:", str(li))
    li.insert(4, 6)
    print("After insert, the value in li is:", str(li))
    li.pre_delete()
    print("After pre delete, the value in li is:", str(li))
    li.behind_delete()
    print("After behind delete, the value in li is:", str(li))
    li.delete(3)
    print("After delete, the value in li is:", str(li))
    index = 3
    print("Is {} in li?".format(index), li.search(index))

    li = LinkedListNil(1, 2, 3)
    print("The value in li is:", str(li))
    li.prepend(4)
    print("After prepend, the value in li is:", str(li))
    li.append(5)
    print("After append, the value in li is:", str(li))
    li.insert(4, 6)
    print("After insert, the value in li is:", str(li))
    li.pre_delete()
    print("After pre delete, the value in li is:", str(li))
    li.behind_delete()
    print("After behind delete, the value in li is:", str(li))
    li.delete(3)
    print("After delete, the value in li is:", str(li))
    index = 3
    print("Is {} in li?".format(index), li.search(index))


if __name__ == '__main__':
    main()