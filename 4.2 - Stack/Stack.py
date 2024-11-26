"""
FelipedelosH
"""
from Node import Node

class Stack:
    def __init__(self) -> None:
        self.pivot = None
        self.size = 0


    def push(self, data):
        new_node = Node(data)
        new_node.next = self.pivot
        self.pivot = new_node
        self.size = self.size + 1

    
    def pop(self):
        if self.pivot == None:
            return None
        
        data = self.pivot.data
        self.pivot = self.pivot.next
        self.size = self.size - 1

        return data


    def count(self):
        return self.size