from Chapter6_Inheritance_and_Abstract_Classes.abstractcollection import AbstractionCollection


class AbstractList(AbstractionCollection):
    """A abstract list implementation."""

    def __init__(self, sourceCollection=None):
        """Maintains a count of modifications to the list."""
        self._modCount = 0
        AbstractionCollection.__init__(self, sourceCollection)

    def getModCount(self):
        """Returns the count of modifications to the list."""
        return self._modCount

    def incModCount(self):
        """Increments the count of modifications."""
        self._modCount += 1

    def index(self, item):
        """Precondition: item is in the list.
        Returns the position of item.
        Raises: ValueError if the item is not in the list."""
        position = 0
        for data in self:
            if data == item:
                return position
            else:
                position += 1
        if position == len(self):
            raise ValueError(str(item) + "not in list.")

    def add(self, item):
        """Adds the item to the end of the list."""
        self.insert(len(self), item)

    def remove(self, item):
        """Precondition: item is in the list.
        Raises: ValueError if the item is not in the list.
        Postcondition: item is remove from self."""
        position = self.index(item)
        self.pop(position)