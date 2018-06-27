from Chapter8_Queues.linkedpriorityqueue import LinkedPriorityQueue
from Chapter8_Queues.linkedqueue import LinkedQueue


class Node(object):
    def __init__(self, value, next_node):
        self.data = value
        self.next = next_node

    def __str__(self):
        return self.data


class ERModel(LinkedQueue):

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        LinkedQueue.__init__(self, sourceCollection)

    def schedule(self, patient):
        """Inserts item after items of greater or equal
                priority or ahead of items of lesser priority.
                if self.isEmpty() or item >= self._rear.data."""
        if self.isEmpty() or patient._condition >= self._rear.data._condition:
            # Item goes at rear
            LinkedQueue.add(self, patient)
        else:
            # Search for a position where it's less
            probe = self._front
            while patient._condition >= probe.data._condition:
                trailer = probe
                probe = probe.next
            newNode = Node(patient, probe)
            if probe == self._front:
                # Item goes at front
                self._front = newNode
            else:
                # Item goes between two nodes
                trailer.next = newNode
            self._size += 1

    def treatNext(self):
        return self.pop()