"""
FelipedelosH
"""
from GraphAdjacencyList import Graph

g = Graph()

# nodes of simply graph
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addNode("F")
g.addNode("G")


# Add conections
g.addEdge("A", "A")
g.addEdge("A", "C")
g.addEdge("A", "B")
g.addEdge("A", "D")
g.addEdge("C", "G")
g.addEdge("B", "F")
g.addEdge("B", "D")
g.addEdge("G", "F")
g.addEdge("D", "F")

# Test delete
g.addNode("X")
g.addEdge("A", "X")
g.addEdge("X", "F")
g.addEdge("X", "X")
g.deleteNode("X")


print("=============GRAPH STATICTIS===============")
print(f"All nodes: {g.nodes}")
print(f"All Edges: {g.edges}")
print(f"DFS: {g.DFS("A")}")
print(f"BFS: {g.BFS("A")}")
