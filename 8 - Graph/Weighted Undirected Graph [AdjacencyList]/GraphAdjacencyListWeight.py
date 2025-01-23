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
        Enter node of graph and return a {table} with minimal distances.
        """
        dijkstra = {}
        total_nodes = len(self.nodes)
        visited = []
        akumulated_distance = 0


        def _init_dijkstra_table():
            nonlocal dijkstra
            dijkstra = {i : [() for i in self.edges] for i in self.edges}

            nonlocal start
            dijkstra[start][0] = (0, start)

        def select_min_weight_candidate_and_mark_visited(step):
            """
            Enter a index of dijkstra table and return 
            best_distance, best_candidate, previous_candiate
            """
            nonlocal dijkstra
            nonlocal visited
            best_candidate = None
            previous_candidate = None # Contains a node of min weight
            best_distance = float('inf') # to save a min distance 
            
            for i in dijkstra:
                _data = dijkstra[i][step]

                if _data == 'X':
                    continue

                if i in visited:
                    continue

                if _data == float('inf'):
                    continue

                if _data:
                    distance, node = _data
                    if distance < best_distance:
                        best_candidate = i
                        previous_candidate = node
                        best_distance = self._getNeighborWeight(i, node)

            # Fill visited
            visited.append(best_candidate)


            # FILL TABULATED VISISTED NODES
            nonlocal total_nodes
            try:
                if step == 0 and best_distance == 0:
                    range_to_fill = range(step+1, total_nodes)
                else:
                    dijkstra[best_candidate][step + 1] = dijkstra[best_candidate][step]
                    range_to_fill = range(step+2, total_nodes)

                for i in range_to_fill:
                    dijkstra[best_candidate][i] = 'X'
            except:
                pass


                
            return best_distance, best_candidate, previous_candidate
        

        def fill_neighbors_distances(step, node):
            nonlocal dijkstra
            nonlocal visited
            nonlocal akumulated_distance

            for i in dijkstra:
                if not i in visited:
                    
                    if self.isNeighbor(node, i):
                        _distance = self._getNeighborWeight(node, i) + akumulated_distance
                        dijkstra[i][step] = (_distance, node)
                    else:
                        if step > 0:
                            if dijkstra[i][step-1] != float('inf'):
                                dijkstra[i][step] = dijkstra[i][step-1]
                                continue
                            
                        dijkstra[i][step] = float('inf')


        # Dijkstra LOGIC
        if start in self.edges:
            # STEP 0: construct table and start point

            print("paso 0: construir la tabla")
            _init_dijkstra_table()
            self.mostrarDj(dijkstra)

            print("paso 1: marcar el incio como mejor candidato")
            best_distance, best_candidate, previous_candidate = select_min_weight_candidate_and_mark_visited(0)
            self.mostrarDj(dijkstra)

            print(f"paso 2: rellenar los vecinos desde step {0}")
            fill_neighbors_distances(0, best_candidate)
            self.mostrarDj(dijkstra)

            print(f"paso 3: buscar el mejor candidato step {0}")
            best_distance, best_candidate, previous_candidate = select_min_weight_candidate_and_mark_visited(0)
            print(f"La menor distancia es: {best_distance} desde el nodo: {best_candidate} ... anteior: {previous_candidate}")
            akumulated_distance = akumulated_distance + best_distance
            print(f"Distancia acumulada: {akumulated_distance}")
            self.mostrarDj(dijkstra)


            print(f"Paso 4: rellenar los vecinos desde step {1}")
            fill_neighbors_distances(1, best_candidate)
            self.mostrarDj(dijkstra)

            print(f"paso 5: buscar el mejor candidato step {1}")
            best_distance, best_candidate, previous_candidate = select_min_weight_candidate_and_mark_visited(1)
            print(f"La menor distancia es: {best_distance} desde el nodo: {best_candidate} ... anteior: {previous_candidate}")
            akumulated_distance = akumulated_distance + best_distance
            print(f"Distancia acumulada: {akumulated_distance}")
            self.mostrarDj(dijkstra)


            print(f"Paso 5: rellenar los vecinos desde step {2}")
            fill_neighbors_distances(2, best_candidate)
            self.mostrarDj(dijkstra)

        
        return dijkstra
    

    def mostrarDj(self, table):
        print("????????????????????????")
        for i in table:
            print(i, table[i])
        print("========================")


