"""
FelipedelosH

Demostration of double linked List
"""
from DoubleLikedList import DoubleLinkedList

list = DoubleLinkedList()

list.addDataEnd(3)
list.addDataStart(2)
list.addDataEnd(4)
list.addDataEnd(5)
list.addDataStart(777)
list.updateValue(0, 1)

list.showAllData()
print(f"Total elements: {list.count()}")
print(f"The number 4 is in list: {list.isDataInList(4)}")
print(f"The number 777 is in list: {list.isDataInList(777)}")