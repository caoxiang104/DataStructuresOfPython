from Chapter6_Inheritance_and_Abstract_Classes.abstractcollection import AbstractionCollection


class AbstractStack(AbstractionCollection):
    """An abstract stack implemention."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        AbstractionCollection.__init__(self, sourceCollection)

    def add(self, item):
        """Adds item to self."""
        self.push(item)