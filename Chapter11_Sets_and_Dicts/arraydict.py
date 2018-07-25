from Chapter11_Sets_and_Dicts.abstractdict import AbstractDict
from Chapter11_Sets_and_Dicts.item import Item


class ArrayDict(AbstractDict):
    """Represents an array-based dictionary."""

    def __init__(self, sourceCollection=None):
        """Will copy items to the collection from sourceCollection if it's present."""
        self._items = list()
        AbstractDict.__init__(self, sourceCollection)

    def __iter__(self):
        """Serves up the keys in the dictionary."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __getitem__(self, key):
        """Precondition: the key is in the dictionary.
        Raise: a KeyError if the key is not in the dictionary.
        Returns the value associated with the key."""
        index = self._index(key)
        if index == -1:
            raise KeyError("Missing: " + str(key))
        return self._items[key].value

    def __setitem__(self, key, value):
        """If the key is not in the dictionary, adds the key and value to it.
        Otherwise, replace the old value with the new value."""
        index = self._index(key)
        if index == -1:
            self._items.append(Item(key, value))
            self._size += 1
        else:
            self._items[index].value = value

    def pop(self, key):
        """Precondition: the key is in the dictionary.
        Raise: a KeyError if the key is not in the dictionary.
        Removes the key and returns the value and associated value
        if the key is in the dictionary, or returns the default value otherwise."""
        index = self._index(key)
        if index == -1:
            raise KeyError("Missing:" + str(key))
        self._size -= 1
        return self._items.pop(index).value

    def _index(self, key):
        """Helper method for key search."""
        index = 0
        for entry in self._items:
            if entry.key == key:
                return index
            index += 1
        return -1