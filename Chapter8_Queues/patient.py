class Patient(object):

    def __init__(self, name, condition):
        self._name = name
        self._condition = condition

    def __ge__(self, other):
        """Used for comparision."""
        return self._condition >= other._condition

    def __str__(self):
        return self._name + "/" + str(self._condition)
