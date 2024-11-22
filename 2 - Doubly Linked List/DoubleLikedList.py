"""
FelipedelosH
"""
from Node import Node

class DoubleLinkedList:
    def __init__(self) -> None:
        self.pivot = None


    def addDataNext(self, data):
        new_node = Node(data)
        if self.pivot == None:
            self.pivot = new_node
        else:
            new_node.next = self.pivot
            self.pivot.previous = new_node
            self.pivot = new_node


    def addDataPrevious(self, data):
        new_node = Node(data)
        if self.pivot == None:
            self.pivot = new_node


    def showAllDataNext(self):
        self._showAllDataNext(self.pivot)
    def _showAllDataNext(self, pivot):
        if pivot != None:
            print(pivot.data)
            self._showAllDataNext(pivot.next)


    def showAllDataPrevious(self):
        self._showAllDataPrevious(self.pivot)
    def _showAllDataPrevious(self, pivot):
        pass

