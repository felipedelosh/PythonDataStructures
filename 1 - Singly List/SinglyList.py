"""
FelipedelosH
"""
from Node import Node

class SinglyList:
    def __init__(self) -> None:
        self.pivot = None


    def addData(self, data):
        if self.pivot == None:
            self.pivot = Node(data)
        else:
            new_node = Node(data)
            self._addData(self.pivot, new_node)
    def _addData(self, pivot, new_node):
        if pivot != None:
            if pivot.next == None:
                pivot.next = new_node
            else:
                self._addData(pivot.next, new_node)


    def showAllData(self):
        self._showAllData(self.pivot)
    def _showAllData(self, pivot):
        if pivot != None:
            print(pivot.data)
            self._showAllData(pivot.next)


    def count(self):
        if self.pivot == None:
            return 0
        return self._count(self.pivot)
    def _count(self, pivot):
        if pivot == None:
            return 0
        else:
            return 1 + self._count(pivot.next)
