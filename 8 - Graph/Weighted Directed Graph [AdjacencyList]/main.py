"""
FelipedelosH
"""

from Graph import Graph

g = Graph()

# Add nodes
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addNode("F")

# Add conections

g.addEdge("A", "B", 3)
g.addEdge("B", "C", 7)
g.addEdge("C", "E", 5)
g.addEdge("E", "D", 9)
g.addEdge("E", "F", 1)
g.addEdge("D", "B", 1)


print("=============GRAPH 1 STATICTIS===============")
print(f"All nodes: {g.nodes}")
print(f"All Edges: {g.edges}")
print(f"DFS: {g.DFS("A")}")
print(f"BFS: {g.BFS("A")}")
print(f"Best route A >> F: {g.getBestRoute("A", "F")}")
print(f"Best route E >> C: {g.getBestRoute("E", "C")}")
