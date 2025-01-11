"""
FelipedelosH
2024
"""
class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = {}


    def addNode(self, x):
        if x not in self.nodes:
            self.nodes.append(x)


    def addEdge(self, A, B):
        if A in self.nodes and B in self.nodes:
            if A not in self.edges:
                self.edges[A] = []
            self.edges[A].append(B)


    def deleteNode(self, x):
        if x in self.nodes:
            self.nodes.remove(x)

            if x in self.edges:
                del self.edges[x]

            for u, v in self.edges.items():
                if x in v:
                    v.remove(x)
