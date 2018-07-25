from Chapter5_Interfaces_Implementations_and_Polymorphism.arraybag import ArrayBag
from Chapter11_Sets_and_Dicts.abstractset import AbstractSet


class ArraySet(AbstractSet, ArrayBag):
    """An array-based implementation of a set."""

    def __init__(self, sourceCollection=None):
        ArrayBag.__init__(self, sourceCollection)

    def add(self, item):
        """Add item to the set if it is not in the set."""
        if item not in self:
            ArrayBag.add(self, item)