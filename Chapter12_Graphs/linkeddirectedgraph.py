from Chapter12_Graphs.linkededge import LinkedEdge
from Chapter12_Graphs.linkedvertex import LinkedVertex
from Chapter6_Inheritance_and_Abstract_Classes.abstractcollection import AbstractionCollection
from Chapter4_Arrays_and_Linked_Structures.arrays import Array


class Node(object):
    def __init__(self, data, label, next_node):
        self.data = data
        self.label = label
        self.next = next_node


class LinkedDirectedGraph(AbstractionCollection):

    def __init__(self, sourceCollection=None):
        """Adds a vertex with the given label to the graph."""
        self._edgeCount = 0
        self._vertices = dict()
        AbstractionCollection.__init__(self, sourceCollection)

    def addVertex(self, label):
        self._vertices[label] = LinkedVertex(label)
        self._size += 1

    def removeVertex(self, label):
        """Returns True if the vertex is removed, or False otherwise."""
        removedVertex = self._vertices.pop(label, None)
        if removedVertex is None:
            return False

        # Examine all other vertices to remove edges directed at the removed vertex
        for vertex in self.vertices():
            if vertex.removeEdgeTo(removedVertex):
                self._edgeCount -= 1

        # Examine all edges from the removed vertex to others
        for edge in removedVertex.incidentEdges():
            self._edgeCount -= 1
        self._size -= 1
        return True

    def addEdge(self, fromLabel, toLabel, weight):
        """Connects the vertices with an edge with a given weight."""
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        fromVertex.addEdgeTo(toVertex, weight)
        self._edgeCount += 1

    def getEdge(self, fromLabel, toLabel):
        """Returns the edge connecting the two vertices, or None if no edge exists."""
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        return fromVertex.getEdgeTo(toVertex)

    def removeEdge(self, fromLabel, toLabel):
        """Returns True if the edge was removed, or False otherwise."""
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        edgeRemovedFlg = fromVertex.removeEdgeTo(toVertex)
        if edgeRemovedFlg:
            self._edgeCount -= 1
        return edgeRemovedFlg

    def edges(self):
        """Supports iteration over the edges in the graph."""
        result = list()
        for vertex in self.vertices():
            edges = vertex.incidentEdges()
            for edge in edges:
                # if edge.getOtherVertex(vertex) in self.vertices():
                result.append(edge)
        return iter(result)

    def vertices(self):
        """Supports iteration over the vertices in the graph."""
        return iter(self._vertices.values())

    def clear(self):
        self._vertices = dict()
        self._edgeCount = 0
        self._size = 0

    def clearEdgeMarks(self):
        for edge in self.edges():
            edge.clearMark()

    def clearVertexMarks(self):
        for vertex in self.vertices():
            vertex.clearMark()

    def sizeEdges(self):
        result = 0
        for edge in self.edges():
            result += 1
        return result

    def sizeVertices(self):
        return self._size

    def __str__(self):
        result = ""
        result += str(self.sizeVertices()) + " Vertices:"
        for vertex in self.vertices():
            result += " " + str(vertex)
        result += "\n" + str(self.sizeEdges()) + " Edges:"
        for edge in self.edges():
            result += " " + str(edge)
        return result

    def containsEdge(self, fromLabel, toLabel):
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        edged = fromVertex.getEdgeTo(toVertex)
        for edge in self.edges():
            if edge == edged:
                return True
        return False

    def getVertex(self, label):
        if label in self._vertices.keys():
            return self._vertices[label]
        else:
            return None

    def containsVertex(self, label):
        if label in self._vertices.keys():
            return True
        else:
            return False

    def incidentEdges(self, label):
        vertex = self._vertices[label]
        return vertex.incidentEdges()

    def neighboringVertices(self, label):
        vertex = self._vertices[label]
        return vertex.neighboringVertices()

    def adjacencyList(self):
        array = Array(self.sizeVertices())
        for i, vertex in enumerate(self.vertices()):
            for edge in vertex.incidentEdges():
                array[i] = Node(edge.getWight(), edge.getToVertex(), array[i])
            array[i] = Node(0, vertex.getLabel(), array[i])
        return array


def main():
    g = LinkedDirectedGraph()

    # Insert vertices
    g.addVertex("A")
    g.addVertex("B")
    g.addVertex("C")
    g.addVertex("D")
    g.addVertex("E")

    # Insert weighted edges
    g.addEdge("A", "B", 3)
    g.addEdge("A", "C", 2)
    g.addEdge("B", "D", 1)
    g.addEdge("C", "D", 1)
    g.addEdge("D", "E", 2)

    print(g)

    # print("Neighboring vertices of B:")
    # for vertex in g.neighboringVertices("B"):
    #     print(vertex)
    # print("Incident edges of B:")
    # for edge in g.incidentEdges("B"):
    #     print(edge)
    #     print(edge.getOtherVertex(g.getVertex("B")))
    #
    # g.removeVertex("B")
    # print(g)
    adj = g.adjacencyList()
    for i in adj:
        while i:
            print(i.label, end=" ")
            i = i.next
        print("")


if __name__ == '__main__':
    main()
    a = list()
