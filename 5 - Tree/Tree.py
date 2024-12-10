"""
FelipedelosH
"""
from Node import Node

class Tree:
    def __init__(self) -> None:
        self.root = None


    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
    def _insert(self, pivot, data):
        if data > pivot.data:
            if pivot.right == None:
                pivot.right = Node(data)
            else:
                self._insert(pivot.right, data)
        else:
            if pivot.left == None:
                pivot.left = Node(data)
            else:
                self._insert(pivot.left, data)


    def delNodeByData(self, data):
        if self.root is None:
            return
        if self.root.data == data:
            self.root = self._del_node(self.root)
        else:
            self._del_node_by_data(self.root, data)
    def _del_node_by_data(self, node, data):
        if node is None:
            return None
        if data < node.data:
            node.left = self._del_node_by_data(node.left, data)
        elif data > node.data:
            node.right = self._del_node_by_data(node.right, data)
        else:
            node = self._del_node(node)
        return node
    def _del_node(self, node):
        if self.isTheNodeALeaf(node):
            return None
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        
        min_right_value = self.get_min_value(node.right)
        node.data = min_right_value
        node.right = self._del_node_by_data(node.right, min_right_value)
        return node

    
    def viewInOrder(self):
        self._viewInOrder(self.root)
    def _viewInOrder(self, pivot):
        if pivot != None:
            self._viewInOrder(pivot.left)
            print(pivot.data)
            self._viewInOrder(pivot.right)


    def viewPostOrder(self):
        self._viewPostOrder(self.root)
    def _viewPostOrder(self, pivot):
        if pivot != None:
            self._viewPostOrder(pivot.left)
            self._viewPostOrder(pivot.right)
            print(pivot.data)


    def viewPreOrder(self):
        self._viewPreOrder(self.root)
    def _viewPreOrder(self, pivot):
        if pivot != None:
            print(pivot.data)
            self._viewPreOrder(pivot.left)
            self._viewPreOrder(pivot.right)


    def searchByData(self, data):
        return self._searchByData(self.root, data) 
    def _searchByData(self, pivot,data):
        if pivot != None:
            if pivot.data == data:
                return pivot
            else:
                if pivot.data < data:
                    return self._searchByData(pivot.right, data)
                else:
                    return self._searchByData(pivot.left, data)

        return None
    

    def getMaxValue(self):
        if self.root is None:
            return None
        
        return self._getMaxValue(self.root)
    def _getMaxValue(self, pivot):
        if pivot.right == None:
            return pivot.data
        else:
            return self._getMaxValue(pivot.right)
    

    def get_min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.data


    def getMinValue(self):
        if self.root is None:
            return None

        return self._getMinValue(self.root)
    def _getMinValue(self, pivot):
        if pivot.left == None:
            return pivot.data
        else:
            return self._getMinValue(pivot.left)
        

    def getHeight(self):
        return self._getHeight(self.root)
    def _getHeight(self, pivot):
        if pivot is None:
            return 0
        else:
            return 1 + max(self._getHeight(pivot.left), self._getHeight(pivot.right))
        

    def isTheNodeALeaf(self, node):
        if node != None:
            if node.left is None and node.right is None:
                return True

        return False
    

    def countOnlyChildrensOfNode(self, node):
        L = 1 if node.left != None else 0
        R = 1 if node.right != None else 0

        return L + R


    def count(self):
        return self._count(self.root)
    def _count(self, pivot):
        if pivot == None:
            return 0
        else:
            return 1 + self._count(pivot.left) + self._count(pivot.right)
