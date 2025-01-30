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

print("=============GRAPH 1 STATICTIS===============")
print(f"All nodes: {g.nodes}")
print(f"All Edges: {g.edges}")
print(f"DFS: {g.DFS("A")}")
print(f"BFS: {g.BFS("A")}")
print(f"Best route A >> H: {g.getBestRoute("A", "H")}")
print(f"Best route A >> C: {g.getBestRoute("A", "C")}")
g_dj_table = g.getDijkstraTable("A")
print("\nDijkstra table:")
for i in g_dj_table:
    print(i, g_dj_table[i])

# Test Dijktra Graph2
g2 = Graph()
g2.addNode("s")
g2.addNode("b")
g2.addNode("c")
g2.addNode("d")
g2.addNode("e")
g2.addNode("t")

g2.addEdge("s", "b", 4)
g2.addEdge("s", "c", 2)
g2.addEdge("b", "c", 1)
g2.addEdge("b", "d", 5)
g2.addEdge("c", "d", 8)
g2.addEdge("c", "e", 10)
g2.addEdge("d", "t", 6)
g2.addEdge("d", "e", 2)
g2.addEdge("e", "t", 2)

print("")
print("=============GRAPH 2 STATICTIS===============")
print(f"All nodes: {g2.nodes}")
print(f"All Edges: {g2.edges}")
print(f"DFS: {g2.DFS("s")}")
print(f"BFS: {g2.BFS("s")}")
print(f"Best route s >> d {g2.getBestRoute("s", "d")}")
print(f"Best route s >> d {g2.getBestRoute("e", "b")}")
g2_dj_table = g2.getDijkstraTable("s")
print("\nDijkstra table:")
for i in g2_dj_table:
    print(i, g2_dj_table[i])
print("")
