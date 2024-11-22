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

    # Extra
    def count(self):
        if self.pivot == None:
            return 0
        return self._count(self.pivot)
    def _count(self, pivot):
        if pivot == None:
            return 0
        else:
            return 1 + self._count(pivot.next)
        
    def isDataInList(self, data):
        return self._isDataInList(self.pivot, data)
    def _isDataInList(self, pivot, data):
        if pivot != None:
            if pivot.data == data:
                return True
            else:
                return self._isDataInList(pivot.next, data)
        else:
            return False
        
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

    def deleteValue(self, data):
        if self.pivot != None:
            # Case 01: is head
            if self.pivot.data == data:
                self.pivot = self.pivot.next
            # Case 02: Other element diferent to head
            else:
                _copy = self.pivot

                while _copy.next != None:
                    if _copy.next.data == data:
                        break
                    _copy = _copy.next

                # Delete
                if _copy.next != None  and _copy.next.data == data:
                    _copy.next = _copy.next.next

    def getValue(self, index):
        _count = self.count()

        if _count == 0 or index >= _count:
            return None
        
        if index == 0:
            return self.pivot.data

        _copy = self.pivot
        _counter = 0
        while _counter < _count:
            if _counter == index:
                return _copy.data

            _copy = _copy.next
            _counter = _counter + 1

        
    def isListEmpty(self):
        return self.pivot == None
