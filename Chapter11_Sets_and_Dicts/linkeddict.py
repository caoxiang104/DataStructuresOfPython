from Chapter11_Sets_and_Dicts.abstractdict import AbstractDict
from Chapter11_Sets_and_Dicts.item import Item


class Node(object):

    def __init__(self, value, prev_node, next_node):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    def __str__(self):
        return str(self.value)


class LinkedDict(AbstractDict):
    """A link-based dict implementation."""

    def __init__(self, sourceCollection=None):
        """Will copy items to the collection from sourceCollection if it's present."""
        self.nil = Node(None, None, None)
        self.nil.next_node = self.nil.prev_node = self.nil
        AbstractDict.__init__(self, sourceCollection)

    def __iter__(self):
        """Serves up the keys in the dictionary."""
        node = self.nil.next_node
        while node.next_node is not self.nil:
            yield node.data.key
            node = node.next_node

    def __getitem__(self, key):
        """Precondition: the key is in the dictionary.
        Raise: a KeyError if the key is not in the dictionary.
        Returns the value associated with the key."""
        node = self.nil.next_node
        while node is not self.nil:
            if node.data.key == key:
                return node.data.value
            else:
                node = node.next_node
        raise KeyError("Missing:" + str(key))

    def __setitem__(self, key, value):
        """If the key is not in the dictionary, adds the key and value to it.
        Otherwise, replace the old value with the new value."""
        node = self.nil.next_node
        while node is not self.nil:
            if node.data.key == key:
                node.data.value = value
                break
            else:
                node = node.next_node
        if node is self.nil:
            self._size += 1
            node = Node(Item(key, value), self.nil.prev_node, self.nil)
            self.nil.prev_node.next_node = node
            self.nil.prev_node = node

    def pop(self, key):
        """Precondition: the key is in the dictionary.
        Raise: a KeyError if the key is not in the dictionary.
        Removes the key and returns the value and associated value
        if the key is in the dictionary, or returns the default value otherwise."""
        node = self.nil.next_node
        while node is not self.nil:
            if node.data.key == key:
                node.prev_node.next_node = node.next_node
                node.next_node.prev_node = node.prev_node
                self._size -= 1
                return node.data.value
            else:
                node = node.next_node
        raise KeyError("Missing:" + str(key))

