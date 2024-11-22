"""
FelipedelosH
"""
from Node import Node

class DoubleLinkedList:
    def __init__(self) -> None:
        self.pivot = None


    def addDataStart(self, data):
        new_node = Node(data)
        if self.pivot == None:
            self.pivot = new_node
        else:
            new_node.next = self.pivot
            self.pivot.previous = new_node
            self.pivot = new_node

    
    def addDataEnd(self, data):
        new_node = Node(data)
        if self.pivot == None:
            self.pivot = new_node
        else:
            _copy = self.pivot

            while _copy.next != None:
                _copy = _copy.next

            _copy.next = new_node
            new_node.previous = _copy


    def showAllData(self):
        if self.pivot != None:
            print(f"Pivote: {self.pivot.data}")

            _cpyN = self.pivot.next
            _cpyP = self.pivot.previous

            while _cpyN != None:
                print(f"NEXT: {_cpyN.data}")
                _cpyN = _cpyN.next

            while _cpyP != None:
                print(f"Previous: {_cpyP.data}")
                _cpyP = _cpyP.previous

