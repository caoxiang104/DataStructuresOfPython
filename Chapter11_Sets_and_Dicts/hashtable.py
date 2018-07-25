from Chapter4_Arrays_and_Linked_Structures.arrays import Array


class HashTable(object):
    """Represents a hash table."""

    EMPTY = None
    DELETE = True

    def __init__(self, capacity=29, hashFunction=hash, linear=True):
        self._size = 0
        self._capacity = capacity
        self._table = Array(self._capacity, HashTable.EMPTY)
        self._hash = hashFunction
        self._homeIndex = -1
        self._actualIndex = -1
        self._linear = linear
        self._probeCount = 0

    def insert(self, item):
        """Insert item into the table
        Precondition: There is at least one empty cell or one previously occupied cell.
        There is not a duplicate item."""
        self._probeCount = 0
        # Get the home index
        self._homeIndex = abs(self._hash(item)) % len(self._table)
        distance = 1
        index = self._homeIndex

        # Stop searching when an empty cell is encountered
        while self._table[index] not in (HashTable.EMPTY, HashTable.DELETE):
            if self._linear:
                increment = index + 1
            else:
                # Quadratic probing
                increment = self._homeIndex + distance ** 2
                distance += 1
            index = increment % len(self._table)
            self._probeCount += 1

        # An empty cell is found, so store the item.
        self._table[index] = item
        self._size += 1
        self._actualIndex = index

    def loadFactor(self):
        return self._size / self._capacity

    def __len__(self):
        return self._size

    def homeIndex(self):
        return self._homeIndex

    def actualIndex(self):
        return self._actualIndex

    def probeCount(self):
        return self._probeCount

    def __str__(self):
        return str(self._table)