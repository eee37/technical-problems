import heapq # NOTE:
from typing import Any, List, Tuple

'''
3 key methods:
    1. is empty
    2. peek
    3. pop
    4. insert
'''
class PriorityQueue:
    def __init__(self, items=[]):
        # NOTE: Using dict in case items are not comparable. this is required to push into heap. would not be needed if items are numbers or strings
        self.queue = []
        self.id_item = dict()
        self.id = 0
        for item, priority in items:
            self.insert(item, priority)

    def is_empty(self) -> bool: # O(1)
        return len(self.queue) == 0

    def peek_highest_priority(self) -> Any: # O(1)
        # NOTE: Remember to handle edge cases
        if self.is_empty(): 
            return None
        return self.id_item[self.queue[0][1]]

    def insert(self, item: Any, priority: int) -> None: # O(logn)
        self.id += 1
        self.id_item.update({self.id: item})
        heapq.heappush(self.queue, (-priority, self.id) )

    def pop_highest_priority(self) -> Any: # O(logn)
        # NOTE: Remember to handle edge cases
        if self.is_empty(): 
            return None
        _, id = heapq.heappop(self.queue) 
        item = self.id_item[id]
        # Remember to update map although not required
        del self.id_item[id]
        return item
        
pq = PriorityQueue([['a', 1], ['b', 2], ['c', 3]])
print(pq.is_empty())
print(pq.peek_highest_priority())
x = pq.pop_highest_priority()
print(x)
pq.insert('d', 4)
print(pq.peek_highest_priority())

