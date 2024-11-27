"""
FelipdelosH
"""
from Tree import Tree

tree = Tree()

tree.insert(9)
tree.insert(5)
tree.insert(10)
tree.insert(11)
tree.insert(1)
tree.insert(7)
tree.insert(6)


print("======== VIEW IN-ORDER =========")
tree.viewInOrder()
print("======== VIEW PRE-ORDER =========")
tree.viewPreOrder()
print("======== VIEW POST-ORDER =========")
tree.viewPostOrder()
