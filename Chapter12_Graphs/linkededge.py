class LinkedEdge(object):

    def __init__(self, fromVertex, toVertex, weight=None):
        self._vertex1 = fromVertex
        self._vertex2 = toVertex
        self._weight = weight
        self._mark = False

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        return self._vertex1 == other._vertex1 and \
               self._vertex2 == other._vertex2 and \
            self._weight == other._weight

    def clearMark(self):
        self._mark = False

    def setMark(self):
        self._mark = True

    def isMark(self):
        return self._mark

    def getWight(self):
        return self._weight

    def setWeight(self, weight):
        self._weight = weight

    def getOtherVertex(self, vertex):
        if vertex is self._vertex1:
            return self._vertex2
        else:
            return self._vertex1

    def getToVertex(self):
        return self._vertex2

    def __str__(self):
        return str(self._vertex1) + ">" + str(self._vertex2) + ":" + str(self._weight)