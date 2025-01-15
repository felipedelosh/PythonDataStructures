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


    def DFS(self, initial_node):
        visited_nodes = []

        if initial_node in self.nodes:
            queue = [initial_node]

            while queue:
                _pivot = queue.pop()

                if _pivot not in visited_nodes:
                    visited_nodes.append(_pivot)                

                    if _pivot in self.edges:
                        for i in reversed(self.edges[_pivot]):
                            if i not in queue and i not in visited_nodes:
                                queue.append(i)

        return visited_nodes


    def BFS(self, initial_node):
        visited_nodes = []

        if initial_node in self.nodes:
            stack = [initial_node]
            
            while stack:
                _pivot = stack.pop(0)
                visited_nodes.append(_pivot)
                
                if _pivot in self.edges:
                    for i in self.edges[_pivot]:
                        if i not in stack and i not in visited_nodes:
                            stack.append(i)


        return visited_nodes
