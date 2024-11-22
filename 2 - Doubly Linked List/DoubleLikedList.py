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
            self._addDataNext(self.pivot, new_node)
    def _addDataNext(self, pivot, new_node):
        if pivot.next == None:
            pivot.next = new_node
            new_node.previous = pivot
        else:
            self._addDataNext(pivot.next, new_node)


    def addDataNextUpdatingPivot(self, data):
        new_node = Node(data)
        if self.pivot == None:
            self.pivot = new_node
        else:
            _copy = self.pivot

            while _copy.next != None:
                _copy = _copy.next

            _copy.next = new_node
            new_node.previous = _copy
            self.pivot = new_node


    def addDataPreviousUpdatingPivot(self, data):
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
        else:
            self._addDataPrevious(self.pivot, new_node)
    def _addDataPrevious(self, pivot, new_node):
        if pivot.previous == None:
            pivot.previous = new_node
            new_node.next = pivot
        else:
            self._addDataPrevious(pivot.previous, new_node)



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
            self._showAllDataPrevious(pivot.previous)

