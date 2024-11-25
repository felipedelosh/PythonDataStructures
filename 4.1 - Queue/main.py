"""
FelipdelosH
"""
from Queue import Queue

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print(f"Total Elements: {queue.count()}")
print(f"1st: {queue.dequeue()}")
print(f"2nd: {queue.dequeue()}")
print(f"3rd: {queue.dequeue()}")
print(f"4th: {queue.dequeue()}")
print(f"5th: {queue.dequeue()}")
print(f"Total Elements: {queue.count()}")
