# coding=utf-8
"""
编写一段代码，将一个填满数组中的项，转移到一个单链表结构中。
这个操作应该保留这些项的顺序不变。
"""
from Chapter4_Arrays_and_Linked_Structures.exercise4_3.arrays import Array


class Node(object):
    def __init__(self, data, next_=None):
        """Instantiates a Node with a default next of None."""
        self._data = data
        self._next = next_


def main():
    array = Array(10)
    for i in range(array.capacity):
        array[i] = i + 1
    head = None
    for i in range(array.logical_size - 1, -1, -1):
        head = Node(array[i], head)
    while head != None:
        print(head._data)
        head = head._next


if __name__ == '__main__':
    main()