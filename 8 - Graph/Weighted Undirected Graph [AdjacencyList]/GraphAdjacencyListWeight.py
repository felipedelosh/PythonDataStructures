"""
FelipedelosH
"""
class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = {}


    def addNode(self, x):
        if x not in self.nodes:
            self.nodes.append(x)

    
    def addEdge(self, A, B, W):
        if A in self.nodes and B in self.nodes and W >= 0:
            if A not in self.edges:
                self.edges[A] = []

            if B not in self.edges:
                self.edges[B] = []

            self.edges[A].append((B, W))
            self.edges[B].append((A, W))


    def deleteNode(self, x):
        if x in self.nodes:
            self.nodes.remove(x)

            if x in self.edges:
                del self.edges[x]

            for u, v in self.edges.items():
                for k in v:
                    if k[0] == x:
                        v.remove(k)