from Chapter6_Inheritance_and_Abstract_Classes.abstractcollection import AbstractionCollection


class Node(object):
    def __init__(self, value, next_node):
        self.data = value
        self.next = next_node

    def __str__(self):
        return self.data


class LinkedQueue(AbstractionCollection):
    """Link-based queue implementation."""

    def __init__(self, sourceCollection=None):
        self._front = None
        self._rear = None
        AbstractionCollection.__init__(self, sourceCollection)

    def add(self, item):
        """Adds item to the rear of the queue."""
        node = Node(item, None)
        if self.isEmpty():
            self._front = node
        else:
            self._rear.next = node
        self._rear = node
        self._size += 1

    def pop(self):
        """Removes and returns the item at top of the queue.
        Precondition: the queue is not empty."""
        if self.isEmpty():
            raise KeyError("The queue is empty")
        oldItem = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return oldItem

    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from top to bottom of queue."""
        def visitNode(node):
            if node is not None:
                tempList.append(node.data)
                visitNode(node.next)
        tempList = list()
        visitNode(self._front)
        return iter(tempList)

    def clear(self):
        """Makes self become empty."""
        self._front = None
        self._rear = None
        self._size = 0