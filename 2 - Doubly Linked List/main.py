"""
FelipedelosH

Demostration of double linked List
"""
from DoubleLikedList import DoubleLinkedList

list = DoubleLinkedList()

#list.addDataNextUpdatingPivot(1)
list.addDataPreviousUpdatingPivot(6)
#list.addDataNextUpdatingPivot(2)
list.addDataPreviousUpdatingPivot(7)
#list.addDataNextUpdatingPivot(3)
list.addDataPreviousUpdatingPivot(8)
#list.addDataNextUpdatingPivot(4)
list.addDataPreviousUpdatingPivot(9)
#list.addDataNextUpdatingPivot(5)

list.showAllDataNext()
print("=================")
list.showAllDataPrevious()

