from Chapter7_Stacks.linkedstack import LinkedStack
from Chapter8_Queues.linkedqueue import LinkedQueue


def topoSort(g, startLabel=None):
    stack = LinkedStack()
    g.clearVertexMarks()
    for v in g.vertices():
        if not v.isMark():
            dfs(g, v, stack)
    return stack


def topoSortBfs(g, startLabel=None):
    queue = LinkedQueue()
    lyst = list()
    g.clearVertexMarks()
    for v in g.vertices():
        if not v.isMark():
            v.setMark()
            bfs(g, queue, lyst)
    return lyst


def dfs(g, v, stack):
    v.setMark()
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMark():
            dfs(g, w, stack)
    stack.push(v)


def bfs(g, queue, lyst):
    if not queue.isEmpty():
        v = queue.pop()
        lyst.append(v)
        for w in g.neighboringVertices(v.getLabel()):
            if not w.isMark():
                w.setMark()
                queue.add(w)
        bfs(g, queue, lyst)


def spanTree(g, startLabel):
    vertex = g.getVertex(startLabel)
    edges = list()
    result = list()

    def recurse(v, edges, result):
        v.setMark()
        for edge in v.incidentEdges():
            if not edge.isMark():
                edges.append(edge)
        result.append(minEdge(edges))
        if not result[len(result) - 1].getToVertex().isMark():
            recurse(result[len(result) - 1].getToVertex(), edges, result)

    recurse(vertex, edges, result)
    g.clearVertexMarks()
    g.clearEdgeMarks()
    return result


def shortestPaths(g, startLabel):
    pass


def minEdge(edges):
    min_ = float('Inf')
    temp = 0
    for i in range(len(edges)):
        if not edges[i].isMark() and edges[i].getWight() < min_:
            temp = i
            min_ = edges[i].getWight()
    edges[temp].setMark()
    return edges[temp]