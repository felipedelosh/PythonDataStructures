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

print(f"TOTAL nodes: {tree.count()}")
print(f"Tree height: {tree.getHeight()}")
print(f"Tree Max value: {tree.getMaxValue()}")
print(f"Tree Min value: {tree.getMinValue()}")
print(f"Search by data: 1 >> {tree.searchByData(1)}")
print(f"Search by data: 777 >> {tree.searchByData(777)}")
print("======== VIEW IN-ORDER =========")
tree.viewInOrder()
print("======== VIEW PRE-ORDER =========")
tree.viewPreOrder()
print("======== VIEW POST-ORDER =========")
tree.viewPostOrder()
