'''
******************* PROBLEM STATEMENT

******************* NOTES

1. Could be done using priority queue instead (see approach 3)
2. Heap tuples can only contain values that can be compared (>, <). So no non numerics
3. Approach 5 merges pairs of list at each round until one list remains
    at each round the number of lists divides by halve.
    At each round we compare all nodes
    so there are logk rounds and each round travers all nodes N. Givens same time complexity
    This approach saves the space complexity bc the same input is overwritten to store the merged lists (see soln, is a bit heard to follow)

******************* SOLUTION
'''

# Definition for singly-linked list.
from typing import List, Optional
from heapq import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # tuple (value, node)

        if not lists:
            return

        minheap = []
        head = None
        current = None

        # initialize heap
        for index, node in enumerate(lists):
            if node:
                minheap.append((node.val, index))

        heapify(minheap)

        while minheap:
            # add new node to result
            next_tuple = heappop(minheap)
            next = lists[next_tuple[1]]
            if not head:
                head = next
                current = head
            else:
                current.next = next
                current = next
            # add new node to heap
            if next.next:
                heappush(minheap, (next.next.val, next_tuple[1]))
                lists[next_tuple[1]] = next.next

        return head

    def mergeKListsTupleNode(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # tuple (value, node)

        if not lists:
            return

        minheap = []
        head = None
        current = None

        # initialize heap
        for node in lists:
            if node:
                minheap.append((node.val, node))

        heapify(minheap)

        while minheap:
            # add new node to result
            next = heappop(minheap)
            if not head:
                head = next
                current = head
                continue
            else:
                current.next = next
                current = next
            # add new node to heap
            if next.next:
                heappush(minheap, next.next)

        return head