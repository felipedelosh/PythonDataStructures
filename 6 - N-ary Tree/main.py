"""
FelipdelosH
"""
from NTree import NTree

nTree = NTree()

nTree.addData(None, 0)
nTree.addData(0, 1)
nTree.addData(0, 2)
nTree.addData(0, 3)
nTree.addData(1, 4)
nTree.addData(1, 5)
nTree.addData(3, 6)
nTree.addData(3, 7)
nTree.addData(3, 8)
nTree.addData(7, 9)
nTree.addData(9, 777)
nTree.deleteNode(9, 777)

print(f"NTree Hight: {nTree.getTreeHeight()}")
print(f"get node with data 3: {nTree.searchByData(3)}")
print(f"get node with data 777: {nTree.searchByData(777)}")
print("=======PreOrder========")
nTree.viewPreOrder()
print("=======PostOrder========")
nTree.viewPostOrder()