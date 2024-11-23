"""
FelipedelosH
"""
from Node import Node

class CircularLinkedList:
    def __init__(self) -> None:
        self.pivot = None

    def addData(self, data):
        new_node = Node(data)
        if self.pivot == None:
            self.pivot = new_node
            self.pivot.next = self.pivot
        else:
            _copy = self.pivot

            while _copy.next != self.pivot:
                _copy = _copy.next

            _copy.next = new_node
            new_node.next = self.pivot
    
    def showAllData(self):
        if self.pivot != None:
            _copy = self.pivot
            while True:
                print(_copy.data)
                _copy = _copy.next

                if _copy == self.pivot:
                    break
