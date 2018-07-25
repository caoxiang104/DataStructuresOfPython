from Chapter6_Inheritance_and_Abstract_Classes.abstractcollection import AbstractionCollection
from Chapter11_Sets_and_Dicts.item import Item


class AbstractDict(AbstractionCollection):
    """Common data and method implementation."""

    def __init__(self, sourceCollection=None):
        """Will copy item to the collection from sourceCollection if it's present."""
        AbstractionCollection.__init__(self)
        if sourceCollection:
            for key, value in sourceCollection:
                self[key] = value

    def __str__(self):
        return "{" + ", ".join(map(str, self.items())) + "}"

    def __add__(self, other):
        """Returns a new dictionary containing the contents of self and other."""
        result = type(self)(map(lambda item: (item.key, item.value), self.items()))
        for key in other:
            result[key] = other[key]
        return result

    def __eq__(self, other):
        """Returns True if self equals other, or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for key in self:
            if key not in other:
                return False
        return True

    def keys(self):
        """Returns a iterator on the keys in the dictionary."""
        return iter(self)

    def values(self):
        """Returns a iterator on the values in the dictionary."""
        return iter(map(lambda key: self[key], self))

    def items(self):
        """Returns a iterator on the items in the dictionary."""
        return iter(map(lambda key: Item(key, self[key]), self))
