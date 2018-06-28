from Chapter9_Lists.abstractlist import AbstractList


class Node(object):
    def __init__(self, value, prev_node, next_node):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    def __str__(self):
        return str(self.value)


class LinkedList(AbstractList):
    """A link-based list implementation."""

    def __init__(self, sourceCollection=None):
        """Set the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        # Uses a circular structure with a sentinel node
        self._head = Node(None, None, None)
        self._head.prev_node = self._head.next_node = self._head
        AbstractList.__init__(self, sourceCollection)

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._head.next_node
        while cursor != self._head:
            yield cursor.value
            cursor = cursor.next_node

    def _getNode(self, key):
        """Helper method: returns a pointer to the node at position key."""
        if key == len(self):
            return self._head
        elif key == len(self) - 1:
            return self._head.prev_node
        probe = self._head.next_node
        while key > 0:
            probe = probe.next_node
            key -= 1
        return probe

    def __setitem__(self, key, value):
        """Precondition: 0 <= key <= len(self)
        Replaces the value at position key.
        Raises: IndexError."""
        if key < 0 or key >= len(self):
            raise IndexError("List index out of range.")
        self._getNode(key).value = value

    def insert(self, key, value):
        """Inserts the value at position key."""
        if key < 0: key = 0
        elif key > len(self): key = len(self)
        theNode = self._getNode(key)
        newNode = Node(value, theNode.prev_node, theNode)
        theNode.prev_node.next_node = newNode
        theNode.prev_node =newNode
        self._size += 1
        self.incModCount()

    def pop(self, key=None):
        """Precondition: 0 <= key <= len(self)
        Removes and returns the value at position key.
        if key is None, key is given a default of len(self) - 1.
        Raises: IndexError."""
        if key < 0 or key >= len(self):
            raise IndexError("List index out of range.")
        if key is None:
            probe = self._head.prev_node
            probe.prev_node.next_node = self._head
            self._head.prev_node = probe.prev_node
        else:
            probe = self._head.next_node
            while key > 0:
                probe = probe.next_node
                key -= 1
            probe.prev_node.next_node = probe.next_node
            probe.next_node.prev_node = probe.prev_node
        value = probe.value
        self._size -= 1
        self.incModCount()
        return value






