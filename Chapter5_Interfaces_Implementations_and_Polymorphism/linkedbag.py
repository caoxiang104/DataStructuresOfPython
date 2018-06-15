class Node(object):
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node

    def __str__(self):
        return self.value


class LinkedBag(object):
    """A lined-based bag implementation."""
    def __init__(self, source_collection=None):
        """Sets the initial state of self, which includes the
                contents of source collection, if it's present."""
        self._items = None
        self._size = 0
        if source_collection:
            for item in source_collection:
                self.add(item)

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._items
        while cursor is not None:
            yield cursor.value
            cursor = cursor.next

    def __len__(self):
        return self._size

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

    def add(self, item):
        """Adds item to self."""
        self._items = Node(item, self._items)
        self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: keyError if item is not in self.
        Post condition: item is remove from self."""
        if item not in self:
            raise KeyError(str(item) + "not in bag.")
        probe = self._items
        trailer = None
        for target_item in self:
            if target_item == item:
                break
            trailer = probe
            probe = probe.next
        if probe == self._items:
            self._items = self._items.next
        else:
            trailer.next = probe.next
        self._size -= 1


def main():
    lis1 = LinkedBag([1, 2, 3])
    lis2 = LinkedBag([1, 2])
    print(lis1 == lis2)


if __name__ == '__main__':
    main()