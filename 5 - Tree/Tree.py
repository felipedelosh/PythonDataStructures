"""
FelipedelosH
"""
from Node import Node

class Tree:
    def __init__(self) -> None:
        self.root = None


    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
    def _insert(self, pivot, data):
        if data > pivot.data:
            if pivot.right == None:
                pivot.right = Node(data)
            else:
                self._insert(pivot.right, data)
        else:
            if pivot.left == None:
                pivot.left = Node(data)
            else:
                self._insert(pivot.left, data)

    
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
