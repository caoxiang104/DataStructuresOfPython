class AbstractSet(object):
    """Generic set method implementation."""

    def __or__(self, other):
        """Returns the union of self or other."""
        return self + other

    def __and__(self, other):
        """Returns the intersection of self and other."""
        intersection = type(self)()
        for item in self:
            if item in other:
                intersection.add(item)
        return intersection

    def __sub__(self, other):
        """Returns the difference of self and other."""
        difference = type(self)()
        for item in self:
            if item not in other:
                difference.add(item)
        return difference

    def issubset(self, other):
        """Returns True if self is a subset of other or False otherwise."""
        for item in self:
            if item not in other:
                return False
        return True

