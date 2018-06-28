from Chapter4_Arrays_and_Linked_Structures.arrays import Array
from Chapter9_Lists.abstractlist import AbstractList
from Chapter9_Lists.arraylistiterator import ArrayListIterator


class ArrayList(AbstractList):
    """An array-based list implementation."""

    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = Array(ArrayList.DEFAULT_CAPACITY)
        AbstractList.__init__(self, sourceCollection)

    def __iter__(self):
        """Supposes iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __getitem__(self, key):
        """Precondition: 0 <= key <= len(self)
        Returns the item at position key.
        Raises: IndexError."""
        if key < 0 or key >= len(self):
            raise IndexError("List index out of range.")
        return self._items[key]

    def __setitem__(self, key, value):
        """Precondition: 0 <= key <= len(self)
        Replaces the value at position key.
        Raises: IndexError."""
        if key < 0 or key >= len(self):
            raise IndexError("List index out of range.")
        self._items[key] = value

    def insert(self, key, value):
        """Insert the value at position key."""
        # Resize array here if necessary.
        if key < 0: key = 0
        elif key > len(self): key = len(self)
        if key < len(self):
            for j in range(len(self), key, -1):
                self._items[j] = self._items[j - 1]
        self._items[key] = value
        self._size += 1
        self.incModCount()

    def pop(self, key=None):
        """Precondition: 0 <= key <= len(self)
        Removes and returns the value at position key.
        if key is None, key is given a default of len(self) - 1.
        Raises: IndexError."""
        if key is None: key = len(self) - 1
        if key < 0 or key >= len(self):
            raise IndexError("List index out of range.")
        value = self._items[key]
        for j in range(key, len(self) - 1):
            self._items[j] = self._items[j + 1]
        self._size -= 1
        self.incModCount()
        # Resize array here if necessary.
        return value

    def listIterator(self):
        """Returns a list iterator."""
        return ArrayListIterator(self)