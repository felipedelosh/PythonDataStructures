"""
FelipedelosH
"""
from Node import Node

class NTree:
    def __init__(self):
        self.root = None


    def addData(self, father, data):
        if self.root == None:
            if father != None:
                self.root = Node(father)

            if data != None:
                self._addData(self.root, father, data)
        else:
            self._addData(self.root, father, data)
    def _addData(self, pivot, father, data):
        if pivot.data == father:
            pivot.children.append(Node(data))
        else:
            for i in pivot.children:
                self._addData(i, father, data)
    

    def view(self):
        self._view(self.root)
    def _view(self, pivot):
        if pivot != None:
            print(pivot.data)
            
            for i in pivot.children:
                self._view(i)
