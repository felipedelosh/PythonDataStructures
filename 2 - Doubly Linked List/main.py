"""
FelipedelosH

Demostration of double linked List
"""
from DoubleLikedList import DoubleLinkedList

list = DoubleLinkedList()

list.addDataNext(5)
list.addDataNext(4)
list.addDataNext(3)
list.addDataNext(2)
list.addDataNext(1)

list.showAllDataNext()
print("=================")
list.showAllDataPrevious()

