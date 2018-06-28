from Chapter9_Lists.abstractlist import AbstractList
from Chapter4_Arrays_and_Linked_Structures.arrays import Array
from Chapter9_Lists.arraylistiterator import ArrayListIterator


class ArraySortedList(AbstractList):

    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = Array(ArraySortedList.DEFAULT_CAPACITY)
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

    def __contains__(self, value):
        """Returns True if value is in self, or False otherwise."""
        left = 0
        right = len(self) - 1
        while left <= right:
            mid = (left + right) // 2
            if self._items[mid] == value:
                return True
            elif self._items[mid] > value:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArraySortedList.DEFAULT_CAPACITY)

    def index(self, value):
        """Precondition: item is in the list.
        Returns the position of item.
        Raises: ValueError if the item is not in the list."""
        left = 0
        right = len(self) - 1
        if value > self._items[right] or value < self._items[left]:
            raise ValueError(str(value) + "not in list.")
        mid = (left + right) // 2
        while left <= right:
            if self._items[mid] == value:
                return mid
            elif self._items[mid] < value:
                left = mid + 1
            else:
                right = mid - 1
        raise ValueError(str(value) + "not in list.")

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

    def add(self, value):
        """Adds the item to the end of the list."""
        if value <= self._items[0]:
            self.insert(0, value)
        elif value >= self._items[len(self) - 1]:
            self.insert(len(self), value)
        else:
            for index in range(1, len(self) - 1):
                if self._items[index] > value:
                    self.insert(index, value)
                    break

    def listIterator(self):
        """Returns a list iterator."""
        return ArrayListIterator(self)

