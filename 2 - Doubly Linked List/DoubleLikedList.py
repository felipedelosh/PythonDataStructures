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


    def count(self):
        if self.pivot == None:
            return 0
        
        if self.pivot != None:
            _count = 1
            _copy = self.pivot.next

            while _copy != None:
                _count = _count + 1
                _copy = _copy.next

            return _count

        return 0
    

    def updateValue(self, index, data):
        _count = self.count()

        if index >= 0 and index < _count:
            _copy = self.pivot
            _counter = 0
            while _counter < index:
                _copy = _copy.next
                _counter = _counter + 1

            # UPDATE
            _copy.data =  data


    def isDataInList(self, data):
        if self.pivot == None:
            return False
        
        _copy = self.pivot
        while _copy != None:
            if _copy.data == data:
                return True
            
            _copy = _copy.next

        return False
    

    def deleteData(self, data):
        if self.pivot is not None:
            # Case 01: is head
            if self.pivot.data == data:
                self.pivot = self.pivot.next
                if self.pivot is not None:
                    self.pivot.previous = None
            # Case 02: Element it's not in head
            else:
                _copy = self.pivot

                while _copy.next is not None:
                    if _copy.next.data == data:
                        break
                    _copy = _copy.next

                # Delete
                if _copy.next is not None and _copy.next.data == data:
                    node_to_delete = _copy.next
                    _copy.next = node_to_delete.next

                    # Validate if it's not the last element
                    if node_to_delete.next is not None:
                        node_to_delete.next.previous = _copy
                    node_to_delete = None



        

    def showAllData(self):
        if self.pivot != None:
            print(self.pivot.data)

            _cpyN = self.pivot.next

            while _cpyN != None:
                print(_cpyN.data)
                _cpyN = _cpyN.next
