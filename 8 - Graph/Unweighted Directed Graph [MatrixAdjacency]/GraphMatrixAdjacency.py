"""
FelipedelosH
"""
class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.index = {node: index for index, node in enumerate(self.nodes)}
        self.edges = [[0] * len(self.nodes) for _ in range(len(self.nodes))]

    def addEdge(self, A, B):
        if A in self.nodes and B in self.nodes:
            u, v = self.index[A], self.index[B]
            self.edges[u][v] = 1
