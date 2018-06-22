from Chapter7_Stacks.abstractstack import AbstractStack


class Node(object):
    def __init__(self, value, next_node):
        self.data = value
        self.next = next_node

    def __str__(self):
        return self.data


class LinkedStack(AbstractStack):
    """Link-based stack implementation."""

    def __init__(self, soureCollection=None):
        self._items = None
        AbstractStack.__init__(self, soureCollection)

    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""
        def visitNode(node):
            if node is not None:
                visitNode(node.next)
                tempList.append(node.data)
        tempList = list()
        visitNode(self._items)
        return iter(tempList)

    def peek(self):
        """Returns the item at top of the stack.
                Precondition: the stack is not empty."""
        if self.isEmpty():
            raise KeyError("The stack is empty.")
        return self._items.data

    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = None

    def push(self, item):
        """Inserts item at top of the stack."""
        self._items = Node(item, self._items)
        self._size += 1

    def pop(self):
        """Removes and returns the item at top of the stack.
        Precondition: the stack is not empty."""
        if self.isEmpty():
            raise KeyError("The stack is empty.")
        oldItem = self._items.data
        self._items = self._items.next
        self._size -= 1
        return oldItem



