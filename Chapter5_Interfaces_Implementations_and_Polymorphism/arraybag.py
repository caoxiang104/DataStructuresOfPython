from Chapter4_Arrays_and_Linked_Structures.exercise4_3.arrays import Array


class ArrayBag(object):
    """An array-based bag implementation."""

    DEFAULT_CAPACITY = 10

    def __init__(self, source_collection=None):
        """Sets the initial state of self, which includes the
        contents of source collection, if it's present."""
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        self._size = 0
        if source_collection:
            for item in source_collection:
                self.add(item)

    def is_empty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0

    def __len__(self):
        """Return the number of items in self."""
        return self._size

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __str__(self):
        """Return string representation of self."""
        return '{' + ", ".join(map(str, self)) + '}'

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other, or False otherwise."""
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if item not in other:
                return False
        return True

    def remove(self, item):
        """Precondition: item is in self.
        Raises: keyError if item is not in self.
        Post condition: item is remove from self."""
        if item not in self:
            raise KeyError(str(item) + "not in bag.")
        target_index = 0
        for target_item in self:
            if target_item == item:
                break
            target_index += 1
        for i in range(target_index, len(self) - 1):
            self._items[i] = self._items[i + 1]
        self._size -= 1

    def clear(self):
        """Make self become empty."""
        self._size = 0
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)

    def add(self, item):
        """Add item to self."""
        self._items[len(self)] = item
        self._size += 1
