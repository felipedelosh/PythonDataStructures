"""
FelipedelosH
"""
from GraphAdjacencyListWeight import Graph

g = Graph()

# ADD nodes
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addNode("F")
g.addNode("G")
g.addNode("H")
g.addNode("I")

# ADD conections
g.addEdge("A", "B", 6)
g.addEdge("A", "D", 10)
g.addEdge("A", "G", 8)
g.addEdge("B", "E", 15)
g.addEdge("B", "H", 13)
g.addEdge("B", "C", 11)
g.addEdge("C", "H", 4)
g.addEdge("D", "E", 6)
g.addEdge("E", "F", 2)
g.addEdge("F", "G", 4)
g.addEdge("F", "I", 6)
g.addEdge("G", "H", 5)
g.addEdge("G", "I", 5)
g.addEdge("H", "I", 7)

# Test delete
g.addNode("X")
g.addEdge("A", "X", 1)
g.addEdge("X", "B", 2)
g.addEdge("X", "X", 3)
g.deleteNode("X")

print("=============GRAPH STATICTIS===============")
print(f"All nodes: {g.nodes}")
print(f"All Edges: {g.edges}")

