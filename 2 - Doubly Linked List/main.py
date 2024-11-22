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
list.addDataStart(1)

list.showAllData()