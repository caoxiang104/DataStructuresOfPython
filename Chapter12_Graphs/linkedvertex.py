from Chapter12_Graphs.linkededge import LinkedEdge


class LinkedVertex(object):

    def __init__(self, label):
        self._label = label
        self._edgeList = list()
        self._mark = False

    def setLable(self, label, g):
        """Set the vertex's label to label."""
        g._vertexs.pop(self._label, None)
        g._vertexs[label] = self
        self._label = label

    def clearMark(self):
        self._mark = False

    def setMark(self):
        self._mark = True

    def isMark(self):
        return self._mark

    def getLabel(self):
        return self._label

    def addEdgeTo(self, toVertex, weight=None):
        self._edgeList.append(LinkedEdge(self, toVertex, weight))

    def getEdgeTo(self, toVertex):
        edge = LinkedEdge(self, toVertex)
        if edge in self._edgeList:
            return edge
        else:
            return None

    def neighboringVertices(self):
        """Returns the neighboring vertices of this vertex."""
        vertices = list()
        for edge in self._edgeList:
            vertices.append(edge.getOtherVertex(self))
        return iter(vertices)

    def removeEdgeTo(self, toVertex):
        """Returns True if the edge exists and is removed, or False otherwise."""
        edged = LinkedEdge(self, toVertex)
        for edge in self._edgeList:
            if edge._vertex1 == edged._vertex1 and edge._vertex2 == edged._vertex2:
                self._edgeList.remove(edge)
                return True

        return False

    def incidentEdges(self):
        edges = list()
        for edge in self._edgeList:
            if edge._vertex1 == self:
                edges.append(edge)
        return iter(edges)

    def __str__(self):
        return str(self._label)

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        return self._label == other._label