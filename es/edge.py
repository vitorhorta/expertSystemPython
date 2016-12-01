class Edge(object):
    def __init__(self, titulo, node):
        self.titulo = titulo
        self.node = node

    def __str__(self):
        return self.titulo
