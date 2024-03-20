from typing import Any, List
import heapq
'''
    Note: Type breaking happens based on 
    When different characters are found then their Unicode value is compared. The character with lower Unicode value is considered to be smaller.
'''
class PriorityQueue:
    def __init__(self, items=[]):
        self.heap = []
        for priority, item in items:
            heapq.heappush(self.heap, (-priority, item))

    # NOTE: Check if empty on push and peek

    def is_empty(self) -> bool:
        return len(self.heap) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.heap[0][1]
        return None
    
    def push(self, priority: int, item: str) -> None:
        if type(priority) != int or type(item) != str:
            raise TypeError() 
        heapq.heappush(self.heap, (-priority, item))
    
    def pop(self) -> str:
        if not self.is_empty():
            return heapq.heappop(self.heap)[1]
        return None

        # raise Exception('')

pq = PriorityQueue()

pq.push(1, 'a')

pq.push(2, 'b')

print(pq.pop())