"""
FelipedelosH

Demostration of Simple List
"""
from SinglyList import SinglyList

# Declare
simpleList = SinglyList()

# Add data
simpleList.addData(1)
simpleList.addData(2)
simpleList.addData(3)
simpleList.addData(4)
simpleList.addData(5)

# Vizualized
simpleList.showAllData()
print(f"TOTAL ELEMTENTS IN LIST: {simpleList.count()}")
print(f"The number 3 is in list: {simpleList.isDataInList(1)}")
print(f"The number 777 is in list: {simpleList.isDataInList(777)}")
print(f"GET ELEMENT IN POS 3: {simpleList.getValue(3)}")
