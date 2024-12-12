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

            if father != None and data != None:
                self._addData(self.root, father, data)

            if father == None and data != None:
                self.root = Node(data)
        else:
            self._addData(self.root, father, data)
    def _addData(self, pivot, father, data):
        if pivot.data == father:
            pivot.children.append(Node(data))
        else:
            for i in pivot.children:
                self._addData(i, father, data)


    def deleteNode(self, father, data):
        if self.root != None and father != None and data != None:
            self._deleteNode(self.root, father, data)
    def _deleteNode(self, pivot, father, data):
        if pivot.data == father:
            pivot.children = [node for node in pivot.children if node.data != data]
        else:   
            for i in pivot.children:
                self._deleteNode(i, father, data)


    def searchByData(self, data):
        if self.root != None:
            return self._searchByData(self.root, data)
        
        return None
    def _searchByData(self, pivot, data):
        if pivot.data == data:
            return pivot
        
        for i in pivot.children:
            result = self._searchByData(i, data)

            if result != None:
                return result
        
        return None
    

    def getTreeHeight(self):
        if self.root != None:
            return self._getTreeHeight(self.root)
        
        return 0
    def _getTreeHeight(self, pivot):
        if pivot.children != []:
            _height_register = [self._getTreeHeight(i) for i in pivot.children]
            return 1 + max(_height_register)
        else:
            return 1


    def view(self):
        self._view(self.root)
    def _view(self, pivot):
        if pivot != None:
            print(pivot.data)
            
            for i in pivot.children:
                self._view(i)

    def viewPreOrder(self):
        self._viewPreOrder(self.root)
    def _viewPreOrder(self, pivot):
        if pivot != None:
            print(pivot.data)
            
            for i in pivot.children:
                self._viewPreOrder(i)


    def viewPostOrder(self):
        self._viewPostOrder(self.root)
    def _viewPostOrder(self, pivot):
        if pivot != None:
            for i in pivot.children:
                self._viewPostOrder(i)

            print(pivot.data)
