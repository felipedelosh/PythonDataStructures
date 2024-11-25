"""
FelipdelosH
"""
from Node import Node

class Queue:
    def __init__(self) -> None:
        self.pivot = None
        self.size = 0


    def enqueue(self, data):
        new_node = Node(data)
        if self.pivot == None:
            self.pivot = new_node
        else:
            _copy = self.pivot

            while _copy.next != None:
                _copy = _copy.next

            _copy.next = new_node

        self.size = self.size + 1


    def dequeue(self):
        if self.pivot == None:
            return None
        
        data = self.pivot.data
        self.pivot = self.pivot.next
        self.size = self.size - 1

        return data


    def count(self):
        return self.size
