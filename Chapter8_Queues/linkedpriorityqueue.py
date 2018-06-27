from Chapter8_Queues.linkedqueue import LinkedQueue


class Node(object):
    def __init__(self, value, next_node):
        self.data = value
        self.next = next_node

    def __str__(self):
        return self.data


class LinkedPriorityQueue(LinkedQueue):
    """A link-based priority queue implement."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        LinkedQueue.__init__(self, sourceCollection)

    def add(self, item):
        """Inserts item after items of greater or equal
        priority or ahead of items of lesser priority.
        if self.isEmpty() or item >= self._rear.data."""
        if self.isEmpty() or item >= self._rear.data:
            # Item goes at rear
            LinkedQueue.add(self, item)
        else:
            # Search for a position where it's less
            probe = self._front
            while item >= probe.data:
                trailer = probe
                probe = probe.next
            newNode = Node(item, probe)
            if probe == self._front:
                # Item goes at front
                self._front = newNode
            else:
                # Item goes between two nodes
                trailer.next = newNode
            self._size += 1