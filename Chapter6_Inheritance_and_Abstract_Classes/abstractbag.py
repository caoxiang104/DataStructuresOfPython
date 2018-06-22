from Chapter6_Inheritance_and_Abstract_Classes.abstractcollection import AbstractionCollection


class AbstractBag(AbstractionCollection):
    """An abstract bag implementation."""

    def __init__(self, soureCollection=None):
        """Sets the initial state of self, which includes the
                contents of sourceCollection, if it's present."""
        AbstractionCollection.__init__(self, soureCollection)

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True
