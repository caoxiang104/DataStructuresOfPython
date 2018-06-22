from Chapter5_Interfaces_Implementations_and_Polymorphism.arraybag import ArrayBag


class ArraySortedBag(ArrayBag):
    """An array-based sorted bag implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        ArrayBag.__init__(self, sourceCollection)

    # Accessor methods
    def __contains__(self, item):
        """Returns True if item is in self, or False otherwise."""
        left = 0
        right = len(self) - 1
        while left <= right:
            midPoint = (left+right) // 2
            if self._items[midPoint] == item:
                return True
            elif self._items[midPoint] > item:
                right = midPoint - 1
            else:
                left = midPoint + 1
        return False

    def add(self, item):
        """Adds item to self."""
        # Empty or last item, call ArrayBag.add
        if self.is_empty() or item >= self._items[len(self) - 1]:
            ArrayBag.add(self, item)
        else:
            # Resize the array if it is full
            if self._size == len(self._items):
                self._items.grow()
            # Search for the first item >= new item
            targetIndex = 0
            while item > self._items[targetIndex]:
                targetIndex += 1
            # Open a hole for new item
            for i in range(len(self), targetIndex, -1):
                self._items[i] = self._items[i-1]
            # Insert item and update size
            self._items[targetIndex] = item
            self._size += 1

    def __eq__(self, other):
        """Returns True if the two bags are equal to each other."""
        if self is other:
            return True
        if type(self) != type(other):
            return False
        if len(self) != len(other):
            return False
        # index = 0
        # while index < len(self):
        #     if self._items[index] != other._items[index]:
        #         return False
        #     index += 1
        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True