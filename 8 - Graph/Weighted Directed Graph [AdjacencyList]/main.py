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
g.addEdge("B", "D", 10)



print("=============GRAPH STATICTIS===============")
print(f"All nodes: {g.nodes}")
print(f"All Edges: {g.edges}")

