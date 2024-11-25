"""
FelipdelosH
"""
from CircularLinkedList import CircularLinkedList

list = CircularLinkedList()

list.addData(1)
list.addData(2)
list.addData("X")
list.addData(3)
list.addData(4)
list.addData(777)
# Proube methods
list.updateValue(5, 5)
list.deleteValue("X")


list.showAllData()
print(f"The number 3 is n List: {list.isDataInList(3)}")
print(f"The number 777 is n List: {list.isDataInList(777)}")
print(f"The element in pos 5 is {list.getData(5)}")
