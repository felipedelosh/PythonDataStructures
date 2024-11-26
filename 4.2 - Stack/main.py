"""
FelipedelosH
"""
from Stack import Stack

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)


print(f"Total Elements: {stack.count()}")
print(f"1st: {stack.pop()}")
print(f"2nd: {stack.pop()}")
print(f"3rd: {stack.pop()}")
print(f"4th: {stack.pop()}")
print(f"5th: {stack.pop()}")
print(f"Total Elements: {stack.count()}")