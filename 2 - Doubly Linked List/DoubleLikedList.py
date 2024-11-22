"""
FelipedelosH
"""
from Node import Node

class DoubleLinkedList:
    def __init__(self) -> None:
        self.pivot = None


    def addDataNext(self, data):
        if self.pivot == None:
            self.pivot = Node(data)


    def addDataPrevious(self, data):
        if self.pivot == None:
            self.pivot = Node(data)


    def showAllDataNext(self):
        self._showAllDataNext(self.pivot)
    def _showAllDataNext(self, pivot):
        if pivot != None:
            print(pivot.data)
            self._showAllDataNext(pivot.next)


    def showAllDataPrevious(self):
        self._showAllDataPrevious(self.pivot)
    def _showAllDataPrevious(self, pivot):
        if pivot != None:
            print(pivot.data)
            self._showAllDataNext(pivot.previous)

