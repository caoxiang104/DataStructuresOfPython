from Chapter4_Arrays_and_Linked_Structures.arrays import Array
from Chapter7_Stacks.abstractstack import AbstractStack


class ArrayStack(AbstractStack):
    """An array-based stack implementation."""
    DEFAULT_CAPACITY = 10  # for all array stack.

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
                contents of sourceCollection, if it's present."""
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(self, sourceCollection)

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def peek(self):
        """Returns the item at top of the stack.
        Precondition: the stack is not empty.
        Raise KeyError if the stack is empty."""
        if self.isEmpty():
            raise KeyError
        else:
            return self._items[len(self) - 1]

    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)

    def push(self, item):
        """Inserts item at top of the stack."""
        # Resize array here if necessary.
        if len(self) == ArrayStack.DEFAULT_CAPACITY:
            temp = Array(ArrayStack.DEFAULT_CAPACITY + 1)
            for i in range(ArrayStack.DEFAULT_CAPACITY):
                temp[i] = self._items[i]
            self._items = temp
            ArrayStack.DEFAULT_CAPACITY += 1
        self._items[len(self)] = item
        self._size += 1

    def pop(self):
        """Removes and returns the item at top of the stack.
        Precondition: the stack is not empty.
        Postcondition: the top item is removed from the stack."""
        if self.isEmpty():
            raise KeyError
        else:
            oldItem = self._items[len(self) - 1]
            self._size -= 1
            # Resize the array if necessary.
            return oldItem



