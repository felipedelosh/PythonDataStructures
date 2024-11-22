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
