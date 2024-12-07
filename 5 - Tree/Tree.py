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
        # Case 0 del a root
        if self.root.data == data:
            if self.isTheNodeALeaf(self.root):
                self.root = None
            else:
                pass
        else:
            self._delNodeByData(self.root, data)
    def _delNodeByData(self, pivot, data):
        if pivot != None:
            _findL = False
            _findR = False
            _direction = ""

            if pivot.left != None:
                if pivot.left.data == data:
                    _findL = True
                    _direction = "L"
                    print(f"Find child, Father >>{pivot.data}")
                    self._delNode(pivot, pivot.left, _direction)

            if pivot.right != None:
                if pivot.right.data == data:
                    _findR = True
                    _direction = "R"
                    print(f"Find child, Father >>{pivot.data}")
                    self._delNode(pivot, pivot.right, _direction)

            if not _findL and not _findR:
                if pivot.data < data:
                    self._delNodeByData(pivot.right, data)
                else:
                    self._delNodeByData(pivot.left, data)
    def _delNode(self, father, del_node, direction):
        print(f"Nodo padre: {father.data}")
        print(f"Nodo a eliminar: {del_node.data}")
        print(f"El nodo a eliminar está en: {direction}")

        # Case 1
        if self.isTheNodeALeaf(del_node):
            if direction == "R":
                father.right = None
            else:
                father.left = None
        # Case 2
        elif self.countOnlyChildrensOfNode(del_node) == 1:
            if direction == "R":
                if del_node.right != None:
                    father.right = del_node.right
                else:
                    father.right = del_node.left
            else:
                if del_node.right != None:
                    father.left = del_node.right
                else:
                    father.left = del_node.left
        # Case 3
        elif self.countOnlyChildrensOfNode(del_node) == 2:
            pass
    
    
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
