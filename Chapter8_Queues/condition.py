class Condition(object):

    def __init__(self, rank):
        self._rank = rank

    def __ge__(self, other):
        """Used for comparision."""
        return self._rank >= other._rank

    def __str__(self):
        if self._rank == 1:
            return "critical"
        elif self._rank == 2:
            return "serious"
        else:
            return "fair"
