from Chapter6_Inheritance_and_Abstract_Classes.abstractcollection import AbstractionCollection
from Chapter4_Arrays_and_Linked_Structures.arrays import Array


class ArrayQueue(AbstractionCollection):
    """array-based queue implementation."""

    DEFAULT_CAPACITY = 10  # for all array queue.

    def __init__(self, sourceCollection=None):
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)
        self._front = -1
        self._rear = -1
        AbstractionCollection.__init__(self, sourceCollection)

    def add(self, item):
        """Adds item to the rear of the queue."""
        if self.isEmpty():
            self._front = 0
        if len(self) == ArrayQueue.DEFAULT_CAPACITY:
            temp = Array(ArrayQueue.DEFAULT_CAPACITY + 1)
            if self._rear > self._front:
                for i in range(ArrayQueue.DEFAULT_CAPACITY):
                    temp[i] = self._items[i]
                self._items = temp
            else:
                for i in range(self._front, ArrayQueue.DEFAULT_CAPACITY):
                    temp[i - self._front] = self._items[i]
                for i in range(self._rear + 1):
                    temp[ArrayQueue.DEFAULT_CAPACITY - self._front + i] = self._items[i]
                self._items = temp
            self._front = 0
            self._rear = ArrayQueue.DEFAULT_CAPACITY - 1
            ArrayQueue.DEFAULT_CAPACITY += 1
        if self._rear == ArrayQueue.DEFAULT_CAPACITY - 1:
            self._rear = -1
        self._items[self._rear + 1] = item
        self._rear += 1
        self._size += 1

    def pop(self):
        """Removes and returns the item at top of the queue.
        Precondition: the queue is not empty."""
        if self.isEmpty():
            raise KeyError("The queue is empty")
        oldItem = self._items[self._front]
        if self._front == ArrayQueue.DEFAULT_CAPACITY - 1:
            self._front = 0
        else:
            self._front += 1
        self._size -= 1
        return oldItem

    def __iter__(self):
        """Supports iteration over a view of self."""
        if self._rear >= self._front:
            cursor = 0
            while cursor < len(self):
                yield self._items[cursor]
                cursor += 1
        else:
            for i in range(self._front, ArrayQueue.DEFAULT_CAPACITY):
                yield self._items[i]
            for i in range(self._rear + 1):
                yield self._items[i]

    def clear(self):
        """Makes self become empty."""
        self._front = -1
        self._rear = -1
        self._size = 0
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)