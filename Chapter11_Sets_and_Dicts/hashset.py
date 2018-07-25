from Chapter4_Arrays_and_Linked_Structures.arrays import Array
from Chapter11_Sets_and_Dicts.abstractdict import AbstractDict, AbstractionCollection


class Node(object):
    def __init__(self, value, next_node):
        self.data = value
        self.next = next_node

    def __str__(self):
        return str(self.data)


class HashSet(AbstractDict, AbstractionCollection):
    """A hashing implementation of a set."""

    DEFAULT_CAPACITY = 3

    def __init__(self, sourceCollection=None, capacity=None):
        if capacity is None:
            self._capacity = HashSet.DEFAULT_CAPACITY
        else:
            self._capacity = capacity
        self._items = Array(self._capacity)
        self._foundNode = self._priorNode = None
        self._index = -1
        AbstractionCollection.__init__(self, sourceCollection)

    def __contains__(self, item):
        """Returns True if item is in the set or False otherwise."""
        self._index = abs(hash(item)) % len(self._items)
        self._priorNode = None
        self._foundNode = self._items[self._index]
        while self._foundNode is not None:
            if self._foundNode.data == item:
                return True
            else:
                self._priorNode = self._foundNode
                self._foundNode = self._foundNode.next
        return False

    def __iter__(self):
        """Supposes iteration over a view of self."""
        cursor = 0
        while cursor < self._capacity:
            if self._items[cursor] is not None:
                temp_node = self._items[cursor]
                while temp_node is not None:
                    yield temp_node.data
                    temp_node = temp_node.next
            cursor += 1

    def __str__(self):
        """Returns the string representation of self."""
        return "[" + ", ".join(map(str, self)) + "]"

    def clear(self):
        """Make self become empty."""
        self._size = 0
        self._items = Array(self._capacity)

    def add(self, item):
        """Add item to the set if it is not in the set."""
        if item not in self:
            newNode = Node(item, self._items[self._index])
            self._items[self._index] = newNode
            self._size += 1

    def remove(self, item):
        """Precondition: item is not in self.
        Raises: KeyError if item is not in self.
        PostCondition: item is removed from self."""
        if item in self:
            if self._priorNode is None:
                self._items[self._index] = self._foundNode.next
            else:
                self._priorNode.next = self._foundNode.next
            self._size -= 1
            return self._foundNode.data
        else:
            raise KeyError(str(item) + "is not in self.")


def main():
    hashset = HashSet(capacity=5)
    for i in range(8):
        hashset.add(i)
    print(hashset)
    hashset.remove(6)
    print(hashset)


if __name__ == '__main__':
    main()