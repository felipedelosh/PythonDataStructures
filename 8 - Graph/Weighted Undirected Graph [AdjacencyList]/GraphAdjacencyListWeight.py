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


    def getAllNeighborsWithWeight(self, node):
        """
        return a list of tuple (node, distance)
        """
        neighbors = []

        if node in self.edges:
            for i in self.edges[node]:
                neighbors.append(i)

        return neighbors
        

    def isNeighbor(self, nodeA, nodeB):
        """
        return if A have directed conection with B
        """
        if nodeA not in self.edges or nodeB not in self.nodes:
            return False
        
        for i in self.edges[nodeA]:
            if i[0] == nodeB:
                return True
            
        return False
    

    def _getNeighborWeight(self, nodeA, nodeB):
        for i in self.edges[nodeA]:
            if i[0] == nodeB:
                return i[1]


    def DFS(self, initial_node):
        visited_nodes = []

        if initial_node in self.nodes:
            stack = [initial_node]

            while stack:
                _pivot = stack.pop()

                if _pivot not in visited_nodes:
                    visited_nodes.append(_pivot)                

                    if _pivot in self.edges:
                        for i in reversed(self.edges[_pivot]):
                            if i[0] not in stack and i[0] not in visited_nodes:
                                stack.append(i[0])

        return visited_nodes


    def BFS(self, initial_node):
        visited_nodes = []

        if initial_node in self.nodes:
            queue = [initial_node]
            
            while queue:
                _pivot = queue.pop(0)
                visited_nodes.append(_pivot)
                
                if _pivot in self.edges:
                    for i in self.edges[_pivot]:
                        if i[0] not in queue and i[0] not in visited_nodes:
                            queue.append(i[0])


        return visited_nodes
    

    def getDijkstraTABULATED(self, start):
        """
        Enter a graph start point a return a table with all steps of Dijkstra table.
        """
        dijkstra_table = []
        visited_nodes = []
        _total_steps = len(self.nodes)

        def markMinDefinitiveCandidate(table_iterator):
            best_candidate = None
            weight_of_best_candidate = float('inf')

            # Find the node with less weight
            for i in dijkstra_table:
                if i not in visited_nodes and dijkstra_table[i][table_iterator] != float('inf'):
                    _w = dijkstra_table[i][table_iterator][0]
                    _n = dijkstra_table[i][table_iterator][1]
                    
                    if _w < weight_of_best_candidate:
                        best_candidate = i
                        weight_of_best_candidate = _w

            visited_nodes.append(best_candidate)

            range_itter = range(table_iterator+1, len(dijkstra_table[best_candidate]))
            for i in range_itter:
                dijkstra_table[best_candidate][i] = '*'


        def getNextDefinitiveCandidate(table_iterator):
            best_candidate = None
            weight_of_best_candidate = float('inf')

            # Find the node with less weight
            for i in dijkstra_table:
                if i not in visited_nodes and dijkstra_table[i][table_iterator] != float('inf'):
                    _w = dijkstra_table[i][table_iterator][0]
                    _n = dijkstra_table[i][table_iterator][1]
                    
                    if _w < weight_of_best_candidate:
                        best_candidate = i
                        weight_of_best_candidate = _w

            print("EPAAA")
            print(best_candidate)
            print(weight_of_best_candidate)


        def fillNeighborsDistance(table_iterator, node, akumulated_distance):
            for i in dijkstra_table:
                if i == node:
                    continue

                _neighbor = i
                if self.isNeighbor(node, _neighbor):
                    dijkstra_table[i][table_iterator] = (self._getNeighborWeight(node, _neighbor) + akumulated_distance, node)
                else:
                    dijkstra_table[i][table_iterator] = (float('inf'))


        if start in self.edges:
            #Step 0: FILL TABLE with empty info
            """
                {
                    NODE:[(), () ... ()],
                    ...,
                    NODE:[(), () ... ()]
                }
            """
            dijkstra_table = {i : [() for i in self.edges] for i in self.edges}

            # Step 1: The first Node have 0 distance
            dijkstra_table[start][0] = (0, start)

            fillNeighborsDistance(0, start, 0)
            markMinDefinitiveCandidate(0)
            data = getNextDefinitiveCandidate(0)


        return dijkstra_table


