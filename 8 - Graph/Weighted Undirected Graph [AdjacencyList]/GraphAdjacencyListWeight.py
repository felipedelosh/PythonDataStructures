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
        controller_akumulated_distance = [(start,0)]


        def _init_dijkstra_table():
            nonlocal dijkstra
            dijkstra = {i : [() for i in self.nodes] for i in self.nodes}

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
                # BUG: in step 0 pass to next step
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


        def update_akumulated_distance(akumulated_distance, best_distance, best_candidate, previous_candidate):
            print(f"Distancia acumulada actual: {akumulated_distance}")
            print(f"Mejor distancia: {akumulated_distance}")
            print(f"Mejor candidato: {best_candidate}")
            print(f"Anterior candidato: {previous_candidate}")
            
            nonlocal controller_akumulated_distance
            controller_akumulated_distance.append((best_candidate, best_distance))

            _A = controller_akumulated_distance[-2][0]
            _B = controller_akumulated_distance[-1][0]
            print(f"Candidatos a evaluar {_A}, {_B}")
            if self.isNeighbor(_A, _B):
                akumulated_distance = akumulated_distance + best_distance
            else:
                print(f"{_A} y {_B} no son vecinos")

                _AKU = 0
                for i in controller_akumulated_distance:
                    if i[0] == _A:
                        continue

                    if not self.isNeighbor(i[0], previous_candidate):
                        continue

                    if i[0] == best_candidate:
                        _AKU = _AKU + i[1]
                        break
                    
                    _AKU = _AKU + + i[1]

                akumulated_distance = _AKU
                
            print(f"UPDATE: Distancia acumulada: {akumulated_distance}")
            print(f"ARR aku: {controller_akumulated_distance}")
            print("**************")

            return akumulated_distance


        # Dijkstra LOGIC
        if start in self.edges:
            # STEP 0: construct table and start point
            _init_dijkstra_table()
            best_distance, best_candidate, previous_candidate = select_min_weight_candidate_and_mark_visited(0)

            for i in range(0, total_nodes):
                print(f"FOR: {i}")
                fill_neighbors_distances(i, best_candidate)
                best_distance, best_candidate, previous_candidate = select_min_weight_candidate_and_mark_visited(i)
                # BUG: a veces la distancia acumulada no es simplemete una sucesión A+B+C ... a veces el algorimo brinca al inicio.
                akumulated_distance = update_akumulated_distance(akumulated_distance, best_distance, best_candidate, previous_candidate)
                


        return dijkstra
    