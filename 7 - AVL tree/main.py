"""
FelipedelosH
"""
from AVLTree import AVLTree

avlTree = AVLTree()


avlTree.addData(10)
avlTree.addData(20)
avlTree.addData(30)
avlTree.addData(40)
avlTree.addData(50)

print("=======FIN ALGORITMO===========")
print(f"Raiz: {avlTree.root.data}")
print(f"IZQ: {avlTree.root.left.data}")
print(f"DER: {avlTree.root.right.data}")
print(f"DER.DER: {avlTree.root.right.right.data}")
# avlTree.addData(40)
# avlTree.addData(50)
# avlTree.addData(25)

# print("===========TREE:STATITICS=============")
# print(f"Total nodes: {avlTree.count()}")
# avlTree.viewInOrder()