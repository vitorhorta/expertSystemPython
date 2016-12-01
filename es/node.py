class Node(object):
    def __init__(self, titulo):
        self.edges = []
        self.titulo = titulo

    def addEdge(self, edge):
        self.edges.append(edge)

    def showChilds(self):
        print self.childs

    def __str__(self):
        return self.titulo

    def ask(self):
        print self
        for (i, item) in enumerate(self.edges):
            print str(i) + ": " + str(item)
        nextIndex = int(raw_input())
        return self.edges[nextIndex].node

    def hasEdges(self):
        return len(self.edges) > 0
