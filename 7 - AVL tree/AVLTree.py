"""
FelipedelosH
"""
from Node import Node

class AVLTree:
    def __init__(self):
        self.root = None


    def addData(self, data):
        self.root = self._addData(self.root, data)
    def _addData(self, pivot, data):
        print(f"Entra a guardar: {data} >> PIVOT: {pivot}")
        if pivot == None:
            new_node = Node(data)
            print(f"Se a creado el nodo:{new_node}>>{new_node.data}")
            return new_node
        if pivot.data < data:
            pivot.right = self._addData(pivot.right, data)
        else:
            pivot.left = self._addData(pivot.left, data)
        
        print(f"continua el {pivot.data} su der: {pivot.right} su izq: {pivot.left}")

        pivot.height = 1 + max(self.getNodeHeight(pivot.left), self.getNodeHeight(pivot.right))
        print(f"Para el NODO: {pivot.data}, su altura es:{pivot.height}")
        f_equilibrium = self.getNodeEquilibrium(pivot)
        print(f"para el nodo{pivot.data} {pivot} su equilibrio es: {f_equilibrium}")

        if f_equilibrium > 1:
            print("+ROTACION...")
            if data < pivot.left.data:
                return self.RR(pivot)
            else:
                pivot.left = self.RL(pivot.left)
                return self.RR(pivot)

        if f_equilibrium < -1:
            print("-ROTACION...")
            if data > pivot.right.data:
                print("Caso data es mayor que pivot")
                return self.RL(pivot)
            else:
                print("Caso data es menor que pivot")
                pivot.right = self.RR(pivot.right)
                return self.RL(pivot)

        print(f"FINAL:{pivot}  >> {pivot.data}")
        print(f"DER: {pivot.right}")
        print(f"IZQ: {pivot.left}")
        return pivot



    def RR(self, node):
        y = node.left
        T3 = y.right
        y.right = node
        node.left = T3
        node.height = 1 + max(self.getNodeHeight(node.left), self.getNodeHeight(node.right))
        y.height = 1 + max(self.getNodeHeight(y.left), self.getNodeHeight(y.right))
        return y


    def RL(self, node):
        print(f"Entra a rotar: El nodo{node.data}")
        y = node.right
        T2 = y.left
        y.left = node
        node.right = T2
        node.height = 1 + max(self.getNodeHeight(node.left), self.getNodeHeight(node.right))
        print(node.height)
        y.height = 1 + max(self.getNodeHeight(y.left), self.getNodeHeight(y.right))
        return y


    def getNodeEquilibrium(self, node):
        if node == None:
            return 0
        else:
            return self.getNodeHeight(node.left) - self.getNodeHeight(node.right)


    def getNodeHeight(self, node):
        if node == None:
            return 0
        else:
            return node.height
        

    def viewInOrder(self):
        self._viewInOrder(self.root)
    def _viewInOrder(self, pivot):
        if pivot != None:
            self._viewInOrder(pivot.left)
            print(pivot.data)
            self._viewInOrder(pivot.right)


    def viewPostOrder(self):
        self._viewPostOrder(self.root)
    def _viewPostOrder(self, pivot):
        if pivot != None:
            self._viewPostOrder(pivot.left)
            self._viewPostOrder(pivot.right)
            print(pivot.data)


    def viewPreOrder(self):
        self._viewPreOrder(self.root)
    def _viewPreOrder(self, pivot):
        if pivot != None:
            print(pivot.data)
            self._viewPreOrder(pivot.left)
            self._viewPreOrder(pivot.right)


    def count(self):
        return self._count(self.root)
    def _count(self, pivot):
        if pivot == None:
            return 0
        else:
            return 1 + self._count(pivot.left) + self._count(pivot.right)
